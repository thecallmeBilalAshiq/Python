# =============================================================================================== #
# ==============================                              =================================== #
# ==============================      Python Practice-04    ===================================== #
# ==============================     Muhammad  Bilal Ashiq    =================================== #
# ==============================                              =================================== #
# =============================================================================================== #


# # -------------------------- Topics -----------------------------# #
# # ---------------------------------------------------------------# #
# #                    1. Dictionary                               # #
# #                    2. Sets                                     # #
# # ---------------------------------------------------------------# #




# ----- Dictionary ------------------->>>>>>>>>>>>>>>> Mutable,, can be chnaged ,, updated. 


#  important ---> the values can be same.

dict22 =  {}    # empty dictionary
dict1 = {
    "bilal":100,
    "kamal":8000,
     0 : 567
}

print(len(dict1))
print(dict1)
print(dict1.items())
print(dict1.keys())
print(dict1.values())
dict1.update({"bilal": 99 , "fahad": 1239})

 both not same
print(dict1.get('bilal'))
print(dict1["bilal"])
#  difference

print(dict1.get('bilagdvfgfgdl'))   # no error
print(dict1["btertertl"])           # error

print(dict1)


# -------------------------------------------------------------------------
words = {
    "bilal": "acha bacha",
    "murgha": "hen",
    "kutta": "dog"
}

word = input("Enter the word you want meaning of: ")
print(words[word])


# --------------------------------------------------------------

dict22 = {}

n = input("Enter the friend name   : ")
l = input("Enter the language name : ")
dict22.update({n: l})

n = input("Enter the friend n   : ")
l = input("Enter the language n : ")
dict22.update({n: l})


print(dict22 )


# #### ================================================== >>>>  Sets <<<< =====================================================
# - Sets -------> mutable and hashable

s = {1,2,3,4,5}

empty_set = set()  # to create an empty set,,,, not use {}
s. add(786)
# s.clear()
s.remove(2)
s.pop()   # removes any random number fro set
print("Length:  ",  len(s))
print(s,type(s))    # repeated elements will not be added... order will also not maintained,,, can displayed in any order or without order



#  -------------- union and intersection

s1 = {1,4,8,30}
s2 = {2,3,45,8,790}


print("Union:        ", s1.union(s2))
print("Intersection: ", s1.intersection(s2))
print({1,8}.issubset(s1))
print({1,4,8,30}.issuperset(s1))

#  ------------------------------------------------ 

s5 = {1, '1'}    #both are different
print(s5)

s6 = {1, 1.0}  # both are same  ,,, only 1 will be displaed 1 time
print(s6)

