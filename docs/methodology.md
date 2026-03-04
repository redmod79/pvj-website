# Paul vs Jesus Series — Investigative Methodology

*This file defines the methodology for ALL studies in the pvj-XX series (Does Paul Contradict Jesus?). Every analysis agent MUST follow this methodology.*

## Central Question

**Does Paul's teaching contradict Jesus's teaching? When Paul and Jesus appear to disagree on faith, works, the law, food, women's roles, marriage, or other topics, is the contradiction real or apparent?**

Two positions are investigated:
- **Contradiction position**: Paul teaches something incompatible with Jesus on this topic. The two cannot be reconciled without distorting what one or both actually said.
- **Harmony position**: The apparent contradiction dissolves when context, audience, vocabulary, scope differences, or fuller reading of both authors is properly accounted for. Paul and Jesus are addressing different questions, different audiences, or using different vocabulary — not teaching opposite things.

**KEY POSITIONAL DISTINCTION:** The Contradiction position argues that Paul introduced teachings that genuinely conflict with what Jesus taught — whether on justification, law, food, women, eschatology, or other topics. The Harmony position argues that when the full context of both authors is examined — including audience, occasion, vocabulary, genre, and the pre-cross vs. post-cross timeline — the apparent contradictions resolve into complementary perspectives on the same truth.

## Required Tool Usage for Every Study

**Every pvj-XX study MUST run `concept_context.py --scope author` on key verses from BOTH Paul and the Gospels.** This compares author-level usage patterns and reveals whether Paul and Jesus use the same vocabulary the same way. Example:

```bash
python D:/bible/tools/context/concept_context.py "Romans 3:28" --scope author
python D:/bible/tools/context/concept_context.py "Matthew 7:21" --scope author
```

This is mandatory because many alleged contradictions arise from the same Greek word carrying different meanings in different authors.

## Investigative Methodology (include verbatim in every agent prompt)

```
INVESTIGATIVE METHODOLOGY:
- You are an investigator, not an advocate. Your job is to report what the evidence says.
- Gather evidence from ALL sides. If a passage is cited by those who claim contradiction, examine it honestly. If a passage is cited by those who claim harmony, examine it honestly.
- Do NOT assume your conclusion before examining the evidence.
- Do NOT state opinions. State what the text says. Do not use editorial characterizations like "genuine tension," "strongest argument," "most significant challenge," "honestly acknowledge," or "non-intuitive reading." Simply state what each passage says and what each side infers from it.
- When presenting findings, state: "The text says X" (explicit). Then state: "From this, the Contradiction interpretation infers Y" and "the Harmony interpretation infers Z" (inferred).
- Never use language like "irrefutable," "obviously," or "clearly proves." Use "the text states," "this is consistent with."
- The conclusion should emerge FROM the evidence, not be imposed ON it.
- Present BOTH the Contradiction and Harmony positions at their strongest. Do not strawman either side.
```

## Evidence Classification (REQUIRED in every CONCLUSION.md)

Every CONCLUSION.md MUST include a multi-tier evidence classification section. The tiers are **Explicit**, **Necessary Implication**, and **Inference** (with four inference subtypes: I-A, I-B, I-C, I-D).

**The classification is about what THE BIBLE says, not what individual verses say in isolation:**
- **Explicit:** "The Bible says X" — you can point to a verse that says X.
- **Necessary Implication:** "The Bible implies X" — you can point to verses that, when combined, force X with no alternative.
- **Inferred:** "Someone claims the Bible teaches X" — but no verse says X and no combination of verses forces X. Something must be added that the text does not contain. Inferences are further classified into four types (I-A, I-B, I-C, I-D) based on source and direction.

**Evidence Hierarchy:** E > N > I-A > I-B (resolved by SIS) > I-C > I-D

**CRITICAL RULE: Inferences cannot block explicit statements or necessary implications.** If explicit texts and necessary implications establish X, the existence of passages that *could be inferred* to teach not-X does not prevent X from being a necessary implication. The passages cited against X must be evaluated on their own terms — if reading them as contradicting X requires adding a concept, choosing between readings, applying an external framework, or systematizing, then that reading is itself an inference and cannot override what the explicit texts state.

### 1. Explicit Statements Table

| # | Explicit Statement | Reference |
|---|---|---|
| E1 | [What the text directly says — a quote or close paraphrase] | [Book Chapter:Verse] |

Rules for explicit statements:
- The text must directly say this. Quote or closely paraphrase the actual words of Scripture.
- One explicit statement per verse or closely related verse cluster.
- Include statements from ALL sides of the debate.
- A paraphrase of a single verse in different words is still explicit. "Thou shalt not kill" = "God forbids murder" -> explicit (same verse, same meaning).
- **THE MEANING OF WORDS IS EXPLICIT.** If a single verse uses a word, what that word means is part of the explicit statement.

**CRITICAL: What the text SAYS vs. what a position INFERS:**
- **E tier** = what the text directly states (what both sides must acknowledge as textual fact)
- **I tier** = what a position interprets/infers from that text

Examples (using passages in this series):
- "Think not that I am come to destroy the law, or the prophets" (Mat 5:17) -> **E** (what the text says)
- "Therefore Jesus's law-keeping commands contradict Paul's faith-alone teaching" -> **I-B** (requires interpreting both authors' scope)
- "Paul says 'justified by faith without the deeds of the law' (Rom 3:28)" -> **E** (what the text states)
- "Therefore Paul contradicts Jesus's 'keep the commandments' (Mat 19:17)" -> **I-B** (requires determining whether both address the same question)
- "Paul says 'not I but the Lord' distinguishing his advice from Jesus's command (1 Cor 7:10)" -> **E** (what the text states)
- "Therefore Paul knew and deferred to Jesus's teaching, proving harmony" -> **I-A** (systematizes E into broader claim)

**The test:** Could both Contradiction and Harmony readers accept this as a factual observation about what the text says, even while disagreeing about what it means or implies? If yes -> E or N. If no (one side must deny it) -> only then classify by position.

### 2. Necessary Implications Table

| # | Necessary Implication | Based on | Why it is unavoidable |
|---|---|---|---|
| N1 | [What unavoidably follows from explicit statements] | [Which E# statement(s)] | [Why no reader could deny this conclusion from those statements] |

Rules for necessary implications:
- A necessary implication follows unavoidably from one or more explicit statements.
- **No additional concept, framework, or interpretation is required** — only understanding what the words mean.
- **Every reader, regardless of theological position, must agree this follows.** If a reasonable reader could disagree, it is an inference, not a necessary implication.
- Include necessary implications from ALL sides of the debate.

**STRICTER N-TIER TEST:**

Ask these three questions for EACH N item:

1. **Universal agreement test:** Would a scholar who holds the OPPOSITE position (Contradiction if you're Harmony, Harmony if you're Contradiction) necessarily agree this follows from the cited E statements?
   - If NO -> it's an inference, not a necessary implication

2. **No interpretation required test:** Does this require choosing between possible meanings, or is it the only possible meaning?
   - If it requires choosing -> it's an inference (I-B)

3. **Zero added concepts test:** Does this add ANY concept, framework, or connection not present in the explicit statements themselves?
   - If YES -> it's an inference (requires criterion #1, #3, or #4b)

### 3. Inferences Table (4-Type Taxonomy)

| # | Claim | Type | What the Bible actually says | Why this is an inference | Criteria |
|---|-------|------|-----|------|----------|
| I1 | [The claim about what the Bible teaches] | [I-A/I-B/I-C/I-D] | [What the relevant verses actually say — cite E# and N# items AND include actual verse references and what they say] | [What must be added beyond what the text contains] | [Which criterion/criteria apply] |

#### The 4-Type Inference Taxonomy

Two dimensions create a 2x2 matrix:

|  | Aligns with E/N | Conflicts with E/N |
|--|--|--|
| **Derived from E/N** | **I-A** (Evidence-Extending) | **I-B** (Competing-Evidence) |
| **Not derived from E/N** | **I-C** (Compatible External) | **I-D** (Counter-Evidence External) |

**I-A (Evidence-Extending):** Uses ONLY vocabulary and concepts found in E/N statements. Only an inference because it systematizes multiple E/N items into a broader claim. Strongest inference type.

**I-B (Competing-Evidence):** Some E/N statements support it, but other E/N statements appear to contradict it. Genuine textual tension where both sides can cite Scripture. Resolved by the Scripture-Interprets-Scripture (SIS) protocol.

**I-C (Compatible External):** Reasoning from outside the text (theological tradition, philosophical framework, historical context) that does not contradict any E/N statements. Supplemental only — adds information the text does not contain but does not override anything the text says.

**I-D (Counter-Evidence External):** External concepts that require overriding, redefining, or qualifying E/N statements to be maintained. Weakest inference type — requires the text to mean something other than what it says.

#### Mechanical Tests for Classification

**Source test** (derived vs. external): Strip away the systematization. Are ALL remaining components found in the E/N tables? YES = text-derived (I-A or I-B). NO = external (I-C or I-D).

**Direction test** (aligns vs. conflicts): Does the claim require ANY E/N statement to mean something other than its lexical value? YES = conflicts (I-B or I-D). NO = aligns/compatible (I-A or I-C).

**Consistency checks:**
- I-A should only require criterion #5 (systematizing) and optionally #4a (SIS). If it requires #1, #2, or #3, it is misclassified.
- Every I-B must have E/N items on BOTH sides. If only one side has E/N support, it is I-A or I-D.
- Every I-D must override at least one E/N statement. If it overrides nothing, it is I-C.

#### Rules for inferences:
- An inference is a claim about what the Bible teaches that **no verse explicitly states** and **no combination of verses necessarily implies.** Something must be added beyond what the text contains.
- State each inference as a Bible-wide claim ("The Bible teaches X"), not as a verse-specific interpretation ("Verse Y means Z"). Then show why no verse says it and no combination forces it.
- **Always include the actual verse references and what they say** in the "What the Bible actually says" column — not just E#/N# numbers. The reader should see the biblical evidence without cross-referencing.
- Include inferences from ALL sides (both Contradiction and Harmony positions)
- Identify what reasoning step is required that the text itself does not state
- Note when an inference requires applying concepts not found in the text

**An inference MUST require at least one of these:**
1. **Adding a concept the text doesn't state** — e.g., "Paul contradicts Jesus on the law" when neither author directly addresses the other's teaching
2. **Choosing between two possible readings** — e.g., interpreting Paul's "works of the law" as all moral obedience vs. only ceremonial observance
3. **Applying an external framework** — e.g., dispensational or covenantal theology to explain the differences
4. **Cross-referencing (split into 4a and 4b — see SIS section below)**
5. **Systematizing into a doctrine** — e.g., combining multiple texts into a comprehensive theological position

**If you cannot identify which of these an inference requires, it is probably a necessary implication and should be moved.**

## Scripture-Interprets-Scripture (SIS) Principle

### What SIS Means for the PVJ Series

Criterion #4 splits into two:
- **#4a** (SIS with verified textual connection) — NOT an inference trigger. When a clear passage interprets an unclear one, and the connection is verified (shared vocabulary, OT quotation, tool-verified parallel score, or the text itself establishes the connection), this is standard hermeneutics, not an inference. Document the connection.
- **#4b** (cross-referencing without verified textual connection) — IS an inference trigger. The reader must supply the connection between passages. The link depends on the interpreter's judgment, not on the text itself.

### How to Document SIS Connections

When using #4a (SIS with verified connection), document:
1. The clear passage and the unclear passage
2. The nature of the connection (shared vocabulary, OT quotation, parallel score, self-reference)
3. Why the clear passage is clearer (using the clarity criteria below)
4. How the clear passage determines the reading of the unclear one

### I-B Resolution Protocol

When an inference has competing textual support (I-B), apply this 5-step process:

**Step 1: Identify tension.** List E/N items FOR and AGAINST the claim.

**Step 2: Assess clarity** of each E/N item on a 3-level scale:
- **Plain**: Directly addresses the topic using relevant vocabulary; no interpretation needed
- **Contextually Clear**: Addresses the topic but requires genre/audience/context awareness
- **Ambiguous**: Could plausibly be read either way

**Step 3: Count and weigh.** Plain statements outweigh Ambiguous ones (not a mere vote count). The weight is determined by clarity level, not just quantity.

**Step 4: Apply SIS.** Plain statements determine the reading of Ambiguous ones. The clear interprets the unclear.

**Step 5: State resolution.** One of:
- **Strong** — Plain statements on one side with only Ambiguous statements on the other
- **Moderate** — Mix of Plain and Contextually Clear on the dominant side
- **Unresolved** — Substantial Plain/Contextually Clear statements on both sides

**Clarity criteria** (what makes a passage "clearer"):
1. **Directness of vocabulary** — actual words vs. figurative language
2. **Genre** — didactic > apocalyptic > parabolic
3. **Scope** — universal statement > specific situation
4. **Frequency** — repeated across authors/testaments > single occurrence
5. **Self-interpretation** — text explains its own meaning = maximally clear

### I-B Resolution Subsection

After the Inferences table, include a dedicated **I-B Resolution** subsection for EACH I-B inference with the full 5-step analysis:

```
#### I-B Resolution: [Inference #] — [Short description]

**Step 1 — Tension:**
- FOR: [E#, N# items supporting the claim]
- AGAINST: [E#, N# items opposing the claim]

**Step 2 — Clarity Assessment:**
| Item | Level | Rationale |
|------|-------|-----------|
| E# | Plain/Contextually Clear/Ambiguous | [Why] |
| ... | ... | ... |

**Step 3 — Weight:**
[Summary of how items on each side weigh]

**Step 4 — SIS Application:**
[How plain statements determine reading of ambiguous ones]

**Step 5 — Resolution: [Strong/Moderate/Unresolved]**
[Explanation]
```

## Classification Decision Trees

Apply these trees mechanically when classifying every evidence item. Every gate is a binary YES/NO answerable from the text itself. Work through each tree in order. Do not skip gates.

---

### Tree 1 — Tier Classification

**Start:** You have an observation or claim about what the Bible says.

```
Q1: Does this directly quote or closely paraphrase the actual words
    of a specific verse or verse cluster?
    NO  -> go to N-CHECK
    YES -> go to E-CHECK

E-CHECK:
  E1: Is this the plain lexical meaning of those words —
      no concept, framework, or interpretation added beyond what
      the words themselves require?
      YES -> TIER: E (Explicit). Stop. Go to Tree 3 (E-Positional).
      NO  -> go to N-CHECK

N-CHECK:
  N1: Does this follow unavoidably from one or more E-items?
      NO  -> TIER: I (Inference). Stop. Go to Tree 2 (I-Type).
      YES -> go to N2

  N2: Would a scholar from the OPPOSITE theological position
      necessarily agree this follows from the cited E-items,
      without any additional reasoning?
      NO  -> TIER: I. Stop. Go to Tree 2.
      YES -> go to N3

  N3: Does reaching this conclusion require choosing between
      two possible meanings of a word or phrase?
      YES -> TIER: I. Stop. Go to Tree 2.
      NO  -> go to N4

  N4: Does this add ANY concept, framework, or connection not
      already present in the cited E-items themselves?
      YES -> TIER: I. Stop. Go to Tree 2.
      NO  -> TIER: N (Necessary Implication). Stop. Go to Tree 4 (N-Positional).
```

---

### Tree 2 — I-Type Classification

**Start:** You have an item classified as I (Inference). Which subtype?

```
SOURCE TEST:
  S1: Strip away any systematization. Are ALL remaining components
      of this claim found verbatim or directly in the E/N tables?
      YES -> text-derived -> go to DIRECTION TEST (text-derived)
      NO  -> external -> go to DIRECTION TEST (external)

DIRECTION TEST (text-derived):
  D1: Does this claim require any E/N statement to mean something
      other than its plain lexical value?
      NO  -> TYPE: I-A (Evidence-Extending). Stop. Go to Tree 5 (I-Positional).
      YES -> TYPE: I-B (Competing-Evidence). Stop. Go to Tree 5.
            [I-B requires a full SIS Resolution subsection in the analysis.]

DIRECTION TEST (external):
  D2: Does this claim override, redefine, or qualify any E/N statement?
      NO  -> TYPE: I-C (Compatible External). Stop. Go to Tree 5.
      YES -> TYPE: I-D (Counter-Evidence External). Stop. Go to Tree 5.

CONSISTENCY CHECKS (run after typing — reclassify if any check fails):
  I-A check: Does it require ONLY criterion #5 (systematizing)?
             If it also requires #1, #2, or #3 -> reclassify.
  I-B check: Does it have E/N items on BOTH sides?
             If only one side has E/N support -> reclassify as I-A or I-D.
  I-D check: Does it override at least one E/N statement?
             If it overrides nothing -> reclassify as I-C.
```

---

### Tree 3 — E-Item Positional Classification

**Start:** You have a verified E-item. Does it support Contradiction, Harmony, or Neutral?

```
STEP 1 — VOCABULARY SCAN:

  V1: Does the verse contain evidence that Paul and Jesus AGREE
      on this topic, or that apparent disagreement is explained
      by context, audience, vocabulary, or scope differences?
      Keywords/indicators: Paul quoting Jesus, Paul citing "the Lord,"
      Paul's teaching paralleling Gospel teaching, Paul distinguishing
      his opinion from Jesus's command, Paul's audience differs from
      Jesus's audience, Paul's vocabulary carrying different semantic
      range than Jesus's same word, Paul's context is post-cross while
      Jesus's is pre-cross
      YES -> Candidate: HARMONY -> go to Step 2

  V2: Does the verse contain evidence of genuine incompatibility
      between Paul's teaching and Jesus's teaching on this topic?
      Keywords/indicators: Paul directly contradicting a specific
      command of Jesus, Paul teaching the opposite of what Jesus
      taught to the same audience on the same question with the
      same vocabulary in the same context
      YES -> Candidate: CONTRADICTION -> go to Step 2

  Both V1 and V2 YES -> note both; Step 2 determines which survives.
  Both V1 and V2 NO  -> NEUTRAL. Stop.


STEP 2 — FOUR VALIDATION GATES:
(Must pass ALL four. Failure at any gate -> go to Step 3.)

  GATE 1 — SUBJECT/OBJECT GATE:
    Is the specific topic of disagreement identifiable from the verse's
    own context? Both Paul's statement and Jesus's statement must be
    addressing the SAME subject for a contradiction to exist.
    Automatic FAIL if:
      * Paul is addressing one topic and Jesus another, and the
        "contradiction" requires conflating the two
      * The verse's subject is genuinely ambiguous between topics
    PASS -> continue to Gate 2
    FAIL -> record "Subjects being compared are not verified as identical." -> go to Step 3.

  GATE 2 — GRAMMAR GATE:
    Does the original-language grammar unambiguously support
    the proposed positional reading with no alternative parsing?
    Automatic FAIL if any of the following apply:
      * Reading depends on punctuation absent from the original
      * A key word has a semantic range that allows a different
        meaning than the proposed reading assumes
      * A modifier or qualifying phrase attaches grammatically to a
        different noun than the reading requires
      * The verse is part of a larger argument and the reading
        ignores the flow of that argument
    PASS -> continue to Gate 3
    FAIL -> record which specific grammar issue. -> go to Step 3.

  GATE 3 — GENRE GATE:
    Is the passage didactic prose?
    Didactic = direct teaching, epistle, law, narrative report,
               direct-speech prophecy ("Thus says the Lord...")
    Automatic FAIL if passage is:
      * An apocalyptic vision (symbolic imagery in Revelation, Daniel)
      * A typological narrative used figuratively
    Note: Most passages in this series are in didactic/epistolary genre
    and will pass this gate.
    PASS -> continue to Gate 4
    FAIL -> record "Genre is [apocalyptic/typological]." -> go to Step 3.

  GATE 4 — HARMONY GATE:
    Is the proposed positional classification consistent with
    all other E-items in the master evidence file?
    Check:
      * Same-author E-items on the same topic
      * Cross-author E-items sharing key vocabulary or subject
      * E-items already classified in the opposite direction on this topic
    If a conflict is found, apply SIS resolution:
      * Use clarity criteria (didactic > apocalyptic > parabolic;
        universal > specific; repeated > single occurrence)
      * Does the clearer passage govern the reading of the less clear?
        YES -> apply that reading, re-run Gate 4 with corrected reading
        NO  -> unresolvable conflict -> FAIL -> record conflicting E-item -> go to Step 3.
    No conflict found -> PASS -> CLASSIFICATION STANDS. Stop.


STEP 3 — RECLASSIFICATION CHECK:
(Reached when any gate fails.)

  RC1: State what the gate failure revealed.
  RC2: Form the CORRECTED textual observation by applying the gate's correction.
  RC3: Re-enter STEP 1 with the corrected observation.
       Does the corrected observation pass V1 (harmony indicators)?
         YES -> HARMONY. Stop.
       Does the corrected observation pass V2 (contradiction indicators)?
         YES -> CONTRADICTION. Stop.
       Neither applies -> NEUTRAL. Stop.
```

---

### Tree 4 — N-Item Positional Classification

**Start:** You have a verified N-item. Same as Tree 3 with one additional gate first.

```
GATE 0 — FOUNDATION GATE (N-items only):
  Verify the item genuinely belongs at N-tier before classifying position.
  Apply all three N-tier tests:
    N-Test 1 (Universal agreement): Would a scholar from the opposite
      position necessarily agree this follows from the cited E-items?
    N-Test 2 (No interpretation required): Is this the only possible
      conclusion — not a choice between two readings?
    N-Test 3 (Zero added concepts): Does this add nothing beyond
      what the source E-items themselves contain?
  All three YES -> PASS -> continue to Tree 3 (Vocabulary Scan onward).
  Any NO -> item is misclassified as N -> send back to Tree 1 (N-CHECK fails) ->
            reclassify as I -> apply Tree 2 -> apply Tree 5.
```

---

### Tree 5 — I-Item Positional Classification

**Start:** You have a typed I-item (I-A, I-B, I-C, or I-D). What position does it support?

```
NOTE: The four-gate validation (Trees 3/4) does NOT apply to I-items.
The inference category already acknowledges that interpretation is required.
Position simply reflects which direction the inference points.

  IP1: Does this inference support the claim that Paul and Jesus
       AGREE on this topic — that the apparent contradiction dissolves
       when context, audience, vocabulary, scope, or fuller reading
       is accounted for?
       YES -> HARMONY

  IP2: Does this inference support the claim that Paul and Jesus
       genuinely DISAGREE on this topic — that the contradiction
       persists even after accounting for context, audience,
       vocabulary, and scope?
       YES -> CONTRADICTION

  IP3: Does the inference support both, or neither?
       BOTH -> verify it is classified I-B (competing evidence from both sides).
               If not I-B, reclassify. Apply SIS resolution to determine
               which direction the weight of evidence favors.
       NEITHER -> NEUTRAL.
               (The inference concerns background, methodology, vocabulary,
                historical context, or is shared framework for both sides.)
```

---

### 4. Verification Phase (REQUIRED)

After completing all tables, run this verification check:

**Step A: Verify explicit statements:**
- Does each E-statement directly quote or closely paraphrase actual verse text?
- Is it actually just the plain meaning of the words in the verse?
- **Is this what the text SAYS (E) or what a position INFERS from it (I)?** If it's an inference, move it.

**Step A2: Verify positional classifications of E-items (REQUIRED):**
For each E-item classified as Contradiction or Harmony (not Neutral), apply **Tree 3 (E-Item Positional Classification)** from the Classification Decision Trees section above. This is mandatory.

**Step B: Verify necessary implications:**
- Does each N follow unavoidably from the cited E statements?
- Could ANY reader deny this conclusion while accepting the explicit statements? If yes -> move to Inferences.
- Apply the three N-tier tests. If any test fails -> move to Inferences.

**Step C: Verify inference classifications (source test):**
For each inference, strip away the systematization. Are ALL remaining components found in the E/N tables?
- YES -> text-derived (I-A or I-B)
- NO -> external (I-C or I-D)

**Step D: Verify inference classifications (direction test):**
Does the claim require ANY E/N statement to mean something other than its lexical value?
- YES -> conflicts (I-B or I-D)
- NO -> aligns/compatible (I-A or I-C)

**Step E: Run consistency checks:**
- Every I-A: Does it only require criterion #5 (and optionally #4a)? If it requires #1, #2, or #3, reclassify.
- Every I-B: Does it have E/N items on BOTH sides? If only one side has E/N support, reclassify as I-A or I-D.
- Every I-D: Does it override at least one E/N statement? If it overrides nothing, reclassify as I-C.

**Step F: Verify SIS connections:**
- Is each #4a connection documented with shared vocabulary, OT quotation, or tool-verified parallel?
- Is each #4b properly treated as an inference trigger?

**Common mistakes to avoid:**
- Do NOT classify the plain meaning of words as inference. "Justified" means justified. "Faith" means faith.
- Do NOT classify observable textual patterns as inference. If Paul quotes Jesus, that's a fact you can observe.
- Do NOT classify unavoidable combinations as inference. If explicit statements A + B together yield C with no alternative, C is a necessary implication.
- The COUNTER-CLAIM to an explicit statement or necessary implication is often the real inference.

**After verification:**
- Move misclassified items between tables as needed
- Update the tally counts
- Ensure every inference has a clear Type (I-A, I-B, I-C, or I-D)
- Ensure every inference identifies which criterion/criteria apply
- Ensure every I-B has a full Resolution subsection
- Ensure every necessary implication cites its source E# statements and explains why it is unavoidable

### 5. Master Evidence Database (REQUIRED before writing Tally)

**Before computing your tally, you MUST check and update the evidence database.**

The evidence database (`D:/bible/bible-studies/pvj-evidence.db`, managed by `D:/bible/evidence_db.py`)
holds all E/N/I items registered by every prior study and assigns IDs atomically — no duplicates, no guessing.

Steps:
1. **Check for existing items** before adding anything new (keyword or semantic search):
   ```bash
   python D:/bible/evidence_db.py find E --ref "Rom 3:28" --text "justified by faith" --db D:/bible/bible-studies/pvj-evidence.db
   python D:/bible/evidence_db.py search "justified by faith apart from works" --tier E --db D:/bible/bible-studies/pvj-evidence.db
   ```
2. **For each E/N/I item in your tables:**
   - If a match exists -> note the master ID in your CONCLUSION.md (e.g., "E23 -> Master E042") and record your study: `python D:/bible/evidence_db.py also-in E042 pvj-XX --db D:/bible/bible-studies/pvj-evidence.db`
   - If no match -> reserve the next ID: `python D:/bible/evidence_db.py next-id E --db D:/bible/bible-studies/pvj-evidence.db` then add it
3. **In your CONCLUSION.md, add a note:** "Evidence items registered in D:/bible/bible-studies/pvj-evidence.db"

### 6. Tally Summary

```
- Explicit statements: [count]
- Necessary implications: [count]
- Inferences: [count]
  - I-A (Evidence-Extending): [count]
  - I-B (Competing-Evidence): [count] ([N] resolved, [M] unresolved)
  - I-C (Compatible External): [count]
  - I-D (Counter-Evidence External): [count]
```

### 7. What CAN Be Said / What CANNOT Be Said

**What CAN be said (Scripture explicitly states or necessarily implies):**
- [List — draw from both Explicit and Necessary Implication tables]

**What CANNOT be said (not explicitly stated or necessarily implied by Scripture):**
- [List of things neither side can claim the text directly says or necessarily implies — including things commonly assumed by BOTH sides]

## Critical Rules Governing the Hierarchy

1. **E > N > I-A > I-B > I-C > I-D.** Higher-tier evidence governs the interpretation of lower-tier claims. An I-D claim cannot override an E statement.

2. **Inferences cannot block explicit statements or necessary implications.** If explicit texts and necessary implications establish X, the existence of passages that *could be inferred* to teach not-X does not prevent X from being established.

3. **I-A inferences are the strongest inferences** because they use only the text's own vocabulary and concepts. They are inferences only because they systematize.

4. **I-B inferences require the SIS protocol.** Both sides have textual support. The resolution must be documented. Plain passages interpret ambiguous ones.

5. **I-D inferences bear the heaviest burden.** They require overriding what the text says with concepts the text does not contain. They are valid only if the text itself provides reason to read against its surface meaning.

6. **SIS connections (#4a) are not inference triggers.** Using clear passages to interpret unclear ones — when the connection is verified — is standard hermeneutics. Only unverified cross-references (#4b) trigger inference classification.

## Positional Tally (REQUIRED in pvj-22 Synthesis ONLY)

**The evidence database (`pvj-evidence.db`) is the deduplication mechanism.** Each study (pvj-01 through pvj-21) checks the database before adding items. By the time pvj-22 runs, the database already contains a deduplicated set. pvj-22's job is to:

1. **Query the evidence database** — it is already deduplicated:
   ```bash
   python D:/bible/evidence_db.py tally --db D:/bible/bible-studies/pvj-evidence.db
   python D:/bible/evidence_db.py list --tier E --classification Harmony --db D:/bible/bible-studies/pvj-evidence.db
   python D:/bible/evidence_db.py list --tier E --classification Contradiction --db D:/bible/bible-studies/pvj-evidence.db
   python D:/bible/evidence_db.py list --tier N --db D:/bible/bible-studies/pvj-evidence.db
   python D:/bible/evidence_db.py list --tier I --db D:/bible/bible-studies/pvj-evidence.db
   ```
2. **Verify integrity** — flag any items that appear to be duplicates
3. **Produce the positional tally** from the database contents

**Classification rules for positional tally:**

- **Harmony:** Item states or implies Paul and Jesus agree on this topic, the apparent contradiction dissolves with proper context/vocabulary/audience analysis, Paul knew and deferred to Jesus's teaching, or the two authors address different questions/audiences.

- **Contradiction:** Item states or implies Paul and Jesus genuinely disagree on this topic in a way that cannot be resolved by context, audience, vocabulary, or scope differences.

- **Neutral/Shared:** Factual observations BOTH sides must accept:
  - Grammatical facts (same word used, word counts, parsing data, semantic ranges)
  - Statistical observations (vocabulary distributions, occurrence counts)
  - Genre identifications
  - Subject identifications
  - Textual observations about what is or isn't stated
  - Greek vocabulary facts
  - Historical context both sides accept
  - Any observation both Contradiction and Harmony scholars can accept as textual fact

### Positional Tally Format

```
## Positional Tally (from Master Evidence Database)

### By Evidence Tier

| Tier | Harmony | Contradiction | Neutral/Shared | Total |
|------|---------|---------------|----------------|-------|
| Explicit (E) | [count] | [count] | [count] | [count] |
| Necessary Implication (N) | [count] | [count] | [count] | [count] |
| I-A (Evidence-Extending) | [count] | [count] | [count] | [count] |
| I-B (Competing-Evidence) | [count] | [count] | [count] | [count] |
| I-C (Compatible External) | [count] | [count] | [count] | [count] |
| I-D (Counter-Evidence External) | [count] | [count] | [count] | [count] |
| **TOTAL** | **[count]** | **[count]** | **[count]** | **[count]** |

**Total unique items (from pvj-evidence.db):** [count]
**Integrity check:** [number] duplicate items found and flagged / 0 duplicates found
**Studies contributing:** [list of pvj-XX studies]
```

## Conclusion Tone Rule

The conclusion section of every study MUST:
- Present the classification results as data
- State what the evidence tiers contain
- NOT use hedging language like "this doesn't prove X" or "this doesn't disprove Y"
- NOT editorialize about what the results mean for either position
- Let the numbers and classifications speak for themselves

## No Editorial Opinion

- Do NOT characterize passages as being "in tension" with each other — simply state what each passage says
- Do NOT call any argument "the strongest" or "the weakest" — present the arguments and the evidence
- Do NOT use "genuinely ambiguous" — state the possible readings and note which the text specifies or does not specify
- Do NOT say something "requires sustained effort to maintain" — state the reasoning required and let the reader assess
- For passages covered by later studies in the series, briefly state what the text says and cross-reference the later study

## Cross-References to Other Studies

When a passage is examined in depth in another pvj-XX study:
- Briefly state what the verse says (quote it)
- Add: *(Examined in depth in pvj-XX-slug.)*
- Do NOT editorialize about the passage — that's for the dedicated study

## Prior Study Conclusions

Each study should consult prior work before beginning analysis. Prior findings inform *what areas to investigate* but not *what to conclude*. Each study investigates independently.

**Primary method — study database (scales to 22 studies):**
```bash
python D:/bible/study_db.py find-passage "Rom 3:31" --db D:/bible/bible-studies/pvj-study.db
python D:/bible/study_db.py find-word "dikaioo" --db D:/bible/bible-studies/pvj-study.db
python D:/bible/study_db.py search "faith works contradiction" --top 5 --db D:/bible/bible-studies/pvj-study.db
python D:/bible/study_db.py get pvj-05 --db D:/bible/bible-studies/pvj-study.db
```

**Secondary method — read CONCLUSION.md directly** for the studies the DB search identifies as most relevant. All prior CONCLUSION.md files are at `D:/bible/bible-studies/pvj-XX-*/CONCLUSION.md`.

---

## Required CONCLUSION.md Template

**Every pvj-XX study MUST produce a CONCLUSION.md that follows this exact structure.** All sections are REQUIRED unless marked (conditional). Use the exact heading levels shown (h1, h2, h3). Do not rename sections, reorder them, or omit any. After writing, verify every section is present.

````markdown
# [Descriptive Study Title] (pvj-XX)

## Study Question
[The original question from the task prompt — copy verbatim]

## Methodology
This study follows the investigative methodology defined in
`D:/bible/bible-studies/pvj-series-methodology.md`.
Evidence items registered in D:/bible/bible-studies/pvj-evidence.db.

---

## Summary Answer
[2-3 sentence direct answer summarizing what the evidence shows.
State what the explicit statements and necessary implications establish.
Do not editorialize — present findings as data.]

## Key Verses
[6-12 most important verses. Format each as:]

**[Reference]** — "[Full KJV verse text]"

[Repeat for each key verse. Select verses that represent the strongest
E-tier evidence on ALL sides. Do not cherry-pick for one position.]

---

## Evidence Classification

Evidence items tracked in D:/bible/bible-studies/pvj-evidence.db.

### 1. Explicit Statements Table

Each E-item has been processed through Tree 1 (Tier Classification) and
Tree 3 (E-Item Positional Classification).

**Also-cited prior items** (already in master evidence DB, cited again by this study):

| # | Explicit Statement | Reference | Position | Master ID |
|---|---|---|---|---|
| E1 | [What the text directly says] | [Book Ch:V] | [Harmony/Contradiction/Neutral] | [Master ID] |

**New items** (added to master evidence DB by this study):

| # | Explicit Statement | Reference | Position | Master ID |
|---|---|---|---|---|
| E2 | [What the text directly says] | [Book Ch:V] | [Harmony/Contradiction/Neutral] | [Master ID] |

---

### 2. Necessary Implications Table

| # | Necessary Implication | Based on | Why it is unavoidable | Position | Master ID |
|---|---|---|---|---|---|
| N1 | [What unavoidably follows] | [E# items] | [Why no reader could deny this] | [Harmony/Contradiction/Neutral] | [Master ID] |

---

### 3. Inferences Table

| # | Claim | Type | What the Bible actually says | Why this is an inference | Criteria | Position |
|---|---|---|---|---|---|---|
| I1 | [The claim] | [I-A/I-B/I-C/I-D] | [Actual verse refs + what they say] | [What must be added] | [1-5] | [Harmony/Contradiction/Neutral] |

---

### I-B Resolution: [I#] — [Short description]
(conditional — include one subsection per I-B inference. Omit section entirely if no I-B items.)

**Step 1 — Tension:**
- FOR: [E#, N# items supporting the claim]
- AGAINST: [E#, N# items opposing the claim]

**Step 2 — Clarity Assessment:**
| Item | Level | Rationale |
|------|-------|-----------|
| E# | Plain/Contextually Clear/Ambiguous | [Why] |

**Step 3 — Weight:**
[Summary of how items on each side weigh by clarity level]

**Step 4 — SIS Application:**
[How plain statements determine reading of ambiguous ones]

**Step 5 — Resolution: [Strong/Moderate/Unresolved]**
[Explanation of resolution]

---

## Verification Phase
(conditional — include when the study has 5+ E items or any contested classifications.)

---

## Tally Summary

- Explicit statements: [count] ([N] Harmony, [N] Contradiction, [N] Neutral)
- Necessary implications: [count] ([N] Harmony, [N] Contradiction, [N] Neutral)
- Inferences: [count]
  - I-A (Evidence-Extending): [count]
  - I-B (Competing-Evidence): [count] ([N] resolved, [M] unresolved)
  - I-C (Compatible External): [count]
  - I-D (Counter-Evidence External): [count]

### Positional Tally (This Study)

| Tier | Harmony | Contradiction | Neutral | Total |
|------|---------|---------------|---------|-------|
| Explicit (E) | [count] | [count] | [count] | [count] |
| Necessary Implication (N) | [count] | [count] | [count] | [count] |
| I-A | [count] | [count] | [count] | [count] |
| I-B | [count] | [count] | [count] | [count] |
| I-C | [count] | [count] | [count] | [count] |
| I-D | [count] | [count] | [count] | [count] |
| **TOTAL** | **[count]** | **[count]** | **[count]** | **[count]** |

---

## What CAN Be Said

**Scripture explicitly states or necessarily implies:**
- [Bullet list — draw ONLY from E and N tier items]
- [Use "Scripture explicitly states..." or "Scripture necessarily implies..."]
- [Include items from ALL positions]

## What CANNOT Be Said

**Not explicitly stated or necessarily implied by Scripture:**
- [Bullet list — claims neither side can make from explicit text alone]
- [Include claims commonly assumed by BOTH sides that are actually inferences]

---

## Conclusion

[Final synthesis paragraphs. Requirements:
- Cite the E/N/I tally counts from this study
- Note I-B tensions and their SIS resolution strength
- Present classification results as data, not advocacy
- Use "the text states," "classified as E-tier," "this is consistent with"
- Do NOT use: "this proves," "this disproves," "genuinely ambiguous,"
  "the strongest argument," "in tension," "requires sustained effort"
- Do not overstate certainty where evidence is inferential
- Cross-reference other pvj-XX studies where relevant]

---
*Study completed: [YYYY-MM-DD]*
*Evidence items registered in D:/bible/bible-studies/pvj-evidence.db*
````

### Template Checklist (verify before declaring CONCLUSION.md complete)

The analysis agent MUST verify all of these are present:

- [ ] `## Study Question` — original question copied verbatim
- [ ] `## Methodology` — methodology file reference + evidence DB note
- [ ] `## Summary Answer` — 2-3 sentence direct answer
- [ ] `## Key Verses` — 6-12 verses with full KJV text
- [ ] `## Evidence Classification` — header present
- [ ] `### 1. Explicit Statements Table` — with Position and Master ID columns
- [ ] `### 2. Necessary Implications Table` — with Position and Master ID columns
- [ ] `### 3. Inferences Table` — with Type, Criteria, and Position columns
- [ ] `### I-B Resolution` subsections — one per I-B item (skip if no I-B items)
- [ ] `## Tally Summary` — counts broken down by tier and position
- [ ] `### Positional Tally (This Study)` — tier x position table
- [ ] `## What CAN Be Said` — bullet list from E and N items only
- [ ] `## What CANNOT Be Said` — bullet list of inference-level claims
- [ ] `## Conclusion` — synthesis citing tally, investigative tone
- [ ] Footer with date and evidence DB confirmation
- [ ] All evidence items registered in `pvj-evidence.db` via Standard Evidence DB Workflow
- [ ] Study registered in `pvj-study.db` via Standard Study DB Workflow
- [ ] `concept_context.py --scope author` run on key verses from BOTH Paul and the Gospels
