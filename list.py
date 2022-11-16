my_list = [ "apples" , "carrots" , "water" , "oranges", "donut"]


print(my_list)

#adding ginger to  list using append
my_list.append("ginger")

print(my_list)

#Print one thing in list using numbers. Always starts off with 0. 
print(my_list[2])

#This is how you get the last value of a list using negative numbers.The numbers always wrap around so -1 would be the last value for
print(my_list[-1])

#used to change value on a list
my_list[0] = "juice"

print(my_list)

#This is how you remove something from a list
del my_list[2]

print(my_list)

#This prints out the lengths of something. For example you can determine the number in the list and string characters
print(len(my_list))

#This can be used to sort items. For example in alphabetical order
my_list.sort()

print(my_list)

#Flips order of a list 
my_list.reverse()
print(my_list)

second_list = [ "purple" , "red" , "green" , "yellow" , "black"]

#This is how you combine lists 
print(my_list + second_list)


#You can seperate the different lists using this
print("  | ".join(my_list + second_list))

#Can make one long string into a list 
names = ("anna , wesey , saint".split(" , "))

print(names)

# my_tuple = ("nike" , "jordan" ,"puma" , "adidas" , "Cdg")

# # my_tuple.append("yeezys")

# print(my_tuple)

# # del my_tuple[2]

# print(my_tuple)

# #You can't add things to tupples since its inmutable
# #my_tuple[0] = "APPLE"

# print(my_tuple)