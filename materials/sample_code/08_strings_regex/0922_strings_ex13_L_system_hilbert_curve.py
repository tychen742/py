import turtle


# L
# L -> +RF-LFL-FR+
# R -> -LF+RFR+FL-
# Save & Run

# The Hilbert Curve can be expressed by a rewrite system (L-system).
# Alphabet : A, B
# Constants : F + −
# Axiom : A
# Production rules:
# A → − B F + A F A + F B −
# B → + A F − B F B − F A +
# Here, "F" means "draw forward", "−" means "turn left 90°", "+" means "turn right 90°"
# (see turtle graphics), and "A" and "B" are ignored during drawing.

def applyRules(character):
    # new_string = ""
    if character == "L":
        new_string = "+RF-LFL-FR+"
    elif character == "R":
        new_string = "-LF+RFR+FL-"
    else:
        new_string = character
    return new_string


# Variable as Parameter
def draw_L_system(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        # elif cmd == 'B':
        #     aTurtle.backward(distance)
        # elif cmd == "":
        #     aTurtle.left(angle)
        # elif cmd == "R"
        #     aTurtle.right(angle)

        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)


def process_string(old_string):
    new_str = ""
    for chr in old_string:  # 1st, this is F
        # applyRules(axiom)
        new_str = new_str + applyRules(chr)  # chr == f here; add up the transformation result of every rule
    print(new_str)
    return new_str


def create_system(num_iteration, axiom):
    start_string = axiom
    # end_string = ""
    for i in range(num_iteration):
        end_string = process_string(start_string)
        start_string = end_string  # iteration here. start_string updates itself for process_string()
    return start_string


# print(create_system(10, "A"))

def main():
    inst = create_system(6, "L")  # create the new string
    print(inst)
    t = turtle.Turtle()  # create the turtle
    wn = turtle.Screen()

    t.up()
    t.back(200)
    t.down()
    t.speed(10000)
    draw_L_system(t, inst, 90, 4)  # draw the picture; inst is the long new string
    # turtle, instructions, angle, segment length 5
    wn.exitonclick()


# print (create_system(5, "F"))

main()
