import json
import copy
from pathlib import Path

src_path = Path('chapters/13-functional/1301-func-prog.ipynb')
dst_path = Path('chapters/13-functional/1302-func-practice.ipynb')

with src_path.open() as f:
    nb = json.load(f)

cells = nb['cells']
split_idx = 16  # zero-based, cell 17 starts recursion section

concept_cells = cells[:split_idx]
practice_cells = cells[split_idx:]

has_summary = any(
    c.get('cell_type') == 'markdown' and '## Summary' in ''.join(c.get('source', []))
    for c in concept_cells
)

if not has_summary:
    concept_cells.append(
        {
            'cell_type': 'markdown',
            'metadata': {'language': 'markdown'},
            'source': [
                '## Summary\n',
                '\n',
                '- Decorators introduce reusable behavior around functions.\n',
                '- Comprehensions and lambda or map or filter provide concise transformation patterns.\n',
                '- Choose the style that keeps code readable for your team.\n',
                '\n',
                'Next: hands-on functional practice with recursion, context managers, and functools.\n',
            ],
        }
    )

nb_concept = copy.deepcopy(nb)
nb_concept['cells'] = concept_cells

practice_intro = {
    'cell_type': 'markdown',
    'metadata': {'language': 'markdown'},
    'source': [
        '# Functional Practice\n',
        '\n',
        'This notebook focuses on applied functional techniques: recursion, context managers,\n',
        'and functools patterns that you can use in larger programs.\n',
    ],
}

nb_practice = copy.deepcopy(nb)
nb_practice['cells'] = [practice_intro] + practice_cells

with src_path.open('w') as f:
    json.dump(nb_concept, f, indent=1, ensure_ascii=False)

with dst_path.open('w') as f:
    json.dump(nb_practice, f, indent=1, ensure_ascii=False)

print(f'Updated {src_path}: {len(concept_cells)} cells')
print(f'Created {dst_path}: {len(nb_practice["cells"])} cells')
