---
name: analysis
description: Systematic analysis patterns for complex problems including decomposition, options evaluation, risk assessment, and structured recommendations. Use for analysis tasks, strategic evaluation, multi-factor comparison, decision-making, or when systematic thinking is needed. Trigger keywords - analyze, analysis, evaluate, assessment, compare, options, strategy, investigate, examine, study, breakdown, insight.
version: 1.0.0
allowed-tools: Read, Grep, Glob, Bash
---

# Skill: Systematic Analysis

## Purpose

This skill provides systematic patterns for analyzing complex problems, evaluating options, assessing risks, and generating structured recommendations. It ensures thorough, evidence-based analysis that leads to actionable insights.

## When to Use

Use this skill when:
- Analyzing code, data, systems, or business situations
- Evaluating multiple options or approaches
- Making strategic decisions with trade-offs
- Assessing risks and opportunities
- Breaking down complex problems
- Comparing alternatives systematically
- Generating insights from information

**Trigger scenarios**: "analyze the architecture", "evaluate these options", "compare approaches", "assess the risks", "what's the best strategy"

## Prerequisites

- Clear understanding of what needs to be analyzed
- Access to relevant information (code, docs, data)
- Defined scope and boundaries
- Success criteria or decision factors

## Core Analysis Process

### Step 1: Clarification

**Goal**: Ensure clear understanding of the analysis target

**Actions**:
1. Restate the question in your own words
2. Identify exactly what is being analyzed:
   - Code/architecture/system?
   - Data/metrics/trends?
   - Business situation/decision?
   - Process/workflow?

3. List 2-4 sub-questions that must be answered
4. Define scope boundaries (what's in/out)
5. Identify success criteria or decision factors

**Quality Check**:
- [ ] Analysis target clearly defined
- [ ] Scope bounded and explicit
- [ ] Key questions identified
- [ ] Success criteria understood

**Example Output**:
```markdown
## Analysis Clarification

**Target**: Authentication system architecture
**Scope**: Code structure, security patterns, scalability (excluding deployment)
**Key Questions**:
1. How secure is the current implementation?
2. Will it scale to 10x users?
3. What are maintenance implications?
**Success Criteria**: Secure, scalable, maintainable
```

### Step 2: Decomposition

**Goal**: Break problem into manageable dimensions

**Actions**:
1. Identify analysis dimensions based on context:

   **Technical Dimensions**:
   - Architecture: Structure, patterns, modularity
   - Code Quality: Complexity, maintainability, testing
   - Performance: Speed, efficiency, scalability
   - Security: Vulnerabilities, attack surface, compliance

   **Business Dimensions**:
   - Value: Benefits, ROI, strategic fit
   - Cost: Development, operations, opportunity cost
   - Risk: What could go wrong, likelihood, impact
   - Timeline: Effort, dependencies, critical path

   **User Dimensions**:
   - Experience: Usability, satisfaction, adoption
   - Impact: Who's affected, how much, when

   **Operational Dimensions**:
   - Maintenance: Complexity, documentation, support
   - Monitoring: Observability, debugging, alerts
   - Integration: Dependencies, compatibility

2. For each relevant dimension:
   - List key factors to examine
   - Note constraints and limitations
   - Define what "good" looks like

3. Prioritize dimensions by importance

**Quality Check**:
- [ ] All relevant dimensions identified
- [ ] Factors are specific and measurable
- [ ] Constraints documented
- [ ] Priorities assigned

**Example Output**:
```markdown
## Dimension Analysis

### 1. Security (Critical)
**Factors**: Authentication method, session management, input validation, encryption
**Constraints**: Must meet OWASP standards
**Good**: Zero critical vulnerabilities, defense in depth

### 2. Scalability (High)
**Factors**: Concurrent users, response time, database load
**Constraints**: Must handle 10x growth
**Good**: Sub-200ms response, horizontal scaling

### 3. Maintainability (Medium)
**Factors**: Code complexity, documentation, test coverage
**Constraints**: Team of 3 developers
**Good**: < 15 cyclomatic complexity, 80%+ coverage
```

### Step 3: Investigation

**Goal**: Gather evidence for each dimension

**Actions**:
1. For each dimension, collect specific evidence:
   - Read relevant files/code
   - Search for patterns
   - Extract metrics and data
   - Review documentation
   - Check dependencies

2. Document findings with evidence:
   - Specific file and line references (file.js:123)
   - Code snippets showing patterns
   - Metrics and measurements
   - Quotes from documentation

3. Identify patterns and trends:
   - What's working well?
   - What's problematic?
   - What's missing?
   - What's surprising?

4. Cross-reference findings:
   - How do dimensions interact?
   - Are there conflicts or synergies?
   - What trade-offs exist?

**Quality Check**:
- [ ] Evidence collected for each dimension
- [ ] File references specific (file:line)
- [ ] Patterns documented with examples
- [ ] Cross-dimensional relationships noted

**Investigation Techniques**:

```bash
# Find code patterns
grep -r "pattern" src/

# Count occurrences
grep -r "TODO\|FIXME" . | wc -l

# Check file structure
find src/ -name "*.js" | head -20

# Analyze complexity (if tools available)
find src/ -name "*.py" -exec wc -l {} +
```

**Example Output**:
```markdown
## Investigation Findings

### Security Analysis
**Authentication**: JWT-based (src/auth/jwt.js:45)
- ✅ Uses bcrypt for password hashing (auth/hash.js:12)
- ⚠️ No rate limiting on login endpoint (routes/auth.js:23)
- ❌ Session tokens don't expire (auth/session.js:67)

**Evidence**:
```javascript
// src/auth/session.js:67
const token = jwt.sign(payload); // No expiration set!
```

**Pattern**: Security basics in place, but missing defense in depth
```

### Step 4: Options Analysis

**Goal**: Identify and evaluate possible approaches

**Actions**:
1. Identify 2-4 realistic options:
   - Status quo (do nothing)
   - Incremental improvements
   - Major rewrite/replacement
   - Hybrid approaches

2. For each option, document:
   - **Description**: What it involves
   - **Advantages**: Why it's good
   - **Disadvantages**: Trade-offs and costs
   - **Risks**: What could go wrong
   - **Effort**: Time, resources, complexity
   - **Impact**: On each dimension

3. Create comparison table:

| Dimension | Option A | Option B | Option C |
|-----------|----------|----------|----------|
| Security | Rating + note | Rating + note | Rating + note |
| Cost | $X, Y weeks | $X, Y weeks | $X, Y weeks |
| Risk | High/Med/Low | High/Med/Low | High/Med/Low |

4. Highlight key differentiators

**Quality Check**:
- [ ] Options are realistic and actionable
- [ ] All options evaluated on same dimensions
- [ ] Trade-offs explicitly stated
- [ ] Effort estimates provided

**Example Output**:
```markdown
## Options Comparison

### Option A: Add Security Patches
**Description**: Add rate limiting, token expiration, input validation to existing system
**Advantages**: Low cost, low risk, quick implementation
**Disadvantages**: Doesn't address architectural issues
**Effort**: 2 weeks, 1 developer
**Risk**: Low (incremental changes)

### Option B: Migrate to OAuth 2.0
**Description**: Replace custom JWT with industry-standard OAuth
**Advantages**: Battle-tested, good libraries, better security
**Disadvantages**: Learning curve, migration complexity
**Effort**: 6 weeks, 2 developers
**Risk**: Medium (migration risk)

### Option C: Keep Current System
**Description**: Accept current security posture
**Advantages**: Zero cost, no risk
**Disadvantages**: Vulnerable to attacks, compliance issues
**Effort**: 0
**Risk**: High (security incidents)

| Criteria | Option A | Option B | Option C |
|----------|----------|----------|----------|
| Security | ⚠️ Better | ✅ Best | ❌ Poor |
| Cost | ✅ Low ($10K) | ⚠️ Medium ($30K) | ✅ Zero |
| Risk | ✅ Low | ⚠️ Medium | ❌ High |
| Timeline | ✅ 2 weeks | ⚠️ 6 weeks | ✅ Now |
| **Recommendation** | **BEST** | Good if budget | Not recommended |
```

### Step 5: Synthesis

**Goal**: Generate clear recommendations

**Actions**:
1. Synthesize key insights (3-5 most important findings):
   - What are the critical discoveries?
   - What patterns emerged?
   - What's surprising or counterintuitive?

2. Make specific recommendations:
   - Recommend 1-2 options with clear justification
   - Provide decision criteria if multiple good options
   - Call out prerequisites and dependencies
   - Note what needs further investigation

3. Document assumptions and unknowns:
   - What did you assume?
   - What's uncertain?
   - What could change the recommendation?

4. Prioritize actions:
   - What's critical vs. nice-to-have?
   - What's quick win vs. long-term?
   - What are dependencies?

**Quality Check**:
- [ ] Top 3-5 insights identified
- [ ] Recommendations specific and actionable
- [ ] Justification evidence-based
- [ ] Assumptions explicit
- [ ] Priorities clear

**Example Output**:
```markdown
## Key Insights

1. **Security gaps are fixable**: Current system has good foundation but missing layers (rate limiting, token expiration)
2. **Quick wins available**: Can achieve 80% security improvement with 20% effort (2 weeks)
3. **Architecture is sound**: No need for major rewrite; incremental improvements sufficient
4. **Compliance deadline**: Must fix before Q2 audit (8 weeks away)

## Recommendation

**Recommend: Option A (Security Patches) + Plan for Option B**

**Rationale**:
- Addresses critical gaps quickly (2 weeks vs. 6 weeks)
- Low risk, high impact
- Buys time for proper OAuth migration later
- Meets compliance deadline with margin

**Prerequisites**:
- [ ] Get approval for 2-week sprint
- [ ] Allocate 1 senior developer
- [ ] Plan downtime for deployment

**Dependencies**:
- None (can start immediately)

**Follow-up**:
- Plan OAuth migration for Q3 (Option B)
- Monitor security metrics post-deployment
- Review in 3 months

## Assumptions

1. Team has capacity for 2-week sprint
2. Current JWT library supports token expiration (verified: yes)
3. No major features planned that would conflict
4. Q2 audit deadline is firm

## Further Investigation

- [ ] Load testing with rate limiting enabled
- [ ] Detailed OAuth migration estimate
- [ ] Review compliance requirements in detail
```

### Step 6: Presentation

**Goal**: Deliver analysis in clear, actionable format

**Actions**:
1. Structure with clear hierarchy:
   - Executive summary (2-3 sentences)
   - Context and goal
   - Key findings (bullets)
   - Detailed analysis (by dimension)
   - Options comparison (table)
   - Recommendations (prioritized)
   - Action checklist (concrete steps)

2. Use effective formatting:
   - Headings for structure
   - Bullets for lists
   - Tables for comparisons
   - **Bold** for emphasis
   - `code` for technical terms
   - ✅⚠️❌ for status indicators

3. Include evidence throughout:
   - File references (src/auth.js:45)
   - Code snippets
   - Metrics and data
   - Documentation quotes

**Quality Check**:
- [ ] Response is well-structured
- [ ] Key points stand out
- [ ] Evidence supports all claims
- [ ] Actions are concrete and sequenced

## Output Format Template

Use this structure for all analysis deliverables:

```markdown
# Analysis: [Topic]

## Executive Summary
[2-3 sentence overview of findings and recommendations]

## Context & Goal
**Analyzing**: [What]
**Purpose**: [Why]
**Scope**: [Boundaries]
**Success Criteria**: [What good looks like]

## Key Findings

1. **[Finding 1]** - [Evidence] → [Implication]
2. **[Finding 2]** - [Evidence] → [Implication]
3. **[Finding 3]** - [Evidence] → [Implication]
4. **[Finding 4]** - [Evidence] → [Implication]

## Detailed Analysis

### [Dimension 1: e.g., Technical Architecture]

**Current State**:
- [Observation with file:line reference]
- [Observation with evidence]

**Strengths**:
- [Strength with rationale]
- [Strength with rationale]

**Weaknesses**:
- [Weakness with impact]
- [Weakness with impact]

**Evidence**:
[Code snippet or data]

### [Dimension 2: e.g., Business Value]
[Similar structure]

## Options Comparison

| Criteria | Option A | Option B | Option C |
|----------|----------|----------|----------|
| [Criterion 1] | [Rating + note] | [Rating + note] | [Rating + note] |
| [Criterion 2] | [Rating + note] | [Rating + note] | [Rating + note] |
| **Cost** | [Estimate] | [Estimate] | [Estimate] |
| **Timeline** | [Estimate] | [Estimate] | [Estimate] |
| **Risk** | [H/M/L] | [H/M/L] | [H/M/L] |
| **Recommendation** | [Ranking] | [Ranking] | [Ranking] |

## Risks & Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | H/M/L | H/M/L | [How to prevent] |
| [Risk 2] | H/M/L | H/M/L | [How to prevent] |

## Recommendations

### Recommended Approach: [Option Name]

**Rationale**: [Why this option is best]

**Prerequisites**:
- [ ] [What needs to be in place first]
- [ ] [What needs to be in place first]

**Implementation Steps**:
1. [Step with timeline and owner]
2. [Step with timeline and owner]
3. [Step with timeline and owner]

**Success Metrics**:
- [How to measure success]
- [How to measure success]

### Alternative (If primary blocked): [Option Name]
[Brief description and when to consider]

## Action Checklist

**Immediate (This Week)**:
- [ ] [Specific action with file/command]
- [ ] [Specific action with file/command]

**Short-Term (This Month)**:
- [ ] [Specific action]
- [ ] [Specific action]

**Long-Term (This Quarter)**:
- [ ] [Specific action]
- [ ] [Specific action]

## Assumptions

1. [Assumption with verification status]
2. [Assumption with verification status]
3. [Assumption with verification status]

## Further Investigation Needed

1. [Question or area requiring more research]
2. [Question or area requiring more research]
```

## Analysis Frameworks

For detailed analysis frameworks and specialized patterns, see:
- **[frameworks.md](frameworks.md)** - Specific analysis frameworks (SWOT, cost-benefit, risk matrices)
- **[examples.md](examples.md)** - Complete analysis examples

Load these only when you need specific frameworks or want to see detailed examples.

## Common Pitfalls to Avoid

1. **Analysis Paralysis**: Don't gather evidence forever. Set time limit, then decide.
2. **Confirmation Bias**: Actively seek disconfirming evidence.
3. **Vague Recommendations**: "Improve security" is vague. "Add rate limiting to login endpoint" is specific.
4. **Missing Evidence**: Every claim needs file:line references or data.
5. **Ignoring Trade-offs**: No option is perfect. State the downsides clearly.
6. **Skipping Prioritization**: Not everything is P0. Rank by impact.

## Integration with Agents

This skill is used by:
- **analyze-agent**: Primary user of this skill
- Any agent needing systematic analysis patterns

Works well with:
- **implementation-guardrails**: Use before analysis to validate approach
- **doc-compliance**: Reference when analyzing against specifications

## Quick Reference

**When analyzing**: Clarify → Decompose → Investigate → Compare → Synthesize → Present

**Key principle**: Evidence over opinion, specific over vague, actionable over descriptive

**Output must have**: Executive summary, evidence-based findings, comparison table, specific recommendations, action checklist
