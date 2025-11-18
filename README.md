# MyClaude Framework

> **Enterprise-grade AI agent framework for business workflows**

MyClaude is a production-ready framework built on Claude Code that transforms Claude into a specialized, extensible platform for business operations. It provides intelligent agents for analysis, documentation, translation, proofreading, and a meta-programming layer that can extend itself.

## 🚀 Quick Start

```bash
# 1. Clone this repository into your project
cp -r my-claude/.claude your-project/
cp my-claude/CLAUDE.md your-project/

# 2. Set your API key
export ANTHROPIC_API_KEY=your-key-here

# 3. Start Claude Code
claude

# 4. Try a command
/analyze "Analyze the project structure"
```

## ✨ Features

### Core Agents (Model-Invoked)
- **analyze-agent**: Deep analysis specialist for code, data, and business situations
- **docs-agent**: Documentation verification and policy compliance specialist
- **translate-agent**: High-quality translation with tone adaptation
- **proofread-agent**: Professional editing and style consistency

### Meta Agents (Self-Extension)
- **skill-crafter**: Creates new skills through conversation
- **agent-crafter**: Designs new agents based on requirements

### Core Skills (Auto-Loaded)
- **analysis**: Systematic analysis patterns for complex problems
- **doc-compliance**: Documentation verification and checklists
- **translation**: Translation patterns with glossaries
- **proofreading**: Editing patterns and style enforcement
- **implementation-guardrails**: Quality gates and validation (5-check system)
- **skill-crafter**: Meta-skill for creating new skills

### Slash Commands (User-Invoked)
- `/analyze` - Deep analysis workflow
- `/check-docs` - Documentation verification
- `/translate` - Translation workflow
- `/proofread` - Editing and proofreading
- `/skill-crafter` - Create new skills interactively
- `/agent-crafter` - Create new agents interactively

## 🏗️ Architecture

```
MyClaude Framework
├── Commands (User-Invoked) → /analyze, /check-docs, etc.
├── Agents (Model-Invoked) → Specialized independent agents
├── Skills (Model-Invoked) → Domain expertise, auto-loaded
├── Settings → Permissions, hooks, quality gates
└── Claude Code → Foundation infrastructure
```

**Key Innovation:** Progressive disclosure pattern keeps context lean while providing unlimited depth when needed.

## 📖 Documentation

- **[Getting Started](docs/getting-started/)** - Installation and quick start
- **[User Guide](docs/user-guide/)** - Commands, agents, skills, workflows
- **[Developer Guide](docs/developer-guide/)** - Creating skills and agents
- **[Reference](docs/reference/)** - Complete API reference

## 🎯 Use Cases

### Business Analysis
```bash
/analyze "Analyze customer churn data and recommend strategies"
```

### Documentation Review
```bash
/check-docs "Verify API documentation matches implementation"
```

### Content Translation
```bash
/translate "Translate marketing copy to Spanish, professional tone"
```

### Content Editing
```bash
/proofread "Edit this blog post for clarity and brand voice"
```

### Meta-Programming
```bash
/skill-crafter "Create skill for API testing"
/agent-crafter "Create agent for security audits"
```

## 🔧 Configuration

MyClaude uses Claude Code's native `.claude/settings.json` for configuration:

**Permissions:** Fine-grained access control (allow/ask/deny)
**Hooks:** Automatic validation, formatting, quality checks
**Quality Gates:** Pre-execution validation via hooks
**Audit Trail:** Complete operation logging

See [Configuration Reference](docs/reference/configuration-reference.md) for details.

## 📊 Enterprise Features

- ✅ **Quality Gates**: Pre-execution validation with confidence scoring
- ✅ **Audit Trail**: Complete operation logging for compliance
- ✅ **Permissions**: Fine-grained access control
- ✅ **Progressive Disclosure**: Efficient context management
- ✅ **Meta-Programming**: Self-extending framework
- ✅ **Version Control**: Team-shareable configuration
- ✅ **Validation**: Automated framework health checks

## 🎓 Examples

See the `examples/` directory for complete usage examples:

- **[simple-analysis/](examples/simple-analysis/)** - Basic analysis workflow
- **[document-review/](examples/document-review/)** - Documentation verification
- **[translation-workflow/](examples/translation-workflow/)** - Translation process
- **[custom-agent/](examples/custom-agent/)** - Creating custom agents

## 🛠️ Development

### Creating a New Skill

```bash
/skill-crafter "Create skill for [your use case]"
```

Or manually create `.claude/skills/your-skill/SKILL.md`:

```yaml
---
name: your-skill
description: What it does and when to use it
version: 1.0.0
---

# Your Skill

Instructions go here...
```

### Creating a New Agent

```bash
/agent-crafter "Create agent for [your use case]"
```

Or manually create `.claude/agents/your-agent.md`:

```yaml
---
name: your-agent
description: When to invoke this agent
tools: Read, Grep, Glob
model: sonnet
skills: relevant-skill-1, relevant-skill-2
---

# Your Agent

Role and instructions go here...
```

## 🔍 Validation

```bash
# Check framework health
python scripts/health_check.py

# Validate configuration
python scripts/validate_framework.py

# Run test scenarios
cd tests && claude < test_agents.md
```

## 📈 Metrics

MyClaude tracks:
- Context usage (progressive disclosure efficiency)
- Quality gate success rates
- Audit trail completeness
- Agent invocation patterns

See `.claude/logs/` for audit logs.

## 🤝 Contributing

1. Create a new skill or agent using the meta-agents
2. Test thoroughly with various scenarios
3. Document in the appropriate guide
4. Share your extensions!

## 📄 License

[Your License Here]

## 🙏 Acknowledgments

- Built on [Claude Code](https://code.claude.com/)
- Inspired by [SuperClaude Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework)
- Powered by Claude Sonnet 4.5

## 📞 Support

- **Documentation**: [docs/](docs/)
- **Analysis**: [ANALYSIS.md](ANALYSIS.md)
- **Architecture**: [ARCHITECTURE.md](ARCHITECTURE.md)
- **Design Philosophy**: [DESIGN_PHILOSOPHY.md](DESIGN_PHILOSOPHY.md)

---

**MyClaude Framework** - Enterprise-grade thinking, pragmatic implementation.
