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

# Chapter 9

Strings

*9.0 Intro · 9.1 Strings · 9.2 Regex · 9.3 Text Analysis*

*← → or Space to navigate · F for fullscreen*

---

<!-- _class: section -->

## 9.1 Strings

Methods, comparison, looping, sorting

---

## String Methods

<div class="cols">
<div>

```python
s = "  Hello, World!  "

print(s.strip())          # 'Hello, World!'
print(s.lower())          # '  hello, world!  '
print(s.upper())
print(s.replace("World", "Python"))
print(s.split(", "))      # ['  Hello', 'World!  ']
print(",".join(["a","b","c"])) # 'a,b,c'
```

</div>
<div>

### Testing methods

```python
"hello".startswith("he")   # True
"hello123".isalnum()        # True
"   ".isspace()             # True
"Hello".istitle()           # True

# Check and membership
"ell" in "hello"            # True
"hello".find("ll")          # 2  (-1 if not found)
"hello".count("l")          # 2
```

</div>
</div>

---

## String Comparison & Sorting

<div class="cols">
<div>

Strings compare **lexicographically** using Unicode code points.

```python
print("apple" < "banana")   # True
print("B" < "a")            # True  (uppercase < lowercase)
print(ord("A"), ord("a"))   # 65 97
```

</div>
<div>

### Sorting strings

```python
words = ["banana", "apple", "Cherry", "date"]

# Default: case-sensitive (uppercase first)
print(sorted(words))
# ['Cherry', 'apple', 'banana', 'date']

# Case-insensitive
print(sorted(words, key=str.lower))
# ['apple', 'banana', 'Cherry', 'date']

# By length
print(sorted(words, key=len))
```

</div>
</div>

---

<!-- _class: section -->

## 9.2 Regular Expressions

Pattern matching with the `re` module

---

## `re` Module Basics

<div class="cols">
<div>

| Function | Returns |
|---|---|
| `re.search(pat, s)` | First match object or `None` |
| `re.findall(pat, s)` | List of all matches |
| `re.sub(pat, rep, s)` | String with replacements |
| `re.compile(pat)` | Compiled pattern object |

</div>
<div>

```python
import re

text = "Call 555-1234 or 555-5678 for info."

# Find all phone numbers
phones = re.findall(r"\d{3}-\d{4}", text)
print(phones)   # ['555-1234', '555-5678']

# Replace
clean = re.sub(r"\d{3}-\d{4}", "XXX-XXXX", text)
```

</div>
</div>

---

## Key Regex Patterns

| Pattern | Matches |
|---|---|
| `.` | Any character except newline |
| `\d` | Digit (0–9) · `\D` non-digit |
| `\w` | Word char (letter/digit/`_`) · `\W` non-word |
| `\s` | Whitespace · `\S` non-whitespace |
| `^` / `$` | Start / end of string |
| `*` `+` `?` | 0+, 1+, 0 or 1 occurrences |
| `{n}` `{m,n}` | Exactly n, or m to n occurrences |
| `[abc]` | Any of a, b, c |
| `(...)` | Capturing group |

---

<!-- _class: section -->

## 9.3 Text Analysis

Cleaning, word frequencies, Counter, Markov generation

---

## Word Frequencies & Counter

<div class="cols">
<div>

### Manual approach

```python
word_counter = {}
for word in text.split():
    word = word.strip(".,!?").lower()
    word_counter[word] = word_counter.get(word, 0) + 1

# Sort by frequency
items = sorted(word_counter.items(),
               key=lambda t: t[1], reverse=True)
```

</div>
<div>

### With Counter

```python
from collections import Counter
import re

words = re.findall(r"\b[a-z]+\b", text.lower())
counts = Counter(words)

# Top 5 words
for word, freq in counts.most_common(5):
    print(freq, word, sep="\t")
```

<div class="callout">

`Counter` replaces the manual loop and adds `.most_common()` directly.

</div>

</div>
</div>

---

## Chapter 9 — Quick Reference

| Concept | Key syntax / notes |
|---|---|
| Strip / clean | `.strip()`, `.lower()`, `.replace()` |
| Split / join | `.split(sep)`, `sep.join(seq)` |
| Membership | `"sub" in s`, `.find()`, `.count()` |
| Regex search | `re.search(pattern, string)` |
| Find all | `re.findall(pattern, string)` |
| Substitute | `re.sub(pattern, repl, string)` |
| Compile | `re.compile(pattern)` for reuse |
| Word freq | `Counter(words).most_common(n)` |
| Markov | `{(w1,w2): [w3, ...]}` bigram model |

---

<!-- _class: title -->

# End of Chapter 9

*Next: Chapter 10 — Object-Oriented Programming*

*classes · instances · inheritance · polymorphism*
