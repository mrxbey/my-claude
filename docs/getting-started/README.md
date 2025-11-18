# Getting Started with MyClaude

**Go from zero to 10x productivity in 5 minutes**

Welcome! This guide will help you run your first workflow and start saving time immediately.

---

## What You'll Learn

1. **Setup** (1 minute) - Get MyClaude running
2. **Your First Workflow** (2 minutes) - Experience the magic
3. **Choose Your Workflows** (2 minutes) - Find workflows for your role

**Total time: 5 minutes to productivity boost**

---

## Step 1: Setup (1 Minute)

### Prerequisites

- Claude Code installed (get it at [code.claude.com](https://code.claude.com))
- Anthropic API key (get from [console.anthropic.com](https://console.anthropic.com))

### Installation

```bash
# 1. Clone or copy the MyClaude framework
git clone https://github.com/your-username/my-claude.git
cd my-claude

# 2. Set your API key
export ANTHROPIC_API_KEY=your-key-here

# 3. Start Claude Code
claude
```

**That's it!** You're ready to use MyClaude.

---

## Step 2: Your First Workflow (2 Minutes)

Let's try a research workflow that would normally take 8 hours but will take 1 hour with MyClaude.

### Choose A or B:

#### Option A: Research Something You're Curious About

Think of a topic you want to learn about. Examples:
- "Best project management tools for remote teams"
- "Emerging trends in sustainable packaging"
- "How to improve customer retention in SaaS"

```bash
/workflows/research-synthesis "YOUR TOPIC HERE"
```

**What happens:**
1. ✅ Claude clarifies your research question (30 seconds)
2. ✅ Finds and evaluates sources (5 minutes)
3. ✅ Extracts key information into evidence table (10 minutes)
4. ✅ Synthesizes findings with insights (15 minutes)
5. ✅ Validates evidence quality (10 minutes)
6. ✅ Generates comprehensive research report (10 minutes)

**Result:** Professional research report with:
- Executive summary
- Key findings with sources
- Evidence table
- Analysis and insights
- Conclusions with confidence levels
- Bibliography

**Time:** 50-60 minutes instead of 8 hours = **8-12x faster**

---

#### Option B: Write a Professional Email

Think of an email you need to send. Examples:
- "Request budget approval from CFO for marketing campaign"
- "Follow up with client about delayed project"
- "Thank colleague for help on recent presentation"

```bash
/workflows/professional-email "YOUR EMAIL PURPOSE HERE"
```

**What happens:**
1. ✅ Analyzes context (recipient, urgency, relationship) (1 minute)
2. ✅ Identifies your goal and success criteria (1 minute)
3. ✅ Selects appropriate tone (formal/professional/casual) (1 minute)
4. ✅ Composes email with clear structure (2 minutes)
5. ✅ Checks clarity and brevity (1 minute)
6. ✅ Proofreads and polishes (1 minute)

**Result:** Professional, context-appropriate email ready to send

**Time:** 7 minutes instead of 30 minutes = **6x faster**

---

### 🎉 Congratulations!

You just completed your first MyClaude workflow!

**What you experienced:**
- ✅ Systematic multi-phase process
- ✅ Quality gates ensuring high standards
- ✅ Professional output without the work
- ✅ Massive time savings

**This is just the beginning.** There are 7 more workflows waiting for you.

---

## Step 3: Choose Your Workflows (2 Minutes)

Based on your role, here are workflows you'll use most:

### I'm a Marketer

**Daily:**
- `/workflows/professional-email` - Campaign emails, client communication
- `/workflows/content-creation` - Blog posts, whitepapers, social media

**Weekly:**
- `/workflows/research-synthesis` - Market research, trend analysis
- `/workflows/competitive-analysis` - Competitor intelligence

**Monthly:**
- `/workflows/proposal-pitch` - Campaign proposals, budget requests

**Try next:** `/workflows/content-creation "Blog post about [YOUR TOPIC]"`

---

### I'm in Sales

**Daily:**
- `/workflows/professional-email` - Client emails, follow-ups
- `/workflows/meeting-prep` - Sales call preparation

**Weekly:**
- `/workflows/proposal-pitch` - Sales proposals, RFP responses
- `/workflows/competitive-analysis` - Battle cards, competitive intel

**Monthly:**
- `/workflows/research-synthesis` - Account research, industry trends

**Try next:** `/workflows/meeting-prep "Sales demo with [PROSPECT NAME]"`

---

### I'm an Executive

**Weekly:**
- `/workflows/professional-email` - Board updates, strategic communication
- `/workflows/research-synthesis` - Market intelligence, strategic research
- `/workflows/competitive-analysis` - Strategic positioning

**Monthly:**
- `/workflows/proposal-pitch` - Board proposals, investor decks
- `/workflows/meeting-prep` - Board meetings, investor meetings

**Try next:** `/workflows/competitive-analysis "Our market position in [INDUSTRY]"`

---

### I'm a Product Manager

**Daily:**
- `/workflows/professional-email` - Stakeholder updates, team communication
- `/workflows/meeting-prep` - Sprint planning, stakeholder meetings

**Weekly:**
- `/workflows/research-synthesis` - User research, market analysis
- `/workflows/feature-development` - Feature planning and execution

**Monthly:**
- `/workflows/competitive-analysis` - Product positioning, feature comparison
- `/workflows/proposal-pitch` - Product proposals, roadmap presentations

**Try next:** `/workflows/research-synthesis "User needs for [FEATURE]"`

---

### I'm a Researcher/Academic

**Weekly:**
- `/workflows/research-synthesis` - Literature reviews, systematic research
- `/workflows/content-creation` - Academic writing, papers

**Monthly:**
- `/workflows/proposal-pitch` - Grant applications, research proposals
- `/workflows/professional-email` - Collaboration outreach, journal communication

**Try next:** `/workflows/research-synthesis "[YOUR RESEARCH TOPIC]"`

---

### I'm a Developer

**Daily:**
- `/workflows/code-review` - Pre-merge reviews, security audits
- `/workflows/professional-email` - Technical communication

**Weekly:**
- `/workflows/feature-development` - New feature implementation
- `/workflows/research-synthesis` - Technical research, architecture decisions

**Monthly:**
- `/workflows/content-creation` - Technical documentation, blog posts

**Try next:** `/workflows/code-review "src/[YOUR MODULE]"`

---

## Quick Reference Card

**Save this for daily use:**

| I want to... | Use this workflow |
|--------------|-------------------|
| Research anything | `/workflows/research-synthesis` |
| Write content (blog, article, whitepaper) | `/workflows/content-creation` |
| Send important email | `/workflows/professional-email` |
| Understand competitors | `/workflows/competitive-analysis` |
| Create proposal/pitch | `/workflows/proposal-pitch` |
| Prepare for meeting | `/workflows/meeting-prep` |
| Review code | `/workflows/code-review` |
| Build new feature | `/workflows/feature-development` |

**Full reference:** [Workflow Quick Reference Guide](../WORKFLOW_GUIDE.md)

---

## Tips for Success

### 1. Be Specific

❌ **Vague**: `/workflows/research-synthesis "marketing"`

✅ **Specific**: `/workflows/research-synthesis "Best email marketing platforms for B2B SaaS companies under 50 employees"`

**More specific = better results**

---

### 2. Provide Context

When using workflows, give relevant context:

```bash
/workflows/professional-email "Request budget approval from CFO.
Context: Need $50K for Q4 marketing campaign, expecting 3x ROI based on Q3 results.
Tone: Professional but concise - she's busy."
```

**More context = more appropriate output**

---

### 3. Trust the Process

Workflows have multiple phases with quality gates. Let them run:

- Phase 1: ✅ (Takes 2-3 minutes - analyzing context)
- Phase 2: ✅ (Takes 5 minutes - gathering information)
- Quality Gate: ✅ (Validating quality standards)
- Phase 3: ✅ (Processing...)

**Don't interrupt. Each phase adds value.**

---

### 4. Use Workflows Daily

The more you use workflows, the more time you save:

**Week 1:** "This is cool" → Save 5 hours
**Week 2:** "This is useful" → Save 10 hours
**Week 4:** "Can't live without it" → Save 15+ hours

**Build the habit. Make it part of your workflow.**

---

## Common Questions

### How do I know which workflow to use?

**Easy decision tree:**
1. Writing something → content-creation or professional-email
2. Researching something → research-synthesis or competitive-analysis
3. Presenting/proposing → proposal-pitch
4. Meeting someone → meeting-prep
5. Code-related → code-review or feature-development

**Still not sure?** Check the [Workflow Quick Reference](../WORKFLOW_GUIDE.md)

---

### How long do workflows take?

**Depends on complexity:**

- **Email workflow**: 5-7 minutes
- **Research workflow**: 45-60 minutes
- **Content creation**: 20-30 minutes
- **Competitive analysis**: 2-3 hours
- **Proposal creation**: 2-3 hours
- **Meeting prep**: 20-30 minutes

**Compare to manual time:** 4-12x faster with higher quality

---

### Can I customize workflows?

**Yes!** Three ways:

1. **Add context to your request** (easiest)
   - "Include specific focus on [aspect]"
   - "Use formal tone"
   - "Target audience is [description]"

2. **Create custom skills** (intermediate)
   - `/skill-crafter "Create skill for [YOUR USE CASE]"`
   - Reusable patterns for your specific needs

3. **Create custom agents** (advanced)
   - `/agent-crafter "Create agent for [YOUR USE CASE]"`
   - Specialized agents for your domain

**See:** [Developer Guide](../developer-guide/) for customization

---

### What if the output isn't perfect?

**Workflows are 90-95% solutions.** You'll still review and refine:

1. **Review the output** - Check accuracy, tone, completeness
2. **Make edits** - Adjust as needed for your specific context
3. **Learn the pattern** - Notice what works, refine future requests

**Goal:** Not perfection without review, but excellent first drafts that save massive time

---

### Can I use multiple workflows together?

**Absolutely!** Workflows compose:

**Example workflow chain:**
```bash
# 1. Research a topic
/workflows/research-synthesis "AI in customer service 2024-2025"

# 2. Use research to write content
/workflows/content-creation "Blog post about AI customer service trends"

# 3. Email to promote the blog
/workflows/professional-email "Send blog post to client list with value-add message"
```

**Result:** Research → Content → Distribution, all in < 2 hours instead of 2+ days

---

## Next Steps

Now that you've completed your first workflow:

### Today
- [ ] Try 2 more workflows from your role section above
- [ ] Bookmark the [Workflow Quick Reference](../WORKFLOW_GUIDE.md)
- [ ] Note how much time you saved

### This Week
- [ ] Use workflows for real work tasks
- [ ] Track time saved (you'll be amazed)
- [ ] Share with a colleague

### This Month
- [ ] Build workflow habits (use 5+ times per week)
- [ ] Explore workflow composition
- [ ] Consider creating custom workflows for your specific needs

---

## Get Help

**Documentation:**
- [Workflow Quick Reference](../WORKFLOW_GUIDE.md) - One-page guide
- [User Guide: Workflows](../user-guide/workflows.md) - Detailed workflow docs
- [Examples Directory](../../examples/) - Real output examples

**Stuck?**
- Check examples for your workflow
- Review [User Guide](../user-guide/README.md)
- Consult [Developer Guide](../developer-guide/) for advanced customization

---

## Welcome to 10x Productivity! 🚀

You're now equipped with 8 powerful workflows that will transform how you work.

**Remember:**
- ✅ Be specific in your requests
- ✅ Provide context
- ✅ Trust the multi-phase process
- ✅ Use workflows daily to build the habit

**The more you use MyClaude, the more time you save. Every week, every month, adding up to hundreds of hours per year.**

**You've got this. Now go reclaim your time!**

---

**Quick Links:**
- 📖 [Workflow Quick Reference](../WORKFLOW_GUIDE.md)
- 📚 [Full Documentation](../user-guide/README.md)
- 💼 [Real Examples](../../examples/)
- 🔧 [Customization Guide](../developer-guide/)
