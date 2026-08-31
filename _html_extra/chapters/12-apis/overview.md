---
marp: true
theme: default
paginate: true
style: |
  section { font-family: 'Segoe UI', system-ui, sans-serif; font-size: 20px; color: #1a1a1a; padding: 30px 50px 60px 50px; background: white; }
  h1 { color: #2a6b37; font-size: 1.8em; border-bottom: 3px solid #b8860b; padding-bottom: 8px; margin-bottom: 16px; }
  h2 { color: #2a6b37; font-size: 1.35em; margin-bottom: 10px; }
  h3 { color: #b8860b; font-size: 1.05em; margin-bottom: 6px; }
  ul { margin-left: 1.2em; } li { margin-bottom: 4px; line-height: 1.4; }
  section.title { background: #2a6b37; color: white; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center; }
  section.title h1 { color: white; border: none; font-size: 2.2em; }
  section.title p { color: #c8e6c9; }
  section.section { background: #2a6b37; color: white; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center; }
  section.section h2 { color: white; border: none; font-size: 1.9em; }
  section.section p { color: #c8e6c9; }
  .cols { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; align-items: start; }
  .callout { background: #e8f5eb; border-left: 4px solid #2a6b37; border-radius: 4px; padding: 7px 11px; margin: 8px 0; font-size: 0.72em; line-height: 1.35; }
  .callout.warn { background: #fff8e1; border-color: #b8860b; }
  .callout.rule { background: #f0f4ff; border-color: #5577cc; }
  pre { background: #f6f8fa !important; border: 1px solid #d0e8d4; border-radius: 6px; margin: 8px 0; font-size: 0.68em; line-height: 1.35; }
  code { color: #c7254e; background: #f6f8fa; border: 1px solid #e0e0e0; border-radius: 3px; padding: 1px 4px; }
  pre code { color: inherit; background: none; border: none; padding: 12px 14px; }
  table { font-size: 0.68em; border-collapse: collapse; width: 100%; }
  th { background: #2a6b37; color: white; padding: 5px 8px; text-align: left; }
  td { padding: 5px 8px; border-bottom: 1px solid #e0e0e0; }
  tr:nth-child(even) td { background: #f7faf7; }
  section::after { color: #aaa; font-size: 0.7em; }
---

<!-- _class: title -->

# Chapter 12

APIs

*12.0 Intro · 12.1 API Basics · 12.2 API Reliability*

*← → or Space to navigate · F for fullscreen*

---

<!-- _class: section -->

## 12.1 API Basics

HTTP · requests.get() · JSON · query parameters · offline fixtures

---

## What is an API?

<div class="cols">
<div>

An **API** (application programming interface) is a contract that lets programs talk to each other. A REST-style web API uses HTTP endpoints to exchange structured data, often JSON.

| HTTP Method | Action |
|---|---|
| `GET` | Read data |
| `POST` | Create data |
| `PUT` | Replace data |
| `PATCH` | Update part of data |
| `DELETE` | Remove data |

</div>
<div>

### Status codes

| Code | Meaning |
|---|---|
| `200` | OK — success |
| `201` | Created |
| `400` | Bad request |
| `401` | Unauthorized |
| `404` | Not found |
| `429` | Rate limited |
| `500` | Server error |

</div>
</div>

---

## `requests.get()` Pattern and JSON

<div class="cols">
<div>

```python
import requests

url = "https://api.example.test/weather"
params = {"city": "Chicago", "units": "fahrenheit"}

response = requests.get(url, params=params,
                        timeout=10)
response.raise_for_status()   # raise on 4xx/5xx

data = response.json()
print(data["temperature"])
```

</div>
<div>

### Offline-safe fixtures

```python
class DemoResponse:
    def __init__(self, payload, status_code=200):
        self._payload = payload
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(self.status_code)

    def json(self):
        return self._payload

response = DemoResponse({"temperature": 72.5})
```

</div>
</div>

---

<!-- _class: section -->

## 12.2 API Reliability

POST · headers · nested JSON · pagination · retry · validation

---

## Authentication & API Keys

<div class="cols">
<div>

```python
import os

# Store secrets in environment variables — never in code
api_key = os.environ["MY_API_KEY"]

# Bearer token
headers = {"Authorization": f"Bearer {api_key}"}

# X-API-Key header
headers = {"X-API-Key": api_key}

response = requests.get(url, headers=headers,
                        timeout=10)
```

</div>
<div>

### POST with JSON body

```python
payload = {
    "name": "Alice",
    "role": "student",
}

response = requests.post(
    "https://api.example.test/users",
    headers={"Authorization": f"Bearer {api_key}"},
    json=payload,   # auto-encodes and sets Content-Type
    timeout=30,
)
```

</div>
</div>

---

## Nested JSON, Pagination, and Retry

<div class="cols">
<div>

### Defensive parsing

```python
payload = {
    "user": {
        "profile": {"department": "Analytics"}
    }
}

department = (
    payload
    .get("user", {})
    .get("profile", {})
    .get("department", "unknown")
)
```

</div>
<div>

### Exponential backoff retry

```python
import time

def get_with_retry(url, retries=3):
    for attempt in range(retries):
        try:
            r = requests.get(url, timeout=10)
            r.raise_for_status()
            return r.json()
        except requests.RequestException as e:
            if attempt == retries - 1:
                raise
            time.sleep(2 ** attempt)   # 1, 2, 4 s
```

</div>
</div>

---

## Chapter 12 — Quick Reference

| Concept | Key syntax / notes |
|---|---|
| GET request | `requests.get(url, params={}, timeout=10)` |
| POST request | `requests.post(url, json={}, headers={})` |
| Prepared request | `requests.Request(...).prepare()` |
| Raise on error | `.raise_for_status()` |
| Parse JSON | `.json()` → dict/list |
| Safe access | `data.get("key", default)` |
| Auth header | `{"Authorization": f"Bearer {token}"}` |
| API key | Store in `os.environ`, never hard-coded |
| Pagination | Loop until `next_page` or cursor is empty |
| Retry | Exponential backoff with a max retry count |

---

<!-- _class: title -->

# End of Chapter 12

*Next: Chapter 13 — Abstract Data Structures*

*stacks · queues · trees · graphs · ADT interface vs implementation*
