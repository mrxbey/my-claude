# Analysis Frameworks (Level 3 Reference)

This file provides detailed analysis frameworks and specialized patterns. Load this only when you need specific framework guidance.

## SWOT Analysis

**When to use**: Strategic planning, business decisions, capability assessment

### Structure

| **Strengths** (Internal, Positive) | **Weaknesses** (Internal, Negative) |
|-------------------------------------|-------------------------------------|
| What do we do well? | What do we lack? |
| What unique resources? | What should we avoid? |
| What competitive advantages? | What do others do better? |

| **Opportunities** (External, Positive) | **Threats** (External, Negative) |
|----------------------------------------|----------------------------------|
| What trends favor us? | What obstacles exist? |
| What gaps in market? | What is competition doing? |
| What can we leverage? | What risks loom? |

### Application Steps

1. List items in each quadrant (5-7 per quadrant)
2. Prioritize by impact
3. Match strategies:
   - **SO Strategies**: Use Strengths to pursue Opportunities
   - **WO Strategies**: Address Weaknesses to pursue Opportunities
   - **ST Strategies**: Use Strengths to mitigate Threats
   - **WT Strategies**: Address Weaknesses and Threats

### Example

**Context**: Should we migrate to microservices?

**Strengths**:
- Experienced team
- Modular monolith (easier to split)
- Good test coverage

**Weaknesses**:
- No DevOps expertise
- Limited ops budget
- Tight timeline

**Opportunities**:
- Better scalability for new market
- Easier team scaling (work in parallel)
- Modern tech stack attracts talent

**Threats**:
- Complexity overhead
- Distributed system failure modes
- Competitor moving faster

**SO Strategy**: Use modular structure to incrementally migrate high-value services
**Recommendation**: Hybrid approach - extract 2-3 key services, keep rest as monolith

---

## Cost-Benefit Analysis

**When to use**: Investment decisions, feature prioritization, resource allocation

### Framework

**Costs** (one-time + ongoing):
- Development: Time × Team × Rate
- Infrastructure: Servers, licenses, tools
- Training: Learning curve, documentation
- Opportunity: What else could we do?
- Risk: Expected value of negative outcomes

**Benefits** (quantified):
- Revenue: Direct income, upsell, retention
- Cost Savings: Efficiency, automation, reduction
- Risk Reduction: Value of mitigated risks
- Strategic: Market position, capability, knowledge

**Calculation**:
```
Net Benefit = Total Benefits - Total Costs
ROI = (Net Benefit / Total Costs) × 100%
Payback Period = Total Costs / Annual Benefits
```

### Template

| Category | Item | Amount | Notes |
|----------|------|--------|-------|
| **Costs** | | | |
| Development | 3 devs × 4 weeks × $8K/week | $96K | Full rewrite |
| Infrastructure | Servers, monitoring | $2K/mo | Ongoing |
| Training | Team learning | $10K | One-time |
| Opportunity | Feature X delayed | $50K | 6-week delay |
| **Total Costs** | | **$156K + $2K/mo** | |
| **Benefits** | | | |
| Revenue | 20% conversion lift | $200K/year | Conservative estimate |
| Cost Savings | 50% ops time | $40K/year | Automation |
| Risk Reduction | Avoid downtime | $30K/year | Expected value |
| **Total Benefits** | | **$270K/year** | |
| **Net Benefit** | | **$114K first year** | |
| **ROI** | | **73% first year** | |
| **Payback Period** | | **7 months** | |

### Decision Rules

- **ROI > 50%**: Strong investment
- **ROI 20-50%**: Consider if strategic fit
- **ROI < 20%**: Probably not worth it
- **Payback < 12 months**: Low risk
- **Payback > 24 months**: High risk

---

## Risk Assessment Matrix

**When to use**: Project planning, security analysis, change management

### Risk Matrix

| Likelihood → | Low (1) | Medium (2) | High (3) |
|--------------|---------|------------|----------|
| **High Impact (3)** | 3 🟡 | 6 🟠 | 9 🔴 |
| **Med Impact (2)** | 2 🟢 | 4 🟡 | 6 🟠 |
| **Low Impact (1)** | 1 🟢 | 2 🟢 | 3 🟡 |

**Priority**:
- 🔴 7-9: Critical - Immediate mitigation required
- 🟠 4-6: High - Plan mitigation
- 🟡 3: Medium - Monitor
- 🟢 1-2: Low - Accept

### Risk Assessment Template

| Risk ID | Description | Likelihood | Impact | Score | Mitigation | Owner |
|---------|-------------|------------|--------|-------|------------|-------|
| R1 | Database migration fails | 2 (Med) | 3 (High) | 6 🟠 | Test on staging, backup plan | DevOps |
| R2 | Learning curve delays | 3 (High) | 2 (Med) | 6 🟠 | Training week, pair programming | Tech Lead |
| R3 | Performance regression | 2 (Med) | 2 (Med) | 4 🟡 | Load testing, monitoring | QA |

### Mitigation Strategies

**Avoid**: Change approach to eliminate risk
- Example: Don't use untested tech → Use proven solution

**Reduce**: Lower likelihood or impact
- Example: Add automated tests → Catch bugs early

**Transfer**: Share risk with others
- Example: Use managed service → Provider handles ops

**Accept**: Acknowledge and monitor
- Example: Minor UI bug → Fix in next sprint

---

## Decision Matrix

**When to use**: Choosing between multiple options with multiple criteria

### Framework

1. **List criteria**: What matters for this decision?
2. **Assign weights**: How important is each criterion? (Total = 100%)
3. **Score options**: Rate each option per criterion (1-10)
4. **Calculate**: Weight × Score for each cell
5. **Total**: Sum weighted scores

### Template

| Criteria | Weight | Option A | Option B | Option C |
|----------|--------|----------|----------|----------|
| | | Score | Weighted | Score | Weighted | Score | Weighted |
| Performance | 30% | 8 | 2.4 | 5 | 1.5 | 9 | 2.7 |
| Cost | 25% | 9 | 2.25 | 6 | 1.5 | 4 | 1.0 |
| Maintainability | 20% | 6 | 1.2 | 8 | 1.6 | 7 | 1.4 |
| Time to Market | 15% | 7 | 1.05 | 9 | 1.35 | 5 | 0.75 |
| Risk | 10% | 8 | 0.8 | 7 | 0.7 | 6 | 0.6 |
| **Total** | **100%** | | **7.7** | | **6.65** | | **6.45** |
| **Rank** | | | **1st** | | **2nd** | | **3rd** |

**Decision**: Option A (highest weighted score)

**Sensitivity Analysis**: If cost weight drops below 15%, Option C wins

---

## Force Field Analysis

**When to use**: Change management, understanding resistance, planning interventions

### Framework

**Driving Forces** (push for change) ← → **Restraining Forces** (resist change)

Identify forces on each side, rate strength (1-5), plan to strengthen drivers and weaken restraints.

### Template

```
CURRENT STATE ────────────────→ DESIRED STATE
   Monolith                      Microservices

Driving Forces (→)                Restraining Forces (←)
━━━━━━━━━━━━━━━━                  ━━━━━━━━━━━━━━━━
Scalability needs      (5)  ←→ (4)  Complexity fear
Modern tech stack      (4)  ←→ (3)  No DevOps skills
Team growth           (4)  ←→ (5)  Time pressure
Market pressure       (3)  ←→ (3)  Budget constraints
                            ←→ (2)  Team resistance

Driving Total: 16              Restraining Total: 17
```

**Strategy**:
1. **Strengthen drivers**: Get exec buy-in (scalability), hire DevOps
2. **Weaken restraints**: Training (skills), incremental approach (time/complexity)
3. **Net effect**: Tip balance toward change

---

## Eisenhower Matrix

**When to use**: Prioritization, time management, delegation decisions

### Framework

| | **Urgent** | **Not Urgent** |
|-------------|-----------|---------------|
| **Important** | **DO FIRST** | **SCHEDULE** |
| | Critical bugs | Strategic planning |
| | Deadlines | Skill development |
| | Emergencies | Process improvement |
| **Not Important** | **DELEGATE** | **ELIMINATE** |
| | Interruptions | Time wasters |
| | Some meetings | Busy work |
| | Some emails | Distractions |

### Application

1. List all tasks/issues
2. Classify each into quadrant
3. Action plan:
   - **Quadrant 1 (DO)**: Execute immediately, don't procrastinate
   - **Quadrant 2 (SCHEDULE)**: Block time, this is where magic happens
   - **Quadrant 3 (DELEGATE)**: Find someone else, automate if possible
   - **Quadrant 4 (ELIMINATE)**: Just say no, stop doing these

---

## Pareto Analysis (80/20)

**When to use**: Identifying high-impact items, bug triage, optimization focus

### Principle

80% of effects come from 20% of causes. Focus on the vital few, not the trivial many.

### Process

1. List all items (bugs, features, issues)
2. Measure impact (users affected, revenue, frequency)
3. Sort by impact (descending)
4. Calculate cumulative %
5. Find 80% cutoff
6. Focus on top 20%

### Example: Bug Prioritization

| Bug | Users Affected | Cumulative % | Priority |
|-----|----------------|--------------|----------|
| Login fails | 10,000 | 50% | **Top 20%** |
| Cart error | 5,000 | 75% | **Top 20%** |
| Slow search | 1,000 | 80% | **Top 20%** ← 80% cutoff |
| Typo on FAQ | 500 | 82.5% | Bottom 80% |
| Minor UI glitch | 300 | 84% | Bottom 80% |
| ... | ... | ... | ... |

**Decision**: Fix top 3 bugs (20% of bugs) to help 16,000 users (80% of impact)

---

## Root Cause Analysis (5 Whys)

**When to use**: Debugging, incident analysis, finding underlying problems

### Technique

Ask "Why?" five times to drill down from symptom to root cause.

### Example

**Problem**: Website is down

1. **Why is the website down?**
   - Because the database isn't responding

2. **Why isn't the database responding?**
   - Because it ran out of connections

3. **Why did it run out of connections?**
   - Because connections aren't being closed

4. **Why aren't connections being closed?**
   - Because error handling doesn't close them

5. **Why doesn't error handling close connections?**
   - Because we don't use try-finally blocks

**Root Cause**: Missing try-finally in database code
**Fix**: Add proper connection cleanup in error paths
**Prevention**: Code review checklist item, linter rule

---

## Comparative Analysis

**When to use**: Vendor selection, technology choices, design alternatives

### Framework

1. Define evaluation criteria (must-have vs. nice-to-have)
2. Score each option (1-10 or Yes/No for must-haves)
3. Eliminate any option failing must-haves
4. Weight and rank remaining options

### Template

| Criteria | Must-Have? | Weight | Option A | Option B | Option C |
|----------|------------|--------|----------|----------|----------|
| Security | ✅ Yes | - | ✅ Pass | ✅ Pass | ❌ Fail |
| API support | ✅ Yes | - | ✅ Pass | ✅ Pass | ✅ Pass |
| Performance | No | 30% | 8 (2.4) | 6 (1.8) | n/a |
| Cost | No | 25% | 7 (1.75) | 9 (2.25) | n/a |
| Community | No | 20% | 9 (1.8) | 7 (1.4) | n/a |
| Learning curve | No | 15% | 6 (0.9) | 8 (1.2) | n/a |
| Documentation | No | 10% | 8 (0.8) | 7 (0.7) | n/a |
| **Total** | | **100%** | **7.65** | **7.35** | **Eliminated** |

**Decision**: Option A (slightly better, especially on performance)

---

## Gap Analysis

**When to use**: Compliance, capability assessment, roadmap planning

### Framework

**Current State** → **Gap** → **Desired State**

1. Define desired state (requirements, standards, goals)
2. Assess current state (what exists today)
3. Identify gaps (what's missing, wrong, or insufficient)
4. Prioritize gaps (impact and effort)
5. Plan to close gaps

### Template

| Requirement | Desired | Current | Gap | Priority | Action |
|-------------|---------|---------|-----|----------|--------|
| Auth | OAuth 2.0 | Custom JWT | Missing OAuth | High | Migrate Q2 |
| Rate limiting | 100/min | None | No limit | Critical | Add now |
| Encryption | At rest | In transit only | No storage encryption | Medium | Plan Q3 |
| Audit logs | All actions | Errors only | Missing success logs | Low | Backlog |

---

## When to Use Which Framework

| Framework | Best For | Output |
|-----------|----------|--------|
| **SWOT** | Strategic planning | Strategies matching S/W to O/T |
| **Cost-Benefit** | Investment decisions | ROI, payback period |
| **Risk Matrix** | Risk assessment | Prioritized risks with mitigation |
| **Decision Matrix** | Multi-criteria choice | Weighted scores, ranked options |
| **Force Field** | Change management | Balanced forces, intervention plan |
| **Eisenhower** | Prioritization | 4 quadrants, clear actions |
| **Pareto** | Focus finding | Top 20% items for 80% impact |
| **5 Whys** | Root cause finding | Underlying cause, not symptom |
| **Comparative** | Vendor/tech selection | Scored comparison |
| **Gap Analysis** | Compliance/roadmap | Prioritized gaps, action plan |

---

## Combining Frameworks

Often, use multiple frameworks in sequence:

**Example Flow**: Major system change

1. **SWOT**: Should we even do this?
2. **Force Field**: What's enabling/blocking us?
3. **Cost-Benefit**: Is it worth the investment?
4. **Risk Matrix**: What could go wrong?
5. **Decision Matrix**: Which approach to take?
6. **Eisenhower**: What to do first?

This comprehensive approach ensures thorough analysis from multiple angles.
