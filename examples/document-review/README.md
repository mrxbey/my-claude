# Example: Document Review & Compliance Checking

## Overview

This example demonstrates using the **docs-agent** to verify that an API implementation complies with a security policy. It showcases automated compliance checking, gap analysis, and remediation planning - critical capabilities for enterprise environments.

**Key Features Demonstrated:**
- ✅ Documentation verification against policies
- ✅ Requirement extraction with unique IDs
- ✅ Compliance table generation (✅/⚠️/❌)
- ✅ Gap analysis with specific code references
- ✅ Remediation roadmap with timelines
- ✅ Risk assessment and recommendations

---

## Scenario

**Company**: TechCorp Inc.
**Challenge**: API security audit required before production deployment
**Policy**: API Security Policy v2.1 with 11 mandatory requirements
**Implementation**: REST API with JWT authentication

**Question**: *Does our implementation comply with the security policy?*

---

## Files in This Example

### Input Files

**1. `security-policy.md`** - The Policy Document
- 11 security requirements (REQ-AUTH-001 through REQ-VER-001)
- Severity levels: CRITICAL, HIGH, MEDIUM, LOW
- Compliance verification process
- 2,450 words

**2. `current-implementation.md`** - The Implementation Documentation
- Describes actual authentication/authorization code
- Includes code snippets with file references
- Self-assessment of compliance status
- 1,800 words

### Output File

**3. `compliance-output.md`** - Example docs-agent Report
- Complete compliance table with 11 requirements
- Gap analysis for non-compliant items
- Remediation roadmap with timelines
- Testing checklist and action items
- 2,200 words

This shows what the docs-agent produces when given the inputs.

---

## How to Run This Example

### Method 1: Using the /check-docs Command

```bash
cd my-claude

# Start Claude Code
claude

# Run documentation verification
> /check-docs Verify that examples/document-review/current-implementation.md
  complies with examples/document-review/security-policy.md
```

### Method 2: Natural Language Request

```bash
claude

> Check if our API implementation in examples/document-review/
  complies with the security policy. Show me gaps and remediation steps.
```

The **docs-agent** will automatically trigger based on keywords like "check", "verify", "complies", "policy", "documentation".

### Method 3: Direct Agent Invocation (Advanced)

```bash
claude

> Use the docs-agent to verify examples/document-review/current-implementation.md
  against examples/document-review/security-policy.md and generate a compliance report
```

---

## What Happens (Behind the Scenes)

### Phase 1: Discovery (0.5 seconds)
```
📁 Finding relevant documentation...
   Found: security-policy.md (policy document)
   Found: current-implementation.md (implementation)
```

### Phase 2: Requirement Extraction (2-3 seconds)
```
📋 Extracting requirements from security-policy.md...
   REQ-AUTH-001: Authentication Required (CRITICAL)
   REQ-AUTH-002: JWT Token-Based Auth (CRITICAL)
   REQ-AUTH-003: HTTPS Only (CRITICAL)
   REQ-AUTHZ-001: RBAC (HIGH)
   ... (11 total)
```

### Phase 3: Verification (5-10 seconds)
```
🔍 Checking implementation against requirements...
   REQ-AUTH-001 ✅ Evidence: auth_routes.py:12-67
   REQ-AUTH-002 ❌ Using HS256 instead of RS256
   REQ-AUTH-003 ✅ Evidence: nginx.conf:15-28
   ... (checking all 11)
```

### Phase 4: Gap Analysis (3-5 seconds)
```
⚠️  Analyzing compliance gaps...
   Critical Gap 1: JWT algorithm mismatch
   Critical Gap 2: Token expiry violation
   Partial Gap: Incomplete log sanitization
```

### Phase 5: Reporting (2-3 seconds)
```
📊 Generating compliance report...
   Compliance table: 11 requirements
   Gap analysis: 3 issues identified
   Remediation roadmap: 5-day plan
   Action items: 25 tasks across 4 teams
```

**Total Time**: ~15-20 seconds for complete analysis

---

## Expected Output Structure

The docs-agent produces a comprehensive report with these sections:

### 1. Executive Summary
```markdown
**Status**: ⚠️ NON-COMPLIANT (2 critical issues)

Issues requiring immediate attention:
1. JWT Algorithm Mismatch (HS256 vs RS256)
2. Token Expiry Violation (2h vs 1h max)
```

### 2. Compliance Table
```markdown
| ID | Requirement | Severity | Status | Evidence | Notes |
|----|-------------|----------|--------|----------|-------|
| REQ-AUTH-001 | Auth Required | CRITICAL | ✅ | auth_routes.py:12 | All endpoints protected |
| REQ-AUTH-002 | JWT Tokens | CRITICAL | ❌ | token_service.py:45 | Using HS256, not RS256 |
...
```

### 3. Gap Analysis (For Each Non-Compliant Item)
```markdown
#### REQ-AUTH-002: JWT Algorithm Non-Compliance

**Current State**: Using HS256 (symmetric)
**Required State**: Must use RS256 (asymmetric)
**Security Impact**: High - shared secret compromise
**Remediation**: [Code example provided]
**Estimated Effort**: 4 hours
```

### 4. Remediation Roadmap
```markdown
### Phase 1: Critical Issues (2-3 days)
1. Day 1: JWT Algorithm Migration
   - [ ] Generate RS256 key pair
   - [ ] Update token_service.py
   - [ ] Test and deploy to staging
...
```

### 5. Action Items by Role
```markdown
**Backend Team**: Start JWT migration (immediate)
**Security Team**: Generate key pair (immediate)
**DevOps Team**: Set up secrets management (this week)
```

---

## Key Features Demonstrated

### ✅ Automated Requirement Extraction

The docs-agent automatically:
- Identifies requirement IDs (REQ-AUTH-001, etc.)
- Extracts severity levels (CRITICAL, HIGH, MEDIUM, LOW)
- Captures requirement descriptions
- Maps requirements to policy sections

**Pattern Recognition**:
```markdown
### REQ-AUTH-001: Authentication Required
**Severity**: CRITICAL
**Requirement**: All API endpoints MUST require authentication...
```
→ Extracts: `{id: "REQ-AUTH-001", severity: "CRITICAL", description: "..."}`

### ✅ Evidence-Based Verification

Every compliance decision includes:
- Specific file references (`auth_routes.py:12-67`)
- Code snippets showing implementation
- Clear pass/fail reasoning
- Security impact assessment

**Example**:
```
✅ REQ-AUTH-001: Compliant
   Evidence: auth_routes.py:12-67
   Reasoning: All endpoints require authentication except exempt /health and /status
```

### ✅ Intelligent Gap Analysis

For non-compliant requirements:
- **Current vs Required**: Side-by-side comparison
- **Security Impact**: Why it matters
- **Remediation Code**: Exact code to fix it
- **Effort Estimate**: Hours/days to remediate

### ✅ Actionable Remediation Plans

Not just "fix this" - provides:
- Day-by-day timeline
- Specific tasks with checkboxes
- Assigned roles/teams
- Testing checklist
- Deployment strategy

### ✅ Risk Assessment

Overall risk level based on:
- Number and severity of gaps
- Security impact of each gap
- Current compliance percentage
- Recommendation for production deployment

---

## Learning Points

### 1. Trigger Keywords for docs-agent

Words that automatically invoke the docs-agent:
- **Verification**: "check", "verify", "validate", "review"
- **Compliance**: "complies", "compliance", "policy", "requirement"
- **Documentation**: "documentation", "docs", "specification", "spec"
- **Standards**: "standard", "regulation", "mandate", "guideline"

### 2. Skill Auto-Loading

The docs-agent automatically loads the **doc-compliance skill**, which provides:
- 5-step verification workflow
- Requirement extraction patterns
- Compliance table templates (✅/⚠️/❌)
- Gap analysis methodology

### 3. Evidence-Based Approach

The framework prioritizes **evidence over assumptions**:
- Every finding references specific files and line numbers
- Code snippets prove implementation status
- Clear reasoning for each compliance decision
- Distinguishes "verified compliant" from "appears compliant"

### 4. Progressive Disclosure in Action

**Startup** (Level 1):
- docs-agent metadata: ~72 tokens
- doc-compliance skill metadata: ~62 tokens
- Total: ~134 tokens

**Active Use** (Level 2):
- docs-agent full prompt: ~3,253 tokens
- doc-compliance skill instructions: ~5,103 tokens
- Total active context: ~8,356 tokens

**Maximum** (Level 3):
- No additional references needed for this example
- Same as Level 2

### 5. Structured Output Format

The compliance report follows a consistent structure:
1. Executive Summary (quick status)
2. Compliance Table (detailed findings)
3. Gap Analysis (deep dive on issues)
4. Remediation Roadmap (action plan)
5. Testing Checklist (verification)

This makes reports **immediately actionable** for different audiences:
- **Executives**: Read executive summary
- **Engineers**: Use gap analysis and remediation code
- **Project Managers**: Follow roadmap timeline
- **QA**: Use testing checklist

---

## Try It Yourself

### Experiment 1: Modify the Policy
Edit `security-policy.md` to add a new requirement:

```markdown
### REQ-AUTH-004: Multi-Factor Authentication
**Severity**: HIGH
**Requirement**: Administrative accounts MUST use MFA.
```

Re-run the docs-agent. It will:
- Extract the new requirement
- Check implementation (will find it missing)
- Add it to the compliance table as ❌
- Generate remediation steps

### Experiment 2: Fix an Issue
Update `current-implementation.md` to document RS256 usage:

```markdown
# Using RS256 algorithm with key pair
token = jwt.encode(
    payload,
    PRIVATE_KEY,
    algorithm='RS256'
)
```

Re-run the docs-agent. REQ-AUTH-002 will change from ❌ to ✅.

### Experiment 3: Change Severity
Edit `security-policy.md` to change REQ-VAL-002 from MEDIUM to HIGH.

Re-run and observe how the risk assessment changes.

### Experiment 4: Add Implementation Details
Add more code snippets to `current-implementation.md` with file references.

See how the docs-agent uses these as evidence in the compliance table.

---

## Comparison: Manual vs Automated Review

### Manual Documentation Review

**Time**: 2-4 hours
**Process**:
1. Read policy document (30 min)
2. Read implementation docs (30 min)
3. Cross-reference each requirement (1-2 hours)
4. Create compliance spreadsheet (30 min)
5. Write gap analysis (30 min)
6. Draft remediation plan (30 min)

**Accuracy**: Depends on reviewer expertise and attention
**Consistency**: Varies between reviewers
**Coverage**: Risk of missed requirements

### Automated Review with docs-agent

**Time**: 15-20 seconds
**Process**:
1. Agent reads all documents
2. Extracts requirements automatically
3. Maps to implementation evidence
4. Generates structured report
5. Produces remediation roadmap

**Accuracy**: High (evidence-based, references verified)
**Consistency**: Same format every time
**Coverage**: All requirements checked systematically

**ROI**: 400x faster, more consistent, more thorough

---

## Real-World Applications

This example pattern applies to:

### Security & Compliance
- GDPR compliance verification
- SOC 2 control mapping
- PCI-DSS requirement checking
- HIPAA regulation compliance

### Software Development
- API spec vs implementation verification
- Coding standards compliance
- Architecture decision records (ADR) adherence
- Design document validation

### Quality Assurance
- Test coverage vs requirements
- Documentation completeness
- Release checklist verification
- Change control compliance

### Operations
- Deployment runbook validation
- Incident response procedure verification
- SLA compliance checking
- Configuration standard enforcement

---

## Related Examples

- [Simple Analysis](../simple-analysis/) - Using analyze-agent for decision analysis
- [Translation Workflow](../translation-workflow/) - Using translate-agent for content translation
- [Custom Agent](../custom-agent/) - Creating specialized agents for your domain

---

## Next Steps

### Explore the Framework
1. Try the `/check-docs` command on your own documentation
2. Read the [docs-agent documentation](../../.claude/agents/docs-agent.md)
3. Learn about the [doc-compliance skill](../../.claude/skills/doc-compliance/SKILL.md)

### Customize for Your Needs
1. Create custom compliance checklists
2. Define your own requirement ID patterns
3. Add company-specific policy templates
4. Integrate with your ticketing system

### Advanced Usage
1. Chain docs-agent with analyze-agent for impact analysis
2. Use implementation-guardrails before building features
3. Automate compliance checks in CI/CD pipelines
4. Generate compliance reports on schedule

---

## Questions?

**Q: Can I use this for non-code documentation?**
A: Yes! Works for any policy → implementation verification (processes, procedures, configurations, etc.)

**Q: How does it handle ambiguous requirements?**
A: The agent marks them as ⚠️ (partially compliant) and notes the ambiguity in the report.

**Q: Can I customize the compliance table format?**
A: Yes, modify the doc-compliance skill to use your preferred format (CSV, JSON, etc.)

**Q: What if my policy uses different requirement ID formats?**
A: The skill adapts to various formats. You can also customize the extraction regex.

**Q: How accurate is the automated review?**
A: High accuracy for documented implementations. Always validate critical findings.

---

**Example Complete!** 🎉

This demonstrates the power of the docs-agent for automated compliance verification. The same patterns work for security policies, coding standards, API specs, and any policy-to-implementation validation.
