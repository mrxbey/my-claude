# User Guide: Workflows

## Overview

Workflows are multi-phase processes that orchestrate multiple agents, skills, and quality gates to complete complex tasks. They combine the power of all MyClaude framework components into structured, repeatable procedures.

Workflows are ideal for:
- **Complex processes**: Multi-step tasks with dependencies
- **Quality-critical work**: Production code, compliance, security
- **Team standardization**: Consistent execution across team
- **Best practice enforcement**: Built-in quality gates and validation

## How Workflows Work

### Workflow Structure

Workflows consist of:

```
Workflow = Phases + Agents + Skills + Quality Gates

Each Phase:
  ├─ Goal (What to achieve)
  ├─ Assigned Agent (Who does it)
  ├─ Actions (Step-by-step process)
  ├─ Skills (Domain expertise used)
  └─ Quality Gate (Validation checkpoint)
```

### Execution Flow

```
1. Phase 1 Execution
   ├─ Agent works autonomously
   ├─ Uses assigned skills
   ├─ Produces deliverable
   └─ Quality Gate Check
       ├─ PASS → Proceed to Phase 2
       └─ FAIL → Fix issues, retry

2. Phase 2 Execution
   ├─ Builds on Phase 1 output
   └─ [Same pattern...]

3. Phase N Execution
   └─ Final deliverable + report
```

### Quality Gates

Quality gates are validation checkpoints between phases:

```markdown
**Quality Gate**: [Question to answer]
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

**If PASS**: Proceed to next phase
**If FAIL**: [Remediation steps]
```

Example:
```markdown
**Quality Gate 1**: Do we understand the requirement fully?
- [ ] Requirements clear and unambiguous
- [ ] Acceptance criteria defined
- [ ] Constraints identified
- [ ] Scope bounded

**If FAIL**: Return to Phase 1, clarify with stakeholders
```

---

## Available Workflows

### Code Review Workflow

**Command**: `/workflows/code-review <path-to-review>`

**Purpose**: Comprehensive multi-agent code review with security, quality, and best practices analysis

**When to use**:
- Pre-merge code review
- Security audit
- Code quality assessment
- Knowledge transfer / onboarding
- Technical debt evaluation

#### Phases

**Phase 1: Initial Analysis** (analyze-agent)

Goal: Understand code structure, purpose, and architecture

Actions:
1. Read and understand code structure
2. Identify main functionality and purpose
3. Note design patterns and architecture
4. Map dependencies and relationships

Deliverable: Code analysis report with structure overview

---

**Phase 2: Documentation Verification** (docs-agent)

Goal: Verify code matches documentation

Actions:
1. Find relevant documentation (README, comments, API docs)
2. Check code matches documentation claims
3. Identify undocumented features
4. Document gaps and inaccuracies

Deliverable: Compliance report with ✅/⚠️/❌ status

---

**Phase 3: Quality Analysis** (analyze-agent + implementation-guardrails)

Goal: Evaluate code quality metrics, security, performance

Actions:
1. **Code Quality**:
   - Complexity metrics (cyclomatic complexity, nesting depth)
   - Maintainability (function length, modularity)
   - Readability (naming, comments, structure)

2. **Security Review**:
   - Input validation
   - Authentication/authorization
   - Sensitive data handling
   - OWASP Top 10 vulnerabilities

3. **Performance**:
   - Algorithmic efficiency
   - Resource usage
   - Scaling implications
   - Bottlenecks

4. **Architecture Fit** (implementation-guardrails):
   - Follows established patterns?
   - Respects layer boundaries?
   - Maintains dependency direction?
   - No circular dependencies?

Deliverable: Quality report with metrics, security findings, performance analysis

---

**Phase 4: Test Coverage Analysis**

Goal: Evaluate testing completeness and quality

Actions:
1. Identify test files for this code
2. Check coverage (unit, integration, e2e)
3. Evaluate test quality (assertions, edge cases, mocking)
4. Note missing tests

Deliverable: Test coverage report with gaps

---

**Phase 5: Best Practices Check**

Goal: Verify compliance with coding standards

Actions:
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

Deliverable: Best practices compliance report

---

**Phase 6: Synthesis & Recommendations**

Goal: Unified review with prioritized action items

Actions:
1. Combine insights from all phases
2. Prioritize issues (🔴 Critical, 🟠 High, 🟡 Medium, 🟢 Low)
3. Generate specific, actionable recommendations
4. Create improvement roadmap

Deliverable: Complete code review report

#### Output Format

```markdown
# Code Review: [Path]

## Executive Summary
- Overall assessment: [Approve / Approve with changes / Request changes / Reject]
- Code quality rating: [1-10]
- Critical issues: [count]
- High priority issues: [count]
- Recommendation: [summary]

## Detailed Findings

### 1. Code Structure & Architecture
- Overview: [description]
- Architecture alignment: [assessment]
- Design patterns: [identified patterns]
- Concerns: [issues]

### 2. Documentation
- Accuracy: [X%]
- Gaps: [list]
- Undocumented features: [list]
- Recommendations: [specific updates]

### 3. Code Quality
**Metrics**:
- Complexity: [average cyclomatic complexity]
- Maintainability: [assessment]
- Readability: [assessment]

**Issues by Priority**:
- 🔴 Critical (X issues)
- 🟠 High (X issues)
- 🟡 Medium (X issues)
- 🟢 Low (X issues)

### 4. Security
- Vulnerabilities: [count]
- Best practices compliance: [X%]
- Critical issues: [list with file:line]
- Recommendations: [specific fixes]

### 5. Performance
- Bottlenecks: [list]
- Optimization opportunities: [list]
- Scaling concerns: [list]

### 6. Testing
- Coverage: [X%]
- Quality: [assessment]
- Missing tests: [list]
- Recommendations: [specific areas]

### 7. Best Practices
- Compliance: [X%]
- Violations: [list with file:line]
- Recommendations: [improvements]

## Prioritized Issues

| Priority | Issue | File:Line | Impact | Recommendation |
|----------|-------|-----------|--------|----------------|
| 🔴 Critical | SQL injection risk | auth.js:45 | Security vulnerability | Use parameterized queries |
| 🔴 Critical | Passwords in plaintext | config.js:12 | Data breach risk | Hash with bcrypt |
| 🟠 High | No input validation | api.js:78 | Security risk | Add validation middleware |
| 🟡 Medium | Complex function (CC=15) | utils.js:234 | Maintainability | Refactor into smaller functions |

## Recommendations

**Immediate (Must Fix)**:
- [ ] Fix SQL injection in auth.js:45
- [ ] Hash passwords in config.js:12
- [ ] Add input validation to all API endpoints

**Short-Term (Should Fix)**:
- [ ] Refactor complex functions (5 identified)
- [ ] Add missing unit tests (coverage 45% → 80%)
- [ ] Update documentation for 3 undocumented endpoints

**Long-Term (Nice to Have)**:
- [ ] Consider caching layer for performance
- [ ] Evaluate alternative logging solution
- [ ] Improve error messages for better UX

## Improvement Roadmap

**Week 1**: Fix critical security issues → Production-safe
**Week 2-3**: Address high priority issues → Quality improved
**Month 2**: Implement improvements → Technical debt reduced
```

#### Example Usage

```
/workflows/code-review src/auth/

→ Reviews authentication module
→ 6-phase analysis with multiple agents
→ Comprehensive report with priorities
→ Actionable roadmap for improvements
```

---

### Feature Development Workflow

**Command**: `/workflows/feature-development <feature-description>`

**Purpose**: End-to-end feature development from requirements through deployment with quality gates

**When to use**:
- New feature development
- Complex changes to existing features
- Production-critical work
- When quality gates are essential

#### Phases

**Phase 1: Requirements Analysis** (analyze-agent)

Goal: Crystal-clear understanding of requirements

Actions:
1. **Clarify Requirements**:
   - Restate feature in your own words
   - Identify user stories
   - Define acceptance criteria
   - List functional and non-functional requirements
   - Define success metrics

2. **Analyze Context**:
   - How does this fit into existing system?
   - What components affected?
   - What dependencies exist?
   - What's in/out of scope?

3. **Identify Constraints**:
   - Technical constraints
   - Timeline constraints
   - Resource constraints
   - Compliance requirements

Deliverable: Requirements analysis document with clear acceptance criteria

Quality Gate 1: Do we understand the requirement fully?
- [ ] Requirements clear and unambiguous
- [ ] Acceptance criteria defined
- [ ] Constraints identified
- [ ] Scope bounded

---

**Phase 2: Pre-Implementation Validation** (implementation-guardrails)

Goal: Prevent building wrong thing

Actions: Run 5-check validation

1. **Duplicate Check** (0.0-1.0):
   - Does this functionality already exist?
   - Can we extend existing feature?

2. **Architecture Fit** (0.0-1.0):
   - Does approach align with architecture?
   - Following established patterns?

3. **Documentation Compliance** (0.0-1.0):
   - Consulted relevant docs and policies?
   - Respecting constraints?

4. **Existing Solutions** (0.0-1.0):
   - Can we use existing libraries/tools?
   - Why build custom?

5. **Problem Understanding** (0.0-1.0):
   - Solving root cause or symptom?
   - Simplest solution?

Calculate confidence: (D1 + D2 + D3 + D4 + D5) / 5

Deliverable: Confidence score and validation report

Quality Gate 2: Should we proceed with this approach?
- [ ] Confidence score ≥ 0.7 (preferably ≥ 0.9)
- [ ] No major architectural concerns
- [ ] No better existing solutions ignored
- [ ] Root cause understood

**If confidence < 0.7**: STOP and re-analyze with analyze-agent + doc-compliance

---

**Phase 3: Design** (analyze-agent)

Goal: Detailed technical design

Actions:
1. **High-Level Design**:
   - Component architecture
   - Data flow
   - API contracts
   - Integration points

2. **Detailed Design**:
   - Module breakdown
   - Class/function structure
   - Database schema changes
   - Configuration needs

3. **Evaluate Alternatives**:
   - Identify 2-3 design options
   - Compare pros/cons
   - Choose best with justification

4. **Plan Implementation**:
   - Break into tasks
   - Identify dependencies
   - Estimate effort
   - Define milestones

Deliverable: Design document with architecture, data flow, task breakdown

Quality Gate 3: Is the design sound?
- [ ] Design follows architecture patterns
- [ ] APIs well-defined
- [ ] Data flow clear
- [ ] Tasks broken down logically
- [ ] Estimates reasonable

---

**Phase 4: Documentation Planning** (docs-agent)

Goal: Plan documentation before coding

Actions:
1. **Identify docs to update**:
   - API documentation
   - User documentation
   - Developer documentation
   - README / CHANGELOG

2. **Create doc checklist**:
   - What needs documenting?
   - What format?
   - What audience?

3. **Draft API contracts** (if applicable):
   - Endpoint definitions
   - Request/response formats
   - Error codes
   - Examples

Deliverable: Documentation plan and API specs

Quality Gate 4: Documentation plan complete?
- [ ] All affected docs identified
- [ ] API contracts defined (if applicable)
- [ ] Examples planned

---

**Phase 5: Implementation**

Goal: Build the feature

Actions:
1. **Setup**:
   - Create feature branch
   - Set up development environment
   - Create initial file structure

2. **Implement Core Logic**:
   - Follow design document
   - Write clean, readable code
   - Add inline comments for complex logic
   - Follow coding standards

3. **Implement Tests** (parallel or TDD):
   - Unit tests for core logic
   - Integration tests for components
   - E2E tests for user flows
   - Edge cases and error handling

4. **Incremental Commits**:
   - Commit small, logical chunks
   - Write clear commit messages
   - Keep history clean

Deliverable: Working implementation with tests

Quality Gate 5: Implementation complete?
- [ ] All acceptance criteria met
- [ ] Tests written and passing
- [ ] Code follows standards
- [ ] No critical TODOs remaining

---

**Phase 6: Code Review** (runs `/workflows/code-review`)

Goal: Ensure code quality

Actions: Run full code review workflow on implementation

Deliverable: Code review report

Quality Gate 6: Code review passed?
- [ ] No critical issues
- [ ] High-priority issues addressed
- [ ] Security review clean
- [ ] Test coverage ≥ target (e.g., 80%)

---

**Phase 7: Documentation** (proofread-agent)

Goal: Complete and polished documentation

Actions:
1. Update API docs (if applicable)
2. Update user documentation
3. Update developer documentation
4. Update README and CHANGELOG
5. Add code examples
6. Proofread all documentation

Deliverable: Complete, polished documentation

Quality Gate 7: Documentation complete?
- [ ] All planned docs written
- [ ] Accuracy verified (matches implementation)
- [ ] Examples tested
- [ ] Proofread and polished

---

**Phase 8: Integration Testing**

Goal: Verify feature works in context

Actions:
1. **Integration testing**:
   - Test with other components
   - Test in staging environment
   - Test edge cases and error scenarios

2. **Performance testing** (if applicable):
   - Load testing
   - Stress testing
   - Performance profiling

3. **User acceptance testing** (if applicable):
   - Validate against user stories
   - Get stakeholder feedback

Deliverable: Test results and issues found

Quality Gate 8: Tests passing?
- [ ] All integration tests pass
- [ ] Performance acceptable
- [ ] UAT approved (if applicable)
- [ ] No blocking issues

---

**Phase 9: Final Review & Deployment Prep**

Goal: Ready for production

Actions:
1. **Final checks**:
   - All tests passing
   - Documentation complete
   - No TODOs or FIXMEs
   - Clean git history

2. **Deployment plan**:
   - Database migrations (if needed)
   - Configuration changes
   - Rollback plan
   - Monitoring plan

3. **Create pull request**:
   - Comprehensive PR description
   - Link to requirements/issues
   - Note any breaking changes
   - Request appropriate reviewers

Deliverable: Pull request ready for merge

Quality Gate 9: Ready for production?
- [ ] All quality gates passed
- [ ] PR approved
- [ ] Deployment plan ready
- [ ] Rollback plan defined
- [ ] Monitoring in place

#### Output Format

```markdown
# Feature Completion Report

**Feature**: [Name]
**Status**: ✅ Complete / ⚠️ Complete with notes / ❌ Blocked

## Quality Gates Summary

- ✅ Gate 1: Requirements Analysis (PASSED)
- ✅ Gate 2: Pre-Implementation Validation (Confidence: 0.92)
- ✅ Gate 3: Design Review (PASSED)
- ✅ Gate 4: Documentation Planning (PASSED)
- ✅ Gate 5: Implementation (PASSED)
- ✅ Gate 6: Code Review (PASSED)
- ✅ Gate 7: Documentation (PASSED)
- ✅ Gate 8: Integration Testing (PASSED)
- ✅ Gate 9: Final Review (PASSED)

## Deliverables

- ✅ Working implementation (src/feature/)
- ✅ Tests (tests/feature/) - Coverage: 85%
- ✅ Documentation (docs/feature.md, API docs)
- ✅ Pull Request (#123)

## Key Metrics

- Confidence Score: 0.92 (Pre-implementation)
- Code Coverage: 85%
- Code Review Issues: 2 medium (resolved)
- Documentation Pages: 3
- Development Time: 2 weeks

## Lessons Learned

**What went well**:
- Clear requirements from start saved rework
- Pre-implementation validation caught architecture issue early
- Test-driven approach ensured quality

**What could improve**:
- More stakeholder involvement in design phase
- Earlier performance testing would have caught scaling issue

**What to do differently next time**:
- Include performance requirements in initial analysis
- Create staging environment earlier in process
```

#### Example Usage

```
/workflows/feature-development user authentication system

→ 9-phase workflow from requirements to deployment
→ Multiple quality gates ensure quality
→ Comprehensive feature completion report
→ Production-ready deliverable
```

---

## Workflow Patterns

### Sequential Workflow

Phases execute one after another:

```
Phase 1 → Phase 2 → Phase 3 → Phase 4 → Done
```

Use when:
- Each phase depends on previous
- Clear linear progression
- Output builds incrementally

Example: Feature Development (requirements → design → implementation → testing → deployment)

---

### Parallel Workflow

Multiple phases execute simultaneously:

```
        ┌─ Phase 1A ─┐
Start ──┼─ Phase 1B ─┼─→ Synthesis → Done
        └─ Phase 1C ─┘
```

Use when:
- Phases are independent
- Want faster completion
- Different expertise areas

Example: Multi-file code review (each file reviewed in parallel, then synthesized)

---

### Iterative Workflow

Phases repeat until quality gate passes:

```
Phase 1 → Quality Gate
            ├─ PASS → Phase 2
            └─ FAIL → [Fix] → Phase 1 (retry)
```

Use when:
- Quality critical
- May need multiple attempts
- Improvement through iteration

Example: Pre-implementation validation (iterate until confidence ≥ 0.9)

---

### Branching Workflow

Different paths based on conditions:

```
Phase 1 → Decision Point
            ├─ Condition A → Path A → Done
            └─ Condition B → Path B → Done
```

Use when:
- Multiple valid approaches
- Context-dependent process
- Different scenarios

Example: Bug fix workflow (critical bug → hotfix path, minor bug → normal path)

---

## Creating Custom Workflows

### As Slash Command

Create workflow command in `.claude/commands/workflows/my-workflow.md`:

```markdown
---
description: Custom workflow for [purpose]
argument-hint: <what-arguments>
---

## Task
[Task description]: $ARGUMENTS

## Multi-Phase Workflow

### Phase 1: [Name] ([agent-name])

**Use [agent-name]** to [goal]:

**Actions**:
1. [Step 1]
2. [Step 2]

**Deliverable**: [What this phase produces]

**Quality Gate**: [Question]
- [ ] Criterion 1
- [ ] Criterion 2

**If gate fails**: [Remediation]

### Phase 2: [Name] ([agent-name])

[Same pattern...]

## Output Format

[Define structured output]

## Quality Standards

This workflow ensures:
- [Standard 1]
- [Standard 2]
```

### Workflow Design Checklist

When creating workflows, ensure:

- [ ] **Clear phases** (3-9 phases typical)
- [ ] **Assigned agents** (specific agent for each phase)
- [ ] **Defined goals** (what each phase achieves)
- [ ] **Quality gates** (validation between phases)
- [ ] **Structured output** (consistent deliverable format)
- [ ] **Remediation paths** (what to do when gates fail)
- [ ] **Integration points** (how phases connect)

---

## Best Practices

### Workflow Design

**✅ Good workflow design**:
- Clear separation of concerns (each phase has distinct purpose)
- Quality gates between critical phases
- Appropriate agents for each phase
- Documented remediation paths
- Structured, consistent output

**❌ Poor workflow design**:
- Too many phases (cognitive overload)
- Phases too granular or too broad
- No quality gates (quality issues compound)
- Unclear agent assignments
- Inconsistent output formats

### Quality Gate Design

**✅ Good quality gate**:
```markdown
**Quality Gate**: Is the design sound and complete?
- [ ] Architecture follows established patterns
- [ ] All APIs defined with request/response formats
- [ ] Data flow documented with diagram
- [ ] Edge cases identified and handled
- [ ] Performance implications considered

**If FAIL**: Return to design phase and address gaps
```

**❌ Poor quality gate**:
```markdown
**Quality Gate**: Is it good?
- [ ] Looks okay

**If FAIL**: Fix it
```

### Agent Assignment

**✅ Good agent assignment**:
```markdown
### Phase 1: Requirements Analysis (analyze-agent)
**Use analyze-agent** because this requires systematic decomposition

### Phase 2: Documentation Verification (docs-agent)
**Use docs-agent** because this requires compliance checking
```

**❌ Poor agent assignment**:
```markdown
### Phase 1: Do everything
**Use Claude** to do all the things
```

---

## Advanced Workflows

### Conditional Branches

```markdown
### Phase 2: Risk Assessment

**If HIGH RISK** (security-critical, data-sensitive):
  → Proceed to Phase 3A: Security Audit
  → Proceed to Phase 3B: Compliance Check

**If LOW RISK** (internal tool, no sensitive data):
  → Skip to Phase 4: Implementation
```

### Nested Workflows

```markdown
### Phase 3: Implementation

For each module in design:
  1. Run mini-workflow:
     - Design module
     - Implement module
     - Test module
     - Review module

  2. Quality Gate: Module complete?
```

### Parallel + Sequential Hybrid

```markdown
### Phase 2: Parallel Analysis

In parallel, run:
  - Phase 2A: Security Analysis (docs-agent)
  - Phase 2B: Performance Analysis (analyze-agent)
  - Phase 2C: Compliance Check (docs-agent)

### Phase 3: Synthesis
Combine all Phase 2 results into unified report
```

---

## Troubleshooting

### Workflow Takes Too Long

**Problem**: Workflow is slow to complete

**Solutions**:
- Reduce scope (focus on critical aspects)
- Combine related phases
- Use faster model (haiku) for simple phases
- Run phases in parallel where possible
- Skip optional phases for low-risk work

### Quality Gate Keeps Failing

**Problem**: Can't pass quality gate

**Solutions**:
- Review gate criteria (too strict?)
- Get more context for that phase
- Use different agent with more expertise
- Break phase into smaller steps
- Ask for human input if automated check insufficient

### Wrong Agent for Phase

**Problem**: Agent struggles with assigned phase

**Solutions**:
- Assign different agent with better expertise
- Provide more context to agent
- Break phase into smaller tasks
- Use skill to augment agent capabilities
- Consider creating custom agent for this workflow

### Workflow Produces Inconsistent Output

**Problem**: Output format varies each time

**Solutions**:
- Define stricter output template
- Add output format example to workflow
- Use quality gate to verify output format
- Consider using templates in skills
- Add validation step before final output

---

## Workflow Examples

### Example: Security Audit Workflow

```markdown
---
description: Comprehensive security audit workflow
argument-hint: <path-to-audit>
---

## Phase 1: Threat Modeling (analyze-agent)
Identify potential threats and attack vectors

## Phase 2: Code Review (docs-agent + analyze-agent)
Review code for security vulnerabilities

## Phase 3: Dependency Audit
Check for known vulnerabilities in dependencies

## Phase 4: Compliance Check (docs-agent)
Verify compliance with security policies

## Phase 5: Report & Recommendations
Prioritized security issues with remediation plan
```

### Example: Refactoring Workflow

```markdown
---
description: Safe refactoring workflow with testing
argument-hint: <path-to-refactor>
---

## Phase 1: Understand Current Code (analyze-agent)
Map current structure, identify refactoring targets

## Phase 2: Pre-Refactoring Tests
Ensure existing tests cover current behavior

## Phase 3: Design Refactoring (analyze-agent)
Plan refactoring approach with before/after structure

## Phase 4: Incremental Refactoring
Small refactorings with test runs between each

## Phase 5: Final Review (code-review workflow)
Comprehensive review of refactored code
```

---

## Next Steps

1. **Try existing workflows**: Run `/workflows/code-review` and `/workflows/feature-development`
2. **Study workflow patterns**: See how phases connect and quality gates work
3. **Create custom workflow**: Design workflow for your common tasks
4. **Iterate**: Refine workflows based on usage and results

## Related Documentation

- [Agents User Guide](agents.md) - Agents that execute workflow phases
- [Skills User Guide](skills.md) - Skills that enhance workflow capabilities
- [Commands User Guide](commands.md) - How to invoke workflows
- [Developer Guide: Creating Workflows](../developer-guide/creating-workflows.md)
