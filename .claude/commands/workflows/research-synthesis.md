---
description: Deep research and synthesis workflow for evidence-based conclusions
argument-hint: <research-topic>
---

Conduct comprehensive research and synthesis on any topic with evidence-based conclusions.

## Task

Research topic: $ARGUMENTS

## Multi-Phase Research Workflow

This workflow systematically researches a topic, synthesizes findings, and produces evidence-based conclusions suitable for business decisions, academic work, or strategic planning.

### Phase 1: Question Clarification (analyze-agent)

**Use analyze-agent** to clarify and scope the research:

1. **Restate Research Question**:
   - Paraphrase the research topic in your own words
   - Identify the core question being asked
   - Define what a good answer looks like

2. **Break Into Sub-Questions**:
   - Decompose into 3-5 specific sub-questions
   - Prioritize by importance
   - Identify dependencies between questions

3. **Define Scope**:
   - What's IN scope (must research)
   - What's OUT of scope (explicitly exclude)
   - Time period (historical, current, future)
   - Geographic scope (global, regional, local)

4. **Identify Success Criteria**:
   - What level of evidence is needed?
   - What confidence level is required?
   - What format should the output take?

**Deliverable**: Research brief with clear question, sub-questions, scope, success criteria

**Quality Gate 1**: Research question well-defined?
- [ ] Question is specific and answerable
- [ ] Sub-questions identified
- [ ] Scope clearly bounded
- [ ] Success criteria defined

---

### Phase 2: Source Discovery

**Find relevant sources**:

1. **Identify Source Types**:
   - Internal: Documents, data, previous research, expert knowledge
   - External: Published research, industry reports, news, data sources
   - Primary: Original research, data, documents
   - Secondary: Analysis, commentary, summaries

2. **Search Strategy**:
   - Use Glob to find relevant internal documents
   - Use Grep to search for keywords across files
   - Identify external sources to consult
   - List expert sources (people to interview, if applicable)

3. **Source Evaluation**:
   - Credibility (who created it? what's their expertise?)
   - Recency (when was it published? still relevant?)
   - Relevance (does it address our question?)
   - Quality (peer-reviewed? well-researched?)

4. **Create Source List**:
   - Primary sources (highest credibility)
   - Secondary sources (supporting evidence)
   - Tertiary sources (background context)

**Deliverable**: Annotated source list with credibility ratings

**Quality Gate 2**: Sources adequate?
- [ ] At least 5-10 relevant sources identified
- [ ] Mix of source types (primary, secondary)
- [ ] Source credibility assessed
- [ ] Gaps in sources identified

---

### Phase 3: Information Extraction

**Extract key information from sources**:

1. **Read and Extract**:
   - Read each source systematically
   - Extract key facts, claims, data points
   - Note supporting evidence for each claim
   - Identify contradictions or disagreements

2. **Organize by Sub-Question**:
   - Map extracted information to sub-questions
   - Identify which sources address which questions
   - Note information gaps

3. **Evidence Quality Assessment**:
   - Strong evidence (multiple independent sources, data-backed)
   - Moderate evidence (single credible source, logical argument)
   - Weak evidence (opinion, speculation, single anecdotal source)

4. **Create Evidence Table**:

| Sub-Question | Finding | Evidence | Source | Quality |
|--------------|---------|----------|--------|---------|
| Q1: [question] | [claim] | [data/quote] | [source] | Strong |

**Deliverable**: Evidence table with organized findings

**Quality Gate 3**: Sufficient evidence gathered?
- [ ] All sub-questions have some evidence
- [ ] Mix of evidence quality levels
- [ ] Contradictions identified
- [ ] Gaps documented

---

### Phase 4: Synthesis & Analysis (analyze-agent)

**Use analyze-agent** to synthesize findings:

1. **Pattern Identification**:
   - What themes emerge across sources?
   - What patterns in the data?
   - What relationships between findings?
   - What trends over time?

2. **Contradiction Resolution**:
   - Where do sources disagree?
   - Why might they disagree? (methodology, data, bias, timing)
   - Which perspective is more credible?
   - Can contradictions be reconciled?

3. **Gap Analysis**:
   - What questions remain unanswered?
   - What evidence is missing?
   - What assumptions are we making?
   - What further research is needed?

4. **Insight Generation**:
   - What are the key insights?
   - What's surprising or unexpected?
   - What are the implications?
   - What does this mean for the original question?

5. **Confidence Assessment**:
   - How confident are we in each finding? (High/Medium/Low)
   - What would increase confidence?
   - What are the risks of being wrong?

**Deliverable**: Synthesis document with patterns, insights, confidence levels

**Quality Gate 4**: Synthesis coherent?
- [ ] Clear patterns identified
- [ ] Contradictions addressed
- [ ] Gaps acknowledged
- [ ] Confidence levels assigned
- [ ] Insights actionable

---

### Phase 5: Evidence Validation

**Validate credibility and accuracy**:

1. **Source Cross-Checking**:
   - Do multiple independent sources agree?
   - Are claims backed by data?
   - Can facts be verified?

2. **Bias Detection**:
   - What biases might sources have? (financial, political, ideological)
   - Are counterarguments considered?
   - Is contrary evidence acknowledged?

3. **Logical Consistency**:
   - Do conclusions follow from evidence?
   - Are there logical fallacies?
   - Are assumptions reasonable?

4. **Recency Check**:
   - Is information current?
   - Have there been significant changes since publication?
   - Is more recent data available?

5. **Credibility Rating**:
   - Rate overall research credibility (1-10)
   - Identify strongest findings
   - Identify weakest findings
   - Note areas needing more research

**Deliverable**: Validation report with credibility assessment

**Quality Gate 5**: Evidence validated?
- [ ] Key claims cross-checked
- [ ] Biases identified and noted
- [ ] Logic verified
- [ ] Recency confirmed
- [ ] Credibility rated

---

### Phase 6: Report Generation

**Create comprehensive research report**:

1. **Structure the Report**:
   - Executive Summary (1 page)
   - Research Question & Methodology
   - Key Findings (organized by sub-question)
   - Analysis & Insights
   - Conclusions & Recommendations
   - Limitations & Further Research
   - Bibliography/Sources

2. **Write Each Section**:
   - Executive Summary: Key findings, conclusions, recommendations (for decision-makers)
   - Methodology: How research was conducted, sources used, limitations
   - Findings: Evidence-based answers to each sub-question
   - Analysis: Patterns, insights, implications
   - Conclusions: Answer to original question, confidence level
   - Recommendations: Actionable next steps based on findings
   - Sources: Full citation list with credibility notes

3. **Add Evidence References**:
   - Every claim must cite source
   - Format: [Finding] (Source, Date) - "Quote or data"
   - Use file:line references for internal documents

4. **Quality Check**:
   - Is it well-structured and readable?
   - Are all findings evidence-based?
   - Are sources properly cited?
   - Are limitations acknowledged?
   - Are recommendations actionable?

**Deliverable**: Comprehensive research report

**Quality Gate 6**: Report complete and professional?
- [ ] All sections present
- [ ] Executive summary clear
- [ ] All findings cited
- [ ] Recommendations actionable
- [ ] Limitations acknowledged
- [ ] Professional presentation

---

## Output Format

### Research Report Structure

```markdown
# Research Report: [Topic]

**Prepared**: [Date]
**Researcher**: [Name/Team]
**Research Question**: [Original question]
**Confidence Level**: [High/Medium/Low]

---

## Executive Summary

**Bottom Line**: [One sentence answer to research question]

**Key Findings**:
1. [Finding 1] - Confidence: High
2. [Finding 2] - Confidence: Medium
3. [Finding 3] - Confidence: High

**Recommendations**:
1. [Action 1] - Why: [Rationale]
2. [Action 2] - Why: [Rationale]

**Limitations**: [Key caveats and what's unknown]

---

## Research Question & Methodology

**Primary Question**: [Question]

**Sub-Questions**:
1. [Sub-question 1]
2. [Sub-question 2]
3. [Sub-question 3]

**Methodology**:
- Sources consulted: [Number and types]
- Time period: [Scope]
- Research approach: [How conducted]

**Scope**:
- IN scope: [What was researched]
- OUT of scope: [What was excluded]

---

## Key Findings

### Finding 1: [Sub-question 1]

**Answer**: [Evidence-based answer]

**Evidence**:
- [Claim 1] (Source A, 2024) - "Supporting quote or data"
- [Claim 2] (Source B, 2024) - "Supporting quote or data"
- [Claim 3] (Source C, 2023) - "Supporting quote or data"

**Confidence**: High/Medium/Low - [Why]

**Contradictions**: [If any, how resolved]

---

### Finding 2: [Sub-question 2]

[Same structure as Finding 1]

---

## Analysis & Insights

### Pattern: [Pattern Name]

**Observation**: [What we noticed across sources]

**Evidence**: [Sources showing this pattern]

**Implication**: [What this means]

---

### Insight: [Insight Name]

**Discovery**: [What we learned that was unexpected]

**Supporting Evidence**: [Data/sources]

**Significance**: [Why this matters]

---

## Conclusions

**Answer to Research Question**:
[Comprehensive answer based on findings]

**Confidence Level**: [High/Medium/Low]

**Reasoning**:
- [Reason 1 for confidence level]
- [Reason 2 for confidence level]

**Key Takeaways**:
1. [Takeaway 1]
2. [Takeaway 2]
3. [Takeaway 3]

---

## Recommendations

### Immediate Actions

1. **[Recommendation 1]**
   - Why: [Based on which findings]
   - Impact: [Expected outcome]
   - Effort: [High/Medium/Low]
   - Timeline: [When to do]

2. **[Recommendation 2]**
   [Same structure]

### Long-Term Considerations

1. **[Strategic recommendation]**
   - Rationale: [Why]
   - Dependencies: [What needs to happen first]

---

## Limitations & Further Research

**Limitations of This Research**:
1. [Limitation 1] - Impact: [How this affects findings]
2. [Limitation 2] - Impact: [How this affects findings]

**Unanswered Questions**:
1. [Question still needing research]
2. [Another gap]

**Recommended Further Research**:
1. [What to research next] - Why: [Reason]
2. [Another research direction] - Why: [Reason]

---

## Sources

### Primary Sources (High Credibility)
1. [Source 1] - [Author, Date] - [URL or location]
   - Used for: [Which findings]
   - Credibility: [Why trustworthy]

2. [Source 2] - [Details]

### Secondary Sources (Moderate Credibility)
1. [Source] - [Details]

### Tertiary Sources (Background Only)
1. [Source] - [Details]

---

## Methodology Appendix

**Search Strategy**:
- Keywords used: [List]
- Databases searched: [List]
- Time frame: [Dates]

**Source Selection Criteria**:
- Credibility: [How assessed]
- Relevance: [How determined]
- Recency: [Cutoff date]

**Evidence Quality Standards**:
- Strong: [Definition]
- Moderate: [Definition]
- Weak: [Definition]
```

---

## Quality Standards

This workflow ensures:
- **Systematic**: All phases completed methodically
- **Evidence-based**: Every finding backed by credible sources
- **Transparent**: Methodology and limitations clear
- **Balanced**: Considers contradictions and alternatives
- **Actionable**: Conclusions lead to clear recommendations
- **Professional**: Suitable for business or academic use

---

## Use Cases

This workflow works for:
- **Market Research**: Understanding markets, customers, competitors
- **Due Diligence**: Evaluating companies, technologies, investments
- **Literature Review**: Academic or technical research synthesis
- **Strategic Analysis**: Industry trends, emerging technologies
- **Competitive Intelligence**: Competitor strategies and positioning
- **Policy Research**: Understanding regulations, best practices
- **Technical Research**: Technology evaluation, vendor selection
- **Historical Analysis**: Understanding past events and decisions

---

## Tips for Best Results

1. **Be Specific**: Narrow, well-defined questions get better answers than broad ones
2. **Diverse Sources**: Mix of primary/secondary, internal/external, old/new
3. **Evidence Quality**: Prioritize data over opinion, multiple sources over single
4. **Document Gaps**: Acknowledge what you don't know - builds credibility
5. **Actionable Output**: Every research report should enable a decision or action
6. **Time-Box**: Set deadlines for each phase to prevent endless research
7. **Iterate**: Use findings from Phase 3 to refine questions in Phase 1 if needed

---

**Example Topics**:
- "What are the best CRM platforms for B2B SaaS companies with <100 employees?"
- "What are the emerging trends in AI-powered customer service for 2024-2025?"
- "Should we build or buy our analytics platform? What are the trade-offs?"
- "What is the competitive landscape for [product category] in [market]?"
- "What are the best practices for remote team collaboration in software development?"
