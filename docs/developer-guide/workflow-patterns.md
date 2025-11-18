# Workflow Composition Patterns

This guide documents proven patterns for composing and orchestrating workflows in the MyClaude framework.

## Overview

Workflows can be **composed** (combined) in powerful ways to handle complex multi-step processes. Understanding these patterns helps you:
- Build more sophisticated workflows
- Reuse existing workflows effectively
- Create maintainable, clear processes
- Avoid common pitfalls

---

## Core Composition Patterns

### 1. Sequential Pattern (A → B → C)

**Description**: Execute workflows or phases one after another, where each step depends on the previous.

**When to Use**:
- Steps must happen in order
- Later steps need output from earlier steps
- Clear linear progression

**Structure**:
```
Phase 1: [Do A]
→ Output: [Result A]

Phase 2: [Do B using Result A]
→ Output: [Result B]

Phase 3: [Do C using Result B]
→ Output: [Final Result]
```

**Real Example**: Content Creation Workflow
```
1. Audience & Purpose → Content brief
2. Research & Outline → Structured outline
3. Draft Creation → First draft
4. Style Refinement → Styled draft
5. Proofreading → Polished draft
6. Compliance Check → Verified draft
7. Final Polish → Publication-ready content
```

**Best Practices**:
- ✅ Clear output from each phase
- ✅ Explicit dependencies (Phase N uses output from Phase N-1)
- ✅ Quality gates between phases
- ❌ Don't make unnecessary dependencies (if phases could be parallel, make them parallel)

---

### 2. Validation-Gated Pattern (A → Gate → B or Stop)

**Description**: Include quality checkpoints that can stop or redirect the workflow if criteria aren't met.

**When to Use**:
- Risk of proceeding with bad inputs
- Quality requirements critical
- Need decision point before continuing
- Resource investment increases in later phases

**Structure**:
```
Phase 1: [Preparation]
→ Output: [Initial work]

Quality Gate: [Validation criteria]
├─ PASS → Continue to Phase 2
└─ FAIL → Stop or return to Phase 1

Phase 2: [Main work]
→ Output: [Result]
```

**Real Example**: Feature Development Workflow
```
Phase 1: Requirements Analysis
Phase 2: Pre-Implementation Validation
  ├─ Confidence ≥ 0.9: Proceed to design
  ├─ Confidence 0.7-0.89: Clarify gaps, then proceed
  └─ Confidence < 0.7: STOP - Re-analyze problem

Phase 3: Design (only if validation passed)
```

**Best Practices**:
- ✅ Clear pass/fail criteria (no ambiguity)
- ✅ Explicit actions for each outcome (pass, fail, partial)
- ✅ Document why gate exists (what risk it mitigates)
- ✅ Make gates meaningful (don't add gates just for process)
- ❌ Don't make gates so strict nothing passes

**Quality Gate Template**:
```markdown
**Quality Gate N**: [Gate purpose]
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

If ALL pass: Proceed to Phase N+1
If ANY fail: [What to do - stop/revise/get approval]
```

---

### 3. Parallel-Then-Merge Pattern (A + B → Synthesize)

**Description**: Execute multiple independent analyses in parallel, then synthesize results.

**When to Use**:
- Multiple perspectives needed
- Independent analyses can run simultaneously
- Synthesis benefits from diverse inputs
- Time is constrained (parallel is faster)

**Structure**:
```
      ┌─ Phase 1A: [Analysis from perspective A]
      │   → Output A
Start ┼─ Phase 1B: [Analysis from perspective B]
      │   → Output B
      └─ Phase 1C: [Analysis from perspective C]
          → Output C

Phase 2: Synthesis (combines Outputs A, B, C)
→ Final integrated result
```

**Real Example**: Code Review Workflow
```
Parallel Analysis:
├─ Code Structure (analyze-agent)
├─ Documentation Check (docs-agent)
├─ Quality Metrics (analyze-agent + implementation-guardrails)
├─ Security Review (analyze-agent)
└─ Test Coverage (analyze-agent)

Synthesis: Combine all findings into comprehensive review report
```

**Best Practices**:
- ✅ Ensure phases are truly independent (no hidden dependencies)
- ✅ Synthesis phase addresses conflicts/contradictions
- ✅ Document how to prioritize if analyses conflict
- ❌ Don't parallelize if one depends on another's output

---

### 4. Iterative Refinement Pattern (A → Verify → Loop if needed)

**Description**: Perform work, check quality, refine if needed, repeat until satisfactory.

**When to Use**:
- Initial attempt unlikely to be perfect
- Incremental improvement safer than big bang
- Quality standard is high
- Feedback loop improves outcome

**Structure**:
```
Phase 1: [Create initial version]
→ Draft

Phase 2: [Verify quality]
→ Quality assessment

Decision:
├─ Quality sufficient: DONE
└─ Quality insufficient: Refine and repeat Phase 2
   (Loop maximum 3 times, then escalate)
```

**Real Example**: Email Composition
```
1. Draft email
2. Clarity check
   ├─ Clear? → Proceed to proofread
   └─ Unclear? → Revise draft, check again

3. Proofread
   ├─ Error-free? → Send
   └─ Errors found? → Fix errors, proofread again
```

**Best Practices**:
- ✅ Set maximum iterations (prevent infinite loops)
- ✅ Track what improved each iteration
- ✅ Define "good enough" criteria (perfection trap)
- ✅ Learn from iterations (why did it need refinement?)
- ❌ Don't iterate without changing approach (if 3 attempts fail, change strategy)

---

### 5. Workflow Composition Pattern (/workflow1 calls /workflow2)

**Description**: One workflow invokes another workflow as a sub-process.

**When to Use**:
- Reuse existing workflows
- Complex workflow has distinct sub-processes
- Want to maintain modularity
- Sub-workflow useful independently

**Structure**:
```
Main Workflow:
  Phase 1: [Preparation]
  Phase 2: [Use /sub-workflow to accomplish X]
  Phase 3: [Continue with sub-workflow output]
```

**Real Example**: Feature Development → Code Review
```
Feature Development Workflow:
  ...
  Phase 6: Code Review
    → Invoke /code-review workflow
    → Use code review output to verify quality gate
  Phase 7: Documentation
  ...
```

**Best Practices**:
- ✅ Sub-workflow should be independently useful
- ✅ Clear interface (what inputs needed, what outputs produced)
- ✅ Document the composition relationship
- ❌ Don't nest too deeply (max 2-3 levels)
- ❌ Don't duplicate workflow logic (extract to shared workflow instead)

**Invocation Examples**:
```markdown
### Phase N: [Task requiring sub-workflow]

**Use /sub-workflow-name** to accomplish [specific goal]:

[Provide context/inputs needed for sub-workflow]

[Describe how to use sub-workflow output in next phase]
```

---

### 6. Multi-Agent Collaboration Pattern

**Description**: Multiple agents work together on different aspects of a task.

**When to Use**:
- Task requires diverse expertise
- Different agents excel at different phases
- Want independent context windows for each aspect
- Benefit from specialized agents

**Structure**:
```
Phase 1: Use analyze-agent for [high-level analysis]
Phase 2: Use docs-agent for [policy/compliance check]
Phase 3: Use translate-agent for [localization]
Phase 4: Use proofread-agent for [final polish]
```

**Real Example**: Proposal Creation
```
Phase 1: Opportunity Analysis (analyze-agent)
  → Understand requirements, stakeholders, win themes

Phase 2: Solution Design (analyze-agent + analysis skill)
  → Tailor solution, quantify value proposition

Phase 3: Compliance Check (docs-agent)
  → Verify against RFP requirements

Phase 4: Polish & Proofread (proofread-agent)
  → Professional, error-free final draft
```

**Agent Selection Guide**:
- **analyze-agent**: For research, analysis, decisions, synthesis
- **docs-agent**: For policy compliance, requirement verification
- **translate-agent**: For multi-lingual content, localization
- **proofread-agent**: For grammar, clarity, style consistency

**Best Practices**:
- ✅ Use right agent for each task (play to strengths)
- ✅ Pass context clearly between agents
- ✅ Document agent hand-offs
- ❌ Don't use multiple agents for same task (redundant)
- ❌ Don't force agent use (if task is simple, just do it directly)

---

### 7. Conditional Branching Pattern

**Description**: Workflow path changes based on conditions or analysis results.

**When to Use**:
- Different paths for different scenarios
- Decision point determines next steps
- One size doesn't fit all
- Want to handle variations systematically

**Structure**:
```
Phase 1: [Analyze situation]
→ Classification

Branch based on classification:
├─ Scenario A: [Do workflow A]
├─ Scenario B: [Do workflow B]
└─ Scenario C: [Do workflow C]
```

**Real Example**: Email Response Workflow
```
Phase 1: Context Analysis
→ Email type determined

Branch:
├─ Request for info → Quick response pattern
├─ Complaint/issue → Problem resolution pattern
├─ Relationship building → Warm, personal pattern
└─ Complex negotiation → Careful, diplomatic pattern
```

**Best Practices**:
- ✅ Exhaustive branches (cover all possibilities)
- ✅ Clear classification criteria (no ambiguity)
- ✅ Document why branches exist (what's different)
- ❌ Don't over-branch (combine similar paths)

---

## Advanced Composition Techniques

### Technique 1: Error Handling

**Add error recovery to workflows**:

```markdown
Phase N: [Attempt operation]

If successful:
  → Continue to Phase N+1

If failed:
  → Fallback: [Alternative approach]
  → Escalation: [When to involve human]
  → Recovery: [How to resume after fix]
```

**Example**:
```
Phase 3: Draft Creation

If writer's block or insufficient research:
  → Fallback: Return to Phase 2 (Research) for more material
  → Escalation: If after 2 attempts still stuck, consult subject matter expert
```

---

### Technique 2: Parallel with Dependencies

**Some phases parallel, some sequential**:

```
Phase 1: [Foundation work]
↓
┌─ Phase 2A: [Independent work A] ─┐
├─ Phase 2B: [Independent work B] ─┤→ Phase 3: [Synthesis]
└─ Phase 2C: [Independent work C] ─┘
```

**Example**: Research & Synthesis
```
Phase 1: Question Clarification
↓
┌─ Research academic sources ────┐
├─ Research industry reports ────┤→ Synthesis
└─ Research internal documents ──┘
```

---

### Technique 3: Confidence-Based Routing

**Route based on confidence level**:

```
Phase 1: Analysis
→ Confidence score: 0.0-1.0

Route based on confidence:
├─ ≥ 0.9: Proceed with plan
├─ 0.7-0.89: Get second opinion (involve analyze-agent)
├─ 0.5-0.69: Gather more data (invoke research-synthesis)
└─ < 0.5: Escalate to human expert
```

**Example**: Implementation Guardrails
```
5-Check Validation → Confidence Score

Score ≥ 0.9: HIGH confidence → Implement
Score 0.7-0.89: MEDIUM confidence → Clarify gaps first
Score < 0.7: LOW confidence → Stop and re-analyze
```

---

## Workflow Composition Examples

### Example 1: Content Marketing Campaign

**Goal**: Create, translate, and publish blog post in 3 languages

**Composition**:
```
1. /content-creation (English) → Original blog post
2. For each language (Spanish, French):
   a. /translate-workflow → Translated version
   b. /proofread (in target language) → Polished version
3. /competitive-analysis → Similar content from competitors
4. Synthesis: SEO optimization based on competitive analysis
```

**Patterns Used**:
- Sequential (content creation phases)
- Parallel (translations)
- Workflow composition (/content-creation, /translate)
- Multi-agent (analyze, translate, proofread)

---

### Example 2: Business Proposal Response

**Goal**: Respond to RFP with winning proposal

**Composition**:
```
1. /research-synthesis (about client, market, competitors)
2. /competitive-analysis (what competitors will propose)
3. /proposal-pitch workflow:
   Phase 2 enhancement: Use research from step 1
   Phase 3 enhancement: Use competitive insights from step 2
4. docs-agent: Verify RFP compliance
5. proofread-agent: Final polish
```

**Patterns Used**:
- Sequential (overall flow)
- Workflow composition (research → competitive → proposal)
- Multi-agent collaboration
- Validation-gated (compliance check)

---

### Example 3: Executive Email Response

**Goal**: Respond to sensitive email from CEO

**Composition**:
```
1. analyze-agent: Understand context, stakeholders, politics
2. /professional-email workflow:
   - Tone: Diplomatic (sensitive topic)
   - Review: Extra emphasis on clarity
3. Iterative refinement:
   - Draft → Review → Refine (repeat 2-3 times)
4. proofread-agent: Ensure zero errors
5. Optional: Get peer review before sending
```

**Patterns Used**:
- Sequential (analysis → composition → review)
- Iterative refinement (multiple review cycles)
- Validation-gated (peer review)

---

## Pattern Selection Decision Tree

**Use this to choose the right pattern**:

```
Q: Do steps depend on each other?
├─ YES → Sequential Pattern
└─ NO → Can they run in parallel?
    ├─ YES → Parallel-Then-Merge Pattern
    └─ NO (but independent) → Separate workflows

Q: Is quality critical and errors costly?
└─ YES → Add Validation Gates

Q: Is first attempt unlikely to be perfect?
└─ YES → Use Iterative Refinement

Q: Do different scenarios need different approaches?
└─ YES → Conditional Branching

Q: Can you reuse an existing workflow?
└─ YES → Workflow Composition (call sub-workflow)

Q: Does task need diverse expertise?
└─ YES → Multi-Agent Collaboration
```

---

## Best Practices Summary

### DO:
✅ **Use simplest pattern that works** - Don't over-engineer
✅ **Document why you chose a pattern** - Helps future maintainers
✅ **Make dependencies explicit** - Clear what depends on what
✅ **Add quality gates at risk points** - Prevent costly errors
✅ **Reuse existing workflows** - Don't reinvent the wheel
✅ **Test compositions** - Ensure handoffs work smoothly

### DON'T:
❌ **Create unnecessary dependencies** - Parallel is faster than sequential
❌ **Over-complicate simple tasks** - Not everything needs a workflow
❌ **Nest workflows too deeply** - Max 2-3 levels
❌ **Ignore error cases** - Plan for failure modes
❌ **Skip quality gates** - They exist for a reason
❌ **Mix patterns unnecessarily** - Keep it as simple as possible

---

## Creating Your Own Workflow Patterns

**When to create a new pattern**:
1. Repeated use case (not one-off)
2. Clear structure that could be templated
3. Benefits from consistency
4. Others could use it

**How to document a pattern**:
1. **Name**: Descriptive name (e.g., "Research-Then-Write Pattern")
2. **Intent**: What problem does it solve?
3. **Structure**: Visual/textual representation
4. **When to Use**: Applicability criteria
5. **Example**: Real-world usage
6. **Best Practices**: Do's and don'ts

---

## Pattern Anti-Patterns (What NOT to Do)

### Anti-Pattern 1: "Workflow Soup"
**Problem**: Too many small workflows, unclear which to use
**Solution**: Consolidate related workflows, clear naming, decision tree

### Anti-Pattern 2: "Linear Everything"
**Problem**: Making everything sequential when could be parallel
**Solution**: Identify truly independent steps, parallelize

### Anti-Pattern 3: "No Gates"
**Problem**: Proceeding even when quality is poor
**Solution**: Add validation gates at key decision points

### Anti-Pattern 4: "Reinventing the Wheel"
**Problem**: Creating new workflows when existing ones work
**Solution**: Check existing workflows first, compose/adapt if possible

### Anti-Pattern 5: "Analysis Paralysis"
**Problem**: Too many validation gates, nothing gets done
**Solution**: Gates only at critical points, make criteria reasonable

---

## Workflow Metrics

**Track these to improve workflows**:

1. **Time Savings**: Before/after workflow adoption
2. **Quality Improvement**: Defect rates, revision cycles
3. **Adoption Rate**: How often workflow is used vs. should be used
4. **Success Rate**: % of times workflow achieves desired outcome
5. **User Satisfaction**: Feedback from workflow users

**Example Metrics**:
- Content Creation: 4 hours → 45 minutes (6.7x faster)
- Professional Email: 30 minutes → 5 minutes (6x faster)
- Research: 8 hours → 2 hours (4x faster)
- Proposal: 8 hours → 3 hours (2.7x faster)

---

## Next Steps

1. **Study existing workflows** to see patterns in action
2. **Try composing workflows** for your specific use cases
3. **Document patterns you discover** - share with team
4. **Iterate and improve** - workflows evolve based on usage

**Remember**: Patterns are tools, not rules. Use what works, adapt what doesn't, create new patterns when needed.
