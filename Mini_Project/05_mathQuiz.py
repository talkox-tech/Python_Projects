import random
def generateQues():
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    operator = random.choice(['+','-','/','*'])
    
    if operator == '+':
        ans = num1 + num2
    elif operator == '-':
            ans = num1 - num2

    elif operator == '*':
        ans = num1 * num2
    else:
        if(num2 != 0):
            ans = float(num1/num2)
        else:
            print("Not Possible")
    return f"{num1} {operator} {num2} will be *for divisin use 'Not possible' ", ans
print("\n---Math Quiz---")
round = 5
maxScor = 0
for i in range(round):
    print("user score: {}\n".format(maxScor))
    question, correctAns = generateQues()
    print(question)
    userAns = int(input("Enter the Answer: "))
    if(userAns == correctAns):
        maxScor+=10
    else:
        if maxScor>0:
            maxScor-=10
if maxScor>0:
    print("Wow!! Your highest Score is {}".format(maxScor))
else:
    print("Needs imporovement!! Keep Learning and Try Again")

    
    
    
