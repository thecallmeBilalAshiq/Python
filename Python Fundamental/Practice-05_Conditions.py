# =============================================================================================== #
# ==============================                              =================================== #
# ==============================      Python Practice-05    ===================================== #
# ==============================     Muhammad  Bilal Ashiq    =================================== #
# ==============================                              =================================== #
# =============================================================================================== #


# # -------------------------- Topics -----------------------------# #
# # ---------------------------------------------------------------# #
# #                    1. Conditional                              # #
# # ---------------------------------------------------------------# #


n = int (input("Enter any score: "))

if (n > 100):
    print(n, " is greater than 100")
elif(n<0):
    print(n, " is wrong score, it is negative")
else:
    print(n, " is less than 100")


n1 = int (input("Enter number: "))
n2 = int (input("Enter number: "))
n3 = int (input("Enter number: "))
n4 = int (input("Enter number: "))


if(n1 > n2) and (n1>n3) and (n1>n4):
    print(n1, " is greatest")
elif(n2 > n1) and (n2>n3) and (n2>n4):
    print(n2, " is greatest")
elif(n3 > n1) and (n3>n2) and (n3>n4):
    print(n3, " is greatest")
elif(n4 > n1) and (n4>n2) and (n4>n3):
    print(n4, " is greatest")
else:
    "Error"



p1 = "can we be friends"
p2 = "subscribe now"  
p3 = "Share it"  
p4 = "click this"

text = input("Enter your comment: ")

if((p1 in text) or (p2 in text )or (p3 in text) or (p4 in text)):
    print("It is considered as spam, reort if it is")

else:
    print("This comment is not a spam")
    


list1 = ["bilal", "kamal", "mill"]

l = input("Enter the name to find: ")
if  (l in list1):
    print("name found")

talking = input("Enter the name: ")

if "bilal".lower() in talking.lower():
    print("we are talking about Bilal")
else:
    print("we are not talking about Bilal")
