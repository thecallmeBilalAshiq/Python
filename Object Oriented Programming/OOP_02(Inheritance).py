# # =================================================================================================== #
# # ==================================                            ===================================== #
# # ==================================       OOP Practice-02      ===================================== #
# # ==================================     Muhammad Bilal Ashiq   ===================================== #
# # ==================================                            ===================================== #
# # =================================================================================================== #


# # # -------------------------- Topics -----------------------------# #
# # # ---------------------------------------------------------------# #
# # #                   1. Object Oriented Programming               # #
# # # ---------------------------------------------------------------# #



class Employee4:
    language = "Python"
    name = "Bilal"
    salary = 10000

    def __init__(self, name, salary):    # Dunder Method (Constructor) - automatically called when an object is created - double __ line walu functions
        print("Constructor of class Employee4")
        self.name = name
        self.salary = salary


    def __str__(self):    # Dunder Method (String Representation) - automatically called when an object is printed
        return f"The Name is {self.name} and Salary is {self.salary}"


class Coder (Employee4):
    def __init__(self, name, salary, language):
        #  # -------------------- Super method  -------------------
        super().__init__(name, salary)    # super() is used to call the constructor of the parent class
        self.language = language    

    def __str__(self):
        return f"The Name is {self.name} and Salary is {self.salary} and Language is {self.language}"
    
    

class Tester (Employee4):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)    # super() is used to call the constructor of the parent class
        self.language = language    

    def __str__(self):
        return f"The Name is {self.name} and Salary is {self.salary} and Language is {self.language}"   

# ----------- Multi-Level inheritance  ---------------------
#  # class A():
#  # class B(A):
#  # class C(B):

# ----------- Multiple inheritance  ---------------------
#  # class A():
#  # class B():
#  # class C(A, B):

#  # ====>>>> No Diamond Problem  - because python sets this according to the Method Resolution Order (MRO) - C(A, B) - C will first look for the method in A and then in B  


# -----------  inheritance  ---------------------
#  # class A():



bilal = Coder("Bilal", 10000, "Python")  
print(bilal)




 #   ------------- @Class Method -----------------------

 #   Test Case 01 (Class method k baghari)
class Employee5:
    a = 1  #   class attribute

    def show (self):
        print(f"Value of class attribute is {self.a}")

bilal = Employee5()
bilal.a = 45
bilal.show()         #


#  #   Test Case 02 (Class method k sath)
class Employee6:
    a = 1  #   class attribute

    @classmethod
    def show (cls):     # cls wese e bs show krny k liyee k ye classmethod ha
        print(f"Value of class attribute is {cls.a}")

bilal = Employee6()
bilal.a = 45

bilal.show()        



# #  # kia howa ?
# # # wese ti object k attribute baazi le jaata ha - leken jab hamclassmethod likh dain gy tu object attribute ki ni suni jay gi - class attributes ki suni jay gi




# #   # ------------------ Property decorators    ------------------

# # class Person:
    def __init__(self, age):
        self._age = age  # _age is private (by convention)


    # This is our Getter using @property
    @property
    def age(self):
        print("Getting value...")
        return self._age

    # This is our Setter (to check values)
    @age.setter
    def age(self, value):
        if value < 0:
            print("Age cannot be negative!")
        else:
            self._age = value

# # Using it:
p = Person(20)

# 1. Reading the value (Calls the @property getter method automatically)
print(p.age)  # Output: Getting value... then 20

# 2. Writing/Changing the value (Calls the @age.setter method automatically)
p.age = -5    # Output: Age cannot be negative!
p.age = 25    # Works fine!




# #  # ------------ Passing string to the constructor ----------


class A:
    def __init__(self, l):
        self.name , self.language, self.salaray = l
    def __str__(self):
        return f"The Name is {self.name} and Salary is {self.salaray} and Language is {self.language}"  


bilal = A(["Bilal", "Python", 10000])
print(bilal)   


