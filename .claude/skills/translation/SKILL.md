---
name: translation
description: Translation and localization patterns including glossary management, tone adaptation, cultural reference handling, and quality validation. Use for translating content between languages, localizing for regions/cultures, adapting tone and formality, maintaining terminology consistency, or cultural adaptation. Trigger keywords - translate, translation, localize, localization, language, multilingual, convert to, adapt for, French, Spanish, German, Japanese, Chinese, cultural.
version: 1.0.0
---

# Skill: Translation & Localization

## Purpose

This skill provides systematic patterns for high-quality translation that preserves meaning while adapting appropriately to target language, culture, and audience. It ensures consistency through glossary management and appropriate tone adaptation.

## When to Use

Use this skill when:
- Translating content between languages
- Localizing for specific regions or cultures
- Adapting tone and formality for target audience
- Maintaining terminology consistency
- Converting formats while preserving meaning
- Cultural adaptation of messaging

**Trigger scenarios**: "translate to Spanish", "localize for Japan", "adapt tone for French market", "convert this to German"

## Prerequisites

- Source content and target language identified
- Audience and formality level understood
- Access to style guidelines (if any)
- Context about content purpose

## Core Translation Process

### Step 1: Context Understanding

**Goal**: Understand source, target, and translation requirements

**Actions**:
1. Identify parameters:
   - **Source language**: What language is original?
   - **Target language**: Translate to which language?
   - **Content type**: Marketing, technical, legal, casual?
   - **Audience**: Who will read this?
   - **Formality**: Formal, informal, professional, friendly?
   - **Purpose**: Inform, persuade, instruct, entertain?

2. Read and understand source:
   - Main message and intent
   - Tone and style
   - Key terminology
   - Cultural references
   - Idiomatic expressions
   - Technical terms

3. Check for guidelines:
   - Style guides (CLAUDE.md, project docs)
   - Existing glossaries
   - Brand voice requirements
   - Localization policies

**Quality Check**:
- [ ] Source and target languages clear
- [ ] Audience and formality identified
- [ ] Style guidelines reviewed
- [ ] Source content understood

### Step 2: Glossary Management

**Goal**: Ensure consistent terminology translation

**Actions**:
1. Identify key terms needing consistency:
   - Technical terms
   - Product/brand names
   - Domain-specific vocabulary
   - Frequently repeated terms

2. Check existing translations:
   - Search previous work
   - Check term bases
   - Review similar content

3. Build/update glossary:

| Source Term | Target Translation | Context | Notes |
|-------------|-------------------|---------|-------|
| authentication | autenticación (ES) | Technical | Standard term |
| login | iniciar sesión (ES) | UI | Preferred over "entrar" |
| password | contraseña (ES) | Security | Never "clave" in this context |

4. Document choices:
   - Why this translation?
   - Alternatives considered?
   - Regional variations?

**Quality Check**:
- [ ] Key terms identified
- [ ] Translations chosen
- [ ] Glossary created/updated
- [ ] Choices documented

**Example Glossary**:
```markdown
## Translation Glossary: English → Spanish (Latin America)

| English | Spanish | Context | Notes |
|---------|---------|---------|-------|
| user | usuario | General | Standard |
| account | cuenta | General | Not "perfil" |
| settings | configuración | UI | Not "ajustes" (Spain) |
| dashboard | tablero | UI | Not "panel de control" (too formal) |
| upload | cargar | Action | Not "subir" (colloquial) |
| download | descargar | Action | Standard |
| delete | eliminar | Action | Permanent; "borrar" = temporary |
```

### Step 3: Translation

**Goal**: Translate preserving meaning and intent

**Actions**:
1. Translate systematically:
   - Section by section or paragraph by paragraph
   - Meaning first, then style
   - Natural phrasing in target language
   - Maintain tone and formality

2. Apply translation principles:

   **Accuracy**: Preserve exact meaning
   - Don't add or omit information
   - Keep factual statements factual
   - Preserve nuance

   **Naturalness**: Sound native
   - Use target language idioms
   - Natural sentence structure
   - Appropriate register

   **Clarity**: Easy to understand
   - Simpler is better
   - Avoid ambiguity
   - Break complex sentences if needed

   **Appropriateness**: Fit audience
   - Match formality level
   - Culturally sensitive
   - Age/context appropriate

   **Consistency**: Use glossary
   - Same terms throughout
   - Parallel structure
   - Unified style

3. Handle special cases:

   **Idioms**: Translate meaning, not words
   ```
   EN: "It's raining cats and dogs"
   ES: "Está lloviendo a cántaros" (raining pitchers)
   FR: "Il pleut des cordes" (raining ropes)
   NOT: Literal translation (nonsense)
   ```

   **Cultural references**: Adapt or explain
   ```
   EN: "Like winning the Super Bowl"
   ES (Spain): "Como ganar la Champions" (equivalent)
   ES (LATAM): "Como ganar el Mundial" (more universal)
   OR: Explain significance if no equivalent
   ```

   **Wordplay**: Note and adapt if possible
   ```
   EN Pun: "Time flies like an arrow"
   → Often can't preserve wordplay
   → Translate meaning OR add note
   → Consider equivalent wordplay in target language
   ```

   **Formality levels**:
   ```
   Formal (business, official):
   - ES: usted, señor/señora
   - FR: vous, monsieur/madame
   - DE: Sie, Herr/Frau
   - JP: です・ます form

   Informal (casual, friendly):
   - ES: tú, names
   - FR: tu, first names
   - DE: du, first names
   - JP: だ・である form
   ```

4. Technical content:
   - Keep technical terms in English if standard (API, HTTP, database)
   - Translate explanations and context
   - Preserve code examples unchanged
   - Translate comments in code if helpful

5. Preserve formatting:
   - Headings structure
   - Bullet points and lists
   - **Bold** and *italic*
   - `code` blocks
   - [Links](url) - translate text, keep URL
   - Tables - translate content, keep structure

**Quality Check**:
- [ ] All content translated
- [ ] Meaning preserved
- [ ] Tone appropriate
- [ ] Formatting maintained
- [ ] Special cases handled
- [ ] Glossary applied

### Step 4: Cultural Adaptation

**Goal**: Adapt to target culture norms

**Actions**:
1. Adjust directness:
   - **High-context cultures** (Asian, Middle Eastern): Indirect, polite, implication
   - **Low-context cultures** (Western): Direct, explicit, clear

   ```
   EN (direct): "This feature is missing"
   JP (indirect): "It would be beneficial if this feature were available"
   ```

2. Handle hierarchical language:
   - Japanese: Complex honorific system (keigo)
   - Korean: 7 levels of politeness
   - German: Sie vs. du distinction
   - Spanish: usted vs. tú/vos

3. Gender and inclusivity:
   - Languages with gendered nouns (Romance, Germanic)
   - Gender-neutral options where available
   - Inclusive language preferences

   ```
   ES: "usuarios" (masculine plural, but understood as all users)
   ES Alt: "usuarios y usuarias" (explicitly inclusive)
   DE: "Nutzer*innen" (gender-inclusive notation)
   ```

4. Number and date formats:
   ```
   Dates:
   - US: MM/DD/YYYY (11/18/2024)
   - Europe: DD/MM/YYYY (18/11/2024)
   - ISO: YYYY-MM-DD (2024-11-18)

   Numbers:
   - US/UK: 1,234.56
   - Europe: 1.234,56 or 1 234,56

   Currency:
   - Position varies: $100, 100€, £100
   ```

5. Measurement units:
   ```
   US: feet, pounds, Fahrenheit
   Metric: meters, kilograms, Celsius
   → Convert or keep with explanation
   ```

**Quality Check**:
- [ ] Directness level appropriate
- [ ] Formality matches culture
- [ ] Gender treatment appropriate
- [ ] Formats localized

### Step 5: Quality Assurance

**Goal**: Validate translation quality

**Actions**:
1. Self-review checklist:
   - [ ] Meaning accurate throughout
   - [ ] No omissions or additions
   - [ ] Terminology consistent (glossary applied)
   - [ ] Tone and style appropriate
   - [ ] Grammar and spelling correct
   - [ ] Formatting preserved
   - [ ] Cultural adaptation appropriate
   - [ ] Names and proper nouns handled correctly

2. Back-translation check (for critical content):
   - Mentally translate back to source
   - Does meaning match original?
   - Any significant drift?

3. Common error checks:

   **False friends** (similar words, different meanings):
   ```
   ES: "embarazada" ≠ embarrassed (= pregnant!)
   ES: "actual" ≠ actual (= current)
   FR: "librairie" ≠ library (= bookstore)
   DE: "Gift" ≠ gift (= poison!)
   ```

   **Gender agreement**:
   ```
   ES: "la problema" ❌ → "el problema" ✅
   FR: "un belle femme" ❌ → "une belle femme" ✅
   ```

   **Verb tenses**:
   ```
   Check tense consistency
   Match temporal context
   Conditional vs. subjunctive
   ```

4. Readability assessment:
   - Sentences flow naturally?
   - Paragraph breaks appropriate?
   - Transitions clear?
   - Overall coherence?

5. Provide alternatives for ambiguity:
   ```markdown
   **Ambiguous phrase**: "We need to address this issue"

   **Option A**: "Tenemos que resolver este problema"
   (We need to solve this problem - implies fixing)

   **Option B**: "Tenemos que abordar este tema"
   (We need to address this topic - implies discussing)

   **Recommended**: Option A if fixing, Option B if discussing
   ```

**Quality Check**:
- [ ] Checklist complete
- [ ] Common errors checked
- [ ] Alternatives for ambiguity
- [ ] Confidence level assessed

### Step 6: Delivery

**Goal**: Present translation with context

**Output Structure**:
```markdown
# Translation: [Title]

## Translation Summary

**Source**: English
**Target**: Spanish (Latin America)
**Type**: Technical documentation
**Formality**: Professional
**Date**: 2024-11-18
**Word Count**: Source: 850 | Target: 920 (8% expansion)

## Translated Content

[Full translation here, preserving all formatting]

## Translation Glossary

| English | Spanish | Context | Notes |
|---------|---------|---------|-------|
| [term] | [translation] | [usage] | [reasoning] |

## Translation Notes

### Important Decisions

**1. "Dashboard" → "Tablero"**
- Original: "dashboard"
- Translation: "tablero"
- Alternatives: "panel de control" (too formal), "panel" (ambiguous)
- Rationale: "Tablero" is standard in Latin American Spanish for UI dashboards

### Cultural Adaptations

**1. Time reference**
- Original: "business hours (9am-5pm)"
- Adapted: "horario laboral (9:00-17:00)"
- Rationale: 24-hour format standard in Spanish-speaking countries

### Ambiguities & Recommendations

**1. "Register" (ambiguous)**
- Option A: "Registrar" (create account)
- Option B: "Inscribirse" (enroll/sign up)
- **Recommended**: "Registrar" for software context

## Quality Metrics

- ✅ **Completeness**: 100% (all content translated)
- ✅ **Consistency**: High (glossary applied throughout)
- ✅ **Confidence**: High (native-level fluency)
- ✅ **Cultural Fit**: High (appropriate for target region)

## Expansion/Contraction

**Text Expansion**: +8% (typical for Spanish)
- English: 850 words
- Spanish: 920 words
- UI consideration: May need adjustments for button labels

## Recommended Review

**Focus areas**:
- Technical terms (párrafos 3-5)
- Cultural references (párrafo 8)
- Call-to-action buttons (verify fit in UI)
```

## Language-Specific Considerations

### Romance Languages (Spanish, French, Italian, Portuguese)

**Characteristics**:
- Gender agreement (nouns, adjectives)
- Formal vs. informal pronouns
- Rich verb conjugations
- Text expansion: +15-25% typically

**Spanish Variants**:
- Spain (ES-ES): vosotros, leísmo, ustedes formal only
- Latin America (ES-LATAM): ustedes for you-plural, tuteo/voseo
- Argentina: vos instead of tú

### Germanic Languages (German, Dutch, Swedish)

**Characteristics**:
- Compound words (very long)
- Capitalized nouns (German)
- Formal vs. informal pronouns
- Text expansion: +10-20%

**German specifics**:
- Nouns capitalized: "das Internet"
- Compound words: "Geschwindigkeitsbegrenzung" (speed limit)
- Gender-inclusive: Nutzer*innen, NutzerInnen, Nutzer(innen)

### Asian Languages (Chinese, Japanese, Korean)

**Characteristics**:
- No spaces between words (Chinese, Japanese)
- Complex honorific systems
- Text compression: -30-50% typically
- Different writing systems

**Japanese specifics**:
- 3 writing systems: hiragana, katakana, kanji
- Politeness levels: casual, polite, respectful, humble
- Loanwords in katakana: コンピュータ (computer)

### Right-to-Left Languages (Arabic, Hebrew)

**Characteristics**:
- Text direction: right to left
- Numbers: left to right
- UI elements: mirrored
- Text expansion: +20-30%

## Common Patterns

### Marketing Copy
- Preserve brand voice
- Adapt cultural references
- Maintain emotional impact
- Use local idioms

### Technical Documentation
- Keep technical terms in English if standard
- Translate explanations
- Preserve code examples
- Translate comments if helpful

### Legal/Formal
- Highest accuracy required
- Maintain formal register
- Preserve exact meaning
- Note any uncertainty

### User Interface
- Keep very concise (space constraints)
- Use standard UI terminology
- Maintain parallel structure
- Test for text expansion

## Integration with Agents

This skill is used by:
- **translate-agent**: Primary user
- Any agent needing translation patterns

Works well with:
- **proofreading**: For final editing of translated content
- **doc-compliance**: For checking translation against brand guidelines

## Quick Reference

**Process**: Understand context → Build glossary → Translate → Adapt culturally → Validate → Deliver

**Key principles**: Meaning > literalness, Natural > correct, Consistent > varied

**Output must have**: Translated content, glossary, decision notes, quality assessment
