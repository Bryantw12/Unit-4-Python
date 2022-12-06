# my_file = open("Bryant.txt" , "a")

# # print(my_file.readlines())

# my_file.write('im writing from python\
#   \n')

# my_file.close()

# my_file = open("Bryant.txt")

# for line in my_file.readlines():
#   print(line, end="")



# with open("todo.txt", "w") as output:
#     output.write(todos)

while True:
  my_file = open("todo.txt" , "a",)
  x = input("What todo would you like to add?")
  my_file.write(x + "\n")
  my_file.close()

 
  my_file=open("todo.txt","r")
  print("Your todos are:") 
  print(my_file.read())
  my_file.close()
  



  # todos.append(x)
