# ### while loop with else
i = 1
while i < 6:
  print(i, end="")
  i += 1
else:
  print()
  print("i is no longer less than 6")


### 1/3 while
i = 0;
while ( i < 10):
  print(i, end=" ")
  i = i + 1
print()

### 2/3 while with continue
### note the increment before continue; code will pause without it
### you can increment first to avoid this but the logic is different
i = 0;
while (i < 10):
  if i == 5:
    i = i + 1
    continue
  print(i, end=" ") 
  i = i + 1
print()

### 3/3 while with break
i = 0;
while (i < 10):
  if i == 5:
    break
  print(i, end=" ") 
  i = i + 1
print()
