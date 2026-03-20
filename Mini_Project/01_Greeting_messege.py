from datetime import datetime

current_time = datetime.now()
hour = current_time.hour

name = input("What is your name?👀\n --> ")
language = input("What is your favorite programming language?🤔\n -->")
print(hour)

if(hour>=0 and hour < 12 ):
    greet = "Good Morning "
elif(hour>= 12 and hour < 16):
    greet = "Good Afternoon "
elif(hour>=16 and hour< 20 ):
    greet = "Good Evening "
else :
    greet = "Good Night "

print("\n-----------------")
print(f"{greet}! {name}")
print("Start your {} journey! {} is a lovely and interesting language".format(language))
