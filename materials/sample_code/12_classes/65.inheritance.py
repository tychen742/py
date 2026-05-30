class Animals:
    def eat(self):
        print('I can eat.')

    def talk(self):
        print('I can talk.')

    def sleep(self):
        print('I can sleep.')


class Cat(Animals):     #  Cat now inherit from Animals
    # def talk(self):
        # print('I can meow.')
    def despise(self):
        print('I despise you.')

    def sleep(self):
        print('I can sleep all I want.')


class Dog(Animals):
    pass

mitten = Cat()
mitten.talk()  #  with and without the method in Cat() will make difference
mitten.despise()
mitten.sleep()
