# My name: Kala Chan
# Who I collaborated with: No One

print("Addition or Subtraction")

question = input("Do you want to do addition or subtraction? (a/s) ")

num1 = int(input("First number: "))
num2 = int(input("Second number: "))

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

if question == "a":
    print("Result:", add(num1, num2))
else:
    print("Result:", sub(num1, num2))