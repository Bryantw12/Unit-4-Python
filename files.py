my_file = open("Bryant.txt" , "r+")

# print(my_file.readlines())

for line in my_file.readlines():


  print(line, end="")

  my_file.writelines(['im writing from python'])
  