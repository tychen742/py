#!/usr/bin/env python3
import json, os
os.chdir('/Users/tychen/workspace/py')

checks = [
    ('chapters/11-testing/1101-exceptions.ipynb', ['## Logging', 'logging.basicConfig', 'safe_sqrt', '## Summary']),
    ('chapters/11-testing/1102-unit-testing.ipynb', ['## pytest', 'test_palindrome', 'pytest.raises']),
    ('chapters/12-oop/1201-oop-design.ipynb', ['@classmethod', 'from_string', '__repr__', '@property', 'total_seconds']),
    ('chapters/12-oop/1202-oop-practice.ipynb', ['super().__init__', 'issubclass', '@dataclass', '## Summary']),
    ('chapters/13-functional/1301-func-prog.ipynb', ['functools', 'reduce', 'partial', 'lru_cache', '## Summary']),
    ('chapters/14-iter-gen/1402-generators.ipynb', ['yield from', 'itertools.count', 'combinations', '## Summary']),
    ('chapters/15-apis/1501-apis.ipynb', ['requests.post', 'Authorization', 'open-meteo', '## Summary']),
]

for path, terms in checks:
    with open(path) as f:
        nb = json.load(f)
    all_text = ' '.join(''.join(c['source']) for c in nb['cells'])
    results = {t: (t in all_text) for t in terms}
    ok = all(results.values())
    status = 'OK' if ok else 'FAIL'
    missing = [t for t, v in results.items() if not v]
    msg = f'{status} {path.split("/")[-1]} ({len(nb["cells"])} cells)'
    if missing:
        msg += f' MISSING: {missing}'
    print(msg)
