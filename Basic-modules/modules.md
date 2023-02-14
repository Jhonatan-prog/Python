### Regex 

```python
import re

urls = """
    https://www.google.com
    http://coreyms.com
    https://youtube.com
    https://www.nasa.gov
"""

regex = re.compile(r'https?://(www\.)?\w+\.(com|gov)', re.IGNORECASE) ## or , re.I
matches = regex.finditer(urls)
subbed = regex.sub(r'\2 \3', urls)

for match in matches:
    print(match)
    print(match.group(2)) ## it shows the matches of groups / output: google coreyms youtube
```

### Itertools

```python
## 6.Iterators and Generators,ZIP function *
## 7.Decorators *
## 8.Requests module *
## 9.Meta programming *
## 10.Lambdas,Filters and Maps *
## 11.Pickle module for serialisation *

import itertools
counter = itertools.count()
print(next(counter)) ## 0
print(next(counter)) ## 1

lista = [200,300,400,500]
a = list(itertools.zip_longest(range(10), lista))
print(a)

counter = itertools.cycle([True, False])
print(next(counter)) ## True
print(next(counter)) ## False
print(next(counter)) ## True
print(next(counter)) ## False

counter = itertools.repeat(2, times=3) ## repeat 2 three times 

square = itertools.starmap(pow, [(4,2), (5,2)])
print(list(square))

# premutations and combinations
## Do not repeat: (a,a) (0,0)
printItems = itertools.permutations(letters, 3)
printItems = itertools.combinations(letters, 3)

## .product (repeat)
printItems = itertools.product(letters, repeat=3)

## it merges the two lists
printItems = itertools.chain(letters,nums)

## compress
letters = ["a","b","c","d","e","f"]
selectors = [True, False, False, True, True, False]

result = itertools.compress(letters, selectors) ## output (a,d,e)

## accumulate
result = itertools.accumulate(nums) ## "sums all the content"
```

### Decorators
```python
## here we are using first-class functions, clousures and decorators
def outer(Xfunction):
    def inner():
        return Xfunction()
    return inner

## deco
def show():
    print('Hello world!, :)')

decorator = outer(show)
decorator()

## same as
@outer
def show():
    print('Hello world!, :)')

show()
```

If you are going to use arguments in your function 
you should use: (*args,**kwargs)

```python
def outer(Xfunction):
    def inner(*args,**kwargs):
        print("this is a deco {}".format(Xfunction.__name__))
        return Xfunction(*args,**kwargs)
    return inner

@outer
def forDec(name, age):
    print("Hello my name is: {} and I'am {} years old".format(name,age))

forDec("Jhona", 17)

## Class to decorate instead of functions
class decorator_class(object):
    def __init__(self, outer):
        self.outer = outer

    def __call__(self, *args, **kwargs):
        print("this is a class-deco {}".format(self.outer.__name__))
        return self.outer(*args,**kwargs)

@decorator_class
def forDec(name, age):
    print("Hello my name is: {} and I'am {} years old".format(name,age))

forDec("Jhona", 17)
```

### Request module

```python
import requests
r = requests.get('url')

## methods
print(r.text) ## print all the html of the website
print(r.content) ## print img code in bytes

## https status code
print(r.status_code)
print(r.ok) ## < 400 response = True
## 200 = sucsses
## 300 = something went wrong (running code)
## 400 = client error
## 500 = server errors

print(r.headers)

## params: Add adtionals params, data: Add data
payload = {"number":5, "price": 25}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)
## outcome = https://imgs.xkcd.com/comics/python.png?number=5&price=25

## To post some info
payload = {"phoneNumber":310584883, "name": "jhony"}
r = requests.post('https://httpbin.org/post', data=payload)
print(r.text)

## To access to data
## .json(): is a method which put the info in a dict
access = r.json()
print(access['form'])
print(access['headers'])

## basic auctification
r = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('corey','testing'))
print(r.text)