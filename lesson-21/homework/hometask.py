import pandas as pd

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)

avarage_grade = df1['avg'] = round((df1['Math']+df1['English']+df1['Science'])/3,2)

studetn_with_hihest_avg_grade = df1[df1['avg']==df1.max()['avg']]

df1['Total'] = df1['Math']+df1['English']+df1['Science']

import matplotlib.pyplot as plt 
plt.bar(['Math','English','Science'], [df1['Math'].mean(),df1['English'].mean(),df1['Science'].mean()])

import pandas as pd

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)

total_sales_product_a = df2['Product_A'].sum()
total_sales_product_b = df2['Product_B'].sum()
total_sales_product_C = df2['Product_C'].sum()


df2['Total_sales'] = df2['Product_A'] + df2['Product_B'] + df2['Product_C']
df2[df2['Total_sales']==df2['Total_sales'].max()]['Date']


pct_change = df2[['Product_A','Product_B','Product_C']].pct_change()
pct_change

products = ['Product_A','Product_B','Product_C']
for product in products:
    plt.plot(df2['Date'].dt.day,df2[product],label=product,marker="o")
plt.legend()


import pandas as pd

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)


average_salary_by_dep = df3.groupby('Department').agg(
    average_dalary = pd.NamedAgg('Salary',aggfunc='mean')
).reset_index()


df3[df3['Experience (Years)']==df3['Experience (Years)'].max()]



ls = df3.sort_values('Salary')['Salary'].pct_change()


distirution=df3.groupby('Department').agg(
    distribution = pd.NamedAgg('Experience (Years)',aggfunc='sum')
).reset_index()
plt.bar(distirution['Department'],distirution['distribution'])


import pandas as pd

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)


df4['total_sales'] = df4['Quantity'] * df4['Total_Price']
total_revenue = df4['total_sales'].sum()

product_orders = df4.groupby('Product').agg(
    total_ordered = pd.NamedAgg('Order_ID',aggfunc='count')
).reset_index()
product_orders[product_orders['total_ordered'] == product_orders['total_ordered'].max()]['Product'].to_list()


avg_quan_ordered = df4['Quantity'].mean() 

grouped = df4.groupby('Product').agg(
    dist = pd.NamedAgg('total_sales',aggfunc='sum')
).reset_index()
plt.pie(x=grouped['dist'],labels=grouped['Product'])

