from datetime import datetime
from dateutil.relativedelta import relativedelta
import time
import datetime as dt
import pytz
import re


def problem1():
    a = input("Input your birth date in the format yyyy-mm-dd: ")

    try:
        born_date = datetime.strptime(a, "%Y-%m-%d")
        cur_date = datetime.now()

        delta = relativedelta(cur_date, born_date)

        years = delta.years
        months = delta.months
        days = delta.days

        print(f"You are exactly {years} years, {months} months, and {days} days old.")
    except ValueError:
        print("Invalid date format. Please enter the date in the format yyyy-mm-dd.")
problem1()

def next_birthday():
    try:
        a = input("Input your birth date in the format yyyy-mm-dd: ")[4:]
        born_date1 = (datetime.strptime(str(int(datetime.now().strftime("%Y")))+a,"%Y-%m-%d") - datetime.now()).days
        born_date2 = (datetime.strptime(str(int(datetime.now().strftime("%Y"))+1)+a,"%Y-%m-%d") - datetime.now()).days
        if born_date1>0:
            print(born_date1)
        else:
            print(born_date2)
        
    except ValueError:
        print("Invalid Date format.")
next_birthday()

def meeting():
    try:
        a=datetime.strptime(input("enter current Date and time like yyyy-mm-dd HH:MM"),"%Y-%m-%d %H:%M")
        b=input("meeting duration in hours and minutes like HH:MM")
        dur_h = int(b.split(":")[0])
        dur_m = int(b.split(":")[1])
        print(a+dt.timedelta(hours=dur_h,minutes=dur_m))
    except ValueError:
        print("Invalid Date Format")
    
meeting()

def time_zone():
    try:
        a=datetime.strptime(input("enter current Date and time like yyyy-mm-dd HH:MM:SS"),"%Y-%m-%d %H:%M:%S")
        local_time_zone = pytz.timezone("Asia/Tashkent")
        inter_time_zone=pytz.timezone(input("Please input timezone to convert"))
        print((local_time_zone.localize(a).astimezone(inter_time_zone).strftime("%Y-%m-%d %H:%M:%S")))
    except Exception as e:
        print(e)
time_zone()

def diff():
    a=datetime.strptime(input("enter future Date and time like yyyy-mm-dd HH:MM:SS"),"%Y-%m-%d %H:%M:%S")
    while True:
        sys.stdout.write(f"\r{(relativedelta(a,datetime.now())).years} years {(relativedelta(a,datetime.now())).months} months {(relativedelta(a,datetime.now())).days} days {(relativedelta(a,datetime.now())).hours} hours {(relativedelta(a,datetime.now())).minutes} minutes {(relativedelta(a,datetime.now())).seconds} seconds")
        sys.stdout.flush()
        time.sleep(1)
diff()


def is_valid_email(email):
    email = input("Enter an email address: ")
    email_regex = r'^[a-zA-Z.+-]+@[a-zA-Z0-9-]+.[a-zA-Z]+$'
    
    if re.match(email_regex, email):
        print(f"'{email}' is a valid email address.")
    print(f"'{email}' is NOT a valid email address.")

is_valid_email()

def strength_check():
    a=input()
    criteria=[False]*4
    if len(a)>=8:
        criteria[0]=True
    for i in a:
        if ord("A")<=ord(i) and ord(i)<=ord("Z"):
            criteria[1]=True
        if ord("a")<=ord(i) and ord(i)<=ord("z"):
            criteria[2]=True
        if ord("0")<=ord(i) and ord(i)<=ord("9"):
            criteria[3]=True
    return True if criteria==[True]*4 else False
strength_check()


def occurance():
    satr=input("Input a text").lower()
    word=input("Searching Word").lower()
    print(satr.count(word))
occurance()       

def date_extract():
    a=datetime.strptime(input("enter Date and time like yyyy-mm-dd"),"%Y-%m-%d").strftime("%Y-%m-%d")
    print(a)
date_extract()
