# Concatenation and repetition

fruit = ["apple", "orange", "banana", "cherry"]

print([1, 2] + [3, 4])

print(fruit + [6, 7, 8, 9])

print([0] * 4)
print([1, 2, ["hello", "goodbye"]] * 2)  ### The nested list will be printed with [] and ''
print([1, 2, ['hello', 'goodbye']] * 2)

### Concatenation creates new lists with elements combined, not lists combined
