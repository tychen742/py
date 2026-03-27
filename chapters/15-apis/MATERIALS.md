# Chapter 15 Materials (APIs)

This checklist is for building and delivering:

- `1500-intro-apis.ipynb`
- `1501-apis.ipynb`

## Must-Have Teaching Materials

- Slide deck or notes covering:
  - HTTP and REST basics (methods, status codes)
  - Using the `requests` library: `get()`, `post()`, `params={}`, `headers={}`, `response.json()`
  - Error handling (`raise_for_status`, timeout, `RequestException`)
  - API key patterns: query param vs. Bearer token header
  - Parsing and navigating nested JSON responses
- Code examples and demos ready to run in class
- Public APIs (httpbin.org for POST/header echo; open-meteo.com for weather GET)

## Notebook Content Targets

### `1501-apis.ipynb`

- What APIs are; REST concept; HTTP methods table; status codes table;
  `requests.get()` and `response.json()`; query parameters (`params={}`);
  error handling (`raise_for_status`, timeout, `RequestException`);
  `requests.post()` with JSON body (`json={}`);
  request headers (`headers={}`) and API key patterns (Bearer token, `X-API-Key`);
  navigating nested JSON (chained `[]`, `.get()` for safe access)
- Exercises: Weather API (open-meteo.com); Working with APIs (POST + nested JSON)

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
2. `1501-apis.ipynb` — REST concepts; `requests.get()` and `requests.post()`; headers; error handling; nested JSON; Weather API and POST exercises

## Coordination Note

Chapter 15 planning and delivery are scoped to `chapters/15-apis/` only.
