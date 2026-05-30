# initialize a result variable to be an empty list
# loop
#    create a new element
#    append it to result
# return the result

### Create a function to return a list of prime numbers from 2 to n

prime = []


def is_prime(n):
    for i in range(2, n):
        for j in range(2, n):
            if i % j == 0:
                prime.append(i)
    return prime


print(is_prime(10))
