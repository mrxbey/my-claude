# MyClaude Agents

This directory contains specialized AI agents that Claude can automatically delegate tasks to. Each agent has independent context and specific expertise.

## Agent Types

### Core Business Agents

**Model-Invoked** - Claude automatically delegates based on task description

- **[analyze-agent.md](analyze-agent.md)** - Deep analysis specialist
- **[docs-agent.md](docs-agent.md)** - Documentation verification specialist
- **[translate-agent.md](translate-agent.md)** - Translation and localization specialist
- **[proofread-agent.md](proofread-agent.md)** - Editing and proofreading specialist

### Meta Agents

**Self-Extension** - Agents that create new framework components

- **[skill-crafter.md](skill-crafter.md)** - Creates new skills interactively
- **[agent-crafter.md](agent-crafter.md)** - Creates new agents interactively

## Agent Anatomy

Each agent is a Markdown file with YAML frontmatter:

```yaml
---
name: agent-name                           # Required: Unique identifier
description: When to invoke this agent     # Required: Natural language triggers
tools: Read, Grep, Glob, Edit, Write      # Optional: Allowed tools (inherits all if omitted)
model: sonnet                              # Optional: sonnet | opus | haiku | inherit
permissionMode: default                    # Optional: default | acceptEdits | bypassPermissions
skills: skill1, skill2                     # Optional: Auto-load these skills
---

# Agent Prompt

Your detailed system prompt and instructions...
```

## How Agents Work

1. **Independent Context**: Each agent has its own context window
2. **Model-Invoked**: Claude automatically delegates based on description
3. **Skill Integration**: Agents can use skills for portable expertise
4. **Tool Restrictions**: Control which tools each agent can use
5. **Result Return**: Agent returns results to main conversation

## When to Use Agents vs Skills

| Use Agent When | Use Skill When |
|----------------|----------------|
| Need independent context | Want to extend main context |
| Complex multi-phase workflow | Provide reference patterns |
| Specialized tool restrictions | No tool restrictions needed |
| Want explicit delegation | Want automatic application |

## Creating New Agents

### Method 1: Use Agent Crafter (Recommended)

```bash
/agent-crafter "Create agent for [your use case]"
```

The agent-crafter will interview you and generate a complete agent file.

### Method 2: Manual Creation

1. Create `.claude/agents/your-agent.md`
2. Add YAML frontmatter with required fields
3. Write clear system prompt with:
   - Role and expertise
   - Workflow phases
   - Quality standards
   - Output format
4. Test by asking Claude to delegate a task

## Agent Best Practices

### Writing Effective Descriptions

✅ **Good**: "Security audit specialist for OWASP vulnerabilities. Use for security reviews, threat modeling, or vulnerability assessment."

❌ **Bad**: "Security agent"

**Include:**
- What the agent does
- When to use it
- Specific trigger keywords

### Designing Agent Workflows

Structure agents with clear phases:

```markdown
## Workflow

### Phase 1: Discovery
- Understand requirements
- Gather context
- Identify constraints

### Phase 2: Analysis
- Apply expertise
- Use relevant skills
- Generate insights

### Phase 3: Synthesis
- Organize findings
- Create recommendations
- Prioritize actions

### Phase 4: Delivery
- Format output
- Validate quality
- Provide next steps
```

### Tool Selection

**Minimal Tools** (Read, Grep, Glob):
- Analysis-only agents
- Read-only operations
- Security-sensitive agents

**Standard Tools** (Read, Grep, Glob, Edit, Write):
- Most agents
- Can modify files
- Follow permission rules

**Extended Tools** (+ Bash):
- Agents that need to execute commands
- Testing and validation agents
- Requires careful permission design

### Skill Integration

Link agents with relevant skills:

```yaml
skills: analysis, doc-compliance, security-patterns
```

Skills provide portable expertise that agents can use automatically.

## Testing Agents

### Test Invocation

```
# Test automatic delegation
Ask Claude: "Use the analyze-agent to review this code"

# Verify agent loads
Claude should respond indicating the agent is active

# Check agent uses skills correctly
Agent should reference skill patterns in response
```

### Validation Checklist

- [ ] YAML frontmatter is well-formed
- [ ] Description clearly states when to use
- [ ] Tools are appropriate for agent's role
- [ ] Workflow phases are clear and actionable
- [ ] Quality standards are explicit
- [ ] Output format is specified
- [ ] Skills are linked if relevant
- [ ] Agent can be invoked automatically

## Agent Examples

See individual agent files for complete examples:

- [analyze-agent.md](analyze-agent.md) - Complex analysis patterns
- [docs-agent.md](docs-agent.md) - Documentation verification
- [translate-agent.md](translate-agent.md) - Translation workflows
- [proofread-agent.md](proofread-agent.md) - Editing patterns

## Troubleshooting

**Agent Not Invoked?**
- Check description includes trigger keywords
- Try explicit invocation: "Use the X agent to..."
- Verify YAML is well-formed

**Agent Missing Tools?**
- Check `tools` field matches needs
- Verify permissions in settings.json
- Consider if agent needs explicit tool list

**Agent Not Using Skills?**
- Check `skills` field lists skill names
- Verify skills exist in .claude/skills/
- Skills should be referenced in agent prompt

## Contributing

When creating agents for the framework:

1. Use agent-crafter for consistency
2. Test with various scenarios
3. Document clearly with examples
4. Share useful agents with the team
5. Version control agent files

---

For more information, see:
- [User Guide: Agents](../../docs/user-guide/agents.md)
- [Developer Guide: Creating Agents](../../docs/developer-guide/creating-agents.md)
- [Official Docs](https://code.claude.com/docs/en/sub-agents)
