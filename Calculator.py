class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b

    @staticmethod
    def calculate(operator, a, b):
        if operator == "+":
            return Calculator.add(a, b)
        elif operator == "-":
            return Calculator.sub(a, b)
        elif operator == "*":
            return Calculator.multiply(a, b)
        elif operator == "/":
            if b == 0:
                print("Division by zero not allowed")
            return Calculator.divide(a, b)
        else:
            print("Invalid operator")
            return None


allowedOperators = ["+", "-", "*", "/"]
continueLoop = True
calculator = Calculator()

while continueLoop:
    a_value = 0
    b_value = 0
    print("Welcome to Calculator, type 'exit' to quit")
    op = str(input("Enter your operator choice: "))
    if op not in allowedOperators:
        if op == "exit":
            print("Goodbye")
            break
        print("Invalid operator")
        continueLoop = False
    try:
        a_value = float(input("Enter first number: "))
        b_value = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input")
        continueLoop = False
    if type(a_value) is str or type(b_value) is str:
        print("Invalid inputted value")
        continueLoop = False
    if not continueLoop:
        break
    print("Your answer is ", calculator.calculate(op, a_value, b_value))
