import math
import random

class Calculator:
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2

    def addition(self):
        # Додавання
        return self.operand1 + self.operand2

    def subtraction(self):
        # Віднімання
        return self.operand1 - self.operand2

    def multiplication(self):
        # Множення
        return self.operand1 * self.operand2

    def division(self):
        # Ділення
        if self.operand2 != 0:
            return self.operand1 / self.operand2
        else:
            return "Error: Division by zero"

    def exponentiation(self):
        # Піднесення до степеня
        return math.pow(self.operand1, self.operand2)
