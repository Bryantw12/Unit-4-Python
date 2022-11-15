todos = ["Take Shower", "Read book", "Fold Clothes", "Floss Teeth"]
print(todos)

x = input("What to add to list?")


while x != "todos":
  print("What to add?")

todos.append(x)


print("Your todo list is ")
print(todos)
