# =============================================================================================== #
# ==============================                              =================================== #
# ==============================      Python Practice-06    ===================================== #
# ==============================     Muhammad  Bilal Ashiq    =================================== #
# ==============================                              =================================== #
# =============================================================================================== #


# # -------------------------- Topics -----------------------------# #
# # ---------------------------------------------------------------# #
# #                            Loops                               # #
# # ---------------------------------------------------------------# #


list1 = [786, "Bilal", "Ashiq", 3.09, True, 'Kamal']
tuple1 = (3,5,6,9,"kaka")
string1 = "Bilal Ashiq"

i = 0

while(i<len(list1)):
    print(list1[i], "\t\n")
    i +=1

# for i in range(30):
#     print(i)

# for i in range(4,61):
#     print(i)

# for k in range (11,100,10):
#     print(k)



for i in list1:
    print(i)
else:
    print("We are done  with list\n")




for i in tuple1:
    print(i)
else:
    print("We are done  with tuple\n")    



for i in string1:
    print(i)
else:
    print("We are done  with string\n")

for i in range(30):
    if (i==12):
        break  # break the whole loop right now when i is 12,, willn not print 11
    print(i)

for i in range(30):
    if (i==12):
        continue  # only skip 12
    print(i)


for a in range(20):
    pass    #  pass,,, for loop will not run ,,, only while loop will run,, next to it

i=0
while(i<10):
    print(i)
    i+=1




#--------------------------------------------------------------------
number = int (input("Entre the number you want to get table: "))
for i in range(1,11):
    print(number ," * ", i , " = " , number*i)      # method 01
    print(f"{number} * {i} = {number*i}")           # both are the right methods





#--------------------------------------------------------------------
list2 = ["Bilal","Kamal","Abu Bakar","Billu",'Ali']

for name in list2:
    if(name.startswith("B")):
        print(f"Assalam-o-Alaikum {name}")
    else:
        print("No name found starting with B")





#####--------------------------------  code to find the prime number

numb = int (input("Enter any number: "))

for i in range(2,numb):
    if (numb%i == 0):
        print(numb , " is not a prime number")
        break
else:
    print(numb ," is a prime number")





    
#####--------------------------------  code to find the pfactorial
n = int (input("Enter any number: "))

factorial = 1
for i in range(1, n+1):
    factorial = factorial * i
print(f"Factorial of {n} is {factorial}")





#####--------------------------------  code to print the triangles

n = int (input("Enter any number: "))

for i in range(1,n+1):
    print("*" * (i) , end="")    # end=""  --->>>>   endline ni aati is se 
    print("") 


for i in range(1,n+1):
    print(" " * (n-i) , end="")
    print("*" * (i) , end="")    # end=""  --->>>>   endline ni aati is se 
    print("") 



n = int (input("Enter any number: "))

for i in range(1,n+1):
    print(" " * (n-i) , end="")
    print("*" * (2*i-1) , end="")    # end=""  --->>>>   endline ni aati is se 
    print("") 





# -------------->>>>>>> Empty Square
n = int(input("Enter the number: "))
for i in range(1, n+1): 
    if(i==1 or i==n):
        print("*"* n, end="")
    else:
        print("*", end="")
        print(" "* (n-2), end="")
        print("*", end="")
    print("")


#   # ----------------------------Reverse Table printing
number = int (input("Entre the number you want to get table: "))
for i in range(1,11):
    print(f"{number} * {11-i} = {number*(11-i)}")           # both are the right methods


# ------------------------- guesiing game

import random

secret_number = random.randint(1, 100)  # Generate a random number
guesses_left = 3

for guess in range(guesses_left):
  user_guess = int(input("Guess a number between 1 and 100: "))
  if user_guess == secret_number:
    print("\n\t=====>>> Congratulations! You guessed the number.")
    break  # Exit the loop if the guess is correct
  elif user_guess < secret_number:
    print("Your guess is too low.")
  else:
    print("Your guess is too high.")

if user_guess != secret_number:  # Check outside the loop (in case no break)
  print("\n\t\t Oh..!!! You ran out of guesses. The secret number was:", secret_number)
