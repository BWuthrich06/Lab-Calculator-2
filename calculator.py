"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    equation = input("Please enter your equation in prefix notation.")
    tokens = equation.split(' ')

    if 'q' in tokens or 'quit' in tokens:
        print("Goodbye.")
        exit()

    elif len(tokens) < 2:
        print("Not enough inputs.")
        continue
    
    
    operator = tokens[0]
    num1 = tokens[1]
    result = 0
    
    if len(tokens) > 2:
        num2 = tokens[2]
    else:
        num2 = "0"
   
    if not num1.isnumeric() or not num2.isnumeric():
        print("Those are invalid inputs, please use numbers!")
        continue

    else:
        if operator == "+":
            result = add(float(num1), float(num2))

        elif operator == "-":
            result = subtract(float(num1), float(num2))

        elif operator == "*":
            result = multiply(float(num1), float(num2))

        elif operator == "/":
            result = divide(float(num1), float(num2))

        elif operator == "square":
            result = square(float(num1))  

        elif operator == "cube":
            result = cube(float(num1))

        elif operator == "pow":
            result = power(float(num1), float(num2))

        elif operator == "mod":
            result = mod(float(num1), float(num2))
        else:
            result = "Invalid operator. Please try again."    
    
    print(result)
    