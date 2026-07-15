# =============================================================================================== #
# ==============================                            ===================================== #
# ==============================      Python Practice-03    ===================================== #
# ==============================     Muhammad  Bilal Ashiq  ===================================== #
# ==============================                            ===================================== #
# =============================================================================================== #


# # -------------------------- Topics -----------------------------# #
# # ---------------------------------------------------------------# #
# #                    1. Tuple                                    # #
# #                    2. List                                     # #
# # ---------------------------------------------------------------# #



# # ---------------------------------------------  Tuple ----------------------------------------------------

#  data set like string immutable,, string same data structure,,, tuples differetn data structute


tuple1 = (1,True,3,"Bilal")
t = (1)        # it is integer ,, it is not tuple
tuple2 = (1,)  # it is a tuple now
print(type(tuple1))


# tuple1[2] = 12     #----> not possible  ,,,, immutable,, cannot be changed like string
print(tuple1) 

print(tuple1.index(3))    # will return the index of first occurrence of 1 in a.
print(len(tuple1))


a = (7, 0, 8, 0, 0, 9)


print(a.count(0))


# # ---------------------------------------------  List ----------------------------------------------------

# list = ["Bilal", 1 , 3.4 , 'Kaka', True , False]

# ------------------------>>>>>>  mutable.. can be changed.
# print(list[4])

list1 = [123, 678, 90, 478, 900,40,678]
print("Sum= ", sum(list1))
# list1.sort()
# print(list1)
# print(list[1:4])
# list.append("Harry")
# print(list)

l1 = [1, 34,62, 2, 6, 11]
# # l1.sort()
# # l1.reverse()
# # l1.insert(2, 333333) # Insert 333333 such that its index in the list is 3
value = l1.pop(3)
print(value)
# print(l1)

# list1.remove(678)
# print(list1)

# list1.clear()
# copied_list = list1.copy()
# print("678 occurs ", list1.count(678) , " times")

print(list1)
# print(copied_list)



marks =  []

v1 = input("Enter marks name: ")
marks.append(v1)

v2 = input("Enter marks name: ")
marks.append(v2)

v3 = input("Enter marks name: ")
marks.append(v3)

v4 = input("Enter marks name: ")
marks.append(v4)


marks.sort()

print("\n --> Marks of student in sorted manner ",marks)
