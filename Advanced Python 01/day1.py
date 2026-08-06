#  --------------------------- Walrus Operator (:=) -------------------------
#   # Repeated Function Calls Bachane Ke Liye: Agar aapko koi lamba function ya len() bar bar call nahi karna, toh ek hi baar variable mein store karke check kar sakte hain:
#   # While Loops Ko Asaan Banane Ke Liye: User input ya file se line read karte waqt loop ki condition mein hi value assign karne ke liye:
#   #  List Comprehensions Mein: Jab kisi calculation ka result bar-bar use karna ho aur code clean rakhna ho.


# Link to study better: https://www.geeksforgeeks.org/python/walrus-operator-in-python-3-8/

num = [1, 2, 3, 4, 5]

while (n := len(num)) > 0:
    print(num.pop())


# -------------------------------------------------------------------------------------------------------------




#    # Type definations 
#    # Like C++ yahan bhi ap bta skty ho type kbaary ma

n :int = 5
bilal:str = "Hello"

#   # from typing se ab ham jo ha list aur tuple aur dict ka type bta skty hain 
from typing import List, Dict, Tuple, Union, Optional

numbers : List[int] = [1, 2, 3, 4, 5]
person: Tuple[str, int] = ("Bilal", 25)
score: Dict[str, float] = {"Math": 90.5, "Science": 85.0}

identifier: Union[int, str] = 42

print(f"n: {n}, bilal: {bilal}, numbers: {numbers}, person: {person}, score: {score}, identifier: {identifier}")




#   # ------------------------- Match Case (Like Switch cases)   ---------------------------


def check_number(x):
    match x:
        case 10:
            print("It's 10")
        case 20:
            print("It's 20")
        case _:
            print("It's neither 10 nor 20")

check_number(10)
check_number(30)


#  # --------------------- Try Except Else Finally -----------------------------
#  --------- try , excpet, else, finally ka use karke hum error handling kar skty hain

""""
1. Try:       Is block mein aap wo code likhte hain jo chalana chahte hain.Agar yahan koi galti nahi hui, toh code theek se chal jata hai.
2. Except:    Agar try wale code mein koi galti (error) aa jaye, toh program crash nahi hota.Balki except wala code chal jata hai jo galti ko sambhal leta hai.
3. Else:      Ye tab chalta hai jab try wale code mein koi galti na aaye.Agar sab kuch theek raha, toh else wala hissa chal jayega.
4. Finally:   Ye block hamesha chalta hai.Chahe galti aaye ya na aaye, finally ke andar ka code lazmi chalega. Ye aam tor par safai (cleanup) ke liye hota hai.
"""

try:
    a = int (input("enter a number: "))
    print (a)
except Exception as e:
    print(e)                          # Agar ghlti ayi tu code crash ki jagga excpetion (valueerror, zerodiviosn error waghera)
else:
    print("No exception occurred")    # Agar code sahi se chal gaya toh ye print hoga
finally:
    print("Execution completed")      # har haal m print hoga, chahe galti aaye ya na aaye


# #  ===>>>> finally ka use karte hue hum file ko safe tareeqe se close kar sakte hain, chahe koi galti aaye ya na aaye.

# try:
#     file = open("data.txt", "w")
#     # Maanlein yahan code mein koi galti aa gayi aur program ruk gaya
#     result = 10 / 0 
# except ZeroDivisionError:
#     print("Galti aa gayi!")
# finally:
#     file.close() # Ye har haal mein chalega!
#     print("File ko safe tareeqe se band kar diya gaya.")


# # Raising Excpetion

b =   int(input("Enter a number: "))
c = int (input("Enter another number: "))

if (c==0):
    raise ZeroDivisionError("Cannot divide by zero")

