---
description: Documentation verification and compliance checking using docs-agent
argument-hint: <what-to-verify>
---

Use the **docs-agent** and **doc-compliance skill** to verify documentation accuracy and compliance.

## Task

Verify documentation for: $ARGUMENTS

## Process

1. **Discover documentation sources**:
   - Identify relevant docs (specs, policies, standards)
   - Note versions and dates
   - Establish precedence hierarchy
   - Check for coverage gaps

2. **Extract requirements**:
   - Build comprehensive requirements list
   - Assign unique IDs (REQ-001, SEC-015, etc.)
   - Categorize (functional, security, performance, etc.)
   - Set priorities (Critical, High, Medium, Low)
   - Define verification method for each

3. **Verify against reality**:
   - For each requirement, assess status:
     - ✅ Fully Met (with evidence)
     - ⚠️ Partially Met (note gaps)
     - ❌ Not Met (document gap)
     - ⏭️ Not Applicable (explain why)
     - ❓ Cannot Verify (note blocker)
   - Document evidence with file:line references
   - Note deviations and contradictions

4. **Analyze gaps**:
   - Categorize: Missing, Incorrect, Incomplete, Undocumented, Outdated
   - Assess impact (security, compliance, usability, etc.)
   - Assign severity (P0 Critical, P1 High, P2 Medium, P3 Low)
   - Suggest specific remediation with file:line
   - Estimate effort to fix

5. **Calculate compliance**:
   - Overall compliance rate (% fully met)
   - Compliance by category
   - Critical vs. non-critical compliance
   - Trend if historical data available

6. **Report findings**:
   - Executive summary with compliance %
   - Detailed compliance table
   - Top 3-5 critical gaps with specific fixes
   - Roadmap to full compliance

## Output Format

Provide a comprehensive compliance report including:
- **Executive Summary**: Compliance level, critical gaps, recommendation
- **Documentation Sources**: List with versions and precedence
- **Compliance Overview**: Table by category with percentages
- **Detailed Compliance**: Full table with status and evidence for each requirement
- **Critical Gaps**: Top issues with impact, current/required state, specific fixes
- **Recommendations**: Immediate, short-term, and long-term actions
- **Compliance Roadmap**: Phases to reach 100% compliance

## Quality Standards

- Complete: All requirements verified, none missed
- Evidence-based: Every status backed by file:line references
- Specific: Remediation includes exact file:line to modify
- Prioritized: Clear P0/P1/P2/P3 classification
- Actionable: Concrete next steps with timeline estimates
