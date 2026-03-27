# Chapter 15 Materials (APIs)

This checklist is for building and delivering:

- `1500-intro-apis.ipynb`
- `1501-apis.ipynb`
- `1502-api-reliability.ipynb`

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
- Public APIs (httpbin.org for POST/header echo; open-meteo.com for weather GET)

## Notebook Content Targets

Use a two-tier model for one chapter per week:

- **Required core**: must be covered in lecture/lab and assessed
- **Enrichment/project track**: optional, extra credit, or follow-up content

### `1501-apis.ipynb`

- Required core:
  - What APIs are; REST concept; HTTP methods table; status codes table
  - `requests.get()` and `response.json()`; query parameters (`params={}`)
  - Error handling (`raise_for_status`, timeout, `RequestException`)
  - Exercise: Weather API (open-meteo.com)

### `1502-api-reliability.ipynb`

- Required core:
  - `requests.post()` with JSON body (`json={}`)
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
  - Fetch data from a public API; parse and display results
- Homework:
  - Query an API endpoint and store results in a dict or list for analysis
- Grading anchors:
  - Correctness
  - Code clarity and style
  - Understanding shown in comments or docstrings

## Reusable Assets to Prepare

- Shared starter code snippets
- Any datasets or input files needed by exercises
- Solution cells (tagged `hide-input`) for all exercises

## Chapter 15 Delivery Order (Recommended)

1. `1500-intro-apis.ipynb` — Chapter intro; learning goals; chapter flow
2. `1501-apis.ipynb` — REST concepts; `requests.get()`; query parameters; error handling; Weather API exercise
3. `1502-api-reliability.ipynb` — POST requests; auth headers; nested JSON; pagination; retry/backoff; response validation

## Coordination Note

Chapter 15 planning and delivery are scoped to `chapters/15-apis/` only.
