from fastapi import FastAPI
import os
os.system("pip install fastapi")
os.system("pip install uvicorn")
app = FastAPI()
 
# Define a route at the root web address ("/")
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


print("this one is going execute through Jenkins") 

print("HI")
print("This Is Rahul Jha")
print("Stay at home")
print("Welcome to Python program")

print("###################")

from itertools import permutations
for x in permutations('asd'):
    print(x)

print("###################")

import time
for x in range(5,4,-3):
    print(x)
    time.sleep(1)
print("offfff")

print("###################")

import datetime
new_year =  datetime.date(2021,11,11)-datetime.date.today()
print(new_year)

print("###################")


"""
value = 1
while value<50:
    print("from 1 to 1oo is ", value)
    #time.sleep(3)
    value = value + 1

print("###################")

import random
ans1 = "i'm Rahul"
ans2 = "You are jealous"
ans3 = "I'm Hot"
ans4 = "Today is Holiday"
ans5 = "We Love India"
ans6 = "i'm developed with python"
ans7 = "i hate Riya"
ans8 = "You should marry with me"
ans9 = "Aap bhot bhukkad ho"
ans10 = "i'm awesome !!"
ans11 = "Maths is boring"
ans12 = "i love Urvashi"
ans13 = "Uh are looser"
ans14 = "Don't call me"
ans15 = "Uh are in trapped Dear"

name = input("Enter Your name:")
input(name +" "+ "What is question for today?")
choice = random.randint(1,16)

if choice == 1:
    answer = ans1

elif choice == 2:
    answer = ans2

else:
    answer = ans15

print("Thanks for Playing today with us",name, "hope you enjoyed today")
print(answer)

"""
