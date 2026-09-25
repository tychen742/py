---
orphan: true
---

# Sync Audit Summary (2026-09-25)

Book-wide run of `audit sync all` (prompt: `~/ai_shared/prompts/audit-sync.md`), one read-only agent per chapter plus the appendices. Each `chNN.md` report ends with a "Top fixes" list. Nine high-stakes findings were verified by hand against the files; all held.

Issue counts depend on how finely each report split its findings, so compare them loosely. Total: 359.

## Urgent (affects students now)

| Where | Problem | Status |
|---|---|---|
| Ch05 homework Q9 | Prompt asks for a "Plan: pro" line that cannot print; grader expects two lines | Fixed 2026-09-25 |
| Ch05 homework Q10 | Input `" q1 revenue "` never given; grader requires exact `Q1 Revenue` | Fixed 2026-09-25 |
| Ch10 10.2, Ch11, Appendix 0503 | Exercise solutions visible (missing `hide-input`); one 11.1 question hidden | Fixed 2026-09-25; a book-wide scan also fixed Ch01 1.1 (2 exercises) and Ch09 9.3 (`namedtuple`) |
| Ch14 14.1 | `binary_search` starts at index 1: skips index 0, can index past the end | Fixed 2026-09-25 (compares `arr[mid - 1]`, as cell 57 does); trace table, output labels, and the decision-tree text (11 levels for 1024 elements) corrected to match |
| Ch02 2.1–2.3 | Container table says `dict` is not mutable; other wrong statements | Fixed 2026-09-25: `dict` mutable, `->` annotation, `str` converts to a string, `%` gives the remainder, precedence table (`^` above `\|`; comparisons, identity, and membership on one level), 2.1 mutability bullets |

## By chapter

| Ch | Issues | Biggest problem |
|---|---|---|
| 01 | 27 | `ord()`/`chr()` used by lab, homework, and slides but never taught; empty object section in 1.2 |
| 02 | 27 | Factual errors in 2.2/2.3; exercises use `for` and `not`/`or` before they are taught |
| 03 | 20 | Accumulator pattern taught only by an exercise, yet homework, lab, glossary, and slides depend on it |
| 04 | 19 | Recursion over a list shown only in an exercise solution; `cache=None` idiom unexplained; stale "Chapter 5" |
| 05 | 26 | Homework grading bugs; nothing assesses 5.2 (pytest, unittest, doctest, mocking) |
| 06 | 20 | Learning goals cover lists only; three stale cross-references |
| 07 | 22 | Nested dicts, `setdefault()`, tuple keys untaught but required by lab and homework; sorting and memoization repeat Ch06/Ch04 |
| 08 | 23 (+4 content errors) | 8.2 uses regex syntax before teaching it; slides cover about 6 of 15 sections; 8.3 barely assessed |
| 09 | 27 | Planning docs describe content that does not exist (card game, `Time`, composition vs. inheritance); homework covers only 9.1 |
| 10 | 28 | Visible solution; lab needs closures, `reduce` start value, tuple sort keys (untaught); `reduce` taught twice |
| 11 | 25 | `itertools.chain` never taught ("already covered" is false); tag problems; pipelines promised but not taught |
| 12 | 26 | Learning goals cover only 12.1; lab uses `json.loads`/`dumps`; `RequestException`/timeouts missing from error handling |
| 13 | 20 | Binary trees, traversals, BSTs promised by docs and slides but absent; `deque` and BFS teaching code hidden |
| 14 | 26 | `binary_search` bug; 14.1 duplicates 14.2 search material; goals cover only 14.1 |
| App | 23 | `__main__` guard taught nowhere; docs misdescribe 0101/0201/0204; 0501 file modes appear only in code |

## Patterns across the book

1. Planning docs: 13 of 14 chapters lack `orphan: true` front matter; most have no exercise lists.
2. Slides: no deck has a learning-goals slide; five decks carry chapter numbers one too high; most cover about a third of their chapter's sections.
3. Assignments depend on material taught only in exercises, or not at all (Ch01, 03, 04, 07, 08, 10, 11, 12).
4. Assessments skip half the chapter (Ch05, 08, 09, 10).
5. Topics taught in several places: memoization (4.3, 7.3, 10.2), sorting (6.2, 7.3), `reduce` (twice in Ch10), search (14.1, 14.2).

## Plan for the patterns

AGENTS.md says "No major changes during the semester," so the order follows mid-semester risk. Start pattern 3 with the chapters students have not reached yet.

| Pattern | What it takes | Mid-semester risk | Suggestion |
|---|---|---|---|
| 1. Planning docs: front matter, exercise lists, section sequences | Front matter and exercise lists can be scripted for every chapter; sequences need judgment (Ch09 describes content that does not exist) | None (author-only files) | Scripted part book-wide now; sequences chapter by chapter from the reports |
| 2. Slides: no learning-goals slides, 5 decks with wrong chapter numbers, about 1/3 coverage | Numbers and goals slides are mechanical (from each landing page), then regenerate the HTML; full coverage means rewriting each deck | Low | Numbers and goals slides for all decks now; full rebuilds later |
| 3. Assignments rely on untaught material | One short text section each: `ord`/`chr` (Ch01), accumulator (Ch03), list recursion (Ch04), nested dicts/`setdefault`/tuple keys (Ch07), `casefold` (Ch08), `reduce` initializer/tuple sort keys (Ch10), `chain`/`islice` (Ch11), `json.loads`/timeouts (Ch12) | Low if done before students reach the chapter (assignments stay the same) | Next, starting with chapters students have not reached |
| 4. Assessments skip half the chapter (Ch05, 08, 09, 10) | New homework/lab items plus grader-key changes in `_html_extra/api/lib/quiz-app.php` | High (changes scores and maximum points mid-semester) | Record the plan in MATERIALS.md now; build between semesters |
| 5. Topics taught in several places | Choose one primary home per topic and link to it from the others | Low, but touches text in several chapters | Record the decisions in the planning docs now; trim the text later |
