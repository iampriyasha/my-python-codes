def isPrime(x):
    for i in (2, x - 1):
        if x%i == 0:
            return False
    
    return True

y=int(input("Insert a Number:"))
if isPrime(y):
	print("The Number is PRIME")
else:		
	print("The number is COMPOSITE")