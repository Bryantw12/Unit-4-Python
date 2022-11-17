
x=int(input("What is your grade?"))

list = []  
list.append(x)
print(list)

x=int(input("What is your second grade?"))

 
list.append(x)
print(list)

x=int(input("What is your third grade?"))

  
list.append(x)
print(list)

x=int(input("What is your forth grade?"))

 
list.append(x)
print(list)





sum = 0 

for grade  in list:
  sum = sum + grade

print(sum / len(list))  


