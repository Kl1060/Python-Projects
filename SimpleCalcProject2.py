num1, op, num2 = input("Enter an equation\n").split()

num1 = int(num1)
num2 = int(num2)

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
print("= " + repr(ans))
