import json

path = '/Users/tychen/workspace/py/chapters/01-intro/0100-py-intro.ipynb'
nb = json.load(open(path))

changes = []

def convert_line(line):
    stripped = line.rstrip('\n')
    nl = '\n' if line.endswith('\n') else ''
    if stripped.startswith('#### '):
        text = stripped[5:].strip()
        return f'<h4>{text}</h4>{nl}'
    elif stripped.startswith('### '):
        text = stripped[4:].strip()
        return f'<h3>{text}</h3>{nl}'
    return line

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] != 'markdown':
        continue
    new_source = []
    changed = False
    for line in cell['source']:
        new_line = convert_line(line)
        if new_line != line:
            changes.append((i+1, repr(line), repr(new_line)))
            changed = True
        new_source.append(new_line)
    if changed:
        cell['source'] = new_source

print("Changes made:")
for cell_num, old, new in changes:
    print(f"  Cell {cell_num}:")
    print(f"    - {old}")
    print(f"    + {new}")

with open(path, 'w') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
    f.write('\n')
print("\nFile saved.")
