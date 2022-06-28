inpA = int(input("enter an integer:"))
inpB = int(input("enter another integer:"))
input_D = input("do you want to add or subtract; press 0 for add, 1 for subtract")
if input_D == "0":
    inpC = inpA+inpB
else:
    inpC = inpA-inpB
print (inpC)