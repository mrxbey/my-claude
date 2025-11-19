# Code Review Input

## Command Used

```bash
/workflows:code-review "src/api/authentication/"
```

## Code Context

**Repository**: Enterprise SaaS Application
**Component**: Authentication API
**Language**: Python (FastAPI)
**Files**:
- `src/api/authentication/routes.py` (250 lines)
- `src/api/authentication/models.py` (180 lines)
- `src/api/authentication/services.py` (320 lines)
- `src/api/authentication/utils.py` (150 lines)

**Total**: ~900 lines of authentication code

## What We're Reviewing

**Purpose**: User authentication system including:
- Login/logout endpoints
- JWT token generation and validation
- Password reset flow
- OAuth2 integration (Google, GitHub)
- Session management
- Rate limiting

**Specific Concerns**:
- Security: Authentication is critical - any vulnerabilities are high risk
- Recent changes: OAuth2 integration just added (needs thorough review)
- Performance: Login endpoint has been slow under load
- Tech debt: Password reset flow has complex logic that needs refactoring

## Code Snippet (routes.py excerpt)

```python
@router.post("/login")
async def login(credentials: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == credentials.email).first()

    if not user or not verify_password(credentials.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Generate JWT token
    token = create_access_token(data={"sub": user.email})

    return {"access_token": token, "token_type": "bearer"}


@router.post("/reset-password")
async def reset_password(request: ResetPasswordRequest, db: Session = Depends(get_db)):
    # Complex password reset logic...
    user = db.query(User).filter(User.email == request.email).first()

    if user:
        reset_token = secrets.token_urlsafe(32)
        user.reset_token = reset_token
        user.reset_token_expires = datetime.utcnow() + timedelta(hours=1)
        db.commit()

        # Send email
        send_reset_email(user.email, reset_token)

    return {"message": "If email exists, reset link sent"}
```

## Review Goals

1. **Security first**: Identify any authentication vulnerabilities
2. **Performance**: Why is login slow under load?
3. **Code quality**: Is the code maintainable and testable?
4. **Best practices**: Does it follow OAuth2 and JWT best practices?
5. **Test coverage**: Are critical paths tested?

## That's It!

The workflow analyzed this authentication code and produced a comprehensive review in 10 minutes.

See [OUTPUT.md](OUTPUT.md) for the complete code review report.
