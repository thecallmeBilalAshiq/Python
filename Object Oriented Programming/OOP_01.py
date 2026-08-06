# =================================================================================================== #
# ==================================                            ===================================== #
# ==================================       OOP Practice-01      ===================================== #
# ==================================     Muhammad Bilal Ashiq   ===================================== #
# ==================================                            ===================================== #
# =================================================================================================== #


# # -------------------------- Topics -----------------------------# #
# # ---------------------------------------------------------------# #
# #                   1. Object Oriented Programming               # #
# # ---------------------------------------------------------------# #


# Class Attribute and Object Attribute

# class Employee1:
#     language = "Python"         # Class attribute
#     name = "Bilal"
#     salary = 10000

# bilal = Employee1()
# bilal.name = "Shaka_Laaka"   # Object Attribute (takes priority over class attribute)
# print(bilal.name, bilal.language, bilal.salary )


# # -------------- Self Parameter ------------------

# # agar self ni likhy gy tu error a jaye ga q k jab ham call krty hain bilal.getinf() tu wosmjhta ha k Employee.getinfo(bilal) tu bracket k andar self ka hona laazmi ha
# # --------- SELF ki jagga koi aur word bhi use kr skty hain lekin conventionally self hi use hota ha
# class Employee:
#     language = "Python"         # Class attribute
#     name = "Bilal"
#     salary = 10000

#     def getinfo(sel):    # agar self ni likhy gy tu error a jaye ga
#         print("This is a method of class Employee")
#         print("Name:", sel.name)   

# bilal = Employee()
# bilal.name = "Shaka_Laaka"   # Object Attribute (takes priority over class attribute)
# print(bilal.name, bilal.language, bilal.salary )

# bilal.getinfo()
# # Or we can also call the method like this:
# Employee.getinfo(bilal)   # same as bilal.getinfo()  (self is passed automatically) 




# ----------------- Static method
# Agar ham self use ni krna chaahty hain tu - mtlb us function m koi bhi object k kaam ni ha -sief prin tkrwana ha 


# class Employee3:
#     language = "Python"         # Class attribute
#     name = "Bilal"
#     salary = 10000

#     @staticmethod        # ab self likhny ki zaroorat ni ha
#     def display():
#         print("This is a static method of class Employee")

#     @staticmethod        # ab self likhny ki zaroorat ni ha
#     def getinfo():    
#         print("method of class Employee")
#         print("Name:", Employee3.name)   

# bilal = Employee3()
# bilal.name = "Shaka_Laaka"   # Object Attribute (takes priority over class attribute)
# print(bilal.name, bilal.language, bilal.salary )

# bilal.getinfo()
# # Or we can also call the method like this:
# Employee3.getinfo()   # same as bilal.getinfo()  (self is passed automatically) 
# bilal.display()







# -------------------------- Constructor --------------------------

# # There is no constructor overlaoding in python

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

    
    
bilal = Employee4("Bilal", 10000)  
print(bilal)