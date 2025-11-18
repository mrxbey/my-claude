# Agents API Reference

Quick reference for all MyClaude agents. See [Agents User Guide](../user-guide/agents.md) for detailed documentation.

## Agent List

| Agent | Purpose | Tools | Model | Skills |
|-------|---------|-------|-------|--------|
| analyze-agent | Systematic analysis using frameworks | Read, Grep, Glob, Edit, Write, Bash | sonnet | analysis, implementation-guardrails |
| docs-agent | Documentation verification and compliance | Read, Grep, Glob | sonnet | doc-compliance, analysis |
| translate-agent | Translation with cultural adaptation | Read, Write | sonnet | translation |
| proofread-agent | Professional editing and proofreading | Read, Write | sonnet | proofreading |
| skill-crafter | Create new skills interactively | Read, Write, Grep, Glob | sonnet | skill-crafter |
| agent-crafter | Create new agents interactively | Read, Write, Grep, Glob | sonnet | - |

## Quick Reference

### analyze-agent

**Triggers**: analyze, evaluate, compare, investigate, study, strategic, decision

**Workflow**: 6 phases
1. Clarify - Restate problem
2. Decompose - Break into dimensions  
3. Investigate - Gather evidence
4. Options - Generate 2-4 alternatives
5. Synthesize - Evaluate trade-offs
6. Present - Structured report

**Output**: Analysis report with options table, recommendation, action checklist

---

### docs-agent

**Triggers**: documentation, docs, verify, compliance, policy, specification, validate

**Workflow**: 5 steps
1. Discovery - Find relevant docs
2. Requirements - Extract with IDs
3. Verification - Check implementation
4. Gap Analysis - Identify gaps
5. Reporting - Compliance table with ✅/⚠️/❌

**Output**: Compliance table, gap analysis, remediation roadmap

---

### translate-agent

**Triggers**: translate, localize, language, multilingual, French, Spanish, German, Japanese

**Workflow**: 6 steps
1. Context - Understand target language/audience
2. Glossary - Build/update terminology
3. Translate - Preserve meaning, adapt tone
4. Cultural - Handle cultural references
5. Variants - Provide alternatives
6. Document - Note translation decisions

**Output**: Translation, glossary, decision notes, quality metrics

---

### proofread-agent

**Triggers**: proofread, edit, grammar, clarity, style, polish

**Workflow**: 5 categories
1. Grammar & Punctuation
2. Clarity & Conciseness
3. Structure & Flow
4. Tone & Style
5. Terminology & Consistency

**Output**: Edited content, change summary, major improvements highlighted

---

### skill-crafter

**Triggers**: create skill, new skill, design skill, add capability

**Workflow**: 6 phases
1. Interview - Purpose, use cases, scope
2. Design - Structure, workflow, tools
3. Generate - SKILL.md with frontmatter
4. Validate - YAML, structure, keywords
5. Integrate - Agent recommendations
6. Test - Scenarios and verification

**Output**: Complete skill in `.claude/skills/[name]/SKILL.md`

---

### agent-crafter

**Triggers**: create agent, new agent, design agent, specialized agent

**Workflow**: 6 phases
1. Interview - Role, tasks, complexity
2. Design - Identity, workflow, decision pattern
3. Tools - Permissions and capabilities
4. Skills - Integration selection
5. Generate - agent.md with YAML + prompt
6. Validate - Test invocation

**Output**: Complete agent in `.claude/agents/[name].md`

## YAML Frontmatter Schema

### Required Fields

```yaml
name: agent-name              # Lowercase, hyphenated
description: Short description with triggers. Triggers - keyword1, keyword2, keyword3.
tools: Read, Grep, Glob       # Comma-separated
model: sonnet                 # sonnet, opus, haiku, inherit
```

### Optional Fields

```yaml
permissionMode: default       # default, acceptEdits, plan
skills: skill1, skill2        # Comma-separated skill names
```

## Related Documentation

- [Agents User Guide](../user-guide/agents.md) - Comprehensive guide
- [Creating Agents](../developer-guide/creating-agents.md) - Development guide
