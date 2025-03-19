import json
import requests 
import json

#1
with open("students.json",'r') as file:
    data=json.load(file)
for student in data:
    print(f"name of student {student} is {data[student]['name']}")
    print(f"age of this student is {data[student]['age']}")

#2

url='https://api.openweathermap.org/data/2.5/weather?lat=41.2995&lon=69.2401&appid=2eafa23a49b58f5f58fb84a5c3c27767'
response = requests.get(url)
json_data = response.json()
print(f"wheather condition in tashkent is: {json_data['weather'][0]['main']}")
print(f"Temperature in tashkent is: {(float(json_data['main']['temp'])-273.15):.2f}°C")
print(f"humidity is: {json_data['main']['humidity']}")

#3

class books:
    books={}
    def __init__(self):
        with open('books.json','r') as file:
            self.books=json.load(file)
    def add_book(self,name, author, genre):
        self.books[name]={}
        self.books[name]['author']=author
        self.books[name]['genre']=genre
    def update_info(self,name, **kwargs):
        for i in kwargs:
            if i=="genre" or i=="author":
                self.books[name][i]=kwargs[i]
    def delete(self,name):
        self.books.pop(name)
    def save(self):
        with open("books.json",'w') as file:
            json.dump(self.books,file,indent=4)
    def look(self):
        print(self.books)

# 4

genre=input()
resp=requests.get(f'https://www.omdbapi.com/?apikey=8db7519f&Genre={genre}').json()
print(resp['Title'])
