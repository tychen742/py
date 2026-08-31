# Chapter 12 Materials (APIs)

This checklist is for building and delivering:

- `1200-apis.ipynb`
- `1201-apis.ipynb`
- `1202-api-reliability.ipynb`

## Must-Have Teaching Materials

- Slide deck or notes covering:
  - HTTP and REST basics (methods, status codes)
  - Using the `requests` library: `get()`, `post()`, `params={}`, `headers={}`, `response.json()`
  - Error handling (`raise_for_status`, timeout, `RequestException`)
  - API key patterns: query param vs. Bearer token header
  - Parsing and navigating nested JSON responses
  - Pagination patterns and response contract validation
  - Rate limiting and retry/backoff strategy
  - Secret management basics (`os.environ`, avoid hardcoding tokens)
- Code examples and demos ready to run in class
- Offline-safe API fixtures for book execution, plus optional live public API examples for class demonstration
- Public APIs for live demos: httpbin.org for POST/header echo; open-meteo.com for weather GET

## Notebook Content Targets

Use a two-tier model for one chapter per week:

- **Required core**: must be covered in lecture/lab and assessed
- **Enrichment/project track**: optional, extra credit, or follow-up content

### `1201-apis.ipynb`

- Required core:
  - What APIs are; REST concept; HTTP methods table; status codes table
  - `requests.get()` pattern and `response.json()` parsing using response-like local fixtures
  - Query parameters (`params={}`) using prepared requests to avoid brittle live calls
  - Error handling (`raise_for_status`, timeout, `RequestException`); weather payload parsing checkpoint

### `1202-api-reliability.ipynb`

- Required core:
  - `requests.post()` pattern with JSON body (`json={}`) using prepared requests
  - Request headers/auth key patterns and secret handling basics
  - Nested JSON parsing; one pagination loop pattern
  - Retry with exponential backoff baseline; response contract validation
  - Exercise: Resilient API Client (core version)
- Enrichment/project track:
  - Compare page-based, cursor-based, and link-based pagination patterns
  - Expand retry logic for status-specific strategies and jitter
  - Extended API-client mini-project with richer validation and logging

## Practice and Assessment Pack

- In-class checks:
  - 2–3 conceptual poll/discussion questions
  - 1–2 "predict the output" questions
- Lab tasks:
  - Parse saved API payloads first; optionally fetch data from a public API during class and display results
- Homework:
  - Build request parameters, parse response payloads, and store results in a dict or list for analysis
- Grading anchors:
  - Correctness
  - Code clarity and style
  - Understanding shown in comments or docstrings

## Reusable Assets to Prepare

- Shared starter code snippets
- Any datasets or input files needed by exercises
- Solution cells (tagged `hide-input`) for all exercises

## Chapter 12 Delivery Order (Recommended)

1. `1200-apis.ipynb` — Chapter intro; learning goals; chapter flow
2. `1201-apis.ipynb` — REST concepts; `requests.get()`; query parameters; error handling; Weather API exercise
3. `1202-api-reliability.ipynb` — POST requests; auth headers; nested JSON; pagination; retry/backoff; response validation

## Coordination Note

Chapter 12 planning and delivery are scoped to `chapters/12-apis/` only.

## Assignments

- `assignments/index.ipynb` — Assignment section landing page
- `assignments/preview.ipynb` — Preview
- `assignments/lab.ipynb` — Lab assignment
- `assignments/homework.ipynb` — Homework questions
