class Car:                                  # #### define a class
    def __init__(self, color, model, year):  # __init__ function always executed on initiation
        self.color = color                  # #### property
        self.model = model                  # #### property
        self.year = year                    # #### property

    def __str__(self):                      # #### return as object
        return f"My car is {self.year} {self.color} {self.model}" # return


my_car = Car("red", "Camry", 2019)          # #### creating an instance

print(my_car)                               # #### print the returned
