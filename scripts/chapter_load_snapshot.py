import json
from pathlib import Path

chapters = {
    "CH10": [
        "chapters/10-algorithms/1000-intro-algorithms.ipynb",
        "chapters/10-algorithms/1001-algorithms.ipynb",
        "chapters/10-algorithms/1002-searching.ipynb",
        "chapters/10-algorithms/1003-sorting.ipynb",
    ],
    "CH11": [
        "chapters/11-testing/1100-exception-testing.ipynb",
        "chapters/11-testing/1101-exceptions.ipynb",
        "chapters/11-testing/1102-unit-testing.ipynb",
    ],
    "CH12": [
        "chapters/12-oop/1200-intro-oop.ipynb",
        "chapters/12-oop/1201-oop-design.ipynb",
        "chapters/12-oop/1201b-oop-objects.ipynb",
        "chapters/12-oop/1202-oop-practice.ipynb",
    ],
    "CH13": [
        "chapters/13-functional/1300-intro-func-prog.ipynb",
        "chapters/13-functional/1301-func-prog.ipynb",
    ],
    "CH14": [
        "chapters/14-iter-gen/1400-intro-iter-gen.ipynb",
        "chapters/14-iter-gen/1401-iterators.ipynb",
        "chapters/14-iter-gen/1402-generators.ipynb",
    ],
    "CH15": [
        "chapters/15-apis/1500-intro-apis.ipynb",
        "chapters/15-apis/1501-apis.ipynb",
        "chapters/15-apis/1502-api-reliability.ipynb",
    ],
}

for ch, files in chapters.items():
    print(f"\n=== {ch} ===")
    ch_total = 0
    for path in files:
        p = Path(path)
        if not p.exists():
            print(f"{path}: MISSING")
            continue
        with p.open() as f:
            nb = json.load(f)
        cells = nb.get("cells", [])
        code = sum(1 for c in cells if c.get("cell_type") == "code")
        md = sum(1 for c in cells if c.get("cell_type") == "markdown")
        h2 = 0
        for c in cells:
            if c.get("cell_type") == "markdown":
                src = "".join(c.get("source", []))
                for line in src.split("\n"):
                    if line.startswith("## "):
                        h2 += 1
        ch_total += len(cells)
        print(f"{path}: cells={len(cells)} code={code} md={md} h2={h2}")
    print(f"{ch} total cells: {ch_total}")
