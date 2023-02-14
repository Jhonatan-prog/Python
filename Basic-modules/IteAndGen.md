For someting to be itereable need to have 
a iterator method

```python
object = {
    "name":"juan", 
    "age": 12, 
    "father": {
        "name":"camillo",
        "age": 32
    }
}

i_object = iter(object)

while True:
    try:
        item = next(i_object)
        print(item)

    except StopIteration:
        print("You do not have more values")
        break

## itereators
class range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        current = self.start
        self.start += 1
        return current

myNums = range(1,10)

for num in myNums:
    print(num)

## 2
class myIteration:
    def __init__(self, maxNum = 0):
        self.maxNum = maxNum
    
    def __iter__(self):
        self.rdm = 0
        return self

    def __next__(self):
        if self.rdm < self.maxNum:
            outcome = 5 ** self.rdm
            self.rdm += 1
            return outcome
        else:
            raise StopIteration

for i in myIteration(6):
    print(i)
```

```python

## Generators

nums = [1,2,3,4,5]

def yi(list):
    for num in list:
        yield(num*num)

a = yi(nums)

for i in a:
    print(i)

## list comph

nums = (i*i for i in [1,2,3,4]) ## generator
print(list(nums))