# 1 
data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} 
df = pd.DataFrame(data)
df.rename(columns = {'First Name' : 'first name' ,'Age' : 'age' , 'City' : 'city'}  , inplace = True)
df.head(3)
print(f"the average age of my smaple data is --- {df['age'].mean()}")
df.filter(['first name' , 'city'])
df['salary'] = [200 , 250 ,980,650]

# 2
import pandas as pd

df2 = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
})

df2
max_sales = df2['Sales'].max()
max_expanse = df2['Expenses'].max()
print(f"max sales is --- {max_sales} and max expanse is --- {max_expanse}")

print(' ')
print(' ')


min_sales = df2['Sales'].min()
min_expanse = df2['Expenses'].min()
print(f"min sales is --- {min_sales} and min expanse is --- {min_expanse}")

print(' ')
print(' ')


mean_sales = df2['Sales'].mean()
mean_expanse = df2['Expenses'].mean()
print(f"average sales is --- {mean_sales} and average expanse is --- {mean_expanse}")


# 3
import pandas as pd

df3 = pd.DataFrame({
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
})

df3

columns = ['January', 'February', 'March', 'April']

for i in columns:
    max_amount = df3[i].max() 
    print(f"Max amount for {i}: {max_amount}")

print(' ')
print(' ')
print(' ')
    
    
columns = ['January', 'February', 'March', 'April']

for i in columns:
    max_amount = df3[i].min() 
    print(f"Min amount for {i}: {max_amount}")
    
print(' ')
print(' ')
print(' ')

    
    
columns = ['January', 'February', 'March', 'April']

for i in columns:
    max_amount = df3[i].mean() 
    print(f"Average amount for {i}: {max_amount}")
