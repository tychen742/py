import turtle


def applyRules(character):
    new_string = ""
    if character == "F":
        new_string = "F-F++F-F"
    else:
        new_string = character
    return new_string
    # if left == "A":
    #     right = "AB"
    # elif left == "B":
    #     right = "A"
    # else:
    #     right = left
    # # print (right)
    # return right


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


def process_string(old_string):
    new_str = ""
    for chr in old_string:  # 1st, this is A
        # applyRules(axiom)
        new_str = new_str + applyRules(chr)  # add up the transformation result of every rule
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
    inst = create_system(4, "F")  # create the string
    print(inst)
    t = turtle.Turtle()  # create the turtle
    wn = turtle.Screen()

    t.up()
    t.back(200)
    t.down()
    t.speed(9)
    draw_L_system(t, inst, 75, 5)  # draw the picture
    # angle 60, segment length 5
    wn.exitonclick()


# print (create_system(5, "F"))

main()
