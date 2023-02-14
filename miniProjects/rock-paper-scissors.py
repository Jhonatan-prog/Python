import random

if __name__ == "__main__":
    def repeat():
        computer = ['rock', 'scissors', 'paper']

        rndomChoiceComputer = random.choice(computer).lower()
        Player = input('choose (Rock, Scissors, Paper): ').lower().strip()

        def correctInput(plyr,compt):
            while plyr != compt[0] and plyr != compt[1] and plyr != compt[2]:
                plyr = input('Only wirte the correct input (rock, scissors or paper): ').lower().strip()

                if plyr == compt[0]or plyr == compt[1] or plyr == compt[2]: 
                    break

        correctInput(Player,computer)
    
        while Player == rndomChoiceComputer:
            print("it was a draw, your choice was: {} and the computer's choice was: {}".format(Player, rndomChoiceComputer))
            rndomChoiceComputer = random.choice(computer).lower()
            Player = input('choose again (Rock, Scissor, Paper): ').lower().strip()
            correctInput(Player,computer)
            
            if Player != rndomChoiceComputer:
                break
        
        if Player == 'rock' and rndomChoiceComputer == 'scissors':
            print("computer choice: " + rndomChoiceComputer + ", and your choice: " + Player)
            print("you've won")

        elif Player == 'scissors' and rndomChoiceComputer == 'paper':
            print("computer choice: " + rndomChoiceComputer + ", and your choice: " + Player)
            print("You've won")

        elif Player == 'paper' and rndomChoiceComputer == 'rock':
            print("computer choice: " + rndomChoiceComputer + ", and your choice: " + Player)
            print("You've won")

        else:
            print("you have lost, your choice was: {} and the computer's choice was: {}".format(Player, rndomChoiceComputer))
    
    repeat()

    ## repeat game
    doUWannaRepeat = input("Do you want to repeat the game? (write yes or not): ").lower().strip()
    while doUWannaRepeat == 'yes':
        repeat()
        doUWannaRepeat = input("Do you want to repeat the game? (write yes or not): ").lower().strip()
        
        if doUWannaRepeat == 'not':
            break

else:
    print("You are trying to run code in another module")