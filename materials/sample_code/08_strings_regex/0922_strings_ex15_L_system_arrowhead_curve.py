import turtle


def create_system(num_iteration, axiom):
    start_string = axiom
    end_string = ""
    for i in range(num_iteration):
        end_string = process_string(start_string)
        start_string = end_string  # iteration here. start_string updates itself for process_string()
    return start_string


def process_string(old_string):
    new_str = ""
    for chr in old_string:  # 1st, this is F
        new_str = new_str + applyRules(chr)  # chr == f here; add up the transformation result of every rule
    return new_str


def applyRules(character):
    new_string = ""
    if character == "X":
        new_string = "YF+XF+Y"
    elif character == "Y":
        new_string = "XF-YF-X"
    else:
        new_string = character
    return new_string


def draw_L_system(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)


def main():
    inst = create_system(5, "YF")  # create the new string
    print(inst)
    t = turtle.Turtle()  # create the turtle
    wn = turtle.Screen()

    t.speed(10000)
    draw_L_system(t, inst, 60, 5)  # draw the picture; inst is the long new string

    wn.exitonclick()


if __name__ == '__main__':
    main()
