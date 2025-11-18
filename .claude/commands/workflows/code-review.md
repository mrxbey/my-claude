---
description: Comprehensive code review workflow orchestrating multiple agents
argument-hint: <path-to-review>
---

Perform a comprehensive code review using multiple specialized agents and skills.

## Task

Review code at: $ARGUMENTS

## Multi-Agent Workflow

This workflow orchestrates several agents for thorough code review:

### Phase 1: Initial Analysis (analyze-agent)

**Use analyze-agent** to understand the code:
1. Read and understand the code structure
2. Identify the purpose and main functionality
3. Note key design patterns and architecture
4. Map dependencies and relationships

**Deliverable**: Code analysis report with structure, purpose, and architecture overview

### Phase 2: Documentation Verification (docs-agent)

**Use docs-agent** to check documentation:
1. Find relevant documentation (README, inline comments, API docs)
2. Verify code matches documentation
3. Check for undocumented features
4. Identify documentation gaps

**Deliverable**: Compliance report showing doc accuracy and gaps

### Phase 3: Quality Analysis (analyze-agent + implementation-guardrails)

**Analyze code quality**:

1. **Code Quality Metrics**:
   - Complexity (cyclomatic complexity, nesting depth)
   - Maintainability (function length, modularity)
   - Readability (naming, comments, structure)

2. **Security Review**:
   - Input validation
   - Authentication/authorization
   - Sensitive data handling
   - Common vulnerabilities (OWASP Top 10)

3. **Performance Considerations**:
   - Algorithmic efficiency
   - Resource usage
   - Scaling implications
   - Bottlenecks

4. **Architecture Fit** (use implementation-guardrails):
   - Follows established patterns?
   - Respects layer boundaries?
   - Maintains dependency direction?
   - No circular dependencies?

**Deliverable**: Quality report with metrics, security findings, performance notes, architecture assessment

### Phase 4: Test Coverage Analysis

**Evaluate testing**:
1. Identify test files for this code
2. Check test coverage (unit, integration, e2e)
3. Evaluate test quality (assertions, edge cases, mocking)
4. Note missing tests

**Deliverable**: Test coverage report with gaps

### Phase 5: Best Practices Check

**Review against best practices**:
1. **Language-specific**:
   - Idioms and conventions
   - Standard library usage
   - Community best practices

2. **General practices**:
   - DRY (Don't Repeat Yourself)
   - SOLID principles
   - Error handling
   - Logging and monitoring

3. **Team standards**:
   - Coding style (from style guide)
   - Naming conventions
   - File organization

**Deliverable**: Best practices compliance report

### Phase 6: Synthesis & Recommendations

**Synthesize findings**:
1. Combine insights from all phases
2. Prioritize issues (Critical, High, Medium, Low)
3. Generate specific, actionable recommendations
4. Create improvement roadmap

**Deliverable**: Comprehensive code review report

## Output Format

Provide a complete code review report including:

### Executive Summary
- Overall assessment (Approve / Approve with changes / Request changes / Reject)
- Code quality rating (1-10)
- Critical issues count
- Recommendation summary

### Detailed Findings

#### 1. Code Structure & Architecture
- Overview of structure
- Architecture alignment
- Design patterns identified
- Concerns or improvements

#### 2. Documentation
- Documentation accuracy: X%
- Gaps identified
- Undocumented features
- Recommended doc updates

#### 3. Code Quality
**Metrics**:
- Complexity: [average cyclomatic complexity]
- Maintainability: [assessment]
- Readability: [assessment]

**Issues by Priority**:
- 🔴 Critical (X issues)
- 🟠 High (X issues)
- 🟡 Medium (X issues)
- 🟢 Low (X issues)

#### 4. Security
- Vulnerabilities found: X
- Security best practices: [compliance %]
- Critical security issues: [list]
- Recommendations: [specific fixes]

#### 5. Performance
- Potential bottlenecks: [list]
- Optimization opportunities: [list]
- Scaling concerns: [list]

#### 6. Testing
- Test coverage: X%
- Test quality: [assessment]
- Missing tests: [list]
- Test recommendations: [specific areas]

#### 7. Best Practices
- Compliance: X%
- Violations: [list with file:line]
- Recommendations: [specific improvements]

### Prioritized Issues

| Priority | Issue | File:Line | Impact | Recommendation |
|----------|-------|-----------|--------|----------------|
| 🔴 Critical | [Issue] | [Location] | [Impact] | [Fix] |

### Recommendations

**Immediate (Must Fix)**:
- [ ] [Critical issue 1 with file:line]
- [ ] [Critical issue 2 with file:line]

**Short-Term (Should Fix)**:
- [ ] [High priority issue 1]
- [ ] [High priority issue 2]

**Long-Term (Nice to Have)**:
- [ ] [Medium/Low priority improvements]

### Improvement Roadmap

**Week 1**: Fix critical issues → [expected outcome]
**Week 2-3**: Address high priority → [expected outcome]
**Month 2**: Implement improvements → [expected outcome]

## Quality Standards for Review

- **Thorough**: All phases completed systematically
- **Evidence-based**: Every finding has file:line reference
- **Specific**: Recommendations are actionable with exact fixes
- **Prioritized**: Clear critical/high/medium/low classification
- **Balanced**: Acknowledge both strengths and weaknesses
- **Constructive**: Focus on improvement, not criticism
