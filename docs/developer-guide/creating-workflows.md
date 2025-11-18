# Developer Guide: Creating Workflows

## Overview

Workflows orchestrate multiple agents and skills through structured, multi-phase processes with quality gates. This guide covers creating custom workflow commands.

## When to Create a Workflow

Create a workflow command when:

✅ **Multi-phase process**: 3+ sequential phases
✅ **Multiple agents**: Coordinating 2+ agents
✅ **Quality gates**: Validation checkpoints between phases
✅ **Reusable process**: Team uses this workflow repeatedly

## Workflow vs. Command

**Simple Command**: Single agent with straightforward task
```markdown
/analyze <topic>  → analyze-agent executes and reports
```

**Workflow Command**: Multiple agents with gates
```markdown
/workflows/code-review
→ analyze-agent (structure)
→ docs-agent (compliance)
→ quality checks
→ synthesis
```

## Workflow Structure

### Basic Template

```markdown
---
description: Multi-phase workflow description
argument-hint: <what-arguments>
---

[Workflow introduction]

## Multi-Phase Workflow

### Phase 1: [Name] ([agent-name])

**Use [agent-name]** to [goal]:

**Actions**:
1. [Step 1]
2. [Step 2]

**Deliverable**: [What this produces]

**Quality Gate**: [Validation question]
- [ ] Criterion 1
- [ ] Criterion 2

**If gate fails**: [Remediation]

### Phase 2: [Name] ([agent-name])

[Same pattern...]

## Output Format

[Structured output template]
```

## Quality Gate Design

### Good Quality Gate

```markdown
**Quality Gate**: Is the analysis complete and evidence-based?
- [ ] All options evaluated (minimum 2)
- [ ] Each option has pros/cons listed
- [ ] Evidence includes file:line references
- [ ] Recommendation has clear rationale

**If FAIL**: Return to Phase 3, gather more evidence
```

**Why good**:
- Specific, testable criteria
- Clear pass/fail conditions
- Actionable remediation

### Poor Quality Gate

```markdown
**Quality Gate**: Is it good?
- [ ] Looks okay

**If FAIL**: Fix it
```

**Why poor**:
- Too vague
- Subjective criteria
- No clear remediation

## Workflow Patterns

### Sequential Workflow

```
Phase 1 → Phase 2 → Phase 3 → Done
```

Each phase completes before next starts.

**Example**: Feature development (requirements → design → implement → test)

---

### Parallel Workflow

```
        ┌─ Phase 1A ─┐
Start ──┼─ Phase 1B ─┼─→ Synthesis
        └─ Phase 1C ─┘
```

Multiple independent phases, then combine results.

**Example**: Security + performance + compliance audits run in parallel

---

### Iterative Workflow

```
Phase 1 → Gate → PASS → Phase 2
            ↓
          FAIL
            ↓
        [Fix] → Phase 1
```

Phases repeat until quality gate passes.

**Example**: Implementation with validation (implement → validate → fix → validate)

---

### Conditional Workflow

```
Phase 1 → Decision
            ├─ Condition A → Path A
            └─ Condition B → Path B
```

Different paths based on conditions.

**Example**: Bug severity determines workflow path (critical → hotfix, normal → standard)

## Complete Example

See `.claude/commands/workflows/feature-development.md` for a production example with:
- 9 phases
- 9 quality gates
- Multiple agents
- Comprehensive output template

## Integration

Add to `.claude/commands/workflows/my-workflow.md`:

```bash
touch .claude/commands/workflows/my-workflow.md
```

Test:
```
/workflows/my-workflow <args>
```

## Best Practices

1. **3-9 phases**: Not too few (loses structure), not too many (overwhelming)
2. **Quality gates**: At least one gate per critical phase
3. **Clear ownership**: Each phase assigned to specific agent
4. **Deliverables**: Each phase produces something concrete
5. **Remediation paths**: Tell what to do when gates fail
6. **Output template**: Standardize workflow results

## Related Documentation

- [User Guide: Workflows](../user-guide/workflows.md) - Using workflows
- [Developer Guide: Creating Commands](creating-commands.md) - Command basics
- [Developer Guide: Creating Agents](creating-agents.md) - Agent design
