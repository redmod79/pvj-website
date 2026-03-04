# Bible Study: James vs Paul: Does James Represent Jesus Against Paul? (pvj-08)

## Question
Does James contradict Paul, and does James represent Jesus's position against Paul? James 2:14-26 says "faith without works is dead" and "by works a man is justified" (James 2:24), while Paul says "justified by faith without the deeds of the law" (Romans 3:28). Both use Abraham as their example — Paul says Abraham was justified by faith (Romans 4:2-3, citing Genesis 15:6) while James says Abraham was justified by works when he offered Isaac (James 2:21, citing Genesis 22). Are they using "justified" (dikaioo G1344) the same way? Are they using "faith" the same way? James describes faith that is alone, without action (James 2:19 "the devils also believe and tremble") — is this the same "faith" Paul means? James was Jesus's brother (Galatians 1:19) — does his position carry special weight as representing Jesus's own teaching?

## Discovered Scope

### Topics Found (from naves_semantic.py)
| Topic | Score | Key Verse References |
|-------|-------|---------------------|
| FAITH | 0.51 | GEN 15:6; ROM 3:22-28; GAL 2:16; 3:6-9; JAS 2:20-23,26; HEB 11:8,17-19 |
| JAMES | 0.44 | MAT 13:55; GAL 1:19; 2:9,12; ACT 15:13-21; 21:18-19; JAS 1:1 |
| JUSTIFICATION | 0.39 | GEN 15:6; ROM 2:13; 3:21-28; 4:3-25; GAL 2:14-21; 3:6-24; JAS 2:20-23,26 |
| PAUL | 0.40 | ROM 11:1; GAL 1:13-19; ACT 15:1-2; PHP 3:5 |

### Verse References (consolidated unique)
James 2:14-26 (full passage), Romans 3:20-31, Romans 4:1-9, Galatians 2:16, Galatians 3:6-9, Genesis 15:6, Genesis 22:1-19, Hebrews 11:8-9,17-19, Galatians 1:19, Galatians 2:9,12, Acts 15:13-21, Acts 21:18-19, Matthew 7:21-23, Matthew 25:34-46, John 6:29, Galatians 5:6, Ephesians 2:8-10, James 1:1

### Strong's Numbers Found
| Strong's | Word | Relevance |
|----------|------|-----------|
| G1344 | dikaioo (justify) | Central verb — used by BOTH James and Paul |
| G4102 | pistis (faith) | Used by both authors — question is whether same sense |
| G2041 | ergon (works) | Used by both authors — question of scope |
| G3551 | nomos (law) | Paul uses erga nomou; James does not use nomos in ch.2 |
| G1343 | dikaiosyne (righteousness) | Both cite Gen 15:6 — "counted for righteousness" |
| G1347 | dikaiosis (justification) | Related forensic term in Paul |
| G3049 | logizomai (count/reckon) | Both cite Gen 15:6 — "counted unto him" |

### Related Existing Studies
| Study | Question | Relevance |
|-------|----------|-----------|
| pvj-04-greek-terms-baseline | Greek vocabulary comparison | Established Paul's semantic range is superset of Jesus's for pistis, ergon, dikaiosyne |
| pvj-05-faith-works-definitions | What do faith and works mean in Paul vs Jesus | Established Paul uses erga nomou, Jesus uses poieo thelema; James 2:24 already registered as E074 |
| pvj-06-paul-faith-apart-works | Paul's full argument in Romans 3-4 | Established Paul's basis-vs-fruit distinction (Eph 2:8-10); Abraham example in Rom 4 |
| pvj-07-jesus-keep-commandments | Jesus's commandment-keeping teaching | Established Jesus's internal qualifications (Mat 19:26, Jhn 6:29) |

Key finding from pvj-05: James 2:24 (E074) and James 2:17 (E075) already registered as Neutral in evidence DB.

### Focus Areas
1. Do James and Paul use dikaioo (G1344) with the same meaning?
   - James: edikaiōthē (aorist passive) in 2:21 — Abraham was justified by works
   - Paul: dikaiousthai (present passive infinitive) in Rom 3:28 — justified by faith
   - James: dikaioutai (present passive indicative) in 2:24 — a man is justified by works
   - Paul: edikaiōthē (aorist passive) in Rom 4:2 — IF Abraham were justified by works
2. Do they use pistis (G4102) with the same meaning?
   - James 2:19: "the devils also believe and tremble" — bare intellectual assent
   - Paul: "faith which worketh by love" (Gal 5:6) — active, operative faith
3. The Abraham test case: Gen 15:6 (believing) vs Gen 22 (offering Isaac)
   - Chronological gap: Gen 15:6 precedes Gen 22 by decades
   - James 2:22: "faith wrought with his works, and by works was faith made perfect"
   - James 2:23: "And the scripture was fulfilled which saith, Abraham believed God"
4. James as Jesus's brother: Does his authority trump Paul?
   - Galatians 1:19: James the Lord's brother
   - Galatians 2:9: James, Cephas, John = pillars
   - Acts 15:13-21: James's speech at Jerusalem Council — agrees with Paul's Gentile mission
   - Acts 21:18-19: James receives Paul warmly

## Research Instructions
- Retrieve all James 2:14-26 verse text
- Retrieve Romans 3:20-31, Romans 4:1-9
- Retrieve Genesis 15:6 and Genesis 22:1-12
- Retrieve Galatians 3:6-9, Hebrews 11:17-19
- Parse James 2:21, 2:24 and Romans 3:28, 4:2 for dikaioo forms
- Run concept_context.py --scope author for James 2:24, Romans 3:28, Galatians 5:6, Matthew 7:21
- Retrieve James-Paul relationship verses (Gal 1:19, 2:9, Acts 15, Acts 21)
- Cross-reference with pvj-05 (E074, E075) and pvj-06 findings

## Workflow
answer-question

---
*Scoped: 2026-03-03*
*Folder: bible-studies/pvj-08-james-faith-without-works/*
