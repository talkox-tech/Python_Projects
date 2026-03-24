import time
beginTime = int(input("Enter the Time for begin the countdown: "))
delayTime = int(input("enter the time for delay in each count (in Seconds): "))
for i in range(beginTime,0,-delayTime):
    print(i)
    time.sleep(delayTime)
print("Time Up")


