import random


class Die:
    # define attributes in the constructor
    def __init__(self, num_sides):
        self.num_sides = num_sides
        # self.value = self.roll()

    def roll(self):
        # self.value = random.randrange(1, self.num_sides + 1)
        # return self.value
        return random.randrange(1, self.num_sides + 1)


def __str__(self):
    return str(self.value)


the_die = Die(6)

for i in range(1):
    # print(the_die, the_die.value)
    print(the_die.roll())
