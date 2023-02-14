### Functions Lamdbas

You would write code on one line

```python

## Map
def sumL (n1,n2):
    return n1 + n2
l1 = [1,2,3]
l2 = [4,5,6]

print(list(map(sumL,l1,l2)))

## Map lambdas
## lambda argument1,argument2:condition, l1,l2 (parameters to replace)
print(list(map(lambda n,m:n+m, l1,l2)))

## filter (Extract items)
def filt(n):
    return (n == 'l')

string = 'Hello world!'
print(list(filter(filt, string))) ## output = ['l', 'l', 'l'] filter(function name, value)

## filter lambdas
print(list(filter(lambda n: n=='o', string))) ## output = ['o', 'o']

## Reduce
import functools
def sumL (n1,n2):
    return n1 - n2

l2 = [4,5,6]

print(functools.reduce(sumL, l2)) ## it sums the contents

## Reduce lambdas
print(functools.reduce(lambda n,m: n+m, l2))


## practice
import functools
string = [1,2,3,4,5,6]

print(list(map(lambda n1,n2: n1+n2, [5,2],[10,5])))
print(list(filter(lambda n:n % 2 == 0, string)))
print(functools.reduce(lambda n,m: n*m, string))