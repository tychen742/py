def squareit(n):
    return n * n

def cubeit(n):
    return n*n*n

def main():
    anum = int(input("Please enter a number: "))
    print(squareit(anum))
    print(cubeit(anum))

if __name__ == "__main__":
    main()