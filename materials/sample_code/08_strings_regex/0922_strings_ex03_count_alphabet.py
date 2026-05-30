import string

dicson = '''“Hope” is the thing with feathers -
That perches in the soul -
And sings the tune without the words -
And never stops - at all -

And sweetest - in the Gale - is heard -
And sore must be the storm -
That could abash the little Bird
That kept so many warm -

I’ve heard it in the chillest land -
And on the strangest Sea -
Yet - never - in Extremity,
It asked a crumb - of me.'''


def count_alphabet(text, alphabet):
    num_total = 0
    num_e = 0
    for i in range(len(dicson)):
        if text[1] in string.ascii_letters:
            num_total = num_total + 1

    for i in range(len(dicson)):
        if text[i] == alphabet:
            num_e = num_e + 1
    return num_total, num_e


num_total, num_e = count_alphabet(dicson, "e")

print("Your text contains", num_total, "alphabetic characters, of which", num_e,
      "({:.2%})".format(num_e / num_total), "are 'e'.")
# print ("Your text contains", result , "are 'e'", "e")
