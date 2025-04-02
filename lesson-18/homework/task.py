import pandas as pd
import datetime
import numpy as np
        

data = pd.read_csv(r'D:\analytics\py files\hw\task\tackoverflow_qa.csv')
data["creationdate"]=pd.to_datetime(data["creationdate"])
print(data[data["creationdate"]<datetime.datetime(2014,1,1)])
print(data[data["score"]>=50])
print(data[(data["score"]>=50) & (data["score"]<=100)])
print(data[data["ans_name"]=="Scott Boston"])
print(data[(data["ans_name"] == "Demitri") | (data["ans_name"] == "doug") | (data["ans_name"] == "Mike Pennington")])
print(data[(data["creationdate"]>=datetime.datetime(2014,3,1)) & (data["creationdate"]<=datetime.datetime(2014,10,1)) & (data['ans_name'].str.strip()=="unutbu")])
cond=(data["score"]>5) & (data["score"]<10) | (data["viewcount"]>=10000)
print(data[cond])
print(data[data['ans_name'].str.strip()!="Scott Boston"])

titanic_df = pd.read_csv(r"D:\analytics\py files\hw\task\titanic.csv")
print(titanic_df.head())
print(titanic_df[(titanic_df['Sex'].str.strip()=="female")&(titanic_df["Pclass"]==1)&(titanic_df["Age"]>=20)&(titanic_df["Age"]<=30)])
print(titanic_df[titanic_df["Fare"]>=100])
another_df=titanic_df[(titanic_df["Fare"]>=100) & (titanic_df["Fare"]<=103)]
print(titanic_df[(titanic_df["Survived"]==1) & (titanic_df["SibSp"]==0)])
df=titanic_df[(titanic_df["Embarked"]=="C") & (titanic_df["Fare"]>=50)]
withsiborsupandchildorpar=titanic_df[(titanic_df["SibSp"]>0) & (titanic_df["Parch"]>0)]
youngerthan15didnotsurvive = titanic_df[(titanic_df["Survived"]==0) & (titanic_df['Age']<=15)]
knowncabinandfare = titanic_df[(titanic_df["Fare"]>=200) & (titanic_df["Cabin"].notna())]
# print(knowncabinandfare)
oddpessengerid=titanic_df[titanic_df["PassengerId"]%2==1]

ticket_counts = df.groupby('Ticket')['Ticket'].transform('count')
unique_passengers = df[ticket_counts == 1][['Name', 'Ticket']]

print(titanic_df[(titanic_df["Name"].str.contains("Miss"))&(titanic_df["Pclass"]==1)&(titanic_df["Sex"]=="female")])
