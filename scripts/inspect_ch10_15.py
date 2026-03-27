import json

notebooks = [
    'chapters/10-algorithms/1001-algorithms.ipynb',
    'chapters/10-algorithms/1002-searching.ipynb',
    'chapters/10-algorithms/1003-sorting.ipynb',
    'chapters/11-testing/1101-exceptions.ipynb',
    'chapters/11-testing/1102-unit-testing.ipynb',
    'chapters/12-oop/1201-oop-design.ipynb',
    'chapters/12-oop/1202-oop-practice.ipynb',
    'chapters/13-functional/1301-func-prog.ipynb',
    'chapters/14-iter-gen/1401-iterators.ipynb',
    'chapters/14-iter-gen/1402-generators.ipynb',
    'chapters/15-apis/1501-apis.ipynb',
    'chapters/15-apis/1502-api-reliability.ipynb',
]

for path in notebooks:
    with open(path) as f:
        nb = json.load(f)
    cells = nb['cells']
    total = len(cells)
    code_count = sum(1 for c in cells if c['cell_type'] == 'code')
    md_count = total - code_count
    headings = []
    for c in cells:
        if c['cell_type'] == 'markdown':
            src = ''.join(c['source'])
            for line in src.split('\n'):
                line = line.rstrip()
                if line.startswith('#'):
                    headings.append(line)
    print(f'\n{path}')
    print(f'  Cells: {total} ({code_count} code, {md_count} markdown)')
    for h in headings:
        print(f'    {h}')
