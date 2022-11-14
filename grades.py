#Putting in Title 
print("Put in Percentage")

# I made x an inter so that python could see it as a number value

x=int(input("What is your grade?"))

x = int(x)

#Made 59 the number for "if" because it decides if the grade is passing or failing

if x <= 59:
    print("F")
#These elif comments are used to determine the grade placements depending on the number
elif x >= 60 and x<= 69:
    print("D")

elif x >= 70 and x<= 79:
    print("D+")

elif x >= 80 and x<= 85:
    print("C")

elif x >= 85 and x<= 89:
    print("B")

else:
    print("A")


#
