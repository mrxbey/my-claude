# MyClaude Framework - 5-Minute Quick Start

Get started with the MyClaude framework in 5 minutes. This guide shows you the most important commands and concepts.

---

## 📦 Setup (30 seconds)

```bash
# Navigate to your project
cd my-claude

# Start Claude Code
claude
```

That's it! The framework is already configured in `.claude/`.

---

## 🎯 Core Concepts (1 minute)

**MyClaude provides 3 types of components:**

1. **Agents** - Specialized AI teammates with expertise (security, translation, analysis)
2. **Skills** - Reusable patterns and frameworks (SWOT analysis, compliance checking)
3. **Commands** - Quick workflows you can invoke (`/analyze`, `/check-docs`, `/translate`)

**Progressive Disclosure**: Components load efficiently
- Startup: ~768 tokens (metadata only)
- Active: ~2-3K tokens (when you use an agent)
- Full: ~8-10K tokens (with references)

---

## 🚀 Try These Examples (3 minutes)

### Example 1: Analyze a Decision (30 seconds)

```
> Analyze the caching strategy options in examples/simple-analysis/
  and recommend the best approach
```

**What happens:**
- `analyze-agent` automatically loads (keyword: "analyze")
- Reads current implementation and requirements
- Generates decision matrix with 3-4 options
- Provides recommendation with action checklist

**Output:** Comprehensive analysis report (~2 minutes to generate)

---

### Example 2: Check Documentation Compliance (30 seconds)

```
> Check if examples/document-review/current-implementation.md
  complies with examples/document-review/security-policy.md
```

**What happens:**
- `docs-agent` automatically loads (keyword: "check", "complies")
- Extracts 11 security requirements from policy
- Verifies implementation against each requirement
- Generates compliance table with ✅/⚠️/❌ status
- Provides remediation roadmap

**Output:** Compliance report with gap analysis

---

### Example 3: Translate Content (30 seconds)

```
> Translate examples/translation-workflow/source-english.md to Spanish,
  formal business tone, use the glossary
```

**What happens:**
- `translate-agent` automatically loads (keyword: "translate", "Spanish")
- Loads glossary with 30+ technical terms
- Translates maintaining brand voice and technical accuracy
- Generates translation notes documenting decisions

**Output:** Professional Spanish translation + decision log

---

## 💡 Quick Reference

### Automatic Agent Triggering

Agents load automatically based on keywords:

| Agent | Triggers | Use For |
|-------|----------|---------|
| **analyze-agent** | analyze, evaluate, compare, decide | Decisions, trade-offs, options |
| **docs-agent** | check, verify, complies, policy | Compliance, documentation review |
| **translate-agent** | translate, Spanish, French, German | Translation, localization |
| **proofread-agent** | proofread, edit, grammar, polish | Editing, style consistency |

### Slash Commands

For specific workflows:

```
/analyze <topic>              # Deep analysis workflow
/check-docs <target>          # Documentation verification
/translate <source> to <target>  # Translation workflow
/proofread <content>          # Professional editing
/agent-crafter <description>  # Create custom agent
/skill-crafter <description>  # Create custom skill
```

### Common Patterns

**Chain agents:**
```
> First use docs-agent to check compliance,
  then use analyze-agent to assess the risk of gaps
```

**Explicit invocation:**
```
> Use analyze-agent to evaluate database options
```

**With specific instructions:**
```
> Translate to Spanish, use formal register (usted),
  prioritize Latin American vocabulary
```

---

## 📚 Next Steps (1 minute)

### Explore Examples

All examples are complete and ready to use:

1. **[simple-analysis](../examples/simple-analysis/)** - Decision analysis with caching strategies
2. **[document-review](../examples/document-review/)** - API security policy compliance
3. **[translation-workflow](../examples/translation-workflow/)** - Product launch translation (EN→ES)
4. **[custom-agent](../examples/custom-agent/)** - Create your own specialized agents

### Learn More

- **User Guides**: [docs/user-guide/](user-guide/) - How to use agents, skills, commands
- **Developer Guides**: [docs/developer-guide/](developer-guide/) - How to extend the framework
- **API Reference**: [docs/reference/](reference/) - Quick lookup for all components

### Try Creating Your Own

```
> /agent-crafter Create an agent for security audits
```

or

```
> /skill-crafter Create a skill for data validation
```

The framework will guide you through the design process interactively.

---

## 🎓 Key Takeaways

1. **Agents auto-trigger** based on keywords - no explicit invocation needed
2. **Skills auto-load** when agents reference them - provides domain expertise
3. **Progressive disclosure** keeps context usage low - efficient even with many components
4. **Evidence-based** - all findings reference specific files and line numbers
5. **Structured output** - consistent formats make results immediately actionable

---

## 💬 Common Questions

**Q: Do I need to invoke agents explicitly?**
A: No! Use natural language. Agents trigger automatically based on keywords.

**Q: Can I use multiple agents together?**
A: Yes! Chain them: "First use X, then use Y" or let them collaborate naturally.

**Q: How do I know which agent will trigger?**
A: The agent descriptions list trigger keywords. Use those terms in your request.

**Q: Can I create my own agents/skills?**
A: Absolutely! Use `/agent-crafter` or `/skill-crafter` for guided creation.

**Q: Where are agents and skills stored?**
A: `.claude/agents/*.md` for agents, `.claude/skills/*/SKILL.md` for skills

---

## 🚨 Getting Help

**Framework issues:**
```bash
python scripts/health_check.py  # Check framework health
python scripts/validate_framework.py  # Validate configuration
```

**Documentation:**
- This quickstart: `docs/QUICKSTART.md`
- User guides: `docs/user-guide/`
- Examples with full walkthroughs: `examples/`

**Next**: Try the [simple-analysis example](../examples/simple-analysis/) to see the full workflow in action!

---

**You're ready to go!** 🎉

The framework is designed to feel like having specialized AI teammates. Just describe what you need in natural language, and the right agent will step in to help.
