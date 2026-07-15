# =================================================================================================== #
# ==================================                            ===================================== #
# ==================================      Python Practice-08    ===================================== #
# ==================================     Muhammad Bilal Ashiq   ===================================== #
# ==================================                            ===================================== #
# =================================================================================================== #


# # -------------------------- Topics -----------------------------# #
# # ---------------------------------------------------------------# #
# #                       1. File Handling                         # #
# # ---------------------------------------------------------------# #

# #--------------------------------------


# f = open("Python Fundamental/file.txt")
# data  = f.read();
# print (data)
# f.close()


# st = "Data to be written in file"
# ff = open("Python Fundamental/file.txt", "w")
# ff.write (st)
# ff.close()

#                     #  ----------------- with statement ----------------- #
# 2️⃣ Reading — 3 Tareeqe

# With statement automatically closes the file after the block of code is executed
with open("Python Fundamental/file.txt", "r") as f:
    print (f.read()) # complete read
    print (f.readline()) # read 1 line
    print (f.readlines())   # read all lines and return as list
   #Verified output: readlines() → ['Line1\n', 'Line2\n', 'Line3\n']. Agar \n nahi chahiye, content.splitlines() use karo.


# # ------------------------------------------------
# import random
# def game():
#     print("You are playing the game")
#     number = random.randint(1,65)
#     print(f"Your score is {number}")
#     return number


# # Best practice — large files ke liye - memory safe

# with open("Python Fundamental/file.txt", "r") as f:
#     for line in f:            # ek time pe ek line RAM mein — memory-safe
#         print(line.strip())   # 1 time 1 li

# with open('Python Fundamental/file.txt') as f:
#     f.tell()   # relative seek, TEXT mode

# # Pathlib module — modern way to handle files and directories - instead of os module, join

# from pathlib import Path

# p = Path("Python Fundamental/file.txt")
# print(p.exists())           # True/False
# print(p.stat().st_size)     # bytes mein size
# print(p.read_text())        # open() ke bina direct read!
# new_path = Path("folder") / "sub" / "file.txt"   # clean joining


with open ("Python Fundamental/file.txt", encoding = "utf-8") as f:
    print(f.read())




