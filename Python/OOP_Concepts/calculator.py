class Calculator:
    def __init__(self, number1, number2, operation):
        self.number1 = number1
        self.number2 = number2
        self.operation = operation

    def addition(self):
        return self.number1 + self.number2

    def subtraction(self):
        return self.number1 - self.number2

    def multiplication(self):
        return self.number1 * self.number2

    def division(self):
        return self.number1 / self.number2

class MathExtension:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def modulus(self):
        return self.num1%self.num2

    def addition(self):
        return f'Sum of {self.num1} and {self.num2} is {self.num1+self.num2}'

class Mathematics(MathExtension, Calculator):
    def __init__(self, number1, number2, operation, value):
        self.value = value
        Calculator.__init__(self, number1, number2, operation)
        MathExtension.__init__(self, number1, number2)

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def square(self):
        return self.getValue()**2

    def absolute(self):
        if self.getValue() < 0:
            return -1*(self.getValue())
        else:
            return self.getValue()


