#!/usr/bin/env python3
"""
build_site.py — Build the "Does Paul Contradict Jesus?" study series website.

Scans D:/bible/bible-studies/pvj-* for all 22 studies,
copies files into docs/studies/, generates mkdocs.yml and index.md,
and copies shared assets from etc-website.
"""

import json
import os
import re
import shutil
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent
STUDIES_SRC = Path("D:/bible/bible-studies")
ETC_WEBSITE = Path("D:/bible/etc-website")
DOCS = PROJECT_ROOT / "docs"
DOCS_STUDIES = DOCS / "studies"

# ── Study metadata ─────────────────────────────────────────────────
SHORT_TITLES = {
    "pvj-01": "Does Paul Know Jesus's Teachings?",
    "pvj-02": "Paul's Authority and Apostleship",
    "pvj-03": "Jesus's Audience vs Paul's Audience",
    "pvj-04": "Greek Terms Baseline",
    "pvj-05": "Faith and Works Definitions",
    "pvj-06": "Paul: Faith Apart from Works",
    "pvj-07": "Jesus: Keep the Commandments",
    "pvj-08": "James vs Paul: Faith Without Works",
    "pvj-09": "Not Under Law vs Not to Destroy",
    "pvj-10": "Schoolmaster vs Jot and Tittle",
    "pvj-11": "Food Laws: Clean and Unclean",
    "pvj-12": "Circumcision",
    "pvj-13": "Christ the Telos of the Law",
    "pvj-14": "Women: Silence vs Jesus's Practice",
    "pvj-15": "Gentile Mission",
    "pvj-16": "Marriage and Celibacy",
    "pvj-17": "All Things Lawful vs Sermon on Mount",
    "pvj-18": "Government Submission",
    "pvj-19": "Eschatology and Imminent Return",
    "pvj-20": "Where Paul Agrees with Jesus",
    "pvj-21": "Patterns Across All Contradictions",
    "pvj-22": "Comprehensive Verdict",
}

FULL_TITLES = {
    "pvj-01": "Does Paul know Jesus's teachings? How often does Paul quote or allude to Jesus directly?",
    "pvj-02": "What is Paul's claimed relationship to Jesus and the other apostles?",
    "pvj-03": "Who was Jesus speaking to and who was Paul writing to? How do audience differences affect the contradiction claim?",
    "pvj-04": "Do Paul and Jesus use the same Greek vocabulary for key theological concepts?",
    "pvj-05": 'What do "faith" and "works" mean in Paul compared to Jesus?',
    "pvj-06": 'What does Paul mean by "justified by faith apart from works of the law" (Romans 3:28)?',
    "pvj-07": 'What does Jesus mean by "keep the commandments" and "do the will of my Father"?',
    "pvj-08": "Does James contradict Paul, and does James represent Jesus's position against Paul?",
    "pvj-09": '"Not under the law" vs "I came not to destroy the law" -- is Paul abolishing what Jesus preserved?',
    "pvj-10": '"No longer under a schoolmaster" vs "one jot shall not pass" -- what ended and what endures?',
    "pvj-11": '"Nothing is unclean of itself" vs Mark 7:19 and Acts 10:14 -- did Jesus or Paul abolish food laws?',
    "pvj-12": '"If circumcised, Christ profits nothing" vs Jesus\'s silence on circumcision',
    "pvj-13": '"Christ is the end (telos) of the law" -- does telos mean termination or goal?',
    "pvj-14": '"Let women keep silence" vs Jesus freely teaching women and choosing female witnesses',
    "pvj-15": '"Lost sheep of Israel" vs "apostle to the Gentiles" -- did Paul contradict Jesus\'s mission focus?',
    "pvj-16": "Paul's celibacy preference vs Jesus on marriage -- does Paul contradict Jesus?",
    "pvj-17": '"All things are lawful" vs the Sermon on the Mount -- is Paul loosening what Jesus tightened?',
    "pvj-18": '"Subject to higher powers" vs Jesus confronting authorities -- submission or resistance?',
    "pvj-19": '"We shall not all sleep" vs "no man knows the day" -- did Paul predict an imminent return?',
    "pvj-20": "Compiling all areas where Paul explicitly agrees with Jesus's teaching",
    "pvj-21": "What patterns emerge across all the alleged contradictions between Paul and Jesus?",
    "pvj-22": "Final verdict: Does Paul contradict Jesus? Assessment of all 15 alleged contradictions.",
}

# Phase groupings (instead of Tiers)
PHASES = [
    {
        "name": "Phase 1 -- Foundations",
        "desc": "Establishing the baseline: Does Paul know Jesus? What authority does he claim? Who are they each speaking to? Do they share the same vocabulary?",
        "studies": ["pvj-01", "pvj-02", "pvj-03", "pvj-04"],
    },
    {
        "name": "Phase 2 -- Faith, Works, and Salvation",
        "desc": "The most commonly alleged contradictions -- faith vs works, Paul vs James, and what Jesus actually taught about commandments.",
        "studies": ["pvj-05", "pvj-06", "pvj-07", "pvj-08"],
    },
    {
        "name": "Phase 3 -- The Law",
        "desc": "Did Paul abolish what Jesus preserved? The law, food laws, circumcision, and the meaning of telos.",
        "studies": ["pvj-09", "pvj-10", "pvj-11", "pvj-12", "pvj-13"],
    },
    {
        "name": "Phase 4 -- Specific Issues",
        "desc": "Women's roles, the Gentile mission, marriage, moral permissiveness, government, and eschatology.",
        "studies": ["pvj-14", "pvj-15", "pvj-16", "pvj-17", "pvj-18", "pvj-19"],
    },
    {
        "name": "Phase 5 -- Synthesis",
        "desc": "Where Paul agrees with Jesus, recurring patterns across all contradictions, and the final verdict.",
        "studies": ["pvj-20", "pvj-21", "pvj-22"],
    },
]

# Standard study files (in display order for nav)
STUDY_FILES = [
    ("CONCLUSION.md", None),           # Landing page (no label = index page)
    ("03-analysis.md", "Analysis"),
    ("02-verses.md", "Verses"),
    ("04-word-studies.md", "Word Studies"),
    ("01-topics.md", "Topics"),
    ("PROMPT.md", "Research Scope"),
]

# Raw data file display names
RAW_DATA_NAMES = {
    "concept-context": "Concept Context",
    "existing-studies": "Existing Studies",
    "greek-parsing": "Greek Parsing",
    "hebrew-parsing": "Hebrew Parsing",
    "naves-topics": "Nave's Topics",
    "parallels": "Cross-Testament Parallels",
    "strongs-lookups": "Strong's Lookups",
    "strongs": "Strong's Lookups",
    "web-research": "Web Research",
    "grammar-references": "Grammar References",
    "evidence-tally": "Evidence Tally",
    "study-db-queries": "Study DB Queries",
}


def get_raw_data_name(filename: str) -> str:
    """Get a display name for a raw-data file."""
    stem = Path(filename).stem
    if stem in RAW_DATA_NAMES:
        return RAW_DATA_NAMES[stem]
    return stem.replace("-", " ").title()


def find_study_folders() -> list[tuple[str, Path]]:
    """Find all pvj-NN-* folders in the studies source directory."""
    folders = []
    for d in sorted(STUDIES_SRC.iterdir()):
        if d.is_dir() and re.match(r"pvj-\d{2}-", d.name):
            slug = d.name
            num = slug.split("-")[1]
            key = f"pvj-{num}"
            folders.append((key, d))
    return folders


def copy_study(key: str, src: Path, preserved_simples: dict):
    """Copy a study folder into docs/studies/."""
    dest = DOCS_STUDIES / src.name
    dest.mkdir(parents=True, exist_ok=True)

    # Copy standard files
    for fname, _ in STUDY_FILES:
        src_file = src / fname
        if src_file.exists():
            shutil.copy2(src_file, dest / fname)

    # Restore preserved conclusion-simple.md, or copy from source
    simple_path = dest / "conclusion-simple.md"
    if src.name in preserved_simples:
        simple_path.write_text(preserved_simples[src.name], encoding="utf-8")
    else:
        simple_src = src / "conclusion-simple.md"
        if simple_src.exists():
            shutil.copy2(simple_src, dest / "conclusion-simple.md")

    # Copy METADATA.yaml if present
    meta = src / "METADATA.yaml"
    if meta.exists():
        shutil.copy2(meta, dest / "METADATA.yaml")

    # Copy raw-data/
    raw_src = src / "raw-data"
    if raw_src.exists() and raw_src.is_dir():
        raw_dest = dest / "raw-data"
        shutil.copytree(raw_src, raw_dest, dirs_exist_ok=True)

    return dest


def build_nav_entry(key: str, slug: str) -> dict:
    """Build a nav entry for one study."""
    num = key.split("-")[1]
    short_title = SHORT_TITLES.get(key, slug)
    nav_title = f"{num} -- {short_title}"

    dest = DOCS_STUDIES / slug
    items = []

    # Landing page: conclusion-simple.md if it exists, else CONCLUSION.md
    simple = dest / "conclusion-simple.md"
    conclusion = dest / "CONCLUSION.md"
    if simple.exists():
        items.append(f"studies/{slug}/conclusion-simple.md")
        if conclusion.exists():
            items.append({"Conclusion": f"studies/{slug}/CONCLUSION.md"})
    elif conclusion.exists():
        items.append(f"studies/{slug}/CONCLUSION.md")

    # Other standard files
    for fname, label in STUDY_FILES:
        if label is None:
            continue
        fpath = dest / fname
        if fpath.exists():
            items.append({label: f"studies/{slug}/{fname}"})

    # Raw data files
    raw_dir = dest / "raw-data"
    if raw_dir.exists() and raw_dir.is_dir():
        raw_items = []
        for f in sorted(raw_dir.iterdir()):
            if f.is_file() and f.suffix == ".md":
                display = get_raw_data_name(f.name)
                raw_items.append({display: f"studies/{slug}/raw-data/{f.name}"})
        if raw_items:
            items.append({"Raw Data": raw_items})

    return {nav_title: items}


def generate_mkdocs_yml(study_folders: list[tuple[str, Path]]):
    """Generate mkdocs.yml."""
    slug_map = {key: src.name for key, src in study_folders}

    lines = []
    lines.append('site_name: "Does Paul Contradict Jesus?"')
    lines.append("site_description: A comprehensive 22-study biblical investigation examining every major alleged contradiction between Paul and Jesus using evidence classification methodology.")
    lines.append("")
    lines.append("theme:")
    lines.append("  name: material")
    lines.append("  palette:")
    lines.append("    - scheme: default")
    lines.append("      primary: deep purple")
    lines.append("      accent: amber")
    lines.append("      toggle:")
    lines.append("        icon: material/brightness-7")
    lines.append("        name: Switch to dark mode")
    lines.append("    - scheme: slate")
    lines.append("      primary: deep purple")
    lines.append("      accent: amber")
    lines.append("      toggle:")
    lines.append("        icon: material/brightness-4")
    lines.append("        name: Switch to light mode")
    lines.append("  features:")
    lines.append("    - navigation.instant")
    lines.append("    - navigation.tracking")
    lines.append("    - navigation.tabs")
    lines.append("    - navigation.sections")
    lines.append("    - navigation.top")
    lines.append("    - navigation.indexes")
    lines.append("    - search.suggest")
    lines.append("    - search.highlight")
    lines.append("    - content.tabs.link")
    lines.append("    - toc.follow")
    lines.append("  font:")
    lines.append("    text: Roboto")
    lines.append("    code: Roboto Mono")
    lines.append("")
    lines.append("plugins:")
    lines.append("  - search")
    lines.append("")
    lines.append("markdown_extensions:")
    lines.append("  - abbr")
    lines.append("  - admonition")
    lines.append("  - attr_list")
    lines.append("  - def_list")
    lines.append("  - footnotes")
    lines.append("  - md_in_html")
    lines.append("  - tables")
    lines.append("  - toc:")
    lines.append("      permalink: true")
    lines.append("  - pymdownx.details")
    lines.append("  - pymdownx.superfences")
    lines.append("  - pymdownx.highlight:")
    lines.append("      anchor_linenums: true")
    lines.append("  - pymdownx.inlinehilite")
    lines.append("  - pymdownx.tabbed:")
    lines.append("      alternate_style: true")
    lines.append("  - pymdownx.tasklist:")
    lines.append("      custom_checkbox: true")
    lines.append("")
    lines.append("extra:")
    lines.append("  social:")
    lines.append("    - icon: fontawesome/solid/book-bible")
    lines.append("      link: /")
    lines.append("")
    lines.append("extra_javascript:")
    lines.append("  - javascripts/verse-popup.js")
    lines.append("  - javascripts/study-breadcrumbs.js")
    lines.append("  - javascripts/external-links.js")
    lines.append("")
    lines.append("extra_css:")
    lines.append("  - stylesheets/extra.css")
    lines.append("")
    lines.append("nav:")
    lines.append("  - Home: index.md")
    lines.append("  - Studies:")
    lines.append("")

    # Study phases nested under "Studies" tab
    for phase in PHASES:
        lines.append(f"    # ── {phase['name']} ──")
        lines.append(f'    - "{phase["name"]}":')
        lines.append("")
        for key in phase["studies"]:
            slug = slug_map.get(key)
            if not slug:
                continue
            nav_entry = build_nav_entry(key, slug)
            for title, items in nav_entry.items():
                lines.append(f'      - "{title}":')
                for item in items:
                    if isinstance(item, str):
                        lines.append(f"        - {item}")
                    elif isinstance(item, dict):
                        for label, val in item.items():
                            if isinstance(val, list):
                                lines.append(f"        - {label}:")
                                for sub in val:
                                    if isinstance(sub, dict):
                                        for slabel, spath in sub.items():
                                            lines.append(f'          - "{slabel}": {spath}')
                                    else:
                                        lines.append(f"          - {sub}")
                            else:
                                lines.append(f"        - {label}: {val}")
        lines.append("")

    lines.append("  - Methodology: methodology.md")
    lines.append('  - "Tools & Process": tools.md')
    lines.append('  - "Master Evidence": master-evidence.md')

    yml_path = PROJECT_ROOT / "mkdocs.yml"
    yml_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  Generated {yml_path}")


def generate_index_md():
    """Generate docs/index.md."""
    content = []

    content.append("# Does Paul Contradict Jesus?")
    content.append("")
    content.append("*A comprehensive 22-study biblical investigation examining every major alleged contradiction between Paul and Jesus -- faith vs works, the law, food laws, circumcision, women's roles, the Gentile mission, and more.*")
    content.append("")
    content.append("---")
    content.append("")
    content.append("## The Question")
    content.append("")
    content.append('Many people claim that Paul contradicts Jesus. Paul says "justified by faith apart from works" while Jesus says "keep the commandments." Paul says "not under the law" while Jesus says "not one jot shall pass from the law." Paul says "let women keep silence" while Jesus freely taught women. Are these genuine contradictions, or do they dissolve when context, audience, vocabulary, and scope are properly accounted for? This series investigates 15 specific alleged contradictions using tool-driven biblical research.')
    content.append("")
    content.append("## The Approach")
    content.append("")
    content.append("Each study is a genuine investigation -- not advocacy for a predetermined conclusion. The agents gathered ALL relevant evidence, presented BOTH the Contradiction and Harmony positions at their strongest, and let the biblical text speak for itself. Evidence was classified into hierarchical tiers:")
    content.append("")
    content.append("- **Explicit (E):** What the text directly says -- a quote or close paraphrase")
    content.append("- **Necessary Implication (N):** What unavoidably follows from explicit statements")
    content.append("- **Inference** (four types):")
    content.append("    - **I-A (Evidence-Extending):** Systematizes E/N items using only the text's own vocabulary")
    content.append("    - **I-B (Competing-Evidence):** Both sides cite E/N support; resolved by Scripture-interprets-Scripture")
    content.append("    - **I-C (Compatible External):** External reasoning that does not contradict E/N")
    content.append("    - **I-D (Counter-Evidence External):** External concepts that require overriding E/N statements")
    content.append("")
    content.append("**Hierarchy:** E > N > I-A > I-B (resolved by SIS) > I-C > I-D")
    content.append("")
    content.append("[**Read the Methodology**](methodology.md){ .md-button }")
    # Link to final verdict
    synth_simple = DOCS_STUDIES / "pvj-22-comprehensive-verdict" / "conclusion-simple.md"
    if synth_simple.exists():
        content.append("[**Skip to the Final Verdict**](studies/pvj-22-comprehensive-verdict/conclusion-simple.md){ .md-button .md-button--primary }")
    else:
        content.append("[**Skip to the Final Verdict**](studies/pvj-22-comprehensive-verdict/CONCLUSION.md){ .md-button .md-button--primary }")
    content.append("")
    content.append("---")
    content.append("")
    content.append("## The 22 Studies")
    content.append("")

    # Generate study tables grouped by phase
    for phase in PHASES:
        content.append(f"### {phase['name']}")
        content.append("")
        content.append(phase["desc"])
        content.append("")
        content.append("| # | Study | Question |")
        content.append("|---|-------|----------|")
        for key in phase["studies"]:
            num = key.split("-")[1]
            short = SHORT_TITLES.get(key, key)
            full = FULL_TITLES.get(key, short)
            slug = None
            for d in sorted(STUDIES_SRC.iterdir()):
                if d.is_dir() and d.name.startswith(f"{key}-"):
                    slug = d.name
                    break
            if slug:
                simple_path = DOCS_STUDIES / slug / "conclusion-simple.md"
                if simple_path.exists():
                    link = f"studies/{slug}/conclusion-simple.md"
                else:
                    link = f"studies/{slug}/CONCLUSION.md"
                content.append(f"| {num} | [{short}]({link}) | {full} |")
            else:
                content.append(f"| {num} | {short} | {full} |")
        content.append("")

    content.append("---")
    content.append("")
    content.append("## What Each Study Contains")
    content.append("")
    content.append("Every study includes multiple layers of research, all accessible through the navigation:")
    content.append("")
    content.append("| File | Contents |")
    content.append("|------|----------|")
    content.append("| **Simple Conclusion** | A plain-language summary of the study's findings -- no technical jargon or evidence tables |")
    content.append("| **Conclusion** | The final evidence classification with Explicit/Necessary Implication/Inference tables, I-B resolutions, tally, and \"What CAN/CANNOT Be Said\" |")
    content.append("| **Analysis** | Verse-by-verse analysis, identified patterns, connections between passages, both-sides arguments |")
    content.append("| **Verses** | Full KJV text for every passage examined, organized thematically |")
    content.append("| **Word Studies** | Hebrew and Greek word studies with Strong's numbers, semantic ranges, and parsing |")
    content.append("| **Topics** | Nave's Topical Bible entries and key research findings |")
    content.append("| **Research Scope** | The original research question and scope that guided the investigation |")
    content.append("| **Raw Data** | Nave's topic output, Strong's lookups, Greek/Hebrew parsing, cross-testament parallels, concept context |")
    content.append("")
    content.append("---")
    content.append("")
    content.append("## Evidence Summary (from Study 22)")
    content.append("")
    content.append("Study 22 synthesized the evidence from Studies 01-21 on the central question of whether Paul contradicts Jesus. The series classified **455 unique evidence items** across 22 studies.")
    content.append("")
    content.append("### Positional Distribution")
    content.append("")
    content.append("| Tier | Harmony | Contradiction | Neutral | Total |")
    content.append("|------|---------|---------------|---------|-------|")
    content.append("| E (Explicit) | 32 | 0 | 249 | 281 |")
    content.append("| N (Necessary Implication) | 11 | 0 | 59 | 70 |")
    content.append("| I-A (Evidence-Extending) | 41 | 3 | 5 | 49 |")
    content.append("| I-B (Competing-Evidence) | 3 | 28 | 1 | 32 |")
    content.append("| I-C (Compatible External) | 4 | 3 | 0 | 7 |")
    content.append("| I-D (Counter-Evidence External) | 1 | 3 | 0 | 4 |")
    content.append("| **Total** | **92** | **37** | **314** | **443** |")
    content.append("")
    content.append("**Not a single explicit statement (E-tier) or necessary implication (N-tier) in the entire 455-item evidence base was classified as supporting contradiction.** All Contradiction-position items exist entirely at the inference level (I-B, I-C, and I-D). Of the 15 alleged contradictions examined:")
    content.append("")
    content.append("- **0** were genuine unresolvable contradictions")
    content.append("- **6** showed genuine tension that was partially (Moderate) resolved")
    content.append("- **7** were fully resolved by context, vocabulary, or audience differences")
    content.append("- **2** were based on proof-texting or misunderstanding (no real contradiction)")
    content.append("")
    synth_simple2 = DOCS_STUDIES / "pvj-22-comprehensive-verdict" / "conclusion-simple.md"
    if synth_simple2.exists():
        content.append("[**Read the Final Verdict**](studies/pvj-22-comprehensive-verdict/conclusion-simple.md){ .md-button .md-button--primary }")
    else:
        content.append("[**Read the Final Verdict**](studies/pvj-22-comprehensive-verdict/CONCLUSION.md){ .md-button .md-button--primary }")

    content.append("")
    content.append("---")
    content.append("")
    # Related Studies — read from shared hub-website/related-studies.json
    links_file = Path("D:/bible/hub-website/related-studies.json")
    if links_file.exists():
        links = json.loads(links_file.read_text(encoding="utf-8"))
        content.append("## Related Studies")
        content.append("")
        content.append("These companion sites use the same tool-driven research methodology:")
        content.append("")
        content.append("| Site | Description |")
        content.append("|------|-------------|")
        for entry in links:
            if entry["id"] == "pvj":
                continue
            content.append(f"| [**{entry['name']}**]({entry['url']}) | {entry['description']} |")

    index_path = DOCS / "index.md"
    index_path.write_text("\n".join(content) + "\n", encoding="utf-8")
    print(f"  Generated {index_path}")


def generate_tools_md():
    """Generate docs/tools.md."""
    content = """# Research Tools & Process

*This page describes the automated research system and investigative methodology that produced the 22 studies in this series.*

---

## Investigative Stance

Each study is produced by an agent that functions as an **investigator, not an advocate.** This distinction governs every step of the process:

- **Gather evidence from all sides.** If a passage is cited by those who argue Paul contradicts Jesus, examine it honestly. If a passage is cited by those who argue the apparent contradiction dissolves, examine it honestly.
- **Present BOTH sides at their strongest.** The Contradiction position and the Harmony position each get their best case presented before the evidence is weighed.
- **Do not assume a conclusion before examining the evidence.** The conclusion emerges FROM the evidence, not the reverse.
- **State what the text says, not opinions about it.** The agent does not use editorial characterizations like "obviously," "clearly proves," or "irrefutable." It states what each passage says and what each interpretive position infers from it.

---

## How the Studies Were Produced

Each study was generated by a multi-agent pipeline, a Claude Code skill that answers Bible questions through tool-driven research. The pipeline ensures that:

- **Scope comes from tools, not training knowledge.** The AI does not decide which verses are relevant based on what it was trained on. Instead, tools search topical dictionaries, concordances, and semantic indexes to discover what Scripture says about the topic.
- **Research and analysis are separated.** The agent that gathers data is not the same agent that draws conclusions. This prevents confirmation bias.
- **Every claim is traceable.** Raw tool output is preserved in each study's `raw-data/` folder, so every finding can be verified against its source.

### The Three-Agent Pipeline

```
Phase 1: Scoping Agent
   | Discovers topics, verses, Strong's numbers, related studies
   | Writes PROMPT.md (the research brief)

Phase 2: Research Agent
   | Reads PROMPT.md
   | Retrieves all verse text, runs parallels, word studies, parsing
   | Runs concept_context.py --scope author on key verses from BOTH Paul and the Gospels
   | Writes 01-topics.md, 02-verses.md, 04-word-studies.md
   | Saves raw tool output to raw-data/

Phase 3: Analysis Agent
   | Reads clean research files
   | Applies the evidence classification methodology
   | Writes 03-analysis.md and CONCLUSION.md
```

**Why three agents instead of one?**

- The **scoping agent** prevents training-knowledge bias. Scope comes from tool discovery, not from what the AI "knows" about theology.
- The **research agent** gets a fresh context window dedicated to data gathering. This maximizes the amount of data it can collect without running out of context.
- The **analysis agent** gets a fresh context window loaded with clean, organized research. This maximizes its capacity for synthesis and careful reasoning.

### Author-Level Comparison

A key requirement for every study in this series: the research agent runs `concept_context.py --scope author` on key verses from **both Paul and the Gospels** to compare how each author uses the same theological concepts. This ensures the analysis accounts for author-level vocabulary patterns rather than assuming the same word means the same thing across different authors.

---

## The Study Files

Each study directory contains these files, produced by the pipeline:

| File | Produced By | Contents |
|------|-------------|----------|
| `PROMPT.md` | Scoping Agent | The research brief: tool-discovered topics, verses, Strong's numbers, related studies, and focus areas |
| `01-topics.md` | Research Agent | Nave's Topical Bible entries with all verse references for each topic |
| `02-verses.md` | Research Agent | Full KJV text for every verse examined, organized thematically |
| `04-word-studies.md` | Research Agent | Strong's concordance data: Hebrew/Greek words, definitions, translation statistics, verse occurrences |
| `raw-data/` | Research Agent | Raw tool output archived by category (Strong's lookups, parsing, parallels, concept context, etc.) |
| `03-analysis.md` | Analysis Agent | Verse-by-verse analysis with full evidence classification applied |
| `CONCLUSION.md` | Analysis Agent | Evidence tables (E/N/I), tally, tally summary, and "What CAN/CANNOT Be Said" |

---

## Data Sources

The tools draw from these primary data sources:

| Source | Description | Size |
|--------|-------------|------|
| **KJV Bible** | Complete King James Version text | 31,102 verses |
| **Nave's Topical Bible** | Orville J. Nave's topical dictionary | 5,319 topics |
| **Strong's Concordance** | James Strong's exhaustive concordance with Hebrew/Greek lexicon | Every word in the KJV mapped to original language |
| **BHSA** (Biblia Hebraica Stuttgartensia Amstelodamensis) | Hebrew Bible linguistic database via Text-Fabric | Full morphological parsing of every Hebrew word |
| **N1904** (Nestle 1904) | Greek New Testament linguistic database via Text-Fabric | Full morphological parsing of every Greek word |
| **Textus Receptus** | Byzantine Greek text tradition | For textual variant comparison |
| **LXX Mapping** | Septuagint translation correspondences | Hebrew-to-Greek word mappings |
| **Sentence embeddings** | Pre-computed semantic vectors | For semantic search across all sources |

---

## Evidence Classification Methodology

The core of the methodology is a three-tier evidence classification system that distinguishes between what Scripture directly states, what necessarily follows from it, and what positions claim it implies.

### The Three Tiers

**E -- Explicit.** "The Bible says X." You can point to a verse that says X. A close paraphrase of the actual words of a specific verse, with no concept, framework, or interpretation added beyond what the words themselves require.

**N -- Necessary Implication.** "The Bible implies X." You can point to verses that, when combined, force X with no alternative. Every reader from any theological position must agree this follows -- no additional reasoning is required.

**I -- Inference.** "A position claims the Bible teaches X." No verse explicitly states X, and no combination of verses necessarily implies X. Something must be added beyond what the text contains.

**Critical rule:** Inferences cannot block explicit statements or necessary implications. If E and N items establish X, the existence of passages that *could be inferred* to teach not-X does not prevent X from being established.

---

### The 4-Type Inference Taxonomy

Inferences are further classified on two dimensions:

|  | Derived from E/N | Not derived from E/N |
|--|--|--|
| **Aligns with E/N** | **I-A** (Evidence-Extending) | **I-C** (Compatible External) |
| **Conflicts with E/N** | **I-B** (Competing-Evidence) | **I-D** (Counter-Evidence External) |

**I-A (Evidence-Extending):** Uses only vocabulary and concepts found in E/N statements. An inference only because it systematizes multiple E/N items into a broader claim. Strongest inference type.

**I-B (Competing-Evidence):** Some E/N statements support it, but other E/N statements appear to contradict it. Genuine textual tension where both sides can cite Scripture. Requires the SIS Resolution Protocol.

**I-C (Compatible External):** Reasoning from outside the text (theological tradition, philosophical framework, historical context) that does not contradict any E/N statement. Supplemental only.

**I-D (Counter-Evidence External):** External concepts that require overriding, redefining, or qualifying E/N statements to be maintained. Weakest inference type.

**Evidence hierarchy:** E > N > I-A > I-B (resolved by SIS) > I-C > I-D

---

### Positional Classification

Evidence items are classified by position (Harmony, Contradiction, or Neutral) based on the same methodology used across the series. **Harmony** means Paul and Jesus are in agreement on this point. **Contradiction** means they are in genuine disagreement. **Neutral** means the item is a factual observation both sides accept.

Items are classified positionally **only when one side must deny the textual observation.** Factual observations that both sides must accept are classified Neutral regardless of which side cites them.

[**Read the Full Methodology**](methodology.md){ .md-button }
"""
    tools_path = DOCS / "tools.md"
    tools_path.write_text(content, encoding="utf-8")
    print(f"  Generated {tools_path}")


def copy_assets():
    """Copy shared assets from etc-website."""
    js_src = ETC_WEBSITE / "docs" / "javascripts"
    js_dest = DOCS / "javascripts"
    js_dest.mkdir(parents=True, exist_ok=True)
    for fname in ["verse-popup.js", "study-breadcrumbs.js", "external-links.js",
                   "verses.json", "strongs.json"]:
        src = js_src / fname
        if src.exists():
            shutil.copy2(src, js_dest / fname)
            print(f"  Copied {fname}")
        else:
            print(f"  WARNING: {src} not found")

    css_src = ETC_WEBSITE / "docs" / "stylesheets" / "extra.css"
    css_dest = DOCS / "stylesheets"
    css_dest.mkdir(parents=True, exist_ok=True)
    if css_src.exists():
        shutil.copy2(css_src, css_dest / "extra.css")
        print(f"  Copied extra.css")

    blb_src = ETC_WEBSITE / "add_blb_links.py"
    if blb_src.exists():
        shutil.copy2(blb_src, PROJECT_ROOT / "add_blb_links.py")
        print(f"  Copied add_blb_links.py")


def copy_methodology():
    """Copy pvj-series-methodology.md to docs/methodology.md."""
    src = STUDIES_SRC / "pvj-series-methodology.md"
    dest = DOCS / "methodology.md"
    if src.exists():
        shutil.copy2(src, dest)
        print(f"  Copied methodology.md")
    else:
        print(f"  WARNING: {src} not found")


def copy_master_evidence():
    """Copy pvj-master-evidence.md to docs/master-evidence.md."""
    src = STUDIES_SRC / "pvj-master-evidence.md"
    dest = DOCS / "master-evidence.md"
    if src.exists():
        shutil.copy2(src, dest)
        print(f"  Copied master-evidence.md")
    else:
        print(f"  WARNING: {src} not found")


def generate_deploy_yml():
    """Generate .github/workflows/deploy.yml."""
    deploy_dir = PROJECT_ROOT / ".github" / "workflows"
    deploy_dir.mkdir(parents=True, exist_ok=True)
    content = """name: Deploy MkDocs to GitHub Pages

on:
  push:
    branches:
      - master

permissions:
  contents: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Configure Git credentials
        run: |
          git config user.email "action@github.com"
          git config user.name "GitHub Actions"

      - uses: actions/setup-python@v5
        with:
          python-version: 3.x

      - name: Cache MkDocs dependencies
        uses: actions/cache@v4
        with:
          key: mkdocs-material-${{ hashFiles('**/requirements.txt') }}
          path: .cache
          restore-keys: mkdocs-material-

      - name: Install MkDocs Material
        run: pip install mkdocs-material

      - name: Deploy to GitHub Pages
        run: mkdocs gh-deploy --force
"""
    (deploy_dir / "deploy.yml").write_text(content, encoding="utf-8")
    print(f"  Generated deploy.yml")


def generate_gitignore():
    """Generate .gitignore."""
    content = """site/
.venv/
__pycache__/
node_modules/
"""
    (PROJECT_ROOT / ".gitignore").write_text(content, encoding="utf-8")
    print(f"  Generated .gitignore")


def generate_readme(study_folders: list[tuple[str, Path]]):
    """Generate README.md."""
    lines = []
    lines.append("# Does Paul Contradict Jesus?")
    lines.append("")
    lines.append("A comprehensive 22-study biblical investigation examining every major alleged contradiction between Paul and Jesus using evidence classification methodology.")
    lines.append("")
    lines.append("## Studies")
    lines.append("")
    lines.append("| # | Study | Question |")
    lines.append("|---|-------|----------|")
    for key, src in study_folders:
        num = key.split("-")[1]
        short = SHORT_TITLES.get(key, key)
        full = FULL_TITLES.get(key, short)
        lines.append(f"| {num} | {short} | {full} |")
    lines.append("")
    lines.append("## Built With")
    lines.append("")
    lines.append("- [MkDocs](https://www.mkdocs.org/) with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)")
    lines.append("- Interactive Bible verse and Strong's number popups")
    lines.append("- Full KJV text and Strong's Concordance data")

    (PROJECT_ROOT / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  Generated README.md")


def main():
    print("=" * 60)
    print("Building 'Does Paul Contradict Jesus?' study website")
    print("=" * 60)

    # Preserve any existing conclusion-simple.md files before cleaning
    preserved_simples = {}
    if DOCS_STUDIES.exists():
        for d in DOCS_STUDIES.iterdir():
            if d.is_dir():
                simple = d / "conclusion-simple.md"
                if simple.exists():
                    preserved_simples[d.name] = simple.read_text(encoding="utf-8")
        shutil.rmtree(DOCS_STUDIES)
    DOCS_STUDIES.mkdir(parents=True)
    print(f"  Preserved {len(preserved_simples)} conclusion-simple.md files")

    # Find all study folders
    print("\n[1/8] Finding study folders...")
    study_folders = find_study_folders()
    print(f"  Found {len(study_folders)} studies")

    # Copy studies
    print("\n[2/8] Copying study files...")
    for key, src in study_folders:
        dest = copy_study(key, src, preserved_simples)
        print(f"  {key}: {src.name} -> {dest.relative_to(PROJECT_ROOT)}")

    # Copy methodology and master evidence
    print("\n[3/8] Copying methodology and master evidence...")
    copy_methodology()
    copy_master_evidence()

    # Copy shared assets
    print("\n[4/8] Copying shared assets from etc-website...")
    copy_assets()

    # Generate mkdocs.yml
    print("\n[5/8] Generating mkdocs.yml...")
    generate_mkdocs_yml(study_folders)

    # Generate index.md
    print("\n[6/8] Generating index.md...")
    generate_index_md()

    # Generate tools.md
    print("\n[7/8] Generating tools.md...")
    generate_tools_md()

    # Generate supporting files
    print("\n[8/8] Generating supporting files...")
    generate_deploy_yml()
    generate_gitignore()
    generate_readme(study_folders)

    print("\n" + "=" * 60)
    print("Build complete!")
    print(f"  Studies: {len(study_folders)}")
    print(f"  Output: {DOCS}")
    print("\nNext steps:")
    print("  1. cd pvj-website && python add_blb_links.py docs/")
    print("  2. python generate_simple_conclusions.py")
    print("  3. python build_site.py  (rebuild after simple conclusions)")
    print("  4. mkdocs serve")
    print("=" * 60)


if __name__ == "__main__":
    main()
