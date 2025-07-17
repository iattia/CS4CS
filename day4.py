print("Hello World")

def phase1():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    sum = num1 + num2
    print(f"The sum is: {sum}")

def phase2():
    num1 = int(input("Enter the first number: "))
    operator = input("Enter the operation (+, -, *, /): ")
    num2 = int(input("Enter the second number: "))
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    elif operator == '/':
        if num2 != 0:
            answer = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Error: Invalid operator.")
        return
    print(f"The result is: {answer}")

def phase3():
    while True:
        phase2()
        loop = input("Do you want to perform another operation? (yes/no): ").lower()
        if  loop == 'no':
            break

def phase4(num1, operator, nume2):
    if operator == '+':
        return num1 + nume2
    elif operator == '-':
        return num1 - nume2
    elif operator == '*':
        return num1 * nume2
    elif operator == '/':
        if nume2 != 0:
            return num1 / nume2
        else:
            print("Error: Division by zero is not allowed.")
            return None
    else:
        print("Error: Invalid operator.")
        return None