---
name: implementation-guardrails
description: 5-check validation before implementing to prevent building wrong things. Triggers - before implementing, validate approach, confidence check, quality gate, verify architecture.
version: 1.0.0
allowed-tools: Read, Grep, Glob, Bash
---

# Skill: Implementation Guardrails

## Purpose

This skill provides a systematic 5-dimensional validation process that runs BEFORE significant implementation work. It prevents common mistakes: building duplicates, violating architecture, ignoring documentation, reinventing wheels, and treating symptoms instead of root causes.

## When to Use

**ALWAYS use this skill before**:
- Implementing new features or capabilities
- Major refactoring or rewrites
- Adding new dependencies or tools
- Architectural changes
- Any work estimated > 1 day

**DO NOT use for**:
- Trivial fixes (typos, formatting)
- Hotfixes for production issues
- Proof-of-concept experiments
- Documentation-only changes

**Trigger scenarios**: "before I implement this", "validate this approach", "run quality gates", "check if this is the right way"

## Prerequisites

- Clear understanding of what you're about to implement
- Access to codebase and documentation
- Ability to search and read files
- Understanding of project architecture

## The 5-Check Validation System

This skill scores 5 dimensions from 0.0 to 1.0, then calculates overall confidence:

1. **Duplicate Check** (0.0-1.0)
2. **Architecture Fit** (0.0-1.0)
3. **Documentation Compliance** (0.0-1.0)
4. **Existing Solutions** (0.0-1.0)
5. **Problem Understanding** (0.0-1.0)

**Overall Confidence** = Average of 5 dimensions

**Decision Rules** (configurable via MYCLAUDE_QUALITY_GATE_THRESHOLD):
- **≥ 0.9**: ✅ Proceed with implementation
- **0.7-0.89**: ⚠️ Clarify missing pieces first
- **< 0.7**: ❌ Stop and re-analyze with analysis + doc-compliance skills

## Dimension 1: Duplicate Check

**Question**: Does this functionality already exist somewhere?

**Goal**: Prevent building redundant features

**Validation Process**:

1. **Search for similar functionality**:
   ```bash
   # Search for relevant keywords
   grep -r "authentication\|auth\|login" src/

   # Find files with related names
   find . -name "*auth*" -o -name "*login*"

   # Search for similar patterns
   grep -r "function.*validate" src/
   ```

2. **Check common locations**:
   - Core utilities (src/utils/, lib/, common/)
   - Similar feature modules
   - Base classes and interfaces
   - Shared components

3. **Review recent changes**:
   ```bash
   # Recent commits might have added this
   git log --all --oneline --grep="feature-keyword"

   # Recently modified files
   git log --since="3 months ago" --name-only | sort | uniq
   ```

4. **Ask questions**:
   - Does a module/function do this already?
   - Is there a partial implementation we can extend?
   - Is this functionality deprecated and needs replacement?

**Scoring**:
- **1.0**: Thoroughly searched, no duplicates found
- **0.8**: Searched common areas, likely no duplicates
- **0.6**: Some search done, but could have missed something
- **0.4**: Limited search, duplicates might exist
- **0.2**: No comprehensive search performed
- **0.0**: Found duplicates but ignoring them

**Red Flags** (Lower score):
- "I didn't check if this exists"
- "There might be something similar"
- "I found X but it's slightly different" (could extend X?)

**Green Flags** (Higher score):
- Searched multiple locations systematically
- Checked git history
- Verified no similar functionality
- Documented search process

## Dimension 2: Architecture Fit

**Question**: Does this approach align with existing architecture and patterns?

**Goal**: Prevent architectural violations and technical debt

**Validation Process**:

1. **Understand architecture**:
   - Read ARCHITECTURE.md, DESIGN.md, docs/architecture/
   - Review existing patterns in codebase
   - Identify architectural layers and boundaries

2. **Check alignment**:
   - **Pattern consistency**: Using established patterns?
   - **Layer respect**: Not violating layer boundaries?
   - **Dependency direction**: Following dependency rules?
   - **Module organization**: Fits existing structure?

3. **Review similar implementations**:
   ```bash
   # How do similar features work?
   grep -r "similar-feature" src/

   # Find architectural documentation
   find docs/ -name "*architecture*" -o -name "*design*"
   ```

4. **Questions to ask**:
   - Does this follow our established patterns (MVC, layered, microservices, etc.)?
   - Are we adding this to the right module/package?
   - Does this create circular dependencies?
   - Are we maintaining separation of concerns?

**Scoring**:
- **1.0**: Perfect alignment with architecture, follows all patterns
- **0.8**: Good fit, minor deviations are justified
- **0.6**: Acceptable but introduces some inconsistency
- **0.4**: Significant architectural concerns
- **0.2**: Major violations of architecture
- **0.0**: Completely breaks architectural principles

**Red Flags** (Lower score):
- "This is a special case, doesn't need to follow patterns"
- Creating new patterns without justification
- Violating layer boundaries
- Circular dependencies
- "We'll refactor later"

**Green Flags** (Higher score):
- Follows established patterns exactly
- Respects layer boundaries
- Maintains dependency direction
- Fits naturally into existing structure
- Extends rather than invents

## Dimension 3: Documentation Compliance

**Question**: Have we consulted relevant documentation and followed requirements?

**Goal**: Ensure compliance with specs, policies, and standards

**Validation Process**:

1. **Identify relevant docs**:
   - Technical specs (API docs, design docs)
   - Policies (security, coding standards)
   - Requirements (user stories, tickets)
   - Standards (industry standards, best practices)

2. **Check compliance**:
   ```bash
   # Find relevant documentation
   find docs/ -name "*spec*" -o -name "*policy*" -o -name "*standard*"

   # Search for requirements
   grep -r "MUST\|SHALL\|REQUIRED" docs/

   # Check CLAUDE.md for project rules
   cat CLAUDE.md | grep -i "requirement\|policy\|standard"
   ```

3. **Verify requirements**:
   - All explicit requirements addressed?
   - Security policies followed?
   - Performance requirements considered?
   - Compliance requirements met?

4. **Questions to ask**:
   - What docs are relevant to this implementation?
   - Have I read and understood them?
   - Am I following all requirements?
   - Any breaking changes or constraints?

**Scoring**:
- **1.0**: All relevant docs reviewed, full compliance
- **0.8**: Major docs reviewed, likely compliant
- **0.6**: Some docs reviewed, mostly compliant
- **0.4**: Limited doc review, compliance uncertain
- **0.2**: Haven't checked documentation
- **0.0**: Knowingly violating documented requirements

**Red Flags** (Lower score):
- "I didn't check the docs"
- "The docs are outdated" (without verification)
- "This is just a quick implementation"
- Skipping security policies
- Ignoring performance requirements

**Green Flags** (Higher score):
- All relevant docs identified and read
- Requirements mapped to implementation
- Compliance verified with evidence
- Exceptions documented and justified

## Dimension 4: Existing Solutions

**Question**: Have we evaluated existing libraries, tools, or approaches?

**Goal**: Prevent reinventing the wheel, prefer proven solutions

**Validation Process**:

1. **Search for existing solutions**:
   - npm, PyPI, Maven Central, etc.
   - Internal libraries and utilities
   - Industry-standard tools
   - Open-source projects

2. **Evaluate options**:
   - What libraries already do this?
   - What tools are standard in this domain?
   - Have others solved this problem?
   - What are the trade-offs?

3. **Document decision**:
   - If using existing: Which one and why?
   - If building custom: Why not use existing?
   - Trade-offs considered?

4. **Questions to ask**:
   - What's the standard way to do this?
   - Why not use library X?
   - What are we gaining by building custom?
   - Cost vs. benefit of custom implementation?

**Scoring**:
- **1.0**: Thoroughly evaluated options, decision well-justified
- **0.8**: Checked major options, reasonable choice
- **0.6**: Some evaluation, choice is acceptable
- **0.4**: Limited evaluation, might have better options
- **0.2**: No evaluation performed
- **0.0**: Ignoring obviously better existing solutions

**Red Flags** (Lower score):
- "Let's just build it ourselves"
- "I didn't check if a library exists"
- Not-Invented-Here syndrome
- Reinventing standard functionality
- Ignoring industry best practices

**Green Flags** (Higher score):
- Evaluated multiple existing solutions
- Documented trade-offs
- Clear justification for choice
- Using proven, maintained libraries
- Building custom only when clearly beneficial

## Dimension 5: Problem Understanding

**Question**: Do we understand the ROOT CAUSE, not just symptoms?

**Goal**: Prevent treating symptoms while ignoring underlying problems

**Validation Process**:

1. **Identify the problem**:
   - What's the actual problem we're solving?
   - Is this the root cause or a symptom?
   - How did we arrive at this solution?

2. **Apply "5 Whys"**:
   ```
   Problem: Users can't log in
   Why? → Server is slow
   Why? → Database queries are slow
   Why? → Missing indexes
   Why? → No performance testing in CI
   Why? → Performance wasn't prioritized

   Root Cause: Lack of performance testing process
   Solution: Add performance testing, THEN add indexes
   ```

3. **Validate approach**:
   - Does this solve the root cause?
   - Or just treat a symptom?
   - Will this create new problems?
   - Is there a simpler solution?

4. **Questions to ask**:
   - What problem does this actually solve?
   - Have I confirmed this is the root cause?
   - Will this prevent recurrence?
   - Am I adding complexity unnecessarily?

**Scoring**:
- **1.0**: Root cause clearly identified and addressed
- **0.8**: Good understanding, likely correct solution
- **0.6**: Partial understanding, solution might help
- **0.4**: Unclear if root cause vs. symptom
- **0.2**: Treating symptoms, not root cause
- **0.0**: Complete misunderstanding of problem

**Red Flags** (Lower score):
- "Let's add a workaround"
- "This quick fix should help"
- "We'll investigate the real cause later"
- Patch on top of patch
- Solving immediate symptom only

**Green Flags** (Higher score):
- Root cause analysis performed
- Clear causal chain documented
- Solution addresses root cause
- Will prevent recurrence
- Simplest solution that could work

## Confidence Calculation

**Overall Confidence Score** = (D1 + D2 + D3 + D4 + D5) / 5

Where D1-D5 are scores for each dimension (0.0-1.0)

**Example Calculation**:
```
Duplicate Check: 0.9 (searched thoroughly, no duplicates)
Architecture Fit: 0.8 (follows patterns, minor adjustments)
Documentation: 0.7 (major docs reviewed, one policy unclear)
Existing Solutions: 1.0 (evaluated libs, justified custom build)
Problem Understanding: 0.9 (root cause identified, solution appropriate)

Overall: (0.9 + 0.8 + 0.7 + 1.0 + 0.9) / 5 = 0.86
```

## Decision Rules

**Overall Confidence ≥ 0.9**: ✅ **PROCEED**
- All dimensions strong
- Implementation approach validated
- Risks understood and mitigated
- Ready for implementation

**Overall Confidence 0.7-0.89**: ⚠️ **CLARIFY FIRST**
- Good foundation but gaps exist
- Identify which dimensions are weak
- Address specific concerns
- Re-run validation after clarification

**Overall Confidence < 0.7**: ❌ **STOP - RE-ANALYZE**
- Significant gaps in validation
- High risk of building wrong thing
- Use analysis skill to understand better
- Use doc-compliance for requirements
- Revisit approach fundamentally

## Execution Process

### Step 1: Run All 5 Checks

For each dimension:
1. Follow validation process
2. Gather evidence
3. Answer key questions
4. Assign score (0.0-1.0)
5. Document rationale

### Step 2: Calculate Overall Score

```python
# Use provided script
python .claude/skills/implementation-guardrails/scripts/confidence_check.py

# Or calculate manually
overall = (d1 + d2 + d3 + d4 + d5) / 5
```

### Step 3: Make Decision

Based on score and decision rules:
- ≥ 0.9: Proceed
- 0.7-0.89: Clarify gaps
- < 0.7: Stop and re-analyze

### Step 4: Document Results

Record validation for future reference:

```markdown
## Implementation Guardrails Validation

**Task**: Implement user authentication system
**Date**: 2024-11-18

### Dimension Scores

1. **Duplicate Check**: 0.9
   - Searched src/auth/, src/security/, lib/
   - Checked git history (last 6 months)
   - Found old auth module (deprecated, removing)
   - Evidence: grep results, git log output

2. **Architecture Fit**: 0.8
   - Follows layered architecture (auth layer → business logic → data)
   - Uses existing security patterns (JWT, bcrypt)
   - Minor deviation: New middleware (justified for rate limiting)
   - Evidence: Matches patterns in src/middleware/

3. **Documentation Compliance**: 0.7
   - Reviewed Security Policy v2.0 (compliant)
   - Reviewed API Spec v2.1 (compliant)
   - ⚠️ Performance SLA unclear (need clarification)
   - Evidence: Policy checklist completed

4. **Existing Solutions**: 1.0
   - Evaluated: Passport.js, Auth0, custom
   - Choice: Passport.js (standard, well-maintained)
   - Custom parts: Rate limiting (no good lib), session store (Redis adapter)
   - Evidence: Comparison table in decision doc

5. **Problem Understanding**: 0.9
   - Root cause: No authentication (new system)
   - Not treating symptom (fresh implementation)
   - Requirements clear from user stories
   - Evidence: User stories US-101, US-102, US-103

### Overall Confidence: 0.86

**Decision**: ⚠️ **CLARIFY FIRST**
- Address: Performance SLA uncertainty (dimension 3)
- Action: Check with product team on SLA requirements
- Timeline: 1 day to clarify
- Then: Re-validate (expect score → 0.90+)

**After Clarification**: Proceed with implementation
```

## Integration with Pre-Commit Hooks

This skill can be enforced via hooks in `.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write(src/**)|Write(lib/**)",
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/skills/implementation-guardrails/scripts/confidence_check.py",
            "timeout": 60
          }
        ]
      }
    ]
  }
}
```

Hook will block writes if confidence < threshold.

## Output Template

```markdown
# Implementation Guardrails Validation

**Task**: [What you're about to implement]
**Date**: [Date]
**Threshold**: [Usually 0.7]

## Dimension Scores

### 1. Duplicate Check: [0.0-1.0]
**Score**: X.X
**Rationale**: [Why this score]
**Evidence**:
- [Search command 1 and results]
- [Search command 2 and results]
**Concerns**: [Any issues found]

### 2. Architecture Fit: [0.0-1.0]
**Score**: X.X
**Rationale**: [Why this score]
**Evidence**:
- [Architectural pattern being followed]
- [File/module showing pattern]
**Concerns**: [Any violations or deviations]

### 3. Documentation Compliance: [0.0-1.0]
**Score**: X.X
**Rationale**: [Why this score]
**Evidence**:
- [Doc 1 reviewed - compliant/not]
- [Doc 2 reviewed - compliant/not]
**Concerns**: [Any requirement gaps]

### 4. Existing Solutions: [0.0-1.0]
**Score**: X.X
**Rationale**: [Why this score]
**Evidence**:
- [Solution 1 evaluated - why chosen/rejected]
- [Solution 2 evaluated - why chosen/rejected]
**Concerns**: [Better alternatives?]

### 5. Problem Understanding: [0.0-1.0]
**Score**: X.X
**Rationale**: [Why this score]
**Evidence**:
- [Root cause analysis performed]
- [5 Whys if applicable]
**Concerns**: [Symptom vs. root cause]

## Overall Confidence

**Score**: X.XX (average of 5 dimensions)
**Threshold**: 0.7

**Decision**: [✅ PROCEED | ⚠️ CLARIFY | ❌ STOP]

## Rationale

[Explanation of decision based on scores]

## Required Actions

[If score < 0.9, list what needs to be done]

- [ ] [Action to improve dimension X]
- [ ] [Action to improve dimension Y]

## Approval

- [ ] All dimensions ≥ 0.7
- [ ] Overall confidence ≥ threshold
- [ ] Concerns addressed or documented
- [ ] Evidence gathered and reviewed
- [ ] Ready to proceed
```

## Integration with Agents

This skill is used by:
- **analyze-agent**: Before analysis leads to implementation recommendations
- Any agent before suggesting significant implementation

Works well with:
- **analysis**: For understanding problems deeply
- **doc-compliance**: For checking documentation requirements

## Quick Reference

**5 Dimensions**: Duplicate | Architecture | Documentation | Existing Solutions | Problem Understanding

**Scoring**: 0.0 (poor) → 1.0 (excellent)

**Decision**: ≥0.9 Proceed | 0.7-0.89 Clarify | <0.7 Stop

**Key principle**: Prevent building the wrong thing through systematic validation

**Always run before**: Significant implementations, refactoring, architecture changes, new dependencies
