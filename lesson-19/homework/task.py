import pandas as pd
df=pd.read_csv(r"task/sales_data.csv")
ass1result1 = df.groupby("Category").agg(
    total_quantity_sold = pd.NamedAgg("Quantity",aggfunc="sum"),
    average_price_per_unit = pd.NamedAgg("Price",aggfunc="mean"),
    max_quantity_sold_in_single_trans = pd.NamedAgg("Quantity",aggfunc="max")
)
print(ass1result1)
max_quantity_in_each_category = df.groupby("Category").agg({"Quantity":"max"})
df["total_price"]=df["Quantity"]*df["Price"]
df['Date'] = pd.to_datetime(df['Date'])
max_sales_date = df.groupby("Date").agg({"total_price":"sum"}).idxmax()
max_sales_value = df.groupby("Date").agg({"total_price":"sum"}).max()
print(list(max_sales_date)[0],":",list(max_sales_value)[0])
df=pd.read_csv(r"task/customer_orders.csv")
res=df.groupby("CustomerID").agg({"Quantity":"sum"})
print(res[res["Quantity"]<=20])
res=df.groupby("CustomerID").agg({"Price":"mean"})
print(res[res['Price']>=120])
res=df.groupby("Product").agg(
    total_quantiy = pd.NamedAgg("Quantity",aggfunc="sum"),
    total_price = pd.NamedAgg("Price",aggfunc="sum")
)
print(res[res["total_quantiy"]<=5])
import sqlite3
with sqlite3.connect(r"task/population.db") as connection:
    ls=connection.cursor()
    df=pd.read_sql("select * from population",connection,index_col="id")
print(df)
df=pd.read_excel(r"task/population_salary_analysis.xlsx")
total_population = df["Number of population"].sum()
df["percentage_population"]=total_population/100*df["Number of population"].notna()
print(df["percentage_population"])
print(df["Average Salary"])
print(df["Median Salary"])
print(df["Number of population"])
