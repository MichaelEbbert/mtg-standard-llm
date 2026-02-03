# MTG-STD-LLM Project

## Project Goal
Vibe code together to fine-tune the Mistral 7B model for Magic: The Gathering Standard format analysis.

## Local Environment
- **GPT4ALL**: Installed at `D:\gpt4all\bin` (available if we need a local client)

## About My Partner
- **Primary language**: Java (26 years experience, highly fluid)
- **Other languages**: Acceptable as needed
- **Career transition**: Moving from full-time Java backend development to 1/4 Java + 3/4 AI Agents work
- **Learning goals**: LLMs, Claude Code, vibe coding, fine-tuning, and AI concepts useful for career growth

## Interaction Preferences
- **One task at a time** when introducing new topics
- Do NOT give multi-step instructions (A, then B, then C, then D) in a single message
- This allows for questions and discussion at each step without scrolling back

## Skills Focus
This project will make heavy use of Claude Code custom skills (folders with `SKILL.md` files).

### Planned Skills
1. **MTG Card Parser** - Transform raw Magic card data into training format

## Teaching Notes
This project doubles as a learning experience. Explain LLM concepts, fine-tuning approaches, and AI agent patterns as we encounter them.

---

## Training Concepts

### Fine-Tune (teach reasoning and understanding)

**Core Rules**
- Turn structure (phases, steps, priority)
- The stack (LIFO, responses, resolving)
- Targeting rules (legal targets, hexproof, shroud, protection)
- Damage (combat vs direct, prevention, replacement effects)
- State-based actions (0 toughness, lethal damage, legend rule)
- Zones (library, hand, battlefield, graveyard, exile, stack, command)
- Layers (how continuous effects apply)

**Card Types**
- Creatures, Instants, Sorceries, Enchantments (auras vs global), Artifacts (equipment, vehicles), Planeswalkers, Lands, Battles

**Keyword Abilities (Evergreen & Deciduous)**
- Evergreen: flying, trample, haste, deathtouch, lifelink, hexproof, vigilance, reach, menace, ward, etc.
- Returning/deciduous: cycling, kicker, flashback, etc.

**Mana System**
- Colors and color identity
- Mana costs vs mana value
- Hybrid, Phyrexian mana
- Mana curves (concept of curving out, ideal distributions)

**Combat**
- Attack/block mechanics, first strike, double strike, trample, multiple blockers

**Synergy Reasoning** (conceptual framework, not specific combos)
- What synergy means: cards that amplify each other's effects
- How to recognize synergy: resource creation + resource consumption patterns
- Categories of synergy: triggers, enablers, payoffs
- Note: Specific synergy examples (e.g., "Card X + Card Y") go in FAISS

**Play Pattern Reasoning** (analytical framework, not specific examples)
- How to identify tension: cards wanting different game states
- Evaluating deck coherence: do all cards support the same plan?
- Sideboard evaluation: does bringing in X weaken existing card Y?
- Note: Specific anti-synergy examples from current meta go in FAISS

**Color Identity & Clans**
- Guilds (2-color): Azorius, Dimir, Rakdos, Gruul, Selesnya, Orzhov, Izzet, Golgari, Boros, Simic
- Shards (3-color): Bant, Esper, Grixis, Jund, Naya
- Wedges (3-color): Abzan, Jeskai, Sultai, Mardu, Temur
- 4-color names

**Format Rules**
- What Standard means, rotation concept
- How to determine format legality

**Strategy Concepts** (frameworks for reasoning, not meta-specific advice)
- Card advantage: what it means, how to evaluate trades
- Tempo: mana efficiency, board development timing
- Archetype definitions: aggro, midrange, control, combo, tempo
- Sideboarding principles: how to think about it
- Note: Current meta archetypes and specific deck advice go in FAISS

**RAG Behavior**
- Trust retrieved card data as authoritative
- Apply rules reasoning to provided data
- Don't hallucinate from vague memories

---

### FAISS (retrieve facts that change)

**Card Data**
- Card text, types, costs, set, rarity, legality

**Set-Specific Keyword Abilities**
- Mechanics unique to each set

**Format Legality**
- Currently legal sets per format
- Card ban lists

**Current Metagame**
- Meta deck names and compositions
- Deck archetype mappings (e.g., "UW Tokens is a control deck")

**Matchup Data** (deck vs deck specifics)
- Strengths and weaknesses are relative to the opposing deck, not absolute
- For each relevant matchup pair, store:
  - Which deck is beatdown, which is control
  - Key cards that matter in this specific matchup
  - Sideboard plans for both sides
  - What each deck is trying to accomplish
- Example: "Mono-Red vs UW Control" has different key cards and plans than "Mono-Red vs Golgari Midrange"
- ~50-70 matchup pairs covers a typical meta (8-12 tier decks)

**Synergy Examples** (specific combos that change with sets/meta)
- Current strong synergy pairs (e.g., "Sacrifice + Braids")
- Set-specific synergy packages
- Deck-specific synergy explanations

**Anti-Synergy / Tension Examples** (meta-specific conflicts)
- Known problematic card pairings in current decks
- Sideboard cards that conflict with maindeck plans

**Rules Citations**
- Comprehensive Rules document (chunked by section)
- Exact rule numbers and text for citation

---

## Architecture Decision
**Hybrid approach**:
- **Fine-tune** = teach reasoning skills and conceptual frameworks (what synergy *means*, how to evaluate tempo, etc.)
- **FAISS** = store facts that change (specific cards, specific synergies, current meta decks, rule citations)

New sets or mid-season meta shifts = FAISS database update, not retraining.
Fine-tuning reserved for improving *how* the model reasons, not *what* it knows about current cards/combos.

---

## TODO: Pre-Fine-Tuning Tasks

### Ability/Keyword Gap Analysis
**Before fine-tuning**, load the full card database into FAISS first. Then:
1. Extract all unique abilities/keywords from the card data
2. Compare against abilities covered in our fine-tuning strategy sources
3. Identify gaps (new mechanics like Warp, Exhaust, bending abilities, etc.)
4. Add strategy content for each missing ability to `data/raw/keywords/keywords.md`

This ensures the model understands how to *reason* about every ability type it will encounter via RAG retrieval.

### Keyword Strategy Content (IN PROGRESS)
- Created `data/raw/keywords/keywords.md` with strategic explanations
- Covers: 18 evergreen, 4 bending abilities, 26 set-specific, 8 deciduous keywords
- Remaining: Lorwyn Eclipsed, TMNT, Marvel mechanics (need identification)
- Status: Rough drafts complete, editing pass needed
