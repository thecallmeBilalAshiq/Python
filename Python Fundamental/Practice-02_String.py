# =================================================================================================== #
# ==================================                            ===================================== #
# ==================================      Python Practice-02    ===================================== #
# ==================================     Muhammad Bilal Ashiq   ===================================== #
# ==================================                            ===================================== #
# =================================================================================================== #


# # -------------------------- Topics -----------------------------# #
# # ---------------------------------------------------------------# #
# #              1. String and String Functions                    # #
# # ---------------------------------------------------------------# #



print("\n---------------------\n")

# 3 methods to write string


a = 'Bilal AShiq'
longname = '''Bilal 
Ashiq
Jiii
'''
name = "bilal"

n = name[0:5]               # (0 - 2) excluding 3
print(n)
f = name[0]
print(f)


print("\n\n",name[-4: -1])
print(name[1:4])

print(name[:4])          # is same as print(name[0:4])
print(name[1:])          # is same as print(name[1:5])
print(longname[1:5:3])   # skipping 

print(len(name))
print(name.endswith("lal"))
print(name.startswith("Bil"))
print(name.capitalize())


a = 'Bilal Ashiq is a CS Student \n and Chairman of the board of Directors at \'entracloud\''
print(a)

string = "This is a test string written by Bilal Ashiq and the the word 'test' repeated twice."
print("---> Orignal String is: " , string,  "\n")



# =====================================>>> STRING  FUNCTIONS <<<<<==========================================

# new_string = string.replace("test", "example")     # Replace all occurrences of 'test' with 'example'
# print(new_string)                                  # Output: This is a example string with the word 'example' repeated twice.
# new_string = string.replace("test", "example", 1)  # Replace only the first occurrence of 'test' with 'example'
# print(new_string)                                  # Output: This is a example string with the word 'test' repeated twice. "


len(string)                 # Returns the length of the string.
string[0:8:2]           
string.upper()              # Converts the string to uppercase.
string.lower()              # Converts the string to lowercase
string.capitalize()         # Capitalizes the first character of the string.
string.title()              # Capitalizes the first character of each word in the string.
string.strip()              # Removes leading and trailing whitespace from the string.
string.lstrip()             # Removes leading whitespace from the string.
string.rstrip()             # Removes trailing whitespace from the string.
a = string.find("test")
print(a)
a = string.find("test", a + 1)  # finds the sting
string.find("Ashiq")
string.isalnum()
string.isdigit()
print(string.isdigit())

######   1. Write a python program to display a user entered name followed by Good Afternoon using input () function.
entered = input()
print("Good Afternoon ", entered)


     #2. Write a program to fill in a letter template given below with name and date.
line1 = ''' 
Dear <|Name|>,
You are  selected!
<|Date|>
'''

print(line1.replace("<|Name|>","Bilal Ashiq").replace("<|Date|>","Date:  04 October 2003"))

#  # replace double space with single space
print(line1.replace("  ", " ")) # Strings are immutable which means that you cannot change them by running functions on them

