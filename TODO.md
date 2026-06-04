# TODO

This is the notes of the author.

- restructure the whole book.
- is SQL DB needed here?
- projects: midterm and final projects
- data science
- done: combine lists, tuples, and sets into one collections chapter
- strings chapter to include files?
- 3.1 should be control flow
- 2.3 is missing built-in functions?
- APIs chapter is SHORT
- find short videos < 10 minutes for each chapter

Move runnable artifacts out of chapters/. The chapter tree contains .py, .db, .txt, .log, .bak, .DS_Store, checkpoint, and cache files. The project convention says content lives in chapters/, while runnable/source material should live under materials/. High-priority examples: chapters/05-testing/*.py, chapters/12-iter-gen/*.db, and chapters/09-strings/datasss/*.

Update tracking docs. PROGRESS.md (line 21) says chapter 08 has no assignments, but the files and TOC show it does. That tracker is useful, but it is currently out of sync with reality.

Standardize content notebook structure. The quality checklist expects each content notebook to open with a box-drawing outline, include worked examples, include exercises, and end with summary/further reading where appropriate. My scan found most content notebooks do not start with the outline box, and many lack summary/reference sections.

Decide on the open structural questions in TODO.md. The most consequential items are combining lists/tuples, whether strings should absorb files, whether SQL belongs in this book, and expanding short chapter 13. These should be resolved before polishing individual notebooks because they affect chapter boundaries.