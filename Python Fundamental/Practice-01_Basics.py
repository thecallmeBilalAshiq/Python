# =================================================================================================== #
# ==================================                            ===================================== #
# ==================================      Python Practice-01    ===================================== #
# ==================================     Muhammad Bilal Ashiq   ===================================== #
# ==================================                            ===================================== #
# =================================================================================================== #



# # -------------------------- Topics -----------------------------# #
# # ---------------------------------------------------------------# #
# #                   1. Printing                                  # #
# #                   2. Modules                                   # #
# #                   3. Comments                                  # #
# #                   4. Repl                                      # #
# #                   5. Data Types                                # #
# #                   6. Operators(Logical,assignment,arithmetic)  # #
# #                   7. Type Function                             # #
# # ---------------------------------------------------------------# #

#  ------------------------------------   Printing  --------------------------------------------

# print one line
print ("Muhammad Bilal Ashiq   1 line print")     

# print multiple line
print ("""
To print
       more than 1 line
            yes it prints
""")


#  -------------------------------------   MODULES  -----------------------------------------------

#  ----  Just sample how to download and import any module -----
# Open termianl write -->      pip install module_name ===>>>> pip install pyjokes
# import module_name.


try:
     import pyttsx3  # pip install pyttsx3 by opening terminal
     engine = pyttsx3.init()
     engine.say("Hey I am Muhammad Beelal Aashiq")  # robot will call my name
     engine.runAndWait()
except ImportError:
     print("pyttsx3 is not installed.")

# -----------------------------------------
import webbrowser

# Open Wikipedia
url = "https://www.linkedin.com/in/bilal-ashiq/"
webbrowser.open(url)

# Open a specific YouTube video
video_url = "https://www.youtube.com/shorts/UgS4K3Nae4s"  # Replace with a real video URL
# webbrowser.open(video_url)

# -------------------------------------------
import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 5, 3]

# Create a line plot
plt.plot(x, y)

# Add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Plot Example")

# Show the plot
plt.show()


#  ------------------------------------   Add Comments  --------------------------------------------


# --->> one line comment   or ctrl + /

'''
multiple line
More tha 1 line comment
Bilal
'''

#  ------------------------------------  REPL    --------------------------------------------

# open  terminal or cmd on windows and right python then enter.. then run your code there.. like (4+5 enter ) print("Hello world")




#  ----------------------------------------------------------------------------  >>>> data types
a = 4                          # a is an integer
var2 = 9.4                     # var2 is a floating point number
d = False                      # d is a boolean variable
name = "Muhammad Bilal Ashiq"  # name is a string
k = None                       # k is a none type variable

print(a+var2) 
print(name)

_bilal = 786               # valid

#    &bilal = 9       # --> Invalid due to & special character
#    Bil@l_Ashiq      # --> Invalid due to @ symbol


#  ----------------------------------------------------------------------------  >>>> Operators


# >>>>>>>......        Arithmetic Operators
a = 7
b = 4
c = a + b
print(c)

#  >>>>>...........        Assignment Operators
a = 2+3
print(a)   # 5
b = 6
b = b-3
print(b)

# >>>>>...........       Comparison Operators

t1 = "bilal" == "bilal"     # always true or false
t2 = 10 > 20      

print(t1)
print(t2)


# >>>>>...........       Logical Operators

t3 = True or False

# Truth table of 'or' 
print("T or F is ", True or False)
print("T or F is ", True or True)
print("F or T is ", False or True)
print("F or F ", False or False , "\n\n\n")

# Truth table of 'and' 
print("T and F is ", True  and False)
print("T and T is ", True  and True)
print("F and T is ", False and True)
print("F and F is ", False and False)

print(not(True))


#  ----------------------------------------------------------------------------  >>>> type
var1 = "19.0"
print(type(var1))


a = "123"
b = float(a)     # str converted into float type now,,, now variable a is not string it is float
t2 = type(b) 
print(b)
print(t2)



#  alt + shift + down_arrow_key  --> duplicate same line down

num1 = input("Enter number 1: ")    
num2 = input("Enter number 2: ")

print("Number a is: ", num1)   # will take input in string by default
print("Number b is: ", num2) 
print("Sum is ", num1 + num2)        # answer will be in string  as it takes the string in inputs

a = int(input("Enter your number: "))     # this is right method for input


print("The square of the number is", a**2)      # good one
print("The square of the number is", a*a)
# print("The square of the number is", a^2) # it is wrong
