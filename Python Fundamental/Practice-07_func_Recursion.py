# =============================================================================================== #
# ==============================                              =================================== #
# ==============================      Python Practice-07    ===================================== #
# ==============================     Muhammad  Bilal Ashiq    =================================== #
# ==============================                              =================================== #
# =============================================================================================== #


# # -------------------------- Topic ------------------------------# #
# # ---------------------------------------------------------------# #
# #                         1.Functions                            # #
# #                         2.Recursion                            # #
# # ---------------------------------------------------------------# #



# =========================================== >>   Function  << =============================================


def func1():
    print("Bilal ")

func1()
func1()

# #with arguments
def sum(n1,n2,n3):
    print("sum= ", (n1+n2+n3))

sum(10,45,120)


def sum(n1,n2,n3):
    print("sum= ", (n1+n2+n3))
    return "Recite Darood Pak"

n = sum(10,45,120)
print(n)

#  #default function
def func3(name, roll ="123"):
    print(name, " ",roll)

func3("Bilal")
func3("Bilal", "786")






# =========================================== >>   Recursion  << =============================================

def fact(num):
    if(num==0):    # factorial of 0 is 1
        return 1
    return num* fact(num-1)

print(fact(1))

# -------------------------------------------------------------
def fahrenhite_to_celcius(f):
    return 5*(f-32)/9

f = int(input("Enter temperature in Fahrenhitr: "))
c = fahrenhite_to_celcius(f)
print(f"{f}°F = {round(c, 2)}°C")


#-------------------------------------------------------------
def summation(n):
    if(n==1):    # important line for a base
        return 1
    return n + summation(n-1)

print(summation(5))

#-------------------------------------------------------------


def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)

pattern(3)


def multiply(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")

multiply(5)
