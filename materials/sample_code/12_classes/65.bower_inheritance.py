class Animal:

    def drink(self):
        print('I drink.')

    def eat(self):
        print('I eat.')

    def talk(self):
        print('I talk.')


class Dog(Animal):  # Cat now inherit from Animals
    def eat(self):
        print('I am a omnivores.')

    def drink(self):
        print('I drink from my water bowel.')

    def love(self):
        print('I love you.')


class Dog(Animal):
    pass


doggy = Dog()
# with and without the method in Dog() will
# make difference; e.g., comment out the talk() method in Dog()
doggy.eat()
doggy.drink()
doggy.love()
