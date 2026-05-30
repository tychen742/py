import math

def circleArea(radius):
    area = math.pi * (radius**2)
    # print(math.pi)
    return area

def main():
    r = 10.0
    result = circleArea(r)
    print(result)

if __name__ == '__main__':
    main()
