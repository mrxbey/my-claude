# Current API Authentication Implementation

**Last Updated**: November 15, 2024
**File**: `src/auth/authentication.py`
**Maintainer**: Backend Team

## Overview

This document describes the current authentication and authorization implementation for our REST API.

## Authentication Implementation

### Token Generation

**Location**: `src/auth/token_service.py:45-78`

```python
def generate_token(user_id: str, role: str) -> str:
    """Generate JWT token for authenticated user"""

    payload = {
        'user_id': user_id,
        'role': role,
        'issued_at': datetime.utcnow(),
        'expires_at': datetime.utcnow() + timedelta(hours=2)  # 2-hour expiry
    }

    # Using HS256 algorithm with secret key
    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm='HS256'
    )

    return token
```

**Status**: ⚠️ **IMPLEMENTED** (but see issues below)

**Issues**:
- Using HS256 instead of RS256 (violates REQ-AUTH-002)
- Token expiry is 2 hours, policy requires max 1 hour (violates REQ-AUTH-002)
- No refresh token mechanism implemented

### Token Validation

**Location**: `src/auth/middleware.py:23-45`

```python
def validate_token(token: str) -> Dict:
    """Validate JWT token and extract payload"""

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=['HS256']
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise AuthenticationError("Token expired")
    except jwt.InvalidTokenError:
        raise AuthenticationError("Invalid token")
```

**Status**: ✅ **IMPLEMENTED**

### Authentication Endpoints

**Location**: `src/api/auth_routes.py:12-67`

#### POST /api/v1/auth/login

```python
@router.post("/auth/login")
async def login(credentials: LoginCredentials):
    """Authenticate user and return JWT token"""

    user = await authenticate_user(
        credentials.username,
        credentials.password
    )

    if not user:
        # Log failed attempt
        logger.warning(
            f"Failed login attempt for user: {credentials.username} "
            f"from IP: {request.client.host}"
        )
        return JSONResponse(
            status_code=401,
            content={"error": "Invalid username or password"}
        )

    token = generate_token(user.id, user.role)

    # Log successful login
    logger.info(
        f"User {user.id} logged in successfully "
        f"from IP: {request.client.host}"
    )

    return {
        "token": token,
        "user_id": user.id,
        "role": user.role
    }
```

**Status**: ✅ **IMPLEMENTED** - Compliant with REQ-LOG-001

## Authorization Implementation

### Role-Based Access Control

**Location**: `src/auth/authorization.py:15-34`

```python
ROLES = {
    'admin': ['read', 'write', 'delete', 'admin'],
    'user': ['read', 'write'],
    'readonly': ['read']
}

def check_permission(user_role: str, required_permission: str) -> bool:
    """Check if user role has required permission"""

    permissions = ROLES.get(user_role, [])
    return required_permission in permissions
```

**Status**: ✅ **IMPLEMENTED** - Compliant with REQ-AUTHZ-001

**Notes**: Default deny implemented (returns False if role not found)

### Resource Ownership Validation

**Location**: `src/api/resource_routes.py:45-67`

```python
@router.get("/api/v1/resources/{resource_id}")
async def get_resource(resource_id: str, user: User = Depends(get_current_user)):
    """Get resource by ID"""

    resource = await db.resources.find_one({"id": resource_id})

    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")

    # Check ownership
    if resource['owner_id'] != user.id and user.role != 'admin':
        logger.warning(f"User {user.id} attempted to access resource {resource_id}")
        raise HTTPException(status_code=403, detail="Access denied")

    return resource
```

**Status**: ✅ **IMPLEMENTED** - Compliant with REQ-AUTHZ-002

## Input Validation Implementation

### Request Validation

**Location**: `src/api/validators.py:8-28`

```python
class CreateResourceRequest(BaseModel):
    """Validation schema for resource creation"""

    name: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., max_length=1000)
    category: str = Field(..., regex="^[a-zA-Z0-9_-]+$")
    tags: List[str] = Field(default=[], max_items=10)

    @validator('tags')
    def validate_tags(cls, tags):
        for tag in tags:
            if len(tag) > 50:
                raise ValueError("Tag length must be <= 50 characters")
        return tags
```

**Status**: ✅ **IMPLEMENTED** - Compliant with REQ-VAL-001

### Rate Limiting

**Location**: `src/middleware/rate_limiter.py:12-35`

```python
# Rate limiting configuration
RATE_LIMITS = {
    '/api/v1/auth/login': '10/minute',
    '/api/v1/resources': '200/minute',  # Higher limit for main endpoint
    'default': '100/minute'
}

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    """Apply rate limiting to all requests"""

    client_id = get_client_identifier(request)
    endpoint = request.url.path

    # Get rate limit for this endpoint
    limit = RATE_LIMITS.get(endpoint, RATE_LIMITS['default'])

    # Check rate limit
    if not await rate_limiter.check_limit(client_id, endpoint, limit):
        return JSONResponse(
            status_code=429,
            content={"error": "Too many requests"}
        )

    return await call_next(request)
```

**Status**: ✅ **IMPLEMENTED** - Compliant with REQ-VAL-002

## HTTPS Configuration

**Location**: `config/nginx.conf:15-28`

```nginx
server {
    listen 80;
    server_name api.example.com;

    # Redirect all HTTP to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name api.example.com;

    ssl_certificate /etc/ssl/certs/api.example.com.crt;
    ssl_certificate_key /etc/ssl/private/api.example.com.key;
    ssl_protocols TLSv1.2 TLSv1.3;

    location / {
        proxy_pass http://localhost:8000;
    }
}
```

**Status**: ✅ **IMPLEMENTED** - Compliant with REQ-AUTH-003

## Logging Implementation

### Security Event Logging

**Location**: `src/logging/security_logger.py:18-42`

```python
def log_security_event(event_type: str, user_id: str, details: Dict):
    """Log security-related events"""

    log_entry = {
        'timestamp': datetime.utcnow().isoformat(),
        'event_type': event_type,
        'user_id': user_id,
        'ip_address': get_client_ip(),
        'details': details
    }

    # Write to security log
    security_logger.info(json.dumps(log_entry))

    # Also send to monitoring system
    monitoring.send_event('security', log_entry)
```

**Status**: ✅ **IMPLEMENTED** - Compliant with REQ-LOG-001

### Sensitive Data Protection

**Location**: `src/logging/formatters.py:8-25`

```python
def sanitize_log_data(data: Dict) -> Dict:
    """Remove sensitive data from logs"""

    sanitized = data.copy()

    # Remove sensitive fields
    sensitive_fields = ['password', 'api_key', 'secret']
    for field in sensitive_fields:
        if field in sanitized:
            sanitized[field] = '[REDACTED]'

    # Mask email addresses
    if 'email' in sanitized:
        email = sanitized['email']
        username, domain = email.split('@')
        sanitized['email'] = f"{username[0]}***@{domain}"

    return sanitized
```

**Status**: ⚠️ **PARTIAL** - Partially compliant with REQ-LOG-002

**Issues**:
- Tokens are not in the sanitization list (should be redacted)
- Credit card masking not implemented
- SSN redaction not implemented

## Error Handling Implementation

**Location**: `src/api/error_handlers.py:10-35`

```python
@app.exception_handler(AuthenticationError)
async def authentication_error_handler(request: Request, exc: AuthenticationError):
    """Handle authentication errors"""

    # Log detailed error server-side
    logger.error(
        f"Authentication error: {exc.message} "
        f"for user: {exc.user_id} "
        f"from IP: {request.client.host}"
    )

    # Return generic error to client
    return JSONResponse(
        status_code=401,
        content={"error": "Authentication failed"}
    )

@app.exception_handler(Exception)
async def general_error_handler(request: Request, exc: Exception):
    """Handle unexpected errors"""

    # Log full stack trace server-side
    logger.exception("Unexpected error occurred")

    # Return generic error (no stack trace to client)
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error"}
    )
```

**Status**: ✅ **IMPLEMENTED** - Compliant with REQ-ERR-001

## API Versioning

**Location**: `src/api/routes.py:8-15`

```python
# API version 1
v1_router = APIRouter(prefix="/api/v1")

v1_router.include_router(auth_routes.router)
v1_router.include_router(resource_routes.router)
v1_router.include_router(user_routes.router)

app.include_router(v1_router)
```

**Status**: ✅ **IMPLEMENTED** - Compliant with REQ-VER-001

## Public Endpoints (Unauthenticated)

**Location**: `src/api/health_routes.py:5-18`

```python
@router.get("/health")
async def health_check():
    """Health check endpoint - no authentication required"""
    return {"status": "healthy"}

@router.get("/status")
async def status_check():
    """Status check endpoint - no authentication required"""
    return {
        "status": "operational",
        "version": "1.2.3",
        "timestamp": datetime.utcnow().isoformat()
    }
```

**Status**: ✅ **IMPLEMENTED** - Compliant with REQ-AUTH-001 (exempt endpoints)

## Summary

### Compliant Requirements
- ✅ REQ-AUTH-001: Authentication required (except exempt endpoints)
- ✅ REQ-AUTH-003: HTTPS only
- ✅ REQ-AUTHZ-001: RBAC implemented
- ✅ REQ-AUTHZ-002: Resource-level permissions
- ✅ REQ-VAL-001: Input validation
- ✅ REQ-VAL-002: Rate limiting
- ✅ REQ-LOG-001: Security event logging
- ✅ REQ-ERR-001: Secure error messages
- ✅ REQ-VER-001: API versioning

### Non-Compliant or Partial Requirements
- ⚠️ REQ-AUTH-002: Token-based auth (using HS256 instead of RS256, 2hr expiry vs 1hr, no refresh tokens)
- ⚠️ REQ-LOG-002: Sensitive data protection (tokens/SSN/CC not fully redacted)

### Not Documented
Some requirements may be implemented but not documented in this file.
