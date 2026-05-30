
class Payroll:
    def __init__(self, **kwargs):
        self.variables = kwargs
        
    def set_vars(self, k, v):               # ### getter method
        self.variables[k] = v

    def get_vars(self, k):                  # ### setter method
        return self.variables.get(k, None)
    
    def overtime(self, hour, rate):
        if hour > 40:
             print('You have over time hours!')

var1 = Payroll(name = 'John', rate = 20, hour = 50, age = 55)
print(var1.get_vars('name'))
print(var1.get_vars('rate'))
# print(overtime)


# ##### getters and setters for data validation
# ##### getters and setters avoid direct access to class memebers