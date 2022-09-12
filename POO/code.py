class ATM:

    ## attributes
    def __init__(self, money, phoneNumber, password, withdrawl):
        self.money = money
        self.phoneNumber = phoneNumber
        self.password = password
        self.__withdrawl = withdrawl ##private attribute

    ## methods
    def getMoney(self):
        self.money = self.money - self.__withdrawl
        return self.money
    
    def nequi(self):
        if self.phoneNumber != None and len(self.phoneNumber) == 10:
            self.money = self.money - self.__withdrawl
            return self.money
        elif len(self.phoneNumber) != 10 or self.phoneNumber != int():
            print('we had a problem with your phone number, make sure you wrote it correct')

P1 = ATM(1500000, None, 8709, 500000)
P1.getMoney()

phoneNumber = input('Enter phone number: ')
P2 = ATM(2000000, phoneNumber, 2078, 800000)
P2.nequi()

print(P2.money)