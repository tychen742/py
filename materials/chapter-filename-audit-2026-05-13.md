# Chapter Filename Consistency Audit

Date: 2026-05-13
Scope: `chapters/*` notebook filenames (`*.ipynb`) only.

## Summary

- Chapter 04 was already normalized to contiguous naming (`0400` to `0403`).
- Most chapter folders are internally consistent and contiguous.
- Inconsistencies are concentrated in three folders:
  - `chapters/08-dict-set/`
  - `chapters/09-strings/`
  - `chapters/11-functional/`
- One wrong-prefix file exists in `chapters/12-iter-gen/`.

## Findings by Folder

### `chapters/01-intro`
- Status: OK
- Files: `0100` to `0102` contiguous.

### `chapters/02-basics`
- Status: OK
- Files: `0200` to `0206` contiguous.

### `chapters/03-control-flow`
- Status: OK
- Files: `0300` to `0302` contiguous.

### `chapters/04-functions`
- Status: OK
- Files: `0400` to `0403` contiguous.

### `chapters/05-testing`
- Status: OK
- Files: `0500` to `0502` contiguous.

### `chapters/06-lists`
- Status: OK
- Files: `0600` to `0605` contiguous.

### `chapters/07-tuples`
- Status: OK
- Files: `0700` to `0704` contiguous.

### `chapters/08-dict-set`
- Status: Inconsistent numeric slot usage
- Multiple files share the same prefix bucket:
  - `0801-dict-core-operations.ipynb`
  - `0801-dict-select-topics.ipynb`
  - `0801-dict.ipynb`
  - `0802-creating-sets.ipynb`
  - `0802-set-advanced.ipynb`
  - `0802-set-methods.ipynb`
  - `0802-set-operations.ipynb`
  - `0802-set.ipynb`
- Also has `0803-dict-advanced.ipynb`.

### `chapters/09-strings`
- Status: Inconsistent numeric slot usage
- Multiple files share each slot bucket:
  - `0901-*` appears 6 times
  - `0902-*` appears 5 times
  - `0903-*` appears 5 times
- This prevents simple contiguous ordering by filename alone.

### `chapters/10-oop`
- Status: OK
- Files: `1000` to `1003` contiguous.

### `chapters/11-functional`
- Status: Mixed numbered and non-numbered files
- Numbered:
  - `1100-intro-func-prog.ipynb`
  - `1101-func-prog.ipynb`
  - `1102-func-practice.ipynb`
- Non-numbered (inconsistent with chapter convention):
  - `generics.ipynb`
  - `module-package.ipynb`
  - `test-debug.ipynb`

### `chapters/12-iter-gen`
- Status: Wrong prefix present
- Files:
  - `0701-databases.ipynb` (wrong chapter prefix for folder)
  - `1200-intro-iter-gen.ipynb`
  - `1201-iterators.ipynb`
  - `1202-generators.ipynb`

### `chapters/13-apis`
- Status: OK
- Files: `1300` to `1302` contiguous.

### `chapters/14-abstract-data-structures`
- Status: OK
- Files: `1400` to `1404` contiguous.

### `chapters/15-algorithms`
- Status: OK
- Files: `1500` to `1503` contiguous.

### `chapters/appendices`
- Status: Acceptable, but mixed index families
- Files include `0101-*` and `0200` to `0204`.
- If strict global consistency is required, this folder needs its own numbering policy.

## Recommended Cleanup Order

1. Fix wrong-prefix file first:
   - `chapters/12-iter-gen/0701-databases.ipynb`
2. Normalize `chapters/11-functional/` by either:
   - renaming non-numbered files into `110x-*`, or
   - moving them into `materials/` if archival/support notebooks.
3. Normalize `chapters/08-dict-set/` into contiguous unique indices.
4. Normalize `chapters/09-strings/` into contiguous unique indices.
5. Optionally define and enforce a numbering policy for `chapters/appendices/`.

## Notes

- Generated artifacts in `_build/` were intentionally excluded from source-of-truth audit decisions.
- No renames/moves were applied in this audit step; this report documents findings only.
