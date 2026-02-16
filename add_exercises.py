import json
import sys

# Load the notebook
with open('/Users/tychen/workspace/py/chapters/05-data-structures/0501-list.ipynb', 'r') as f:
    nb = json.load(f)

# Define exercises for each section
exercises = {
    "### Basic List Creation": {
        "question": """# Exercise: Create Different Types of Lists
# Create the following lists:
# 1. A list called 'colors' with three color names
# 2. An empty list called 'empty_list'
# 3. A list called 'mixed' with a string, an integer, and a float
### Your code starts here:



### Your code ends here.""",
        "solution": """# Solution
colors = ['red', 'blue', 'green']
empty_list = []
mixed = ['hello', 42, 3.14]

print(f"Colors: {colors}")
print(f"Empty list: {empty_list}")
print(f"Mixed list: {mixed}")"""
    },
    "### `list()` Constructor": {
        "question": """# Exercise: Convert Using list() Constructor
# 1. Convert the string "Python" into a list of characters
# 2. Create a list of numbers from 10 to 14 using range() and list()
### Your code starts here:



### Your code ends here.""",
        "solution": """# Solution
chars = list('Python')
numbers = list(range(10, 15))

print(f"Characters: {chars}")
print(f"Numbers: {numbers}")"""
    },
    "### List Comprehension": {
        "question": """# Exercise: List Comprehension Practice
# 1. Create a list of cubes (x^3) for numbers 1 through 5
# 2. Create a list of only odd numbers from 1 to 20
### Your code starts here:



### Your code ends here.""",
        "solution": """# Solution
cubes = [x**3 for x in range(1, 6)]
odds = [x for x in range(1, 21) if x % 2 != 0]

print(f"Cubes: {cubes}")
print(f"Odd numbers: {odds}")"""
    },
    "### Indexing and Slicing": {
        "question": """# Exercise: Indexing and Slicing Practice
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']
# 1. Get the third element (index 2)
# 2. Get the last element using negative indexing
# 3. Get a slice of elements from index 1 to 4 (not including 4)
# 4. Get every other element
### Your code starts here:



### Your code ends here.""",
        "solution": """# Solution
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']
third = fruits[2]
last = fruits[-1]
slice_1_to_4 = fruits[1:4]
every_other = fruits[::2]

print(f"Third element: {third}")
print(f"Last element: {last}")
print(f"Slice [1:4]: {slice_1_to_4}")
print(f"Every other: {every_other}")"""
    },
    "### List Operators": {
        "question": """# Exercise: List Concatenation and Repetition
# 1. Create two lists: list1 = [1, 2, 3] and list2 = [4, 5, 6]
# 2. Concatenate them to create list3
# 3. Create list4 by repeating [0] three times
### Your code starts here:



### Your code ends here.""",
        "solution": """# Solution
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
list4 = [0] * 3

print(f"List1 + List2: {list3}")
print(f"[0] * 3: {list4}")"""
    },
    "### List Methods/Functions": {
        "question": """# Exercise: Using List Methods
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# 1. Append the number 7 to the end
# 2. Remove the first occurrence of 1
# 3. Find the index of the number 5
# 4. Count how many times 1 appears in the original list
### Your code starts here:



### Your code ends here.""",
        "solution": """# Solution
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
count_of_1 = numbers.count(1)  # Do this before removing
numbers.append(7)
numbers.remove(1)
index_of_5 = numbers.index(5)

print(f"After append and remove: {numbers}")
print(f"Index of 5: {index_of_5}")
print(f"Count of 1 in original: {count_of_1}")"""
    }
}

# Find sections and insert exercises
new_cells = []
i = 0
while i < len(nb['cells']):
    cell = nb['cells'][i]
    new_cells.append(cell)
    
    # Check if this is a markdown cell with a section header
    if cell['cell_type'] == 'markdown':
        source = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
        
        # Check each exercise key
        for section_title, exercise_content in exercises.items():
            if section_title in source and source.strip().startswith(section_title):
                # Find the end of this section (next ### or ##)
                j = i + 1
                while j < len(nb['cells']):
                    next_cell = nb['cells'][j]
                    if next_cell['cell_type'] == 'markdown':
                        next_source = ''.join(next_cell['source']) if isinstance(next_cell['source'], list) else next_cell['source']
                        if next_source.strip().startswith('###') or next_source.strip().startswith('##'):
                            # Insert exercise before this next section
                            question_cell = {
                                "cell_type": "code",
                                "metadata": {"tags": ["thebe-interactive"]},
                                "source": exercise_content["question"],
                                "outputs": [],
                                "execution_count": None
                            }
                            solution_cell = {
                                "cell_type": "code",
                                "metadata": {"tags": ["hide-input"]},
                                "source": exercise_content["solution"],
                                "outputs": [],
                                "execution_count": None
                            }
                            # Add remaining cells up to j
                            for k in range(i + 1, j):
                                new_cells.append(nb['cells'][k])
                            # Add exercise cells
                            new_cells.append(question_cell)
                            new_cells.append(solution_cell)
                            # Skip to j
                            i = j - 1
                            break
                    j += 1
                else:
                    # Reached end of notebook, add exercise at the end of section
                    for k in range(i + 1, len(nb['cells'])):
                        new_cells.append(nb['cells'][k])
                    question_cell = {
                        "cell_type": "code",
                        "metadata": {"tags": ["thebe-interactive"]},
                        "source": exercise_content["question"],
                        "outputs": [],
                        "execution_count": None
                    }
                    solution_cell = {
                        "cell_type": "code",
                        "metadata": {"tags": ["hide-input"]},
                        "source": exercise_content["solution"],
                        "outputs": [],
                        "execution_count": None
                    }
                    new_cells.append(question_cell)
                    new_cells.append(solution_cell)
                    i = len(nb['cells'])
                break
    
    i += 1

# Update notebook
nb['cells'] = new_cells

# Save the updated notebook
with open('/Users/tychen/workspace/py/chapters/05-data-structures/0501-list.ipynb', 'w') as f:
    json.dump(nb, f, indent=1)

print("Exercises added successfully!")
