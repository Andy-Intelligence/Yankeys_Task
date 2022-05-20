

class addition():
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


    def decision(self):

        print("Please press \"1\" to end and \"2\" to continue ")

        self.select = int(input())

        return self.select



def main():

    while True:

        var1 = int(input("Please type in a value:"+ " "))
        var2 = int(input("Please type in another value:"+ " "))
        obj1 = addition(var1,var2)
        obj1.addition()
        obj1.show_addition()
        select = obj1.decision()

        if select == 1:
            break

        else:
            continue


if __name__ == "__main__":
    main()