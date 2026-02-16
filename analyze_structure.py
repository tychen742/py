import json

with open('/Users/tychen/workspace/py/chapters/05-data-structures/0501-list.ipynb', 'r') as f:
    notebook = json.load(f)

# Build structure
structure = []
for i, cell in enumerate(notebook['cells']):
    if cell.get('source'):
        source = ''.join(cell['source'])
        first_line = source.split('\n')[0] if source else ''
        
        # Track markdown section headers (###)
        if cell['cell_type'] == 'markdown' and first_line.startswith('###'):
            structure.append({
                'type': 'section',
                'index': i,
                'title': first_line.strip()
            })
        
        # Track code exercises
        elif '### EXERCISE' in source:
            structure.append({
                'type': 'exercise',
                'index': i,
                'title': first_line.strip()[:60]
            })
        
        # Track other code cells with content
        elif cell['cell_type'] == 'code' and source.strip() and '# Solution' not in source:
            structure.append({
                'type': 'code',
                'index': i
            })
        
        # Track markdown with content
        elif cell['cell_type'] == 'markdown' and source.strip():
            structure.append({
                'type': 'markdown',
                'index': i
            })

# Analyze structure - find exercises that have  content after them in the same section
print("STRUCTURE ANALYSIS:")
print("=" * 90)

for i, item in enumerate(structure):
    if item['type'] == 'exercise':
        # Find the current section
        current_section = None
        for j in range(i - 1, -1, -1):
            if structure[j]['type'] == 'section':
                current_section = structure[j]
                break
        
        # Find next section
        next_section_index = None
        for j in range(i + 1, len(structure)):
            if structure[j]['type'] == 'section':
                next_section_index = j
                break
        
        # Check if there's content between this exercise and next section
        has_content_after = False
        content_items = []
        
        end_index = next_section_index if next_section_index else len(structure)
        for j in range(i + 1, end_index):
            # Skip solutions (next item after exercise)
            if j == i + 1:
                continue
            if structure[j]['type'] in ['code', 'markdown']:
                has_content_after = True
                content_items.append(str(structure[j]['index']))
        
        section_name = current_section['title'] if current_section else "No section"
        
        if has_content_after:
            print(f"\n❌ NEEDS MOVING:")
            print(f"   Section: {section_name}")
            print(f"   Exercise (cell {item['index']}): {item['title']}")
            print(f"   Content after exercise at cells: {', '.join(content_items[:5])}")
        else:
            print(f"\n✓ OK: {item['title'][:50]}")

print("\n" + "=" * 90)
