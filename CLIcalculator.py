class Calculator():

    var1 = 0
    var2 = 0
    tSum = 0

    def __init__(self,var1,var2):
        self.var1 = var1
        self.var2 = var2





    def addition(self):
        self.tSum = self.var1 + self.var2
        return self.tSum

    def show_addition(self):
        print("The first number is " + str(self.var1))
        print("The second number is " + str(self.var2))
        print("The total sum is "+ str(self.tSum))
        return print(self.tSum)


    def subtraction(self):
        self.tSum = self.var1 - self.var2
        self.tSum

    def show_subtraction(self):
        print("The first number is " + str(self.var1))
        print("The second number is " + str(self.var2))
        print("The total after subtraction is "+ str(self.tSum))
        return print(self.tSum)


    def multiplication(self):
        self.tSum = self.var1 * self.var2
        self.tSum

    def show_multiplication(self):
        print("The first number is " + str(self.var1))
        print("The second number is " + str(self.var2))
        print("The total after multiplication is "+ str(self.tSum))
        return print(self.tSum)


    def division(self):
        self.tSum = self.var1 / self.var2
        self.tSum


    def show_division(self):
        print("The first number is " + str(self.var1))
        print("The second number is " + str(self.var2))
        print("The total after division is "+ str(self.tSum))
        return print(self.tSum)

    def modulus(self):
        self.tSum = self.var1 % self.var2
        self.tSum

    def show_modulus(self):
        print("The first number is " + str(self.var1))
        print("The second number is " + str(self.var2))
        print("The solution after the modulus operation is "+ str(self.tSum))
        return print(self.tSum)


    def decision(self):

        print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n"\
        "5. Modulus\n"\
        "6. End this Program")

        self.select = int(input("Select operations form 1, 2, 3, 4 :"))

        return self.select

def main():

    while True:
        var1 = int(input("Enter first number: "))
        var2 = int(input("Enter second number: "))
        obj = Calculator(var1,var2)
        select = obj.decision()

        if select == 1:
            obj.addition()
            obj.show_addition()

        elif select == 2:
            obj.subtraction()
            obj.show_subtraction()

        elif select == 3:
            obj.multiplication()
            obj.show_multiplication()

        elif select == 4:
            obj.division()
            obj.show_division()

        elif select == 5:
            obj.modulus()
            obj.show_modulus()

        elif select == 6:
            break

        else:
            print("Invalid Input")



if __name__ == "__main__":
    main()