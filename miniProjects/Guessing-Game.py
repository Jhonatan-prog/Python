## Gussing number
import numpy as np

numbers = np.array(np.arange(16))
print("Choose a number between 0 and 16")
player1Num = input("Insert Number: ")

def Guessing(nums,plaNum):
    lives = 3
    numberR = np.random.choice(nums)
    plaNum = int(plaNum)

    try:
        if numberR == plaNum:
            print("correct")
        else:
            lives -= 1
            print()
            print("Wrong, the number was {} and you wrote {}, {} lives left".format(numberR,plaNum,lives))

            while numberR != plaNum and lives >= 1:
                lives -= 1
                numberR = np.random.choice(nums)     
                input("Insert Number again: ")
                print()

                if numberR == plaNum:
                    print("correct")
                else:
                    print("Wrong again..., the number was {}, {} lives left".format(numberR,lives))
                    if lives == 0:
                        print("End, you lost")
                        print()

    except ValueError:
        print("Sorry, but that is not a number")

Guessing(numbers,player1Num)