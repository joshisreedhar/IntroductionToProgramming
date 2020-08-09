print("You have started the Calculator")
print("Which operation do you want to perform \nNote : Use the following convention")
print("For Addition :- a \nFor Subtraction :- s \nFor Multipication :- m \nFor Division :- d")
print("If you choose s you are subtracting 2nd number from 1st number")

Operation = input("Operation: ")
if Operation != "a" and Operation != "s" and Operation != "m" and Operation != "d":
    print("This function is not available")
else:
    num1 = float(input("Enter 1nd number: "))
    num2 = float(input("Enter 2nd number: "))

    if Operation == "a":
        result = num1+num2
        print("The Addition result is", result)
	
    elif Operation == "s":
        result = num1-num2
        print("The Subtraction result is", result)
	
    elif Operation == "m":
        result = num1*num2
        print("The Multiplication result is", result)
	
    elif Operation == "d":
        result = num1/num2
        print("The Division result is", result)
input("")
