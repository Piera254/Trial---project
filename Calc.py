print ("Welcome to our site")

#getting input
number1 = int(input ("Enter first number: "))
number2 = int (input("Enter Second number: "))
operand  = (input ( "Enter operand: "))


if operand == "+":

    result = number1 + number2
elif   operand == "-":
    result = number1 - number2
elif operand == "/":
    result = number1/number2
elif operand == "*":
    result = number1 * number2

else:
    print ("Invalid. Please try again")
    
    
print ( number1, operand, number2, "=" , result)
