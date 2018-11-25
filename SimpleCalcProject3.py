flag = 1
while flag == 1:
    num1, op, num2 = input("Enter an equation\n").split()
    if num1 == 'ANS' or num1 == 'ans':
        num1 = ans
        num2 = int(num2)
    elif num2 == 'ANS' or num2 == 'ans':
        num2 = ans
        num1 = int(num1)
    else:
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
    ans = int(ans)
    userinp = input("Calculate another equation? (y/n)\n")
    if userinp == 'y':
        flag = 1
    elif userinp == 'n':
        flag = 0

