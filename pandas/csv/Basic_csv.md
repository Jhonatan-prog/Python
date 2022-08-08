[Documentation](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)

#### CSV Pandas

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
```