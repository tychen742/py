# ##### contact list

class Person:
    def __init__(self, fname, lname, company, phone):
        self.firstname = fname
        self.lastname = lname
        self.company = company
        self.phone_number = phone

    def print_name (self):
        print(self.firstname, self.lastname, self.company)

class Sales(Person):
    pass

contact = Sales("TY", "Chen", "MST", "555-345-6666")

contact.print_name()
