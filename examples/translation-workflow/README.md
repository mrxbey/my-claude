# Example: Translation Workflow with Glossary Management

## Overview

This example demonstrates using the **translate-agent** for professional translation with glossary management, cultural adaptation, and quality control. It showcases enterprise-grade localization capabilities essential for global product launches.

**Key Features Demonstrated:**
- ✅ High-quality translation (English → Spanish)
- ✅ Glossary management with 30+ technical terms
- ✅ Cultural adaptation (idioms, metaphors, formality)
- ✅ Tone and register control (formal business)
- ✅ Translation decision documentation
- ✅ Quality metrics (expansion rate, readability)

---

## Scenario

**Company**: CloudTech Inc.
**Challenge**: Launch CloudSync Pro product in Latin American markets
**Content**: Product announcement with pricing, features, testimonials (847 words)
**Target**: Professional Spanish translation for business audience

**Question**: *How do we translate our product launch while maintaining brand voice and technical accuracy?*

---

## Files in This Example

### Input Files

**1. `source-english.md`** - Original Content
- CloudSync Pro product launch announcement
- Features, pricing, testimonials, FAQ
- 847 words, business-professional tone
- Mix of marketing copy and technical specs

**2. `glossary.json`** - Translation Glossary
- 30+ technical terms with approved translations
- Style guide (formality, tone, formatting)
- Regional considerations (LatAm vs Spain)
- Cultural adaptation notes

### Output Files

**3. `target-spanish.md`** - Spanish Translation
- Professional Latin American Spanish
- 912 words (+7.7% expansion, within normal range)
- Maintains brand voice and technical accuracy
- Formal "usted" register throughout

**4. `translation-notes.md`** - Decision Log
- Key translation decisions explained
- Cultural adaptations documented
- Alternative translations considered
- Quality metrics and validation

---

## How to Run This Example

### Method 1: Using the /translate Command

```bash
cd my-claude

# Start Claude Code
claude

# Run translation
> /translate examples/translation-workflow/source-english.md
  from English to Spanish, use the glossary in examples/translation-workflow/glossary.json
```

### Method 2: Natural Language Request

```bash
claude

> Translate the CloudSync Pro announcement in examples/translation-workflow/
  to Latin American Spanish. Use formal business tone and maintain technical accuracy.
```

The **translate-agent** automatically triggers on keywords like "translate", "translation", "Spanish", "localize".

### Method 3: With Specific Instructions

```bash
claude

> Translate examples/translation-workflow/source-english.md to Spanish.
  Use formal register (usted), prioritize Latin American vocabulary,
  keep brand names unchanged, document key decisions.
```

---

## What Happens (Behind the Scenes)

### Phase 1: Context Understanding (1-2 seconds)
```
📋 Analyzing translation request...
   Source: English (US)
   Target: Spanish (Latin America)
   Content type: Product marketing + technical specs
   Tone: Business professional
   Word count: 847 words
```

### Phase 2: Glossary Loading (0.5 seconds)
```
📚 Loading glossary...
   Found: glossary.json (30 terms)
   Applying style guide:
   - Formality: Business (usted form)
   - Vocabulary: Latin American Spanish
   - Technical terms: Translate when natural, keep English when standard
```

### Phase 3: Translation (10-15 seconds)
```
🌐 Translating content...
   Processing sections:
   ✅ Headline and intro
   ✅ Feature descriptions
   ✅ Pricing tiers
   ✅ Customer testimonials
   ✅ Technical specs
   ✅ FAQ section
   ✅ Contact information
```

### Phase 4: Quality Control (3-5 seconds)
```
✔️ Validating translation...
   ✅ Glossary consistency: 30/30 terms
   ✅ Tone consistency: Formal throughout
   ✅ Cultural adaptation: 5 idioms adapted
   ✅ Text expansion: +7.7% (acceptable)
   ✅ No untranslated content
```

### Phase 5: Documentation (2-3 seconds)
```
📝 Generating translation notes...
   Key decisions documented: 5
   Alternatives considered: 8
   Cultural adaptations: 3
   Quality metrics calculated
```

**Total Time**: ~20-25 seconds for complete translation + documentation

---

## Expected Output Structure

### 1. Translated Content

**Professional Spanish**:
```markdown
# Presentamos CloudSync Pro: Colaboración en Tiempo Real para Equipos

Nos complace anunciar **CloudSync Pro**, nuestra plataforma de colaboración...
```

**Key characteristics**:
- Natural phrasing (not word-for-word)
- Consistent terminology
- Appropriate formality
- Cultural relevance

### 2. Glossary with Decisions

```json
{
  "english": "game-changing",
  "spanish": "revolucionaria",
  "notes": "Sports metaphor adapted. 'Revolucionaria' better captures impact.",
  "alternatives": ["transformadora"],
  "approved": true
}
```

### 3. Translation Notes

```markdown
### "Enterprise Plan" → "Plan Enterprise"

**Decision**: Keep "Enterprise" in English
**Rationale**: Industry standard, globally recognized
**Alternative**: "Plan Corporativo" (rejected, less familiar)
```

### 4. Quality Metrics

```markdown
**Text Expansion**: +7.7% (847 → 912 words)
**Reading Level**: Secondary education (appropriate for B2B)
**Glossary Application**: 30/30 terms consistent
**Tone**: Formal business (usted) throughout
```

---

## Key Features Demonstrated

### ✅ Intelligent Glossary Management

The translate-agent:
- Loads and applies glossary terms consistently
- Tracks all 30+ technical terms throughout
- Documents when terms appear and how they're used
- Suggests additions to glossary for new terms

**Example**:
```
"notification fatigue" → "fatiga de notificaciones"
Applied consistently in: Feature description, comparison table
```

### ✅ Cultural Adaptation

Not just word-for-word translation:

**Idioms**:
- "game-changing" → "revolucionaria" (not literal "cambia el juego")
- "peace of mind" → "tranquilidad" (not literal "paz mental")

**Formality**:
- All CTAs use formal "usted": "Regístrese", "Invite a su equipo"
- Maintains professional distance appropriate for B2B

**Regional Choices**:
- "encriptación" (LatAm) not "cifrado" (Spain)
- "correo electrónico" (standard) not "email" (anglicism)
- "ustedes" (universal) not "vosotros" (Spain-specific)

### ✅ Tone and Register Control

**Consistent formality**:
```
English: "Start your free trial"
Spanish: "Comience su prueba gratuita" (formal usted)
NOT: "Comienza tu prueba" (informal tú)
```

**Brand voice maintained**:
- Enthusiasm preserved: "¡Por supuesto!" (Absolutely!)
- Professional: "Nos complace anunciar" (We're pleased to announce)
- Action-oriented: "¿Listo para transformar...?" (Ready to transform...?)

### ✅ Technical Accuracy

**Preserves**:
- Numbers: 100 GB, 1 TB, 99.9% (with Spanish formatting rules)
- Acronyms: API, SLA, RGPD (GDPR), SOC 2
- Brand names: CloudSync Pro, CloudTech Inc.
- URLs: cloudsyncpro.com (unchanged)

**Translates appropriately**:
- "API endpoints" → "puntos finales de API" (technical accuracy)
- "bank-level encryption" → "encriptación de nivel bancario" (metaphor preserved)

### ✅ Alternative Translations

For ambiguous or nuanced terms, provides alternatives:

```markdown
**"seamlessly"**:
1. sin problemas (without problems) - ✅ CHOSEN
2. perfectamente (perfectly) - too absolute
3. fluidamente (fluidly) - too technical

**Rationale**: "sin problemas" is conversational and business-appropriate
```

---

## Learning Points

### 1. Trigger Keywords for translate-agent

Words that automatically invoke translate-agent:
- **Languages**: "Spanish", "French", "German", "Japanese", "Chinese"
- **Actions**: "translate", "translation", "localize", "localization"
- **Concepts**: "multilingual", "language", "adapt", "cultural"

### 2. Skill Auto-Loading

The translate-agent uses the **translation skill**, which provides:
- 6-step translation workflow
- Glossary management patterns
- Cultural adaptation frameworks (Romance, Germanic, Asian, RTL)
- Tone and formality control
- Quality validation checkpoints

### 3. Progressive Context Loading

**Startup** (Level 1):
- translate-agent metadata: ~69 tokens
- translation skill metadata: ~56 tokens
- Total: ~125 tokens

**Active** (Level 2):
- translate-agent prompt: ~3,444 tokens
- translation skill instructions: ~3,429 tokens
- Total active: ~6,873 tokens

**With Glossary**:
- Plus glossary.json: ~600 tokens
- Grand total: ~7,473 tokens (still efficient)

### 4. Text Expansion is Normal

Spanish text is typically 10-15% longer than English:
- More prepositions needed ("de", "a", "con")
- Formal conjugations longer ("usted" vs "you")
- Compound terms spelled out

**This example**: +7.7% (lower due to technical cognates)

### 5. Professional Translation Quality

Enterprise translation requires:
1. **Accuracy**: Correct meaning
2. **Fluency**: Natural phrasing
3. **Consistency**: Same terms throughout
4. **Style**: Appropriate formality
5. **Cultural fit**: Resonates with audience

The translate-agent addresses all five.

---

## Try It Yourself

### Experiment 1: Change Target Formality

Edit `glossary.json` to specify informal tone:

```json
{
  "style_guide": {
    "formality": "Casual - use 'tú' form",
    ...
  }
}
```

Re-run translation. All CTAs will change:
- "Regístrese" → "Regístrate" (Sign up)
- "Comience" → "Comienza" (Start)
- "Explore" → "Explora" (Explore)

### Experiment 2: Add New Glossary Terms

Add a term to `glossary.json`:

```json
{
  "english": "dashboard",
  "spanish": "panel de control",
  "notes": "Prefer 'panel de control' over 'tablero'"
}
```

Re-run and verify consistency.

### Experiment 3: Different Target Language

```bash
claude

> Translate examples/translation-workflow/source-english.md to French,
  formal business tone
```

Agent will adapt workflow for French:
- Different formality markers (vous vs tu)
- French-specific idioms
- Appropriate text expansion (~15-20%)

### Experiment 4: Add Cultural Notes

Update `glossary.json` with region-specific terms:

```json
{
  "regional_considerations": {
    "target": "Spain (European Spanish)",
    "vocabulary": "Use European terms: cifrado, ordenador",
    "pronouns": "Use vosotros instead of ustedes"
  }
}
```

Translation will adapt for Spanish market.

---

## Comparison: Manual vs Automated Translation

### Manual Professional Translation

**Time**: 3-4 hours for 847 words
**Process**:
1. Initial translation (2 hours)
2. Glossary consultation (30 min)
3. Quality review (30 min)
4. Formatting (30 min)
5. Documentation (30 min)

**Cost**: $0.10-0.20/word = $85-170
**Consistency**: Depends on translator memory
**Turnaround**: 1-2 business days

### Automated Translation with translate-agent

**Time**: 20-25 seconds (translation + documentation)
**Process**:
1. Glossary auto-loaded
2. Translation with consistency checks
3. Quality validation
4. Documentation generated

**Cost**: Essentially free (after framework setup)
**Consistency**: 100% (glossary-enforced)
**Turnaround**: Real-time

**ROI**: 500x faster, perfect consistency, instant turnaround

**Note**: Human review still recommended for:
- Legal content
- Marketing launch materials
- First translation in a new language
- Content with cultural nuance

---

## Real-World Applications

This pattern works for:

### Marketing Content
- Product launches
- Blog posts
- Social media campaigns
- Email newsletters
- Press releases

### Technical Documentation
- API documentation
- User guides
- Release notes
- Knowledge base articles
- Support FAQs

### Business Documents
- Contracts (with legal review)
- Proposals
- Presentations
- White papers
- Case studies

### Localization Projects
- Website content
- Mobile app strings
- Software UI
- Video subtitles
- Training materials

---

## Best Practices from This Example

### 1. Build Comprehensive Glossaries

Include:
- ✅ Approved translations
- ✅ Context and usage notes
- ✅ Alternatives considered
- ✅ Why chosen over alternatives

### 2. Document Decisions

For key terms, explain:
- Why this translation?
- What alternatives existed?
- What's the cultural consideration?
- When to deviate from glossary?

### 3. Specify Target Audience

Be explicit about:
- Geographic region (LatAm vs Spain)
- Formality level (tú vs usted)
- Industry/domain (technical vs consumer)
- Context (marketing vs legal)

### 4. Quality Check Systematically

Always verify:
- Glossary consistency
- Tone consistency
- Cultural appropriateness
- Technical accuracy
- No untranslated segments

### 5. Plan for Review

Even with AI translation:
- In-country native speaker review
- Subject matter expert review (technical accuracy)
- Legal review (compliance terms)
- Marketing review (brand voice)

---

## Quality Metrics Explained

### Text Expansion Rate

**Normal ranges**:
- Spanish: +10-15%
- French: +15-20%
- German: +10-35%
- Japanese: -10-55% (more compact)

**This example**: +7.7%
- Lower than typical due to technical terms (many cognates)
- "API", "GB", "TB" unchanged
- Still within acceptable range

### Reading Level

**Flesch Reading Ease** (adapted for Spanish):
- 30-49: Difficult (university level)
- 50-59: Fairly difficult (high school / early university)
- 60-69: Standard (general education)
- 70-79: Fairly easy (middle school)

**This translation**: 58/100
- Appropriate for business professionals
- Technical enough to be credible
- Accessible to decision-makers

### Glossary Application Rate

**This example**: 30/30 terms (100%)

- Every glossary term applied consistently
- No deviations without documentation
- Alternatives noted when considered

---

## Related Examples

- [Document Review](../document-review/) - Using docs-agent for compliance checking
- [Simple Analysis](../simple-analysis/) - Using analyze-agent for decision analysis
- [Custom Agent](../custom-agent/) - Creating specialized agents

---

## Next Steps

### Explore the Framework
1. Try `/translate` with your own content
2. Read the [translate-agent documentation](../../.claude/agents/translate-agent.md)
3. Learn about the [translation skill](../../.claude/skills/translation/SKILL.md)

### Customize for Your Needs
1. Build glossaries for your products/services
2. Define brand-specific style guides
3. Add company terminology
4. Create language-pair specific rules

### Advanced Usage
1. Batch translate multiple files
2. Update translations when source changes
3. A/B test different translation approaches
4. Integrate with your CMS/localization platform

---

## Questions?

**Q: Can this handle technical documentation?**
A: Yes! The glossary system ensures technical term consistency. Add your domain-specific terms.

**Q: What about right-to-left languages (Arabic, Hebrew)?**
A: The translation skill includes RTL-specific guidance for formatting and cultural adaptation.

**Q: How do I handle regional variants (LatAm vs Spain)?**
A: Specify in glossary `regional_considerations`. Agent adapts vocabulary and grammar accordingly.

**Q: Can I translate code comments and docstrings?**
A: Yes, but keep code/variables unchanged. Agent recognizes code blocks and preserves syntax.

**Q: Is this good enough for production?**
A: For internal docs and drafts: yes. For public-facing marketing/legal: recommend human review.

---

**Example Complete!** 🎉

This demonstrates enterprise-grade translation with glossary management, cultural adaptation, and quality control. The translate-agent handles the heavy lifting while maintaining linguistic quality and brand consistency.
