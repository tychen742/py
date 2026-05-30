for i in range(1, 13):
    for k in range(1, 100):
        print("_", end=" ")
    print()
    for j in range(1, 13):
        # if j < 10:
        print(i, "*", j, "=", i * j, "\t", "| ", end="")
        # if j >= 10:
        #     print (i, "*", j, "=", i * j,  end="")
    print()
