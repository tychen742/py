# Chapter 15 Organization (APIs)

This chapter is currently split into:

- `1500-intro-apis.ipynb`
- `1501-apis.ipynb`

## Scope and Sequencing

Use this sequence to avoid overlap and keep pacing clear:

1. `1500-intro-apis.ipynb`
   - Chapter title; learning goals; chapter flow (tableofcontents)

2. `1501-apis.ipynb`
   - What APIs are; HTTP methods and status codes; `requests.get()` and `response.json()`;
     query parameters (`params={}`);
     error handling (`raise_for_status`, timeout, `RequestException`);
     `requests.post()` with JSON body (`json={}`);
     request headers (`headers={}`) and API key patterns (Bearer token, `X-API-Key`);
     navigating nested JSON (chained `[]` subscripts, `.get()` for safe access);
     2 exercises

## File Roles

- `1500-intro-apis.ipynb`: Chapter title; learning goals; brief motivation; chapter flow (`{tableofcontents}`).
- `1501-apis.ipynb`: REST API concepts; `requests.get()` and `requests.post()`; query parameters; headers and API key patterns; error handling; navigating nested JSON. Exercises: Weather API; Working with APIs (POST + nested JSON).
- `MATERIALS.md`: teaching/assessment assets and prep checklist.

## Source of Truth

Use `chapters/15-apis/*` as the only Chapter 15 track for planning, delivery, and assessment.

## Build/Quality Checklist

- Keep each notebook executable top-to-bottom.
- Keep function definitions in chapter notebooks self-contained.
- Add at least one checkpoint exercise per major section.
- Ensure chapter outcomes align with any Chapter 15 assignment/quiz prompt.
- Tag question cells `thebe-interactive` and solution cells `hide-input`.
