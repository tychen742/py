# Chapter 15 Organization (APIs)

This chapter is split into:

- `1500-intro-apis.ipynb`
- `1501-apis.ipynb`
- `1502-api-reliability.ipynb`

## Scope and Sequencing

Use this sequence to avoid overlap and keep pacing clear:

1. `1500-intro-apis.ipynb`
   - Chapter title; learning goals; chapter flow (tableofcontents)

2. `1501-apis.ipynb`
   - What APIs are; HTTP methods and status codes; `requests.get()` and `response.json()`;
     query parameters (`params={}`);
     error handling (`raise_for_status`, timeout, `RequestException`);
     Weather API exercise

3. `1502-api-reliability.ipynb`
   - `requests.post()` with JSON body (`json={}`);
     request headers (`headers={}`) and API key patterns (Bearer token, `X-API-Key`);
     navigating nested JSON (chained `[]` subscripts, `.get()` for safe access);
     authentication workflow and secret handling with environment variables;
     pagination patterns (page-based, cursor-based, link-based);
     retry with exponential backoff for transient failures;
     response contract validation and defensive parsing;
     resilient API client exercise

## One-Week Delivery Scope (Required vs Enrichment)

### Required Core (in-class + required homework)

- `1500-intro-apis.ipynb`
   - Full notebook
- `1501-apis.ipynb`
   - API fundamentals, HTTP methods/status, `requests.get()`, `params={}`
   - Error handling basics (`raise_for_status`, timeout, `RequestException`)
   - Weather API exercise
- `1502-api-reliability.ipynb`
   - POST with JSON payloads, headers/auth pattern overview
   - Nested JSON parsing, one pagination pattern, retry/backoff baseline
   - Response validation basics and resilient-client checkpoint exercise

### Enrichment / Project Track (optional, extra credit, or follow-up week)

- `1502-api-reliability.ipynb`
   - Multiple pagination styles (page/cursor/link) in one comparative lab
   - Advanced retry policy tuning and rate-limit handling strategies
   - Extended production-style API client mini-project

## File Roles

- `1500-intro-apis.ipynb`: Chapter title; learning goals; brief motivation; chapter flow (`{tableofcontents}`).
- `1501-apis.ipynb`: REST API concepts and fundamentals; `requests.get()`; query parameters; error handling. Exercise: Weather API.
- `1502-api-reliability.ipynb`: POST requests; headers and API key patterns; nested JSON navigation; pagination; retries/backoff; response validation. Exercise: Resilient API Client.
- `MATERIALS.md`: teaching/assessment assets and prep checklist.

## Source of Truth

Use `chapters/15-apis/*` as the only Chapter 15 track for planning, delivery, and assessment.

## Build/Quality Checklist

- Keep each notebook executable top-to-bottom.
- Keep function definitions in chapter notebooks self-contained.
- Add at least one checkpoint exercise per major section.
- Ensure chapter outcomes align with any Chapter 15 assignment/quiz prompt.
- Tag question cells `thebe-interactive` and solution cells `hide-input`.
