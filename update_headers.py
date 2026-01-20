import json
import pathlib

path = pathlib.Path('/Users/tcn85/workspace/py/chapters/ch06-lists-tuples.ipynb')
data = json.loads(path.read_text())
before_exercises = True
allowed_h2 = {'lists', 'tuples'}
changed = False
hashes3 = '#' * 3

for cell in data['cells']:
    if cell.get('cell_type') != 'markdown':
        continue
    new_source = []
    for line in cell.get('source', []):
        stripped = line.lstrip()
        leading_ws = line[:len(line) - len(stripped)]
        if stripped.startswith('#'):
            hashes = 0
            for ch in stripped:
                if ch == '#':
                    hashes += 1
                else:
                    break
            rest = stripped[hashes:]
            heading_text = rest.strip()
            if before_exercises and heading_text.lower() == 'exercises':
                before_exercises = False
            if before_exercises and hashes == 2 and heading_text.lower() not in allowed_h2:
                stripped = hashes3 + rest
                line = l          +                                 line = l          +                                 line = l    _s                line = l          ys                line =de                line = l       da              
