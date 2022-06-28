
from operator import truediv
from os import system, name
  
# import sleep to show output for some time period
from time import sleep
from tkinter import Y
  
# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
clear()
i='y'
while i != 'n':

    clear()
    numberOne = int(input("Enter a number:"))
    numberTwo = int(input("Enter another number:"))

    clear()
    
    x = int(input("1.Add\n2.Subtract\n3.Multiply\n4.Division"))
    result = 0
    if x==1:
        result=numberOne+numberTwo
    if x==2:
        result=numberOne-numberTwo
    if x==3:
        result=numberOne*numberTwo
    if x==4:
        if numberTwo == 0:
            input ("The problem contains an invalid input. Press 'Enter' to try again.")
            continue
        else:
            result=numberOne/numberTwo

    clear()
    print ("Result:" + str(result))
    i=input("Would you like to continue? Press y/n:")
print ("Completed!")
clear()