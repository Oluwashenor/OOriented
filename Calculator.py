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
            return Calculator.divide(a, b)
        else:
            print("Invalid operator")
            return None


calculator = Calculator()
print("Adesina")
print(calculator.calculate("+", 1, 2))
print(calculator.calculate("-", 1, 2))
