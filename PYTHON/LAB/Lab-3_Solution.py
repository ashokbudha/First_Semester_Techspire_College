#UNDERSTAND THE CONCEPTS, SYNTAX AND TRY TO CODE ON YOUR OWN 
#variable should not be same
#try to print using different print functions.

# Task 1: Accept a number and display it.
num = float(input("Enter a number: "))
print("The number you entered is:", num)

# Task 2: Accept 2 numbers and display their addition.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("The addition of the numbers is:", num1 + num2)

# Task 3: Accept 2 input values and perform arithmetic operations.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter an arithmetic operation (+, -, *, /, %): ")
if operation == "+":
    print("Result:", num1 + num2)
elif operation == "-":
    print("Result:", num1 - num2)
elif operation == "*":
    print("Result:", num1 * num2)
elif operation == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Division by zero is not allowed.")
elif operation == "%":
    if num2 != 0:
        print("Result:", num1 % num2)
    else:
        print("Modulo by zero is not allowed.")
else:
    print("Invalid operation.")

# Task 4: Accept 2 numbers and swap them.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Before swapping: num1 =", num1, "num2 =", num2) #This step is optional
num1, num2 = num2, num1                                 #this is used for swapping
print("After swapping: num1 =", num1, "num2 =", num2)   #displays output

# Task 5: Accept 5 subject marks and calculate total and percentage.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter first number: "))
num3 = float(input("Enter first number: "))
num4 = float(input("Enter first number: "))
num5 = float(input("Enter first number: "))

total_marks=num1+num2+num3+num4+num5
percentage_=total_marks / 5 *100
print(total_marks, percentage_)

#or you can use below concept

marks = []
for i in range(1, 6):
    marks.append(float(input(f"Enter marks for subject {i}: ")))
total = sum(marks)
percentage = total / 5
print("Total marks:", total)
print("Percentage:", percentage)


# Task 6: Calculate salary of an employee.
#understanding the question is important!

basic = float(input("Enter Basic salary: "))
grade_pay = 2 * basic
da = 0.7 * basic
ta = 200
hra = 0.2 * basic
salary = grade_pay + da + ta + hra
print("The salary of the employee is:", salary)
