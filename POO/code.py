class ATM:

    ## attributes
    def __init__(self, money, phoneNumber, password, withdrawl, payMethod):
        self.money = money
        self.phoneNumber = phoneNumber
        self.password = password
        self.__withdrawl = withdrawl ##private attribute
        self.__payMethod = payMethod ##private attribute

    ## methods
    def getMoney(self):
        self.money = self.money - self.__withdrawl
        return self.money
    
    def nequi(self):
        if self.phoneNumber != None and len(self.phoneNumber) == 10 and self.__payMethod == "nequi":
            if self.__withdrawl > self.money:
                return "sorry, you don't have that amount of money, the money you have rn is: {}".format(self.money)
            else:
                self.money = self.money - self.__withdrawl
                return self.money

        elif len(self.phoneNumber) != 10 or self.phoneNumber != int():
            return 'we had a problem with your phone number or with your pay method, make sure you wrote it correctly'

phoneNumber = input('Enter phone number: ')
amountwihdrwl = int(input('How much money do you want to withdrawl?:\n'))

P1 = ATM(1500000, None, 8709, amountwihdrwl, "ATM")
P1.getMoney()

P2 = ATM(5000000, phoneNumber, 2078, amountwihdrwl, "nequi")
P2.nequi()

print(P1.money)