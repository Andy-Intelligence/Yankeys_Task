import time

class ATM:
    pwStore = ()
    pwtStore = []
    userPwt = []
    userPw = ()
    curBal = 0
    debt = 0
    cred = 0
    curBal = curBal
    restart = ('y')
    chances = 4
    yn = False


    def __init__(self,name):
        self.name = name
        self.pwStore = ()
        self.userPw = ()
        self.curBal = self.curBal



    def createPw(self):
        print("Please Create a Password")
        for i in range(4):
            self.p = int(input())
            self.userPwt.append(self.p)
        self.userPw = tuple(self.userPwt)
        print("Okay that Password has been saved Please input it to continue")
        return self.userPw


    def intro(self):
        return print("Welcome to {} ATM".format(self.name))

    def request(self):
        return print("Please enter your 4 digit code")

    def pwGet(self):
        self.pwStore = ()
        self.pwtStore = []
        for i in range(4):
            self.p = int(input())
            self.pwtStore.append(self.p)

        self.pwStore = tuple(self.pwtStore)
        return self.pwStore

    def pwCheck(self,pwStore,userPw):
        self.pwStore = pwStore
        self.userPw = userPw
        while self.chances >= 0:
            if self.userPw == self.pwStore and self.chances != 0:
                print("Access Granted")
                break

            elif self.userPw != self.pwStore and self.chances != 0:
                print("Access Denied Please Try Again:")
                self.chances = self.chances - 1
                self.pwGet()

            else:
                print("No More Chances, Your ATM has been Blocked Please Contact Customer Care Support")
                break
        if self.chances == 0:
            exit(1)



    def decision(self):
        print("Please Press 1 for your Balance\n"
              "Please Press 2 to Make a Withdrawal\n"
              "Please Press 3 to Pay in\n"
              "Please Press 4 to Return Card\n")

        self.select = int(input("What Would you like to Choose?:"))

        return self.select


    def withdraw(self):
        self.debt = int(input("How Much Would You Like to Withdraw?"))
        self.curBal = self.curBal - self.debt
        print("\nWould You Like to go Back? ")
        self.restart = ("\nSelect \"y\" or \"n\" ")
        if self.restart == "y":
            self.decision()
        elif self.restart == "n":
            self.withdraw()
        else:
            print("Please Choose a Viable Option")

        return self.curBal

    def deposit(self):
        self.cred = int(input("How Much Would You Like to Deposit?"))
        self.curBal = self.curBal + self.cred
        print("\nWould You Like to go Back? ")
        self.restart = input("\nSelect \"y\" or \"n\" ")
        if self.restart == "y":
            self.decision()
        elif self.restart == "n":
            self.deposit()
        else:
            print("Please Choose a Viable Option")
        return self.curBal

    def balCheck(self):
        print("Your Account balance is #{}".format(self.curBal))
        print("\nWould You Like to go Back? ")
        self.restart = input("\nSelect \"y\" or \"n\" ")
        if self.restart == "y":
            self.decision()
        elif self.restart == "n":
            self.balCheck()
        else:
            print("Please Choose a Viable Option")
        return self.curBal

    def getCard(self):
        print("Please Wait While Your Card is Returned...")
        time.sleep(2)
        return print("Please Take Your Card")




def main():
    while True:


        select = obj.decision()

        if select == 1:
            obj.balCheck()

        elif select == 2:
            obj.withdraw()
            obj.balCheck()

        elif select == 3:
            obj.deposit()
            obj.balCheck()

        elif select == 4:
            obj.getCard()

        else:
            print("Please Choose Any of the Options Listed")




if __name__ == "__main__":
    print("What Bank Would You Like to Use")
    print("1. Fidelity\n"
          "2. Wema\n"
          "3. Access")
    print("Please Select \'1\' or \'2\' or \'3\'")

    Bank = int(input())
    if Bank == 1:
        Bank = "Fidelity"
    elif Bank == 2:
        Bank = "Wema"
    elif Bank == 3:
        Bank = "Access"
    else:
        print("Please Chose one of the Viable Options")

    obj = ATM(Bank)
    obj.intro()
    userPw = obj.createPw()
    obj.request()
    pwStore = obj.pwGet()
    yn = obj.pwCheck(pwStore,userPw)

    main()





