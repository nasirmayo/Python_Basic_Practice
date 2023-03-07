class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname


    def print_name(self):
        print(self.firstname, self.lastname)



class student(person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year


    def welome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)



student_obj = student('Mike', 'Olsan', 2019)
student_obj.welome()




