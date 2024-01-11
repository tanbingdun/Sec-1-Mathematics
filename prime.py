print("Welcome to Prime Number Checker by Mr Tan!\n")

while True:

	num = int(input("Enter a whole number: "))
	
	if num == 0 or num == 1:
	    print(num, f"is not a prime number. {num} is neither prime nor composite.\n")
	elif num > 1:
	   # check for factors
	   for i in range(2,num):
	       if (num % i) == 0:
	           print(num,"is not a prime number.")
	           print(i,"times",num//i,f"is {num}.\n")
	           break
	   else:
	       print(num,"is a prime number.\n")
	       
	# if input number is less than
	# or equal to 1, it is not prime
	else:
	   print(num,"is not a prime number.")
   

