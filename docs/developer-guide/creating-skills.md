# Developer Guide: Creating Skills

## Overview

This guide covers how to create custom skills for the MyClaude framework. Skills are reusable domain expertise that agents automatically load when relevant keywords appear in conversation.

## When to Create a Skill

Create a new skill when:

✅ **Reusable pattern**: Used across multiple projects or agents
✅ **Domain expertise**: Specialized knowledge to package
✅ **Progressive disclosure valuable**: Large reference material benefits from lazy loading
✅ **Multiple agents benefit**: Several agents will use this capability

❌ Don't create a skill when:

- One-off task or project-specific → Use instructions in agent instead
- Already covered by existing skill → Extend existing skill
- Too simple (just a checklist) → Include directly in agent workflow
- Won't be reused → Not worth the overhead

## Creation Methods

### Method 1: Using `/skill-crafter` (Recommended)

The fastest way to create a skill is using the meta-skill:

```
/skill-crafter Create a skill for API testing
```

The skill-crafter will:
1. Interview you about purpose and use cases
2. Design skill structure and workflow
3. Generate complete SKILL.md with proper frontmatter
4. Validate YAML and structure
5. Provide integration recommendations
6. Give you test scenarios

**Advantages**:
- Interactive design process
- Validates structure automatically
- Follows progressive disclosure pattern
- Generates complete file with proper keywords
- Provides testing guidance

### Method 2: Manual Creation

For full control or learning purposes, create manually:

```bash
# Create skill directory
mkdir -p .claude/skills/my-skill

# Create main skill file
touch .claude/skills/my-skill/SKILL.md

# Optional: Create reference materials
mkdir -p .claude/skills/my-skill/references
touch .claude/skills/my-skill/references/detailed-framework.md

# Optional: Create templates
mkdir -p .claude/skills/my-skill/templates
touch .claude/skills/my-skill/templates/report-template.md

# Optional: Create scripts
mkdir -p .claude/skills/my-skill/scripts
touch .claude/skills/my-skill/scripts/automation.py
```

**Advantages**:
- Full control over structure
- Learn skill anatomy deeply
- Customize without constraints

## Progressive Disclosure Pattern

Skills use a 3-level loading strategy:

### Level 1: Metadata (~50 tokens, always loaded)

```yaml
---
name: skill-name
description: What skill does, when to use. Trigger keywords - kw1, kw2, kw3, kw4, kw5, kw6, kw7, kw8, kw9, kw10.
version: 1.0.0
allowed-tools: Read, Grep, Glob
project: false
---
```

**Loaded**: At framework startup (all skills)
**Purpose**: Enable skill discovery and triggering
**Token budget**: ~50 tokens per skill

### Level 2: Core Instructions (~500 tokens, loaded when triggered)

```markdown
# Skill Name

## Purpose
[Clear statement of what this provides]

## When to Use
[3-5 scenarios]

## Workflow
[3-6 phases with goals, actions, quality checks]

## Quick Reference
[Essential patterns, checklists]
```

**Loaded**: When skill triggers (keywords match)
**Purpose**: Provide workflow and essential patterns
**Token budget**: ~500 tokens

### Level 3: References (~2000+ tokens, loaded on demand)

```markdown
# Detailed Frameworks

## Framework 1: [Name]
[Complete methodology with examples]

## Framework 2: [Name]
[Complete methodology with examples]

[8 more frameworks...]
```

**Loaded**: When explicitly needed ("use SWOT analysis")
**Purpose**: Deep expertise and detailed methodologies
**Token budget**: ~2000+ tokens

**Benefits**:
- Startup: <500 tokens for all skills metadata
- Active use: ~1000 tokens (metadata + core)
- Deep expertise: ~3000+ tokens (metadata + core + references)
- Supports unlimited skills without context overflow

## Skill File Structure

### Simple Skill (Instructions Only)

```
.claude/skills/my-skill/
└── SKILL.md
```

**Use for**:
- Straightforward workflows
- Checklists
- Basic patterns
- No complex reference material

**Example**: Code review checklist skill

---

### Medium Skill (Instructions + References)

```
.claude/skills/my-skill/
├── SKILL.md
└── references/
    ├── framework1.md
    └── framework2.md
```

**Use for**:
- Multiple frameworks or methodologies
- Detailed reference material
- Level 3 loading beneficial

**Example**: `analysis` skill with 10 frameworks

---

### Complex Skill (Full Suite)

```
.claude/skills/my-skill/
├── SKILL.md
├── references/
│   ├── specifications.md
│   └── best-practices.md
├── scripts/
│   └── validation.py
└── templates/
    ├── report-template.md
    └── checklist-template.md
```

**Use for**:
- Automated validation
- Standardized outputs
- Complex workflows
- Multiple supporting files

**Example**: `implementation-guardrails` with validation script

## SKILL.md Template

```markdown
---
name: skill-name
description: What this skill does, when to use it, what problems it solves. Use for [use-case-1], [use-case-2], [use-case-3]. Trigger keywords - keyword1, keyword2, keyword3, keyword4, keyword5, keyword6, keyword7, keyword8, keyword9, keyword10, keyword11, keyword12.
version: 1.0.0
allowed-tools: Read, Grep, Glob, Bash
project: false
---

# [Skill Name] Skill

## Purpose

[Clear 2-3 sentence statement of what this skill provides and why it's valuable]

## When to Use

Use this skill when:
- [Specific scenario 1]
- [Specific scenario 2]
- [Specific scenario 3]
- [Specific scenario 4]
- [Specific scenario 5]

Do NOT use when:
- [Anti-pattern 1]
- [Anti-pattern 2]

## Prerequisites

Before using this skill, ensure:
- [ ] [Prerequisite 1]
- [ ] [Prerequisite 2]
- [ ] [Prerequisite 3]

## Workflow

### Phase 1: [Name]

**Goal**: [What this phase achieves - single clear objective]

**Actions**:
1. [Concrete actionable step]
2. [Concrete actionable step]
3. [Concrete actionable step]
4. [Concrete actionable step]

**Quality Check**:
- [ ] [Testable validation criterion]
- [ ] [Testable validation criterion]
- [ ] [Testable validation criterion]

**If quality check fails**: [Specific remediation steps]

### Phase 2: [Name]

[Same pattern... 3-6 phases total]

## Output Format

[Define structured output template]

```markdown
# [Standard Output Format]

## [Section 1]
[Expected content structure]

## [Section 2]
[Expected content structure]

## [Action Items]
- [ ] [Actionable item template]
```

## Quick Reference

### [Pattern/Framework/Checklist 1]

[Essential information for quick access]

### [Pattern/Framework/Checklist 2]

[Essential information for quick access]

[3-5 quick reference items]

## Integration

**Used by agents**:
- `[agent-1]`: [How they use this skill]
- `[agent-2]`: [How they use this skill]

**Combines well with**:
- `[skill-1]`: [How they complement each other]
- `[skill-2]`: [How they complement each other]

**Related tools**:
- [Tool 1]: [When to use]
- [Tool 2]: [When to use]

## Examples

### Example 1: [Typical Scenario]

**Context**: [Situation description]

**Using this skill**:
1. [Phase 1 application]
2. [Phase 2 application]
3. [Phase 3 application]

**Result**: [Outcome achieved]

### Example 2: [Edge Case]

[Same pattern...]

[2-3 examples total]

## Notes

- [Important consideration 1]
- [Important consideration 2]
- [Gotcha or limitation]

## Version History

- **1.0.0** (YYYY-MM-DD): Initial release
  - [Feature 1]
  - [Feature 2]
```

## YAML Frontmatter Reference

### Required Fields

**`name`**: Skill identifier (lowercase, hyphenated)
```yaml
name: api-testing
```

**`description`**: What + when + keywords (150-250 chars)

Must include:
- What the skill does (20-40 chars)
- When to use it (20-40 chars)
- Use cases (30-50 chars)
- 10-15 trigger keywords

```yaml
description: API testing patterns including endpoint validation, response verification, error handling. Use for API development, integration testing, contract validation. Trigger keywords - API, test, testing, endpoint, validation, verify, response, request, integration, contract, REST, GraphQL, HTTP, status-code.
```

**`version`**: Semantic versioning
```yaml
version: 1.0.0
```

Format: `MAJOR.MINOR.PATCH`
- MAJOR: Breaking changes to workflow or output
- MINOR: New features, new frameworks added
- PATCH: Bug fixes, clarifications

### Optional Fields

**`allowed-tools`**: Tools this skill needs
```yaml
allowed-tools: Read, Grep, Glob, Bash
```

Options: `Read`, `Grep`, `Glob`, `Edit`, `Write`, `Bash`, `Task`, `WebFetch`

**`project`**: Is this project-specific or managed?
```yaml
project: false
```

- `false`: Managed skill (part of framework)
- `true`: Project-specific skill (custom for this project)

## Trigger Keywords Strategy

### Keywords Formula

Include 10-15 keywords covering:

**1. Primary actions (2-3)**:
```
test, testing, validate
```

**2. Domain terms (3-4)**:
```
API, endpoint, REST, HTTP
```

**3. Related concepts (2-3)**:
```
integration, contract, response
```

**4. Use cases (2-3)**:
```
development, verification, quality
```

**5. Specific frameworks/patterns (1-2)**:
```
GraphQL, status-code
```

### Good Description Examples

**Analysis skill**:
```yaml
description: Systematic analysis patterns including SWOT, cost-benefit, risk matrices, decision matrices. Use for complex decisions, strategic evaluation, multi-factor comparison, options analysis, trade-off analysis. Trigger keywords - analyze, analysis, evaluate, assessment, compare, investigate, examine, study, review, decision, strategic, options, SWOT, cost-benefit, breakdown.
```

**Why this works**:
- ✅ Clear what it does (analysis patterns)
- ✅ Lists specific frameworks (SWOT, cost-benefit, etc.)
- ✅ Clear when to use (complex decisions, strategic evaluation)
- ✅ 15 diverse keywords (analyze, evaluate, SWOT, etc.)

**API Testing skill**:
```yaml
description: API testing patterns including endpoint validation, response verification, error handling. Use for API development, integration testing, contract validation. Trigger keywords - API, test, testing, endpoint, validation, verify, response, request, integration, contract, REST, GraphQL, HTTP, status-code.
```

**Why this works**:
- ✅ Domain clear (API testing)
- ✅ Specific patterns (endpoint validation, etc.)
- ✅ Clear use cases (API development, integration testing)
- ✅ 14 targeted keywords

### Poor Description Examples

❌ **Too vague**:
```yaml
description: Helps with testing
```

Problems:
- No specific patterns mentioned
- No clear use cases
- No trigger keywords

❌ **Too narrow**:
```yaml
description: REST API endpoint testing only. Trigger keywords - REST.
```

Problems:
- Too specialized (misses GraphQL, HTTP, etc.)
- Only 1 keyword (won't trigger reliably)
- Limited use cases

## Workflow Design

### Phase Structure Template

```markdown
### Phase [N]: [Descriptive Name]

**Goal**: [Single clear objective - what is achieved]

**Actions**:
1. [Concrete step with specific tool/command if applicable]
2. [Concrete step with expected outcome]
3. [Concrete step with what to look for]
4. [Concrete step with decision point if applicable]

**Quality Check**:
- [ ] [Testable criterion with specific threshold if applicable]
- [ ] [Testable criterion with clear pass/fail]
- [ ] [Testable criterion with measurable outcome]

**If quality check fails**: [Specific remediation - what to do next]

**Output**: [What this phase produces]
```

### Good Workflow Example (5 phases)

```markdown
## Workflow

### Phase 1: Discover API Endpoints

**Goal**: Complete inventory of all API endpoints to test

**Actions**:
1. Read API specification files (OpenAPI/Swagger if available)
2. Grep codebase for route definitions (@app.route, @router, etc.)
3. Extract HTTP methods (GET, POST, PUT, DELETE) for each endpoint
4. Document authentication requirements per endpoint
5. List query parameters and request body schemas

**Quality Check**:
- [ ] All endpoints documented with method + path
- [ ] Authentication requirements noted
- [ ] Request/response schemas identified
- [ ] No duplicate endpoints in list

**If quality check fails**: Search additional files (config/, routes/, controllers/), check for API gateway definitions

**Output**: Endpoint inventory table with auth, params, schemas

### Phase 2: Design Test Cases

**Goal**: Comprehensive test coverage for each endpoint

**Actions**:
1. For each endpoint, create test cases:
   - Happy path (valid request → expected response)
   - Invalid auth (no token, expired token, wrong permissions)
   - Invalid input (missing required, wrong type, boundary values)
   - Error conditions (server error, not found, conflict)
2. Define expected status codes for each case
3. Define expected response structure
4. Identify integration dependencies (database, external APIs)

**Quality Check**:
- [ ] Each endpoint has 4+ test cases (happy, auth, invalid, error)
- [ ] Expected status codes documented
- [ ] Response structures defined
- [ ] Dependencies identified

**If quality check fails**: Add missing test cases, especially edge cases and error scenarios

**Output**: Test case specification with expected outcomes

### Phase 3: Implement Tests

[Similar structure...]

### Phase 4: Execute Tests

[Similar structure...]

### Phase 5: Report Results

[Similar structure...]
```

**Why this works**:
- Clear progression (Discover → Design → Implement → Execute → Report)
- Each phase builds on previous
- Concrete actions with specific tools
- Testable quality checks
- Clear output from each phase

### Poor Workflow Example

```markdown
## Workflow

### Phase 1: Test the APIs

**Actions**:
- Look at the APIs
- Write some tests
- Run them
- See if they work

**Check**: Is it good?
```

**Why this fails**:
- Too vague ("look at", "some tests")
- No clear goal
- No quality criteria
- No structure

## Quick Reference Design

Quick reference provides instant access to common patterns:

```markdown
## Quick Reference

### HTTP Status Code Guide

**2xx - Success**:
- 200 OK: Standard success
- 201 Created: Resource created
- 204 No Content: Success with no response body

**4xx - Client Error**:
- 400 Bad Request: Invalid syntax/parameters
- 401 Unauthorized: Authentication required
- 403 Forbidden: Authenticated but no permission
- 404 Not Found: Resource doesn't exist
- 422 Unprocessable Entity: Validation failed

**5xx - Server Error**:
- 500 Internal Server Error: Server failed
- 502 Bad Gateway: Upstream service failed
- 503 Service Unavailable: Temporarily down

### Common Test Patterns

**Authentication Test**:
```python
def test_endpoint_requires_auth():
    response = client.get("/api/resource")
    assert response.status_code == 401
```

**Happy Path Test**:
```python
def test_create_resource():
    response = client.post("/api/resource", json={"name": "test"}, headers=auth_headers)
    assert response.status_code == 201
    assert response.json["name"] == "test"
```

**Validation Test**:
```python
def test_invalid_input():
    response = client.post("/api/resource", json={})  # Missing required field
    assert response.status_code == 422
    assert "name" in response.json["errors"]
```

### Request Validation Checklist

- [ ] Required fields present
- [ ] Field types correct (string, int, bool)
- [ ] String lengths within bounds
- [ ] Numbers within valid ranges
- [ ] Email/URL formats valid
- [ ] Enum values from allowed set
- [ ] Foreign keys exist
- [ ] Business rules satisfied
```

**Why this works**:
- Organized by category
- Includes code examples
- Provides checklists
- Easy to scan

## Reference Files

### When to Use Reference Files

Use Level 3 references when:

✅ **Detailed frameworks**: Complex methodologies needing full explanation
✅ **Multiple options**: 5+ alternatives/patterns to choose from
✅ **Extensive examples**: Comprehensive examples that would bloat core
✅ **Specifications**: Full specs, RFCs, or standards

### Reference File Structure

```markdown
# Detailed API Testing Frameworks

## Framework 1: Contract Testing

**Purpose**: Verify API adheres to published contract (OpenAPI, GraphQL schema)

**When to use**:
- You have API specification
- Multiple consumers depend on API
- Breaking changes must be avoided

**Process**:
1. Load API specification (OpenAPI YAML/JSON)
2. For each endpoint in spec:
   - Generate test from schema
   - Validate request matches allowed params/body
   - Validate response matches schema
3. Run against actual implementation
4. Report discrepancies (spec vs. reality)

**Tools**:
- Dredd (OpenAPI contract testing)
- Pact (Consumer-driven contracts)
- Spectral (OpenAPI linting)

**Example**:
```yaml
# OpenAPI spec excerpt
/users/{id}:
  get:
    responses:
      200:
        content:
          application/json:
            schema:
              type: object
              required: [id, name, email]
              properties:
                id: {type: integer}
                name: {type: string}
                email: {type: string, format: email}
```

```python
# Contract test generated from spec
def test_get_user_matches_contract():
    response = client.get("/users/1")
    assert response.status_code == 200

    # Validate against schema
    schema = load_schema("/users/{id}", "get", "200")
    validate(response.json, schema)  # Throws if doesn't match
```

**Best for**: Established APIs with multiple consumers

---

## Framework 2: Property-Based Testing

[Same detailed structure...]

---

[8 more frameworks...]
```

### Linking to References

From SKILL.md, reference Level 3 content:

```markdown
## Workflow

### Phase 2: Choose Testing Strategy

**Goal**: Select appropriate testing framework

**Actions**:
1. Review **Detailed API Testing Frameworks** (in references/)
2. Consider:
   - Do you have an API spec? → Contract Testing
   - Complex input validation? → Property-Based Testing
   - User scenarios? → Behavior-Driven Testing
3. Choose framework(s) appropriate for your context

**Quality Check**:
- [ ] Framework selected with justification
- [ ] Framework appropriate for your API type
```

## Scripts and Automation

### When to Include Scripts

Include scripts when:

✅ **Automated validation**: Can programmatically check quality
✅ **Complex calculations**: Scoring, metrics, analysis
✅ **CI/CD integration**: Scripts run in pipelines
✅ **Repetitive tasks**: Common operations to automate

### Script Example

```python
#!/usr/bin/env python3
"""
API Testing Confidence Check

Calculates confidence score based on test coverage dimensions.
"""

import sys
import json
from typing import Dict, Tuple

def calculate_coverage(metrics: Dict[str, int]) -> float:
    """Calculate test coverage percentage"""
    if metrics["total_endpoints"] == 0:
        return 0.0
    return (metrics["tested_endpoints"] / metrics["total_endpoints"]) * 100

def calculate_confidence(metrics: Dict[str, any]) -> Tuple[float, str, str]:
    """
    Calculate overall testing confidence score.

    Returns: (confidence, decision, message)
    """

    # Dimension 1: Endpoint Coverage (0.0-1.0)
    coverage = calculate_coverage(metrics) / 100

    # Dimension 2: Test Variety (0.0-1.0)
    variety = min(metrics["test_types_used"] / 4, 1.0)  # 4 types: happy, auth, invalid, error

    # Dimension 3: Assertion Quality (0.0-1.0)
    assertion_quality = min(metrics["assertions_per_test"] / 3, 1.0)  # Target: 3+ assertions/test

    # Overall confidence
    confidence = (coverage + variety + assertion_quality) / 3

    # Decision
    if confidence >= 0.9:
        decision = "✅ PROCEED"
        message = "High confidence in test coverage"
    elif confidence >= 0.7:
        decision = "⚠️ IMPROVE"
        message = "Acceptable coverage, but improvements recommended"
    else:
        decision = "❌ INSUFFICIENT"
        message = "Test coverage insufficient for production"

    return confidence, decision, message

def main():
    """Main entry point"""

    # Example usage
    metrics = {
        "total_endpoints": 10,
        "tested_endpoints": 9,
        "test_types_used": 4,  # happy, auth, invalid, error
        "assertions_per_test": 2.5
    }

    confidence, decision, message = calculate_confidence(metrics)

    print(f"\n🎯 API Testing Confidence Score: {confidence:.2f}")
    print(f"{decision}: {message}\n")

    print("Dimensions:")
    print(f"  Coverage: {(metrics['tested_endpoints']/metrics['total_endpoints'])*100:.1f}%")
    print(f"  Variety: {min(metrics['test_types_used']/4, 1.0)*100:.1f}%")
    print(f"  Quality: {min(metrics['assertions_per_test']/3, 1.0)*100:.1f}%")

    # Exit code for CI/CD
    sys.exit(0 if confidence >= 0.7 else 1)

if __name__ == "__main__":
    main()
```

### Referencing Scripts from Workflow

```markdown
### Phase 5: Validate Coverage

**Goal**: Ensure test coverage meets quality standards

**Actions**:
1. Collect metrics:
   - Total endpoints vs. tested endpoints
   - Test types used (happy, auth, invalid, error)
   - Average assertions per test
2. Run confidence check script:
   ```bash
   python .claude/skills/api-testing/scripts/confidence_check.py
   ```
3. Review confidence score and decision

**Quality Check**:
- [ ] Confidence score ≥ 0.7
- [ ] All critical endpoints tested
- [ ] All 4 test types represented

**If quality check fails**: Add missing tests, increase assertions per test
```

## Templates

### When to Include Templates

Include templates for:

✅ **Standardized outputs**: Consistent report format across uses
✅ **Boilerplate structures**: Starting point for common documents
✅ **Complex formats**: Tables, checklists that benefit from template

### Template Example

```markdown
# API Test Report Template

## Executive Summary

- **API**: [API name and version]
- **Test Date**: [YYYY-MM-DD]
- **Overall Status**: ✅ Passing / ⚠️ Passing with warnings / ❌ Failing
- **Coverage**: [X]% ([tested]/[total] endpoints)
- **Test Quality**: [High/Medium/Low]

## Test Results

### Endpoint: [Method] [Path]

**Status**: ✅ Pass / ❌ Fail

**Test Cases**:

| Case | Expected | Actual | Status |
|------|----------|--------|--------|
| Happy path | 200 OK | 200 OK | ✅ |
| Invalid auth | 401 | 401 | ✅ |
| Missing param | 422 | 500 | ❌ |
| Not found | 404 | 404 | ✅ |

**Issues**:
- [Issue 1 description]
- [Issue 2 description]

[Repeat for each endpoint]

## Coverage Summary

| Category | Tested | Total | Coverage |
|----------|--------|-------|----------|
| Public endpoints | X | Y | Z% |
| Authenticated endpoints | X | Y | Z% |
| Admin endpoints | X | Y | Z% |
| **Total** | **X** | **Y** | **Z%** |

## Test Quality Metrics

- **Average assertions per test**: [X]
- **Test types coverage**:
  - ✅ Happy path (100%)
  - ✅ Authentication (100%)
  - ⚠️ Invalid input (75%)
  - ❌ Error handling (50%)

## Issues Found

### Critical Issues (Block Release)

1. **[Issue Title]**
   - Endpoint: [method] [path]
   - Expected: [expected behavior]
   - Actual: [actual behavior]
   - Impact: [description of impact]
   - Recommendation: [how to fix]

### High Priority Issues

[Same format]

### Medium Priority Issues

[Same format]

## Recommendations

- [ ] [Recommendation 1]
- [ ] [Recommendation 2]
- [ ] [Recommendation 3]

## Appendix

### Test Environment
- Base URL: [URL]
- Version: [version]
- Database: [details]

### Test Configuration
[Configuration details]
```

### Using Templates in Workflow

```markdown
## Output Format

Use the **API Test Report Template** (in templates/) to structure your output.

Fill in:
- Executive Summary with overall status
- Endpoint-by-endpoint results
- Coverage summary table
- Issues with priority levels
- Actionable recommendations
```

## Validation

### Use Framework Validator

```bash
python scripts/validate_framework.py --verbose
```

Checks:
- YAML frontmatter well-formed
- Required fields present
- Trigger keywords count (should have 10-15)
- Description length (100-250 chars recommended)
- Version format (semver)

### Manual Validation Checklist

**YAML Frontmatter**:
- [ ] `name` field present and lowercase-hyphenated
- [ ] `description` is 100-250 chars
- [ ] `description` includes 10-15 trigger keywords
- [ ] `version` uses semver format (X.Y.Z)
- [ ] `allowed-tools` list is valid (if present)
- [ ] `project` is boolean (if present)

**Progressive Disclosure**:
- [ ] Level 1 (metadata): <100 tokens
- [ ] Level 2 (core SKILL.md): <700 tokens
- [ ] Level 3 (references): Separate files

**Workflow**:
- [ ] 3-6 clear phases
- [ ] Each phase has Goal + Actions + Quality Check
- [ ] Quality checks are testable
- [ ] Remediation paths defined

**Quick Reference**:
- [ ] 3-5 quick reference items
- [ ] Code examples where applicable
- [ ] Easy to scan format

**Integration**:
- [ ] Documents which agents use this
- [ ] Lists complementary skills
- [ ] Provides 2-3 examples

**Output Format**:
- [ ] Structured template defined
- [ ] Consistent across uses

## Testing

### Test Triggering

1. **Create test request with keywords**:
   ```
   "I need to test the API endpoints for our user service"
   ```
   (Should trigger if keywords include: API, test, endpoints)

2. **Verify skill loads**:
   - Check skill name appears in context
   - Verify workflow is accessible
   - Confirm quick reference available

3. **Test Level 3 loading**:
   ```
   "Use contract testing framework from API testing skill"
   ```
   (Should load references/ files)

### Test Scenarios

```markdown
## Test Scenarios

### Test 1: Basic Triggering
**Keywords**: "API testing"
**Expected**: Skill loads, Level 2 content available
**Verify**: Workflow phases present, quick reference accessible

### Test 2: Specific Framework
**Keywords**: "Use contract testing for API"
**Expected**: Level 3 references load, contract testing framework available
**Verify**: Detailed methodology present with examples

### Test 3: Integration with Agent
**Setup**: Agent has `api-testing` in skills list
**Request**: "Use my-agent to test API"
**Expected**: Agent loads skill automatically
**Verify**: Agent can access workflow and frameworks
```

## Integration

### Add to Agent

Update agent's YAML frontmatter:

```yaml
---
name: api-development-agent
skills: api-testing, implementation-guardrails
---
```

Document in agent's "Skills I Use" section:

```markdown
## Skills I Use

**api-testing**:
- What: Provides API testing patterns and frameworks
- When: During Phase 3 (Testing) of my workflow
- How: Use contract testing for spec-driven APIs, property-based testing for complex validation
```

### Update README

Add to `.claude/skills/README.md`:

```markdown
#### api-testing

**Purpose**: API testing patterns including contract testing, property-based testing, integration testing

**When used**:
- API development and testing
- Integration testing
- Contract validation
- Quality assurance

**Frameworks provided**:
- Contract Testing (spec-driven)
- Property-Based Testing (input validation)
- Behavior-Driven Testing (user scenarios)
- Load Testing (performance)

**Tools**: Read, Grep, Glob, Bash
```

## Advanced Topics

### Skill Versioning

Use semantic versioning:

```yaml
version: 1.0.0
```

**When to bump**:

**MAJOR (1.0.0 → 2.0.0)**:
- Breaking changes to workflow structure
- Removed phases or frameworks
- Changed output format (incompatible)

**MINOR (1.0.0 → 1.1.0)**:
- Added new frameworks
- Added new phases (non-breaking)
- Enhanced existing capabilities

**PATCH (1.0.0 → 1.0.1)**:
- Bug fixes
- Clarifications
- Documentation improvements

### Multi-Skill Coordination

Skills can reference each other:

```markdown
## Integration

**Combines well with**:

**implementation-guardrails**:
- Use before implementing API tests
- Validates test strategy with 5-check system
- Ensures you're testing the right things

**Typical flow**:
1. Use `implementation-guardrails` to validate test approach
2. Use `api-testing` to implement tests
3. Use `doc-compliance` to verify API docs match implementation
```

### Conditional Framework Selection

```markdown
### Phase 2: Choose Testing Strategy

**Goal**: Select appropriate frameworks for your context

**Decision tree**:

```
Do you have API specification (OpenAPI, GraphQL schema)?
├─ YES → Use Contract Testing framework
│   └─ Multiple consumers? → Add Consumer-Driven Contracts
└─ NO → Use Behavior-Driven Testing framework
    └─ Complex input validation? → Add Property-Based Testing

Is performance critical?
└─ YES → Add Load Testing framework

Is this a critical production API?
└─ YES → Add all frameworks for comprehensive coverage
```

**Actions**:
1. Answer questions in decision tree
2. Select 1-3 frameworks
3. Document framework choices and rationale

**Quality Check**:
- [ ] Framework selection justified
- [ ] Frameworks appropriate for API type and criticality
```

## Common Patterns

### Analysis Skill Pattern

```yaml
name: domain-analysis
description: [domain] analysis patterns...
version: 1.0.0
```

Structure:
- Multiple analysis frameworks (5-10)
- Reference file with detailed methodologies
- Decision matrix for framework selection
- Output templates for each framework

### Verification Skill Pattern

```yaml
name: domain-compliance
description: [domain] verification patterns...
version: 1.0.0
```

Structure:
- Requirements extraction patterns
- Compliance table templates
- Gap analysis methodology
- Remediation roadmap templates

### Content Creation Skill Pattern

```yaml
name: domain-content
description: [domain] content creation patterns...
version: 1.0.0
```

Structure:
- Content structure patterns
- Style guide templates
- Quality checklists
- Example gallery

### Validation Skill Pattern

```yaml
name: domain-validation
description: [domain] validation patterns...
version: 1.0.0
```

Structure:
- Multi-dimensional scoring
- Validation scripts (Python)
- Decision thresholds
- Remediation pathways

## Troubleshooting

### Skill Not Loading

**Problem**: Skill doesn't seem to be available

**Solutions**:
- Check YAML frontmatter is valid (run validator)
- Verify file named exactly `SKILL.md` (case-sensitive)
- Ensure in correct directory: `.claude/skills/[skill-name]/`
- Add more trigger keywords to description
- Restart Claude Code to reload metadata

### Skill Loads But Missing Content

**Problem**: Skill triggers but workflow not available

**Solutions**:
- Check SKILL.md file is complete
- Verify no YAML parsing errors
- Check file encoding is UTF-8
- Review file permissions (readable)

### Reference Files Not Loading

**Problem**: Level 3 content not accessible

**Solutions**:
- Check files in `references/` directory
- Verify file names match references in SKILL.md
- Use explicit references: "Load contract testing from references"
- Check file paths are relative to skill directory

### Too Much Context Usage

**Problem**: Skill consuming too many tokens

**Solutions**:
- Move detailed content to references/
- Reduce Level 2 (core) to <500 tokens
- Keep metadata <50 tokens
- Use progressive disclosure properly
- Link to external docs instead of including

## Example: Complete Skill

See `.claude/skills/analysis/SKILL.md` for a complete production example with:
- Proper YAML frontmatter
- 6-phase workflow
- Quick reference section
- Integration documentation
- Multiple examples
- References file with 10 frameworks

## Next Steps

1. **Use `/skill-crafter`** to create your first custom skill
2. **Test thoroughly** with keyword triggering
3. **Validate** with framework validator
4. **Integrate** with relevant agents
5. **Document** in README
6. **Version control** and share with team

## Related Documentation

- [User Guide: Skills](../user-guide/skills.md)
- [Developer Guide: Creating Agents](creating-agents.md)
- [Developer Guide: Extending Framework](extending-framework.md)
- [Reference: Skill Specifications](../reference/skills-reference.md)
