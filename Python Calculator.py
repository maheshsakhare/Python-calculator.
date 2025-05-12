def add(n1,n2):
    return n1+n2

# TODO: Write out the other 3 functions, subtract, multiply and divide)

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

# TODO: Add these 4 functions into a dictionary as the values.
# keys = "+","-","*","/"

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
    }


# TODO: Use the dictionary to perform the calculations.
# Multiply 4*8 using the dictionary.

def calculator():

    should_accumulate = True
    num1 = float(input("What it the first number?:"))

    while should_accumulate:
        
        for symbol in operations:
                   print(symbol)

        operations_symbol = input("Pick and operation:")
        num2 = float(input("What is the second number?:"))

        answer = operations[operations_symbol](num1,num2)
        print(f"{num1} {operations_symbol} {num2} = {answer}")
                   
        choice = input("Type 'y' to cacuating with {answer}, or type 'n' to start a new calcuations:").lower()

        if choice == 'y':
            num1 = answer
        else:
            should_accumulate = False
            print("\n"*20) # To add space to start a new calculation.
            calculator() # This is called Recursion.

calculator()
