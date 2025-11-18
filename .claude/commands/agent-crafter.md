---
description: Interactive agent creation workflow using agent-crafter meta-agent
argument-hint: <agent-description>
---

Use the **agent-crafter meta-agent** to create a new Claude Code subagent.

## Task

Create a new agent for: $ARGUMENTS

## Interactive Design Process

The agent-crafter will guide you through an interactive conversation to design and generate a complete agent. You'll be asked about:

### 1. Role & Domain
- What specialized role should this agent fulfill?
- What domain expertise is needed?
- Can you describe the agent in one sentence?

### 2. Typical Tasks
- What are 3-5 typical tasks this agent will handle?
- Are these analysis tasks, implementation tasks, or both?
- How complex are the tasks (simple, medium, complex)?

### 3. Workflow Pattern
- Is the work sequential, exploratory, or iterative?
- Does it need multiple phases or just execute?
- What quality checks are important?

### 4. Tools & Permissions
- Should this be read-only or can it modify files?
- Does it need bash execution?
- Any tool restrictions for security?

### 5. Skills & Integration
- What existing skills should this agent use?
- Does it work alone or coordinate with other agents?
- Any new skills needed that don't exist yet?

### 6. Model & Performance
- Does this need deep reasoning (sonnet/opus) or can be faster (haiku)?
- Is independent context important (subagent) or can share main context?

## What You'll Get

The agent-crafter will generate:

1. **Complete agent file** (`.claude/agents/[agent-name].md`) with:
   - YAML frontmatter:
     - name, description with trigger keywords
     - tools list (Read, Grep, Glob, Edit, Write, Bash)
     - model selection (sonnet/opus/haiku/inherit)
     - permissionMode (default/acceptEdits/plan)
     - skills list (which skills to auto-load)
   - Agent identity:
     - Role and expertise
     - Primary question (what agent asks for every task)
     - Decision pattern (how agent thinks)
     - Approach (methodology summary)
   - When to Use scenarios
   - Complete workflow (3-6 phases with Goal + Actions + Quality Checks)
   - Quality standards and validation gates
   - Tools & techniques
   - Output template
   - Integration notes
   - Examples

2. **Validation report** confirming:
   - YAML frontmatter correct
   - All required sections present
   - Workflow is clear and actionable
   - Quality standards explicit
   - Integration well-defined

3. **Integration recommendations**:
   - Which skills the agent should use
   - Which other agents it might work with
   - When to use this agent vs. others

4. **Testing plan**:
   - 3-5 test scenarios that should trigger this agent
   - Expected behavior for each
   - How to verify it worked correctly

## Output Location

New agent will be created at:
```
.claude/agents/[agent-name].md
```

## Next Steps After Creation

1. **Review** the generated agent file
2. **Test** by asking Claude to delegate tasks matching the description
3. **Refine** if needed:
   - Adjust description if not triggering correctly
   - Modify workflow if missing steps
   - Update tool list if needed
4. **Document** by updating `.claude/agents/README.md`
5. **Commit** to version control: `git add .claude/agents/[agent-name].md && git commit -m "feat: Add [agent-name] agent"`

The agent will be immediately available for Claude to delegate to once created!

## Agent Design Patterns

### Read-Only Agents (Analysis, Review)
**Tools**: Read, Grep, Glob
**Use for**: Analysis, verification, auditing
**Safe**: Cannot modify anything

### Standard Agents (Most Agents)
**Tools**: Read, Grep, Glob, Edit, Write
**Use for**: Documentation, content creation, modifications
**Permissions**: Controlled by settings.json

### Execution Agents (Testing, Automation)
**Tools**: Read, Grep, Glob, Edit, Write, Bash
**Use for**: Testing, automation, complex workflows
**Caution**: Full capability, needs careful permissions

## Quality Standards

All generated agents will:
- Have clear professional identity
- Include structured 3-6 phase workflow
- Specify appropriate tool set
- List relevant skills to use
- Define quality gates
- Provide output templates
- Include integration guidance
- Have concrete examples
