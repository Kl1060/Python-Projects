num1 = int(input("Enter a number\n"))
op = input("Enter an operation\n")
num2 = int(input("Enter a second number\n"))

if op == '+':
    ans = num1 + num2
elif op == '-':
    ans = num1 - num2
elif op == '*':
    ans = num1 * num2
elif op == '/':
    ans = num1 / num2
else:
    print(op + "is not a valid operation")

# repr takes the ans and makes it into a string to print out
print("The answer is: " + repr(ans))

