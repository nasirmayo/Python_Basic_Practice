class my_first_class:
    x = 5

my_first_object = my_first_class()
print(my_first_object.x)



class my_first_class:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_function_in_class(self):
        print("Hello my name is", self.name)

    def my_function(self):
        print("this is a function")

object = my_first_class('nasir', 33)
print(object.name)
print(object.age)
object.my_function_in_class()
object.my_function()

print(object.name)
object.name = 'sana'
print(object.name)
print("nasir 3333")

