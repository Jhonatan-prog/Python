## Dice roll simulator
if __name__ == "__main__":
    import numpy as np
    
    D4 = np.array(np.arange(1,5))

    def RollDice(D4):
        try:
            Roll = input("What roll do you want?: ")
            RNumbers = input("Write the number of Dices: ")
            RNumbers = int(RNumbers)

            ##code
            if Roll == 'D4' and RNumbers == 1:
                RollRamdon = [n for n in D4]
                print(np.random.choice(RollRamdon))
                
            elif Roll == 'D4' and RNumbers == 2:
                RollRamdon = [n for n in D4]
                print(np.random.choice(RollRamdon),"and",np.random.choice(RollRamdon))

            elif Roll == 'D4' and RNumbers == 3:
                RollRamdon = [n for n in D4]
                print(np.random.choice(RollRamdon),",",np.random.choice(RollRamdon),"and",np.random.choice(RollRamdon))

        except TypeError:
            print("Error")

    RollDice(D4)

else:
    print("You are trying to run code in another module")