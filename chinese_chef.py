
# import the Chef class from the chef.py file
#    to allow us inherit the Chef class into our new class called
#       ChineseChef. By doing this, it wil extend or override the Chef class
#        and still allow us to use all the functions from the Chef class
from chef import Chef


# ChineseChef class will inherit the functions from the Chef class in the chef.py file
class ChineseChef(Chef):

    # extend Chef class with a new function
    def make_fried_rice(self):
        print("The chef makes fried rice")

    # override Chef class make_special_dish function with different code/data
    def make_special_dish(self):
        print("The chef makes orange chicken")

