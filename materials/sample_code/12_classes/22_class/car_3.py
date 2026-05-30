class Car:                                  # #### define a class
    def __init__(self, color, model, year):  # __init__ function always executed on initiation
        self.color = color                  # #### property
        self.model = model                  # #### property
        self.year = year                    # #### property
        
    def age(self):
        import datetime
        today = datetime.date.today()
        this_year = today.year
        print(f"My car is", this_year - self.year, "years old.")

    def __str__(self):                      # #### return as object
        return f"My car is {self.year} {self.color} {self.model}" # return


my_car = Car("red", "Camry", 2019)          # #### creating an instance

print(my_car)                               # #### print the returned

my_car.age()                                # . calling function

# ##### this class is getting useful as method(s) provide functionalities