import sqlite3
queries=[]
qs = '''
drop table if exists Roster
create table if not exists Roster(name text,Species text, age int);
insert into Roster values ('Benjamin Sisko','Human',40),('Jadzia Dax','Trill',300),('Kira Nerys','Bajoran',29);
update Roster set name = 'Ezri Dax' where name = 'Jadzia Dax';
'''
for i in qs.split("\n"):
    if i!='':
        queries.append(i)
# print(queries)


with sqlite3.connect("ex.sqlite") as file:
    for i in queries:
        file.execute(i)
    ls=file.execute("select name,age from Roster").fetchall()
    for i in ls:
        print(i)    
