[Documentation](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)

#### CSV Pandas and File Handling python

With **header** we can remove all the columns.
With **na_values** we change the NA value
The **skiprows** ignores the rows you select

```python
Columns_name = ['Marian','colors','Total']
df.read_csv('NewInfo', header=None, name=Columns_name, index_col='Index Name',na_values=['nothing'])
print(df)
```

#### Series and creating a csv

```python
NaIndex = ['A','B','C','D']

## DataFrame
Info = {
    'Names': ['Alex','Camillo','Juan','Matias'], 
    'Age': [17,5,20,40],
    'Country': ['Venezuela','Colombia','USA','Peru'],
    'Merried': [False] * 4,
}

Serie1 = pd.Series(['Apple','Pineaple','Banana','Watermelon'])
df = pd.DataFrame(Info, index=NaIndex)

## csv
df.to_csv('NewInfo')
print(df)

```

#### Opneing a file

```python
## Open the file to write and remove the other file before 
df = open('PartidosPoliticos.txt', "w")
## Open the file to add content
df = open('PartidosPoliticos.txt', "a")
## Open mode lecture file 
df = open('PartidosPoliticos.txt', "r")

str = ["Hello","what","is","up"]
df = open('Problems.txt', "r")
str = df.readline()
df.close()
print(df)

## read mode

with open('gas_prices.csv', 'r') as f:
    size_to_read = 2
    
    f_contents = f.read(size_to_read)
    print(f.tell)
    
    while len(f_contents) > 0:
        print(f_contents, end='\n')
        f_contents = f.read(size_to_read)

## writing mode

with open('gas_prices.csv', 'r') as rf:
    with open('gas_pri_copy.txt', 'w') as wf:
        for line in rf.read():
            wf.write(line)

with open('requestPractice.png', 'wb') as f:
    f.write(r.content)

### csv
csv_file = open('Website-text_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','text','video_src'])
```

```python
## os

import os

print(os.getcwd())
os.chdir('/Users/Usuario/Documents/Python/Python/Matplotlib')

os.makedirs('first')

print(os.listdir())

os.removedirs('first')

print(os.listdir())

##
mod_time = os.stat('Matp.py').st_mtime
print(datetime.fromtimestamp(mod_time))
```