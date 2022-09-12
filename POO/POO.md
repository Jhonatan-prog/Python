```python
class book:

    ## attributes
    def __init__(self, pageNumbers, bookType, bookTopping, nameBook, standarPrice = 100000):
        self.pageNumbers = pageNumbers
        self.bookType = bookType
        self.bookTopping = bookTopping
        self.nameBook = nameBook
        self.standarPrice = standarPrice
    
    ## methods
    def Bprice(self):
        ## Super cons to return standar price
        if self.pageNumbers > 100:
            Bprice = self.standarPrice * self.pageNumbers 
            Bprice / 2

        return Bprice
            
## Objects
B1 = book(150, 'Adventures', 'it has striking colors', 'Black Leopard Red Wolf')
B1.Bprice()

B2 = book()

print(B1.standarPrice)
```


### inheritance

```python
class games:

    ## Attributes
    def __init__(self, gameName, gamePrice, gameType):
        self.gameName = gameName
        self.gamePrice = gamePrice
        self.gameType = gameType 

    ## Methods
    def refund(self):
        statedGame = 'Good'
        if statedGame != 'Good':
            self.gamePrice - self.gamePrice
            return self.gamePrice
    
class boardgames(games):

    def __init__(self, gameName, gamePrice, gameType, material):
        super().__init__( gameName, gamePrice, gameType)
        self.matrial = material


## Object
price = input('Enter price: ')
g1 = games("Lol", int(price), '5vs5')
g2 = boardgames('chess', '20000', 'boardGame', 'wood')

print(g2.gameName)
```

##### function isinstance() and issubclass()

**isinstance(object, class)**: it returns 'True' if object is from class **class** or one of the daughters class

**issubclass(class, classInfo)**: it checks the inheritances of the class. returns True if class is a subclass of classInfo. Otherwise, it'd return False.

```python
>>> c = Coche('rojo', 20)
>>> cv = CocheVolador('azul', 60)
>>> isinstance(c, Coche)
True
isinstance(cv, Coche)
True
>>> isinstance(c, CocheVolador)
False
>>> isinstance(cv, CocheVolador)
True
>>> issubclass(CocheVolador, Coche)
True
>>> issubclass(Coche, CocheVolador)
False

```

##### Encapsulation: private attributes

By default all attributes are publics, to convert a public attribute to private attribute you need to use: 
self._nameAttribute or self.__nameAttribute.

You could access to the attribute from outside but it is not recomendable (use this just for attributes that you are not gonna call later)

```python
class A:
    def __init__(self):
        self._contador = 0  # Este atributo es privado
    def incrementa(self):
        self._contador += 1
    def cuenta(self):
        return self._contador
```

##### polymorphism

Two or more **releated class** compacted inside a new funticion using a **for loop** and then passing the class to a specific var, create a polymorphism.

```python
class Perro:
    def sonido(self):
        print('Guauuuuu!!!')
class Gato:
    def sonido(self):
        print('Miaaauuuu!!!')
        
class Vaca:
    def sonido(self):
        print('Múuuuuuuu!!!')

def a_cantar(animales):
    for animal in animales:
        animal.sonido()
if __name__ == '__main__':
    perro = Perro()
    gato = Gato()
    gato_2 = Gato()
    vaca = Vaca()
    perro_2 = Perro()
    granja = [perro, gato, vaca, gato_2, perro_2]
    a_cantar(granja)

```

##### ATM

```python

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

```