class Car:                                  # #### define a class
    def __init__(self, color, model, year):  # __init__ function always executed on initiation
        self.color = color                  # #### property
        self.model = model                  # #### property
        self.year = year                    # #### property


my_car = Car("red", "Camry", 2019)          # #### creating an instance

print(my_car)                               # #### the object: <__main__.Person object at 0x15039e602100>
print(my_car.model)                         # #### dot notation: Camry


# ##### __init__ means this is a class constructor

# ##### "self" is always the first parameter
# ##### "self" is a paramter referencing to the current class instatnce
# ##### "self" is used to access instance attributes and methods (class members) 
# ##### "self" is a convention and can be called anything else

