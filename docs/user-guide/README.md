# MyClaude User Guide

Welcome to the MyClaude framework user guide. This guide will help you understand and effectively use all framework components.

## Quick Start

**New to MyClaude?** Start here:
1. Read [Commands Guide](commands.md) to learn user-invoked workflows
2. Try `/analyze examples/simple-analysis/` to see the framework in action
3. Explore [Agents Guide](agents.md) to understand automatic delegation

## User Guides

### Core Guides

- **[Commands Guide](commands.md)** - User-invoked slash commands for explicit workflow control
- **[Agents Guide](agents.md)** - Model-invoked specialists that automatically handle tasks
- **[Skills Guide](skills.md)** - Domain expertise that enhances agent capabilities
- **[Workflows Guide](workflows.md)** - Multi-phase processes with quality gates

### Key Concepts

**Commands** (User-Invoked):
```
/analyze <topic>          → Explicit analysis workflow
/workflows/code-review    → Multi-agent review process
```

**Agents** (Model-Invoked):
```
"Analyze the caching strategy"  → auto-triggers analyze-agent
"Check docs for compliance"     → auto-triggers docs-agent
```

**Skills** (Auto-Loaded):
- Load automatically based on trigger keywords
- Provide frameworks and patterns to agents
- Use progressive disclosure for efficiency

**Workflows** (Orchestrated):
- Multi-phase processes
- Quality gates between phases
- Multiple agents working together

## Getting Started

### Try Your First Analysis

```
/analyze examples/simple-analysis/
```

This demonstrates:
- Automatic agent delegation
- Skill integration (analysis frameworks)
- 6-phase systematic workflow
- Evidence-based output

### Check Documentation Accuracy

```
/check-docs @README.md against implementation
```

This demonstrates:
- File reference with `@`
- Documentation verification workflow
- Compliance table output

### Create a Custom Skill

```
/skill-crafter Create a skill for API testing
```

This demonstrates:
- Interactive meta-agent
- Framework self-extension
- Template-based generation

## Common Tasks

### Analysis Tasks
- **Strategic decisions**: `/analyze <decision-topic>`
- **Architecture evaluation**: `/analyze <architecture-component>`
- **Options comparison**: `/analyze <options-to-compare>`

### Documentation Tasks
- **Verify accuracy**: `/check-docs @docs/spec.md`
- **Check compliance**: Use docs-agent for policy compliance
- **Update docs**: Use proofread-agent for quality

### Content Tasks
- **Translation**: `/translate English to Spanish`
- **Editing**: `/proofread <content>`
- **Localization**: Use translate-agent with cultural adaptation

### Development Tasks
- **Code review**: `/workflows/code-review src/`
- **Feature development**: `/workflows/feature-development <feature>`
- **Create custom tools**: Use skill-crafter or agent-crafter

## Framework Components

| Component | Count | Purpose |
|-----------|-------|---------|
| Agents | 6 | Specialized autonomous workers |
| Skills | 6 | Domain expertise and frameworks |
| Commands | 8 | User-invoked workflows |
| Workflows | 2 | Multi-phase orchestration |

## Progressive Disclosure

The framework uses 3-level loading for efficiency:

**Level 1** (~500 tokens): All metadata loaded at startup
**Level 2** (~1500 tokens): Active agent + 1-2 skills
**Level 3** (~5000 tokens): Deep expertise with references

This allows unlimited skills while keeping context minimal.

## Getting Help

- **Commands**: See [Commands Guide](commands.md)
- **Agents**: See [Agents Guide](agents.md)
- **Skills**: See [Skills Guide](skills.md)
- **Workflows**: See [Workflows Guide](workflows.md)

## Next Steps

1. **Try the examples**: `examples/simple-analysis/`
2. **Read the guides**: Start with commands, then agents, then skills
3. **Extend the framework**: Use `/skill-crafter` or `/agent-crafter`
4. **Share with team**: All configuration is version-controlled

Happy building! 🚀
