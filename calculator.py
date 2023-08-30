"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    equation = input("Please enter your equation in prefix notation.")
    tokens = equation.split(' ')

    operator = tokens[0]
    num1 = tokens[1]
    num2 = tokens[2]
    result = 0

    if 'q' or 'quit' in tokens:
        print("Goodbye.")
        exit()
    
    elif len(tokens) < 2:
        print("Not enough inputs.")
        continue
    
    elif not num1.isnumeric() or not num2.isnumeric():
        print("Those are invalid inputs, please use numbers!")
        continue

    else:
        if operator == "+":
            result = add(num1, num2)

        elif operator == "-":
            result = subtract(num1, num2)

        elif operator == "*":
            result = multiply(num1, num2)

        elif operator == "/":
            result = divide(num1, num2)

        elif operator == "square":
            result = square(num1)  

        elif operator == "cube":
            result = cube(num1)

        elif operator == "pow":
            result = power(num1, num2)

        elif operator == "mod":
            result = mod(num1, num2)
        else:
            result = "Invalid operator. Please try again."    
    
    print(result)
    