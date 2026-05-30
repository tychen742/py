# mytuple = ("apple", "banana", "cherry")
# myiterator = iter(mytuple)
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))
# for x in mytuple:
#     print(x)


# mystr = "banana"
# myit = iter(mystr)

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else: 
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

for x in myiter:
    print(x)