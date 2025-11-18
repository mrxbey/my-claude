# Example: Creating a Custom Agent

## Overview

This example demonstrates how to create a custom specialized agent using the **agent-crafter**. We'll walk through building a `security-audit-agent` from scratch, showing the design process, implementation, testing, and integration.

**What You'll Learn:**
- ✅ Agent design principles (when to create an agent vs using existing ones)
- ✅ Using agent-crafter for interactive agent creation
- ✅ Agent identity and workflow design
- ✅ Skill and tool selection
- ✅ Testing and validation
- ✅ Integration with existing framework

---

## Scenario

**Company**: TechCorp Inc.
**Need**: Security audits for code before production deployment
**Challenge**: Existing agents don't specialize in security analysis
**Solution**: Create a dedicated `security-audit-agent`

**Requirements**:
1. Scan code for security vulnerabilities
2. Check against OWASP Top 10
3. Verify secure coding practices
4. Generate actionable remediation reports

---

## Method 1: Using /agent-crafter Command

The fastest way to create a new agent:

```bash
cd my-claude
claude

> /agent-crafter Create an agent for security audits.
  It should scan code for vulnerabilities, check OWASP Top 10,
  and generate remediation reports.
```

### What Happens (Interactive Process)

**Phase 1: Interview** (30 seconds)
```
🤖 Agent Crafter: I'll help you design a security audit agent.

Q1: What is the primary role of this agent?
> Security code analysis and vulnerability detection

Q2: What specific tasks should it handle?
> 1. OWASP Top 10 vulnerability scanning
> 2. Secure coding practice verification
> 3. Dependency vulnerability checking
> 4. Security report generation

Q3: What's the typical workflow complexity?
> Multi-phase: Discovery → Analysis → Report → Remediation

Q4: Should it work independently or with other agents?
> Can chain with analyze-agent for risk assessment,
  docs-agent for policy compliance
```

**Phase 2: Design** (15 seconds)
```
📋 Designing agent identity...

**Proposed Name**: security-audit-agent

**Identity**: Security specialist for vulnerability detection
and secure coding verification

**Workflow**: 5-phase security audit process
1. Discovery - Find code to audit
2. OWASP Scan - Check Top 10 vulnerabilities
3. Practice Check - Verify secure coding standards
4. Dependency Audit - Check known CVEs
5. Report - Generate findings with severity levels
```

**Total Time**: ~75 seconds

---

## Agent Design Principles

### When to Create a New Agent

✅ **Create an agent when**:
- Specialized domain expertise needed (security, data science, etc.)
- Distinct workflow with 3+ phases
- Will be reused frequently
- Benefits from independent context window
- Requires specific tool combinations

❌ **Don't create an agent when**:
- Existing agent can handle it
- One-off task (use skill or direct prompting)
- Simple, single-step operation
- No clear workflow structure

### Anatomy of a Good Agent

**1. Clear Identity**
- What domain/role? (e.g., "security specialist")
- What expertise? (e.g., "OWASP Top 10, CVE databases")
- What's the approach? (e.g., "systematic scanning")

**2. Structured Workflow**
- 3-6 distinct phases
- Each phase has clear goal
- Phase outputs feed into next phase
- Quality checks at each phase

**3. Right Tools**
- Only tools actually needed
- Match tools to workflow (Bash for scanners, Grep for patterns)
- Consider permission requirements

**4. Appropriate Skills**
- Leverage existing skills when possible
- Skills provide reusable patterns
- Don't duplicate skill functionality in agent

**5. Trigger Keywords**
- 5-10 relevant keywords in description
- Domain terms (security, audit, vulnerability)
- Action terms (scan, check, verify)
- Standard acronyms (OWASP, CVE, XSS)

---

## Common Agent Patterns

### Analysis-Type Agents

**Pattern**: Decompose → Investigate → Synthesize
**Example**: analyze-agent, security-audit-agent
**Characteristics**:
- Multi-dimensional evaluation
- Evidence gathering
- Structured output (tables, reports)

### Transformation-Type Agents

**Pattern**: Input → Process → Validate → Output
**Example**: translate-agent, proofread-agent
**Characteristics**:
- Clear input/output formats
- Quality validation built-in
- Can be chained

### Verification-Type Agents

**Pattern**: Extract Requirements → Check → Report Gaps
**Example**: docs-agent
**Characteristics**:
- Checklist-driven
- Pass/fail criteria
- Gap identification

### Meta-Type Agents

**Pattern**: Interview → Design → Generate → Validate
**Example**: agent-crafter, skill-crafter
**Characteristics**:
- Interactive design process
- Template-based generation
- Self-validation

---

## Testing Your New Agent

### Test 1: Basic Invocation

```bash
claude

> Use security-audit-agent to scan examples/document-review/
  for security vulnerabilities
```

**Expected**:
- Agent loads successfully
- Finds code files
- Runs OWASP checks
- Generates security report

### Test 2: Natural Language Trigger

```bash
claude

> Run a security audit on the authentication code in src/auth/
```

**Expected**:
- Agent auto-triggers (keyword: "security audit")
- Analyzes authentication implementation
- Reports vulnerabilities if any

### Test 3: Integration with Other Agents

```bash
claude

> First, use security-audit-agent to find vulnerabilities,
  then use analyze-agent to assess the risk and prioritize fixes
```

**Expected**:
- Security audit runs first
- analyze-agent evaluates findings
- Combined report with risk-based prioritization

---

## Best Practices

### Agent Development

1. **Start with agent-crafter** - Don't build from scratch
2. **Test incrementally** - Validate each phase separately
3. **Document decisions** - Why this workflow? Why these tools?
4. **Version control** - Track agent evolution
5. **Gather feedback** - Refine based on actual usage

### Agent Maintenance

1. **Update trigger keywords** if agent not loading
2. **Refine workflows** based on common failure modes
3. **Add examples** of successful audits
4. **Keep skills up-to-date** if they evolve
5. **Review tool usage** - remove unused, add needed

### Integration

1. **Document agent relationships** - Works well with X, chains after Y
2. **Define clear handoff points** - When to use which agent
3. **Test common combinations** - Security + analyze, docs + security
4. **Avoid overlap** - Don't duplicate existing agent functionality

---

## Practice Exercises

Try creating these agents:

1. **data-migration-agent**: Agent for safely migrating databases
2. **performance-audit-agent**: Agent for finding performance bottlenecks
3. **accessibility-agent**: Agent for checking WCAG compliance
4. **refactoring-agent**: Agent for code improvement suggestions

---

## Next Steps

### Explore Framework

1. Use `/agent-crafter` to create your first custom agent
2. Read [Creating Agents Guide](../../docs/developer-guide/creating-agents.md)
3. Study existing agents in `.claude/agents/`
4. Review [Agents API Reference](../../docs/reference/agents-reference.md)

### Advanced Topics

1. **Agent orchestration**: Chain multiple agents
2. **Conditional branching**: Agent chooses next agent based on findings
3. **Parallel execution**: Run multiple agents concurrently
4. **Agent memory**: Share context between agent invocations

---

## Questions?

**Q: How do I know if I need a new agent or just a new skill?**
A: Agent = has workflow. Skill = provides patterns/frameworks. If you need both workflow AND patterns, create both.

**Q: Can agents call other agents?**
A: Yes! Use the Task tool to invoke sub-agents. Common pattern: analysis-agent calls docs-agent for policy verification.

**Q: How do I handle agent permissions?**
A: Set `permissionMode` in YAML:
- `default`: Ask for dangerous operations
- `acceptEdits`: Auto-approve edits
- `plan`: Agent plans but doesn't execute

**Q: What if my agent isn't triggering?**
A: Check description keywords. Add more domain-specific terms. Test with explicit invocation first.

**Q: Can I have multiple agents for the same domain?**
A: Yes, but differentiate clearly: `security-audit-agent` (comprehensive), `quick-security-scan-agent` (fast triage).

---

## Related Examples

- [Simple Analysis](../simple-analysis/) - Using analyze-agent for decision analysis
- [Document Review](../document-review/) - Using docs-agent for compliance checking
- [Translation Workflow](../translation-workflow/) - Using translate-agent for localization

---

**Example Complete!** 🎉

You now know how to create custom specialized agents using agent-crafter. The same principles apply to any domain: data science, DevOps, legal compliance, accessibility, performance optimization, and more.

**Key Takeaway**: Agents are specialized team members. Design them like you'd design a role: clear expertise, defined workflow, right tools for the job.
