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

### Research & Synthesis Workflow

**Command**: `/workflows/research-synthesis <research-topic>`

**Purpose**: Conduct comprehensive, evidence-based research on any topic with systematic synthesis and professional reporting

**When to use**:
- Market research and competitive intelligence
- Literature reviews (academic or business)
- Due diligence and investment research
- Technology evaluation and vendor selection
- Strategic planning and trend analysis
- Policy research and best practices

#### Phases

**Phase 1: Question Clarification** (analyze-agent)

Goal: Define clear, bounded research question

Actions:
1. Restate research question in your own words
2. Break into 3-5 specific sub-questions
3. Define scope (what's IN vs OUT)
4. Identify success criteria and confidence level needed

Deliverable: Research brief with clear question, sub-questions, scope

Quality Gate 1: Research question well-defined and answerable?

---

**Phase 2: Source Discovery**

Goal: Identify relevant, credible sources

Actions:
1. Identify source types (internal/external, primary/secondary)
2. Use Glob/Grep for internal documents
3. Identify external sources (research, reports, data)
4. Evaluate source credibility and recency
5. Create annotated source list

Deliverable: Source list with credibility ratings

Quality Gate 2: At least 5-10 relevant, credible sources identified?

---

**Phase 3: Information Extraction**

Goal: Extract key information systematically

Actions:
1. Read each source and extract key facts, claims, data
2. Organize information by sub-question
3. Assess evidence quality (strong/moderate/weak)
4. Create evidence table mapping findings to sources

Deliverable: Evidence table with organized findings

Quality Gate 3: All sub-questions have sufficient evidence?

---

**Phase 4: Synthesis & Analysis** (analyze-agent)

Goal: Generate insights from evidence

Actions:
1. Identify patterns and themes across sources
2. Resolve contradictions between sources
3. Conduct gap analysis (what's missing?)
4. Generate insights and implications
5. Assign confidence levels to each finding

Deliverable: Synthesis document with patterns, insights, confidence levels

Quality Gate 4: Synthesis coherent with actionable insights?

---

**Phase 5: Evidence Validation**

Goal: Verify credibility and accuracy

Actions:
1. Cross-check claims across multiple sources
2. Detect potential biases
3. Verify logical consistency
4. Check recency of information
5. Rate overall research credibility (1-10)

Deliverable: Validation report with credibility assessment

Quality Gate 5: Evidence validated and biases identified?

---

**Phase 6: Report Generation**

Goal: Create professional research report

Actions:
1. Structure report (Executive Summary, Methodology, Findings, Analysis, Conclusions, Recommendations, Sources)
2. Write each section with evidence-based content
3. Add source citations for every claim
4. Include limitations and further research needs

Deliverable: Comprehensive research report

Quality Gate 6: Report complete, professional, and all findings cited?

#### Output Format

```markdown
# Research Report: [Topic]

## Executive Summary
- Bottom line answer
- 3-5 key findings with confidence levels
- Recommendations
- Limitations

## Key Findings
[For each sub-question: Answer, Evidence with sources, Confidence level]

## Analysis & Insights
[Patterns, surprising discoveries, implications]

## Conclusions
[Comprehensive answer with confidence level and reasoning]

## Recommendations
[Immediate actions and long-term considerations]

## Sources
[Primary, secondary, tertiary sources with credibility notes]
```

#### Example Usage

```
/workflows/research-synthesis "Best CRM platforms for B2B SaaS companies with <100 employees"

→ 6-phase systematic research
→ Evidence table with 10+ sources
→ Comprehensive report with recommendations
→ Time: 8 hours → 1 hour (8-12x faster)
```

**Use Cases**: Market research, vendor selection, academic research, due diligence, trend analysis, policy research

**📖 See Example**: [Research & Synthesis Example](../../examples/research-synthesis/) - Complete 12-page research report with evidence table and citations

---

### Content Creation Workflow

**Command**: `/workflows/content-creation <content-type-and-topic>`

**Purpose**: Create professional content (blogs, articles, whitepapers, marketing copy) from research through publication

**When to use**:
- Blog posts and articles
- Whitepapers and technical content
- Marketing copy and landing pages
- Case studies and success stories
- Email newsletters
- Social media content
- Press releases

#### Phases

**Phase 1: Audience & Purpose Definition** (analyze-agent)

Goal: Clarify who you're writing for and why

Actions:
1. Define target audience (role, expertise, interests)
2. Clarify content purpose (inform/persuade/entertain/convert)
3. Define success metrics
4. Determine tone & style (formality, voice, perspective)

Deliverable: Content brief with audience, purpose, success metrics, tone

Quality Gate 1: Content goals clear and aligned?

---

**Phase 2: Research & Outline**

Goal: Gather information and structure content

Actions:
1. Research topic (can use research-synthesis workflow)
2. Identify 3-5 main points with supporting evidence
3. Create detailed outline (hook, intro, body, conclusion, CTA)
4. Gather supporting materials (stats, quotes, examples)

Deliverable: Detailed outline with supporting materials

Quality Gate 2: Outline has clear main points and logical flow?

---

**Phase 3: Draft Creation**

Goal: Write complete first draft

Actions:
1. Write attention-grabbing hook
2. Write introduction previewing main points
3. Write body sections (each with evidence and examples)
4. Write conclusion summarizing and reinforcing
5. Craft compelling call-to-action
6. Add descriptive subheadings

Deliverable: Complete first draft

Quality Gate 3: All sections written and follows outline?

---

**Phase 4: Style & Tone Refinement**

Goal: Ensure style matches audience and brand

Actions:
1. Read aloud test for natural flow
2. Check tone consistency (formality, voice)
3. Assess clarity (jargon, sentence complexity)
4. Add engagement elements (varied sentence length, active voice)
5. Format for readability (short paragraphs, bullets, white space)

Deliverable: Style-refined draft

Quality Gate 4: Tone appropriate and content engaging?

---

**Phase 5: Proofreading** (proofread-agent)

Goal: Error-free, polished content

Actions:
1. Fix grammar, spelling, punctuation
2. Improve clarity and structure
3. Ensure terminology consistency
4. Remove redundancy and tighten prose
5. Verify all facts and links

Deliverable: Proofread draft with corrections

Quality Gate 5: Error-free and style guide compliant?

---

**Phase 6: Compliance & Brand Check** (docs-agent)

Goal: Verify brand compliance

Actions:
1. Check brand guidelines (voice, terminology, messaging)
2. Verify content policy compliance
3. SEO optimization (if applicable)
4. Legal review (if needed)

Deliverable: Compliance verification report

Quality Gate 6: Compliant with all brand and content policies?

---

**Phase 7: Final Polish**

Goal: Perfect headlines, formatting, CTAs

Actions:
1. Write 5-10 headline variations and choose best
2. Refine opening hook for maximum impact
3. Enhance subheadings for scannability
4. Strengthen call-to-action
5. Final format check (HTML/Markdown, images, links)

Deliverable: Publication-ready content

Quality Gate 7: Headline compelling, CTA strong, formatting perfect?

#### Output Format

Publication-ready content file with:
- Compelling headline
- Engaging hook and intro
- Well-structured body (3-5 sections)
- Strong conclusion
- Clear call-to-action
- Proper formatting
- Meta description (if applicable)

#### Example Usage

```
/workflows/content-creation "Blog post: 10 Ways AI is Transforming Customer Service in 2024"

→ 7-phase content development
→ Research, outline, draft, refine, proofread, compliance, polish
→ 1,500-word publication-ready article
→ Time: 2 hours → 30 minutes (4-5x faster)
```

**Use Cases**: Blog posts, whitepapers, marketing copy, case studies, guides, email newsletters, social media, press releases

**📖 See Example**: [Content Creation Example](../../examples/content-creation/) - Publication-ready 1,482-word blog post with SEO optimization

---

### Professional Email Workflow

**Command**: `/workflows/professional-email <email-purpose-or-context>`

**Purpose**: Compose professional, context-aware emails with appropriate tone and clear messaging

**When to use**:
- Important emails (executives, clients, stakeholders)
- Sensitive communications (difficult conversations, bad news)
- First contact emails
- Request emails (approval, information, action)
- Thank you and follow-up emails
- Any email where tone and clarity matter

#### Phases

**Phase 1: Context Analysis** (analyze-agent)

Goal: Understand situation and relationship

Actions:
1. Review email thread context (if replying)
2. Analyze relationship (role, seniority, history)
3. Assess urgency and priority
4. Consider cultural and organizational norms

Deliverable: Context brief with recipient profile, urgency, norms

Quality Gate 1: Context understood including relationship and urgency?

---

**Phase 2: Goal Identification**

Goal: Define what you want to achieve

Actions:
1. Identify primary purpose (request info, provide info, request action, etc.)
2. Define desired outcome and timeline
3. Set success criteria (what response do you want?)

Deliverable: Clear goal statement with success criteria

Quality Gate 2: Goal specific with clear desired outcome?

---

**Phase 3: Tone Selection**

Goal: Choose appropriate tone for context

Actions:
1. Determine formality level (formal/professional/casual)
2. Choose approach (direct/diplomatic/friendly)
3. Select tone markers appropriate for level
4. Ensure tone matches relationship and content

Deliverable: Tone profile (formality + approach + markers)

Quality Gate 3: Tone matches relationship and context?

---

**Phase 4: Email Composition**

Goal: Write well-structured email

Actions:
1. Craft specific, actionable subject line
2. Choose appropriate greeting
3. State purpose in first sentence
4. Write 1-3 short body paragraphs (context, details, action items)
5. Clear closing with call-to-action
6. Professional sign-off with signature

Deliverable: Complete draft email

Quality Gate 4: Email has clear structure and purpose stated upfront?

---

**Phase 5: Clarity & Brevity Check**

Goal: Ensure email is clear and concise

Actions:
1. Test clarity (understandable without re-reading?)
2. Edit for brevity (remove redundancy, filler words)
3. Improve scannability (bullets, bold, white space)
4. Apply one-main-ask rule

Deliverable: Refined, concise email

Quality Gate 5: Under 200 words with one clear main point?

---

**Phase 6: Proofread & Polish** (proofread-agent)

Goal: Error-free, professional email

Actions:
1. Fix grammar, spelling, punctuation
2. Verify tone (professional, not passive-aggressive)
3. Check completeness (all info included, attachments mentioned)
4. Professional polish (no ALL CAPS, consistent formatting)

Deliverable: Proofread, polished email ready to send

Quality Gate 6: Error-free, complete, and professional?

#### Output Format

```
Subject: [Clear, specific, actionable]

[Greeting],

[Purpose statement - why I'm writing]

[Context paragraph - background if needed]

[Details/Request paragraph]

[Action items]:
1. [What I need]
2. [By when]

[Closing sentence]

[Sign-off],
[Name]
[Title, contact]
```

#### Example Usage

```
/workflows/professional-email "Request budget approval from CFO for Q3 marketing campaign ($50K)"

→ 6-phase email composition
→ Context-aware tone selection (formal, concise for executive)
→ Clear action items with deadline
→ Time: 30 minutes → 5 minutes (6x faster)
```

**Use Cases**: Executive emails, client communication, difficult conversations, requests, follow-ups, thank you notes

**📖 See Example**: [Professional Email Example](../../examples/professional-email/) - Real email examples showing tone adaptation and professional quality

---

### Competitive Analysis Workflow

**Command**: `/workflows/competitive-analysis <product-or-market>`

**Purpose**: Analyze competitors systematically and generate strategic recommendations

**When to use**:
- Product strategy and positioning
- Market entry decisions
- Pricing strategy
- Sales enablement (battle cards)
- Investor presentations
- Strategic planning

#### Phases

**Phase 1: Competitor Identification** (analyze-agent)

Goal: Map competitive landscape

Actions:
1. Identify direct competitors (same product, same market)
2. Identify indirect competitors (different product, same need)
3. Identify emerging threats (new entrants, disruptors)
4. Identify adjacent players (could enter your market)

Deliverable: Competitor list (5-10) with categorization

Quality Gate: Comprehensive competitor set identified?

---

**Phase 2: Information Gathering**

Goal: Collect data on each competitor

Actions:
1. Research product/service features and capabilities
2. Analyze pricing (tiers, discounts, value props)
3. Assess market position (share, growth, customer base)
4. Identify strengths and weaknesses
5. Understand strategy (positioning, messaging, target audience)

Sources: Company websites, reviews, news, social media, industry reports

Deliverable: Competitor profiles with data

Quality Gate: Sufficient data for fair comparison?

---

**Phase 3: Comparison Framework** (analyze-agent)

Goal: Create structured comparison

Actions:
1. Build feature comparison matrix
2. Compare pricing across tiers
3. Compare market position and growth
4. Analyze customer segments and geographic presence

Deliverable: Comparison matrices and charts

Quality Gate: Fair, data-driven comparison completed?

---

**Phase 4: SWOT Analysis** (analyze-agent + analysis skill)

Goal: Analyze each major competitor

For each competitor:
- Strengths (advantages, resources, customer praise)
- Weaknesses (limitations, complaints, gaps)
- Opportunities (for them - trends, expansion possibilities)
- Threats (to them - challenges, disruptions, risks)

Deliverable: SWOT for each key competitor

Quality Gate: Balanced, evidence-based SWOT analyses?

---

**Phase 5: Strategic Positioning**

Goal: Identify where you fit

Actions:
1. Create positioning map (price vs features)
2. Analyze differentiation (unique, similar, behind)
3. Identify competitive advantages (defensible vs temporary)
4. Assess vulnerabilities (where you're exposed)

Deliverable: Positioning map and strategic analysis

Quality Gate: Clear positioning identified?

---

**Phase 6: Strategic Recommendations**

Goal: Generate actionable insights

Recommendations in 4 categories:
1. **Defend**: Where to strengthen current position
2. **Attack**: Where to take market share
3. **Expand**: White space opportunities
4. **Watch**: Emerging threats to monitor

Format: Action, Why, Impact, Effort, Priority, Timeline

Deliverable: Prioritized strategic recommendations

Quality Gate: Recommendations actionable and prioritized?

#### Output Format

```markdown
# Competitive Analysis: [Market/Product]

## Executive Summary
- Market landscape overview
- Key competitors
- Your position
- Top 3 recommendations

## Competitor Profiles
[For each: Overview, strengths, weaknesses, strategy]

## Comparison Analysis
- Feature matrix
- Pricing comparison
- Market position

## SWOT Analysis
[For key competitors]

## Strategic Positioning
- Positioning map
- Differentiation summary
- Opportunities and threats

## Recommendations
[Defend/Attack/Expand/Watch with rationale and priority]
```

#### Example Usage

```
/workflows/competitive-analysis "AI-powered customer service platforms"

→ 6-phase competitive intelligence
→ Feature comparison, SWOT, positioning map
→ Strategic recommendations (defend/attack/expand/watch)
→ Time: 12 hours → 2-3 hours (4-6x faster)
```

**Use Cases**: Product strategy, pricing decisions, market entry, sales enablement, investor presentations

**📖 See Example**: [Competitive Analysis Example](../../examples/competitive-analysis/) - 20-page strategic analysis with positioning map and actionable recommendations

---

### Proposal & Pitch Workflow

**Command**: `/workflows/proposal-pitch <proposal-type-and-opportunity>`

**Purpose**: Create winning proposals, pitches, and grant applications

**When to use**:
- Sales proposals and RFP responses
- Grant applications (research, nonprofit)
- Partnership proposals
- Investor pitches
- Internal project proposals
- Business cases

#### Phases

**Phase 1: Opportunity Analysis** (analyze-agent)

Goal: Understand requirements and stakeholders

Actions:
1. Understand requirements (what are they buying/funding?)
2. Identify decision criteria
3. Analyze stakeholders (decision makers, influencers)
4. Identify win themes (why should they choose you?)

Deliverable: Opportunity brief with requirements, stakeholders, win themes

Quality Gate: Clear understanding of what they want?

---

**Phase 2: Solution Design**

Goal: Tailor solution to their needs

Actions:
1. Match your offering to their requirements
2. Highlight relevant capabilities
3. Differentiate from competitors
4. Address risks and concerns

Deliverable: Customized solution design

Quality Gate: Solution clearly addresses their needs?

---

**Phase 3: Value Proposition** (analyze-agent + analysis skill)

Goal: Build compelling value case

Actions:
1. Quantify benefits (ROI, cost savings, revenue impact, time savings)
2. Articulate qualitative benefits (strategic advantages, peace of mind)
3. Compare to alternatives (status quo, build in-house, competitors)
4. Show why your option is best

Deliverable: Value proposition with quantified benefits

Quality Gate: Value clear and compelling with numbers?

---

**Phase 4: Proposal Structure**

Goal: Organize proposal logically

Standard structure:
1. Executive Summary (1 page)
2. Problem/Opportunity
3. Proposed Solution
4. Why Us (experience, case studies, team)
5. Implementation Plan
6. Investment (pricing)
7. Next Steps

Deliverable: Proposal outline

Quality Gate: Structure logical and complete?

---

**Phase 5: Draft Creation**

Goal: Write compelling proposal

Actions:
1. Write executive summary (LAST)
2. Start with their problem, not your solution
3. Use evidence-based content (data, examples, testimonials)
4. Include visual elements (ROI charts, timelines, process diagrams)

Deliverable: Complete draft proposal

Quality Gate: All sections written and cohesive?

---

**Phase 6: Compliance Check** (docs-agent)

Goal: Verify against requirements

Actions:
1. Verify every requirement addressed
2. Check format compliance (page limits, required sections)
3. Validate submission requirements

Deliverable: Compliance checklist

Quality Gate: All requirements met?

---

**Phase 7: Polish & Proofread** (proofread-agent)

Goal: Professional, error-free proposal

Actions:
1. Proofread thoroughly
2. Professional formatting
3. Consistent terminology
4. Visual polish

Deliverable: Publication-ready proposal

Quality Gate: Error-free and professional?

#### Output Format

Professional proposal with:
- Executive summary (can stand alone)
- Problem statement
- Tailored solution
- Evidence and case studies
- Implementation plan
- Clear pricing
- Compelling visuals

#### Example Usage

```
/workflows/proposal-pitch "RFP response for enterprise CRM implementation (500-person company)"

→ 7-phase proposal development
→ Opportunity analysis, solution design, value prop, compliance
→ Winning proposal with ROI calculations
→ Time: 8 hours → 2-3 hours (3-4x faster)
```

**Use Cases**: Sales proposals, RFP responses, grant applications, partnership proposals, investor pitches, business cases

**📖 See Example**: [Proposal & Pitch Example](../../examples/proposal-pitch/) - Complete 12-page proposal with ROI calculations and executive summary

---

### Meeting Preparation Workflow

**Command**: `/workflows/meeting-prep <meeting-type-and-topic>`

**Purpose**: Prepare thoroughly for important meetings with research, talking points, and success planning

**When to use**:
- Executive/stakeholder meetings
- Sales calls and demos
- Client meetings
- Board meetings
- Investor pitches
- Performance reviews
- Negotiations
- Project kickoffs

#### Phases

**Phase 1: Meeting Context Analysis**

Goal: Understand meeting purpose and desired outcome

Actions:
1. Clarify meeting basics (purpose, agenda, format, duration)
2. Define YOUR desired outcome
3. Set success criteria (minimum acceptable, target, ideal)

Deliverable: Meeting context brief

Quality Gate: Clear purpose and desired outcome defined?

---

**Phase 2: Participant Research** (analyze-agent)

Goal: Understand each attendee

Actions:
1. Research each participant (role, background, recent activities)
2. Map stakeholders (decision makers, influencers, supporters/skeptics)
3. Identify what they care about (priorities, concerns, questions)

Deliverable: Participant profiles with priorities and concerns

Quality Gate: Understand each person's perspective?

---

**Phase 3: Talking Points & Key Messages**

Goal: Prepare what to communicate

Actions:
1. Develop 3-5 core messages with evidence
2. Craft opening statement (30-60 seconds)
3. Organize supporting points (data, case studies, testimonials)
4. Prepare closing statement with next steps

Deliverable: Talking points document

Quality Gate: Messages clear and compelling?

---

**Phase 4: Question Preparation**

Goal: Prepare questions and answers

Actions:
1. List questions to ask (information gathering, strategic, relationship-building)
2. Anticipate questions they'll ask
3. Prepare answers with evidence
4. Plan objection handling

Deliverable: Question list (to ask + anticipated with answers)

Quality Gate: Prepared for likely questions and objections?

---

**Phase 5: Materials & Logistics**

Goal: Ensure everything is ready

Actions:
1. Prepare materials (slides, one-pagers, documents, demos)
2. Complete pre-work (send agenda, confirm attendance, test tech)
3. Verify logistics checklist

Deliverable: Materials ready, logistics confirmed

Quality Gate: Everything prepared and working?

---

**Phase 6: Success Planning**

Goal: Plan for follow-through

Actions:
1. Plan meeting flow (opening, main discussion, Q&A, closing)
2. Assign note-taker
3. Plan follow-up (thank you email, notes, action items)
4. Prepare contingencies (what if they say no, key person missing, etc.)

Deliverable: Meeting flow plan and follow-up strategy

Quality Gate: Ready to run effective meeting?

#### Output Format

```markdown
# Meeting Preparation Brief

## Meeting Details
- Date/Time, Attendees, Duration, Purpose
- My Goal, Success Criteria

## Participant Profiles
[For each: Role, Priorities, Style, Likely questions]

## My Talking Points
[3-5 key messages with evidence]

## Questions
- To Ask Them: [Strategic, information gathering]
- They Might Ask Me: [With prepared answers]

## Materials Checklist
[Slides, documents, demos]

## Success Criteria
- Minimum, Target, Ideal outcomes

## Follow-Up Plan
[Thank you email, notes, action items, next meeting]
```

#### Example Usage

```
/workflows/meeting-prep "Quarterly business review with Fortune 500 client"

→ 6-phase meeting preparation
→ Participant research, talking points, Q&A prep
→ Comprehensive prep brief with success planning
→ Time: 2 hours → 30 minutes (3-6x faster)
```

**Use Cases**: Sales calls, exec meetings, board meetings, investor pitches, performance reviews, negotiations, kickoffs

**📖 See Example**: [Meeting Preparation Example](../../examples/meeting-prep/) - Comprehensive meeting brief with participant profiles, Q&A prep, and success planning

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
