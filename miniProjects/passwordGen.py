## Random password generator
import random
import numpy as np

if __name__ == "__main__":
    passwords = {
        'jhonatan:' : 'jhonfity12_4',
        'Camillo:': 'CaneloTwZ1',
        'Sofia:': np.nan,
        'Ah Kum:': '约瑟夫·杰肯',
        'Mariano:': 'MarianoCanelas19',
        'Kevin': 'k2a19300492',
    }

    def generator(GenratePassw):
        GenratePassw = list(GenratePassw)
        print(random.choice(GenratePassw))
        print()
        button = input("Do you want another password? (type Yes or Not): ").lower().strip()

        ## The problem in this code is the function, when it breaks the while loop
        ## does not follow the next line of code
        if button != "yes" and button != "not":
            while True:
                button = input("(type Yes or Not): ").lower().strip()

                if button == "yes" or button == "not":
                    break

        if button == "yes":
            while True:
                print(random.choice(GenratePassw))
                print()
                button = input("Do you want another password? (type Yes or Not): ").lower().strip()
                
                if button == "not": 
                    break
            

    generator(passwords.items())

else:
    print("You are trying to run code in another module")