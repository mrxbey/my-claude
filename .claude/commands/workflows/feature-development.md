---
description: Feature development workflow from analysis through implementation
argument-hint: <feature-description>
---

Complete feature development workflow using multiple agents and quality gates.

## Task

Develop feature: $ARGUMENTS

## Multi-Phase Workflow

This workflow guides feature development from conception through completion with built-in quality gates.

### Phase 1: Requirements Analysis (analyze-agent)

**Use analyze-agent** to understand requirements:

1. **Clarify Requirements**:
   - Restate feature in your own words
   - Identify user stories and acceptance criteria
   - List functional and non-functional requirements
   - Define success metrics

2. **Analyze Context**:
   - How does this fit into existing system?
   - What components are affected?
   - What dependencies exist?
   - What's the scope (in/out)?

3. **Identify Constraints**:
   - Technical constraints
   - Timeline constraints
   - Resource constraints
   - Compliance requirements

**Deliverable**: Requirements analysis document with clear acceptance criteria

**Quality Gate 1**: Do we understand the requirement fully?
- [ ] Requirements clear and unambiguous
- [ ] Acceptance criteria defined
- [ ] Constraints identified
- [ ] Scope bounded

### Phase 2: Pre-Implementation Validation (implementation-guardrails)

**Use implementation-guardrails skill** for 5-check validation:

1. **Duplicate Check** (0.0-1.0):
   - Does this functionality already exist?
   - Can we extend existing feature instead?

2. **Architecture Fit** (0.0-1.0):
   - Does this approach align with architecture?
   - Are we following established patterns?

3. **Documentation Compliance** (0.0-1.0):
   - Have we consulted relevant docs and policies?
   - Are we respecting constraints?

4. **Existing Solutions** (0.0-1.0):
   - Can we use existing libraries/tools?
   - Why build custom if alternatives exist?

5. **Problem Understanding** (0.0-1.0):
   - Are we solving root cause or symptom?
   - Is this the simplest solution?

**Calculate confidence**: (D1 + D2 + D3 + D4 + D5) / 5

**Deliverable**: Confidence score and validation report

**Quality Gate 2**: Should we proceed with this approach?
- [ ] Confidence score ≥ 0.7 (preferably ≥ 0.9)
- [ ] No major architectural concerns
- [ ] No better existing solutions ignored
- [ ] Root cause understood

**If confidence < 0.7**: Stop and re-analyze. Use analyze-agent + doc-compliance to address gaps.

### Phase 3: Design (analyze-agent)

**Design the solution**:

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
   - Choose best approach with justification

4. **Plan Implementation**:
   - Break into tasks
   - Identify dependencies
   - Estimate effort
   - Define milestones

**Deliverable**: Design document with architecture, data flow, task breakdown

**Quality Gate 3**: Is the design sound?
- [ ] Design follows architecture patterns
- [ ] APIs well-defined
- [ ] Data flow clear
- [ ] Tasks broken down logically
- [ ] Estimates reasonable

### Phase 4: Documentation Planning (docs-agent)

**Plan documentation before coding**:

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

**Deliverable**: Documentation plan and API specs

**Quality Gate 4**: Documentation plan complete?
- [ ] All affected docs identified
- [ ] API contracts defined (if applicable)
- [ ] Examples planned

### Phase 5: Implementation

**Implement the feature**:

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

**Deliverable**: Working implementation with tests

**Quality Gate 5**: Implementation complete?
- [ ] All acceptance criteria met
- [ ] Tests written and passing
- [ ] Code follows standards
- [ ] No critical TODOs remaining

### Phase 6: Code Review (use /code-review workflow)

**Review the implementation**:

Run the `/code-review` workflow on your implementation:
```
/code-review src/feature/
```

This will check:
- Code structure and architecture
- Documentation accuracy
- Code quality and security
- Test coverage
- Best practices

**Deliverable**: Code review report with issues

**Quality Gate 6**: Code review passed?
- [ ] No critical issues
- [ ] High-priority issues addressed
- [ ] Security review clean
- [ ] Test coverage ≥ target (e.g., 80%)

### Phase 7: Documentation

**Write the documentation**:

1. **Update API docs** (if applicable)
2. **Update user documentation**
3. **Update developer documentation**
4. **Update README and CHANGELOG**
5. **Add code examples**

**Use proofread-agent** to polish documentation

**Deliverable**: Complete, polished documentation

**Quality Gate 7**: Documentation complete?
- [ ] All planned docs written
- [ ] Accuracy verified (matches implementation)
- [ ] Examples tested
- [ ] Proofread and polished

### Phase 8: Integration Testing

**Test in context**:

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

**Deliverable**: Test results and any issues found

**Quality Gate 8**: Tests passing?
- [ ] All integration tests pass
- [ ] Performance acceptable
- [ ] UAT approved (if applicable)
- [ ] No blocking issues

### Phase 9: Final Review & Deployment Prep

**Prepare for deployment**:

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
   - Write comprehensive PR description
   - Link to requirements/issues
   - Note any breaking changes
   - Request appropriate reviewers

**Deliverable**: Pull request ready for merge

**Quality Gate 9**: Ready for production?
- [ ] All quality gates passed
- [ ] PR approved
- [ ] Deployment plan ready
- [ ] Rollback plan defined
- [ ] Monitoring in place

## Output Format

At the end of this workflow, provide:

### Feature Completion Report

**Feature**: [Name]
**Status**: ✅ Complete / ⚠️ Complete with notes / ❌ Blocked

**Quality Gates Summary**:
- ✅ Requirements Analysis
- ✅ Pre-Implementation Validation (Confidence: 0.92)
- ✅ Design Review
- ✅ Documentation Planning
- ✅ Implementation
- ✅ Code Review
- ✅ Documentation
- ✅ Integration Testing
- ✅ Final Review

**Deliverables**:
- [ ] Working implementation (src/feature/)
- [ ] Tests (tests/feature/)
- [ ] Documentation (docs/feature.md)
- [ ] Pull Request (#123)

**Key Metrics**:
- Confidence Score: 0.92
- Code Coverage: 85%
- Code Review Issues: 2 medium (resolved)
- Documentation Pages: 3

**Lessons Learned**:
- [What went well]
- [What could improve]
- [What to do differently next time]

## Quality Standards

This workflow ensures:
- **Quality-first**: Multiple validation gates prevent issues
- **Evidence-based**: Decisions backed by analysis
- **Well-documented**: Documentation planned and executed
- **Well-tested**: Comprehensive test coverage
- **Reviewable**: Clean code and clear commits
- **Production-ready**: All gates passed before deployment
