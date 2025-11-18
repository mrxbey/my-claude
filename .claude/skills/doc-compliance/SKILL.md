---
name: doc-compliance
description: Documentation verification and policy compliance patterns including requirements extraction, compliance checklists, validation tables, and gap analysis. Use for checking documentation accuracy, validating against specs, ensuring policy compliance, or verifying implementation matches requirements. Trigger keywords - documentation, docs, verify, compliance, policy, specification, requirements, validate, check against, standards, regulations.
version: 1.0.0
allowed-tools: Read, Grep, Glob
---

# Skill: Documentation Compliance

## Purpose

This skill provides systematic patterns for verifying documentation accuracy, checking compliance with specifications and policies, and ensuring implementations match requirements. It transforms loose requirements into structured checklists with clear pass/fail criteria.

## When to Use

Use this skill when:
- Verifying documentation accuracy against implementation
- Checking compliance with policies, standards, or regulations
- Validating API documentation matches code
- Ensuring requirements are met
- Auditing against specifications
- Cross-referencing multiple documentation sources
- Generating compliance reports

**Trigger scenarios**: "verify docs match code", "check against requirements", "ensure compliance with policy", "validate the spec", "audit documentation"

## Prerequisites

- Access to relevant documentation (specs, policies, standards)
- Access to implementation (code, configuration, system)
- Clear understanding of what compliance means for this context
- Defined scope (what to verify)

## Core Compliance Process

### Step 1: Documentation Discovery

**Goal**: Identify all relevant documentation sources

**Actions**:
1. Locate documentation sources:
   - **Project docs**: README, docs/, inline comments
   - **Specifications**: API specs, design docs, architecture docs
   - **Policies**: Internal guidelines, compliance requirements
   - **Standards**: Industry standards (OWASP, PCI-DSS, etc.)
   - **External docs**: Library docs, vendor specs

2. For each source, document:
   - Location (file path or URL)
   - Type (specification, policy, guide, reference)
   - Version or date
   - Precedence (primary, secondary, reference)
   - Scope (what it covers)

3. Build source hierarchy:
   - Which source takes precedence if conflict?
   - Which are normative (must follow) vs. informative (guidance)?

4. Check for completeness:
   - Are there gaps in documentation coverage?
   - Any missing policies or specs?

**Quality Check**:
- [ ] All relevant docs identified
- [ ] Source locations documented
- [ ] Versions/dates captured
- [ ] Precedence hierarchy clear
- [ ] Coverage gaps noted

**Documentation Map Template**:
```markdown
## Documentation Sources

### Primary Sources (Must Comply)

1. **API Specification v2.1**
   - Location: docs/api-spec.md
   - Date: 2024-11-01
   - Scope: All REST API endpoints
   - Status: Current

2. **Security Policy**
   - Location: .claude/policies/security.md
   - Date: 2024-10-15
   - Scope: Authentication, authorization, data handling
   - Status: Current

### Secondary Sources (Should Follow)

3. **Style Guide**
   - Location: docs/style-guide.md
   - Date: 2024-09-01
   - Scope: Code style, naming conventions
   - Status: Current

### Reference Sources (Informative)

4. **OAuth 2.0 RFC 6749**
   - Location: https://tools.ietf.org/html/rfc6749
   - Date: 2012-10
   - Scope: OAuth implementation guidance
   - Status: Industry standard

### Gaps Identified
- No performance SLA documentation
- Missing disaster recovery procedures
```

### Step 2: Requirements Extraction

**Goal**: Build comprehensive requirements checklist

**Actions**:
1. Extract requirements from each source:
   - Read documentation systematically
   - Identify explicit requirements (MUST, SHALL, REQUIRED)
   - Identify implicit requirements (expected behaviors)
   - Note prohibitions (MUST NOT, SHALL NOT)

2. Categorize requirements:
   - **Functional**: What the system must do
   - **Security**: Authentication, authorization, encryption, etc.
   - **Performance**: Speed, scalability, efficiency
   - **Reliability**: Uptime, error handling, recovery
   - **Compliance**: Regulatory, policy, standards
   - **Documentation**: What must be documented

3. For each requirement, document:
   - **ID**: Unique identifier (REQ-001, SEC-015, etc.)
   - **Description**: What is required
   - **Source**: Where it comes from (file:line or section)
   - **Category**: Type of requirement
   - **Priority**: Critical, High, Medium, Low
   - **Verification**: How to check if met

4. Handle requirement types:
   - **Must Have**: Non-negotiable, blocks approval
   - **Should Have**: Important but not blocking
   - **May Have**: Nice to have
   - **Must Not Have**: Explicitly prohibited

**Quality Check**:
- [ ] All explicit requirements extracted
- [ ] Each requirement has unique ID
- [ ] Sources cited with file:line
- [ ] Categories assigned
- [ ] Priorities set
- [ ] Verification method defined

**Requirements Template**:
```markdown
## Requirements List

### Security Requirements (Category: SEC)

| ID | Requirement | Source | Priority | Verification Method |
|----|-------------|--------|----------|---------------------|
| SEC-001 | All passwords MUST be hashed with bcrypt | security.md:12 | Critical | Check auth code for bcrypt usage |
| SEC-002 | API endpoints MUST have rate limiting | security.md:45 | Critical | Check middleware configuration |
| SEC-003 | Session tokens MUST expire within 24h | security.md:67 | High | Check token generation code |
| SEC-004 | All input MUST be validated | security.md:89 | Critical | Check input validation middleware |

### Functional Requirements (Category: FUNC)

| ID | Requirement | Source | Priority | Verification Method |
|----|-------------|--------|----------|---------------------|
| FUNC-001 | System SHALL support user registration | api-spec.md:23 | Critical | Check /register endpoint exists |
| FUNC-002 | Users SHALL be able to reset passwords | api-spec.md:45 | High | Check /reset-password endpoint |

### Performance Requirements (Category: PERF)

| ID | Requirement | Source | Priority | Verification Method |
|----|-------------|--------|----------|---------------------|
| PERF-001 | API responses MUST be < 200ms p95 | sla.md:12 | High | Load testing, monitoring |
| PERF-002 | System SHALL handle 1000 concurrent users | sla.md:23 | Medium | Capacity testing |

### Prohibition (MUST NOT)

| ID | Prohibition | Source | Priority | Verification Method |
|----|-------------|--------|----------|---------------------|
| PRO-001 | Passwords MUST NOT be logged | security.md:34 | Critical | Check logging code |
| PRO-002 | Credentials MUST NOT be in version control | security.md:56 | Critical | Check git history |
```

### Step 3: Verification & Assessment

**Goal**: Check each requirement against reality

**Actions**:
1. For each requirement, assess status:
   - ✅ **Fully Met**: Completely satisfied with evidence
   - ⚠️ **Partially Met**: Partially satisfied or unclear
   - ❌ **Not Met**: Not satisfied
   - ⏭️ **Not Applicable**: Doesn't apply to current scope
   - ❓ **Cannot Verify**: Need more information

2. Document evidence for each:
   - **File location**: Where requirement is satisfied (file:line)
   - **Code/config excerpt**: Specific implementation
   - **Notes**: Any deviations, concerns, or context
   - **Confidence**: How confident in the assessment

3. Search systematically:
   ```bash
   # Find relevant code
   grep -r "bcrypt" src/auth/

   # Find configuration
   cat config/security.json

   # Check for specific patterns
   grep -r "rate.*limit" src/middleware/

   # Find logging statements
   grep -r "password\|secret\|token" src/ | grep -i "log"
   ```

4. Cross-reference:
   - Does implementation match documentation?
   - Are there contradictions between sources?
   - Is anything documented but not implemented?
   - Is anything implemented but not documented?

5. Flag issues:
   - Deviations from spec
   - Contradictions between docs
   - Undocumented features
   - Documented but missing features

**Quality Check**:
- [ ] Every requirement assessed
- [ ] Evidence documented with file:line
- [ ] Status clear (✅⚠️❌⏭️❓)
- [ ] Deviations noted
- [ ] Contradictions highlighted
- [ ] Confidence level stated

**Verification Table Template**:
```markdown
## Compliance Verification

### ✅ Fully Met Requirements (X/Y)

| ID | Requirement | Evidence | Notes |
|----|-------------|----------|-------|
| SEC-001 | Passwords hashed with bcrypt | src/auth/hash.js:12 | ✅ Using bcrypt.hash() with salt rounds=10 |
| FUNC-001 | User registration supported | src/routes/auth.js:45 | ✅ POST /api/register endpoint exists |

**Evidence for SEC-001**:
```javascript
// src/auth/hash.js:12
const hash = await bcrypt.hash(password, 10); // ✅ Correct
```

### ⚠️ Partially Met Requirements (X/Y)

| ID | Requirement | Evidence | Issue | Confidence |
|----|-------------|----------|-------|------------|
| SEC-002 | Rate limiting required | src/middleware/rateLimit.js:23 | Only on login endpoint, not all APIs | Medium |
| SEC-003 | Tokens expire in 24h | src/auth/jwt.js:34 | Set to 7 days, not 24h | High |

**Evidence for SEC-002**:
```javascript
// src/middleware/rateLimit.js:23
app.use('/api/login', rateLimit({ max: 5 })); // ⚠️ Only login
// Missing: Other endpoints don't have rate limiting
```

### ❌ Not Met Requirements (X/Y)

| ID | Requirement | Gap | Impact | Priority to Fix |
|----|-------------|-----|--------|-----------------|
| SEC-004 | All input validated | No validation middleware found | HIGH - Injection risk | Critical |
| PRO-001 | Passwords not logged | Found in logs (server.js:123) | HIGH - Security leak | Critical |

**Evidence for PRO-001**:
```javascript
// src/server.js:123
console.log('Login attempt:', { username, password }); // ❌ VIOLATION!
```

### ⏭️ Not Applicable (X/Y)

| ID | Requirement | Reason |
|----|-------------|--------|
| PERF-002 | 1000 concurrent users | Pilot phase, target is 100 users |

### ❓ Cannot Verify (X/Y)

| ID | Requirement | Blocker | Next Step |
|----|-------------|---------|-----------|
| PERF-001 | API < 200ms p95 | No load testing done | Run load tests |
```

### Step 4: Gap Analysis

**Goal**: Identify and prioritize what needs fixing

**Actions**:
1. Categorize gaps:
   - **Missing**: Required but not found
   - **Incorrect**: Present but wrong
   - **Incomplete**: Partial implementation
   - **Undocumented**: Exists but not documented
   - **Outdated**: Documented but obsolete

2. For each gap:
   - Describe the issue clearly
   - Explain the impact (security, compliance, usability, etc.)
   - Assess severity (Critical, High, Medium, Low)
   - Suggest specific remediation with file:line
   - Estimate effort (hours, days, weeks)

3. Prioritize by:
   - **P0 (Critical)**: Blocks compliance, security risk, must fix
   - **P1 (High)**: Significant impact, should fix soon
   - **P2 (Medium)**: Moderate impact, fix when possible
   - **P3 (Low)**: Minor issue, nice to fix

4. Group by theme:
   - Security gaps
   - Functional gaps
   - Documentation gaps
   - Performance gaps

**Quality Check**:
- [ ] All gaps categorized
- [ ] Impact assessed
- [ ] Severity assigned
- [ ] Remediation specific
- [ ] Effort estimated
- [ ] Priorities set

**Gap Analysis Template**:
```markdown
## Gap Analysis

### Summary

- **Total Requirements**: 25
- **Fully Met**: 15 (60%)
- **Partially Met**: 5 (20%)
- **Not Met**: 3 (12%)
- **Not Applicable**: 2 (8%)

- **Overall Compliance**: 60% (Fully Met only)
- **Overall Compliance**: 80% (Fully + Partially Met)

### Critical Gaps (P0) - BLOCKING

#### GAP-1: No Input Validation (REQ: SEC-004)

**Category**: Missing
**Impact**: HIGH - Injection vulnerabilities (SQL, XSS, command injection)
**Current State**: No validation middleware or schema checks
**Required State**: All endpoints validate input against schema
**Evidence**: No validation found in src/middleware/, src/routes/

**Remediation**:
1. Install validation library (e.g., joi, express-validator)
2. Create validation schemas for each endpoint
3. Add validation middleware: `src/middleware/validate.js`
4. Apply to all routes in `src/routes/`

**Effort**: 3 days
**Files to Modify**:
- src/middleware/validate.js (create)
- src/routes/*.js (add validation)
- package.json (add dependency)

**Test**: Send malicious input, verify rejection

#### GAP-2: Passwords Logged (REQ: PRO-001)

**Category**: Incorrect
**Impact**: HIGH - Credentials exposed in logs
**Current State**: Password logged in src/server.js:123
**Required State**: No sensitive data in logs
**Evidence**:
```javascript
// src/server.js:123
console.log('Login attempt:', { username, password }); // VIOLATION
```

**Remediation**:
1. Remove password from log statement
2. Search codebase for other logging violations:
   ```bash
   grep -r "password\|secret\|token" src/ | grep "log\|console"
   ```
3. Add linter rule to prevent future violations

**Effort**: 2 hours
**Files to Modify**:
- src/server.js:123 (remove password from log)
- .eslintrc.js (add no-secrets rule)

**Test**: Review all logs, verify no credentials

### High Priority Gaps (P1)

#### GAP-3: Token Expiration Too Long (REQ: SEC-003)

**Category**: Incorrect
**Impact**: MEDIUM - Longer attack window if token stolen
**Current State**: 7 days (168 hours)
**Required State**: 24 hours max
**Evidence**: src/auth/jwt.js:34

**Remediation**:
```javascript
// src/auth/jwt.js:34
// Change from:
const token = jwt.sign(payload, secret, { expiresIn: '7d' });
// To:
const token = jwt.sign(payload, secret, { expiresIn: '24h' });
```

**Effort**: 30 minutes
**Files to Modify**: src/auth/jwt.js:34
**Test**: Verify token expires after 24h

### Medium Priority Gaps (P2)

[Similar structure for medium priority items]

### Low Priority Gaps (P3)

[Similar structure for low priority items]
```

### Step 5: Compliance Reporting

**Goal**: Present findings in clear, actionable format

**Actions**:
1. Calculate metrics:
   - Overall compliance rate (% fully met)
   - Compliance by category (security, functional, etc.)
   - Critical vs. non-critical compliance
   - Trend (improving/declining if historical data)

2. Create executive summary:
   - Compliance level (%)
   - Critical gaps (count and types)
   - Overall recommendation (pass/fail/conditional)
   - Key risks
   - Timeline to full compliance

3. Build detailed compliance table:
   - All requirements with status
   - Evidence or gap description
   - Priority for gaps

4. Highlight top issues:
   - 3-5 most critical gaps
   - Specific file:line references
   - Concrete remediation steps

5. Provide roadmap to full compliance:
   - Phase 1: Critical gaps (timeline)
   - Phase 2: High priority (timeline)
   - Phase 3: Medium/Low priority (timeline)

**Quality Check**:
- [ ] Metrics calculated accurately
- [ ] Executive summary concise
- [ ] Detailed table complete
- [ ] Top issues actionable
- [ ] Roadmap realistic

**Report Template**:
```markdown
# Documentation Compliance Report

## Executive Summary

**Date**: 2024-11-18
**Scope**: Authentication system compliance with Security Policy v2.0
**Overall Compliance**: 60% (15/25 requirements fully met)
**Recommendation**: ⚠️ **CONDITIONAL PASS** - Fix 3 critical gaps before production

**Key Findings**:
- ✅ Password hashing implemented correctly (bcrypt)
- ✅ HTTPS enforced on all endpoints
- ❌ No input validation (critical gap)
- ❌ Passwords found in logs (critical gap)
- ⚠️ Rate limiting incomplete (only on login)

**Risks**:
- HIGH: Injection vulnerabilities without input validation
- HIGH: Credential exposure in application logs
- MEDIUM: Extended attack window with 7-day tokens

**Timeline to Full Compliance**:
- Week 1: Fix critical gaps (2) → 80% compliance
- Week 2-3: Fix high priority gaps (3) → 95% compliance
- Month 2: Complete remaining items → 100% compliance

## Scope

**Verifying**: Authentication system implementation
**Against**: Security Policy v2.0 (25 requirements)
**Coverage**: src/auth/, src/middleware/, src/routes/auth.js
**Out of Scope**: Frontend, deployment, infrastructure

## Documentation Sources

1. **Security Policy v2.0** (primary)
   - Location: .claude/policies/security.md
   - Date: 2024-10-15
   - Requirements: 20
   - Status: Current

2. **API Specification v2.1** (secondary)
   - Location: docs/api-spec.md
   - Date: 2024-11-01
   - Requirements: 5
   - Status: Current

## Compliance Overview

| Category | Total | Fully Met | Partially Met | Not Met | % Fully | % Total |
|----------|-------|-----------|---------------|---------|---------|---------|
| Security | 15 | 8 | 4 | 3 | 53% | 80% |
| Functional | 8 | 6 | 1 | 1 | 75% | 88% |
| Performance | 2 | 1 | 0 | 1 | 50% | 50% |
| **Total** | **25** | **15** | **5** | **5** | **60%** | **80%** |

**Note**: % Total includes Partially Met as progress toward full compliance

## Detailed Compliance

[Include full verification table from Step 3]

## Critical Gaps

[Include detailed gap analysis from Step 4, focusing on P0 items]

## Recommendations

### Immediate Actions (Week 1) - CRITICAL

- [ ] **GAP-1**: Implement input validation (3 days, P0)
  - File: src/middleware/validate.js (create)
  - Install: joi or express-validator
  - Apply: All routes in src/routes/

- [ ] **GAP-2**: Remove passwords from logs (2 hours, P0)
  - File: src/server.js:123
  - Search: grep -r "password.*log" src/
  - Add: Linter rule to prevent recurrence

### Short-Term (Week 2-3) - HIGH

- [ ] **GAP-3**: Fix token expiration (30 min, P1)
  - File: src/auth/jwt.js:34
  - Change: '7d' → '24h'

- [ ] **GAP-4**: Complete rate limiting (1 day, P1)
  - Files: src/routes/*.js
  - Add: Rate limiting to all API endpoints

### Medium-Term (Month 2) - MEDIUM/LOW

[List P2 and P3 items]

## Compliance Roadmap

**Phase 1 (Week 1)**: Fix Critical Gaps
- Close GAP-1 and GAP-2
- Result: 80% compliance (20/25)
- Risk: Reduced to MEDIUM

**Phase 2 (Week 2-3)**: Fix High Priority
- Close GAP-3, GAP-4, GAP-5
- Result: 95% compliance (24/25)
- Risk: LOW

**Phase 3 (Month 2)**: Complete Remaining
- Close all P2/P3 items
- Result: 100% compliance (25/25)
- Risk: NONE

**Milestone**: Ready for production after Phase 1

## Assumptions

1. Security Policy v2.0 is current and authoritative
2. No new requirements will be added during remediation
3. Team has capacity for fixes per timeline
4. Testing environment available for validation

## Contradictions Found

None identified. All documentation sources aligned.

## Attachments

- requirements_list.csv (all 25 requirements)
- evidence_files.zip (code excerpts)
- gap_details.md (full gap analysis)
```

## Output Format

**Always structure compliance reports with**:
1. Executive summary with compliance %
2. Scope and sources
3. Compliance overview table
4. Detailed verification table
5. Gap analysis with priorities
6. Specific recommendations with file:line
7. Roadmap to full compliance
8. Assumptions and limitations

## Common Verification Patterns

### API Documentation vs. Implementation

```markdown
1. Extract endpoints from API spec
2. Find route definitions in code
3. Compare:
   - Endpoint paths match?
   - HTTP methods correct?
   - Request parameters match?
   - Response formats match?
   - Error codes documented?
4. Report deviations with file:line
```

### Security Policy Compliance

```markdown
1. Extract security requirements
2. Search codebase for implementation:
   - Authentication: grep -r "auth\|login\|password"
   - Authorization: grep -r "permission\|role\|access"
   - Encryption: grep -r "encrypt\|bcrypt\|crypto"
3. Build compliance checklist
4. Flag gaps with specific fixes
```

### Code Comments vs. Implementation

```markdown
1. Extract documented behavior from comments
2. Read actual implementation
3. Verify match:
   - Does code do what comment says?
   - Are parameters as documented?
   - Edge cases handled as described?
4. Update comments or fix code
```

## Integration with Agents

This skill is used by:
- **docs-agent**: Primary user of this skill
- **analyze-agent**: When analysis requires checking against docs

Works well with:
- **analysis**: For analyzing compliance results
- **implementation-guardrails**: Check documentation compliance before implementing

## Quick Reference

**When verifying**: Discover docs → Extract requirements → Verify → Analyze gaps → Report

**Key principle**: Evidence-based verification, specific file:line references, clear status (✅⚠️❌)

**Output must have**: Compliance %, detailed table, gap analysis with priorities, roadmap to 100%
