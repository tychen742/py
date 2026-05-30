### LIST Type Conversion
### STRING SPLIT method turns STRING to LIST
song = "The rain in Spain..."
wds = song.split()
print(wds)

### LIST JOIN method turns LIST to STRING with Glue
glue = ";;;;;"
new_string = glue.join(wds)
print(new_string)

list_poem = ["You", "may", "write", "me", "down", "in", "history"]
glue = " "
string_poem = glue.join(list_poem)
print(string_poem)
print(list_poem)  ### the list is not changed by JOIN method

### list type conversion function
xs = list("Crunchy Frog")
print(xs)

glue = ""
new_xs = glue.join(xs)
print(new_xs)

### "list" function can turn sequence into list.
##### sequence: LIST, TUPLE, RANGE, and STRING
