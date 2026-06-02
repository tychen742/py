# Chapter Quality Checklist

Use before finalizing any chapter. Adapted from `rubrics/chapter-quality.md` in ai_shared.

## Structure

- [ ] 5 or fewer `##` headings per notebook
- [ ] Sections are well organized and logically sequenced
- [ ] All important topics for this chapter are included
- [ ] No topics that belong in another chapter

## Landing Page (`xx00*.ipynb`)

- [ ] Intro paragraph with 3–5 bullet points of the most essential concepts
- [ ] Embedded video for the most important concept
- [ ] Numbered learning goals (measurable outcomes, no "understand" or "learn about")
- [ ] Chapter table of contents (`{tableofcontents}`)
- [ ] Chapter glossary

## Content Notebooks

- [ ] Opens with a box-drawing section outline
- [ ] Each section has at least one worked example
- [ ] Each `##`/`###` section with essential content has one exercise
- [ ] Exercises use two cells: `thebe-interactive` (question) and `hide-input` (solution)
- [ ] Chapter intro notebook (`CH00-*-intro.ipynb`) has no exercises
- [ ] All code cells run correctly top-to-bottom

## Assignments

- [ ] `assignments/` folder exists with `preview.ipynb`, `homework.ipynb`, `lab.ipynb`
- [ ] All three appear in the Jupyter Book left menu under Assignments

## Prose

- [ ] Second person ("you"), active voice
- [ ] Short paragraphs; breaks at concept boundaries
- [ ] No filler openers
- [ ] No unexplained jargon on first use

## Datasets

- [ ] Simple datasets (fruits, names, nums) used for concept illustration
- [ ] Business/domain datasets used where context benefits the topic
- [ ] Same datasets reused across chapters for consistency
