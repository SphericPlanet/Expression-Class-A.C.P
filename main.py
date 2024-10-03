class Expression:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def display(self):
        result = self.num1 + self.num2 + self.num3
        print(f"The result of the expression {self.num1} + {self.num2} + {self.num3} is: {result}")

if __name__ == "__main__":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    
    expr = Expression(num1, num2, num3)
    expr.display()
