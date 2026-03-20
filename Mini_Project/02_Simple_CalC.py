#Simple_Calculator
print("\n--- Calculator---")
a = float(input("Enter a number"))
b = float(input("Enter second number"))
print("\n---Result--- ")
print(f"The sum of {a} & {b} = {a+b}")
print(f"The Difference is {a} & {b} = {a-b}") if a>b else print(f"The Difference is {a} & {b} = {b-a}")
print(f"The product is {a} & {b} = {a*b}")
print(f"The Divide is {a//b}") if b!=0 else print("Divide is not possible by 0")   ##use "//"" if you don't result in not double value form