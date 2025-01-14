# Part A 
# 1. Write a program that accepts a variable length of arguments and print the value. Hint: use function

# def multipleArgs(*args):
#     for arg in args:
#         print(arg);

# multipleArgs(1,2,3,"Ashok Budha", True);


# 2. Write a program to create function calc() that will accept two variables and calculate the two variables. Hint: Use addition and subtraction.

# def calc(a, b):
#     print(f"The sum of {a} and {b} is {a+b}.\n The difference of {a} and {b} is {a-b}.")
    
# calc(1, 2);


# 3. Write a program to create a function named employee() using the following conditions:
# a. Program should accept the employee’s name and salary and display both.
# b. If the salary is missing in the function call, then assign default value 9000 to salary.

# def employee(name, salary=9000):
#     print(f"The name of employee is {name} and salary is ${salary}")

# employee("Ashok Budha", 10000000)




# 4. Write a Python program to create the following:
# a. Create an outer function that will accept two parameters, y and z.
# b. Create an inner function inside an outer function that will calculate the addition of y and z.
# c. Lastly, the outer function will add 5 into addition and return it


# def outerFunction(y, z):
#      def innerFunction(y, z):
#          return y + z
     
#      return 5 + innerFunction(y,z)
 
# result = outerFunction(3,4)
# print(f"The result is {result}")
         












# 5. Based on the example given, assign a new name to the function and call it using the new name


# def student(name, age):
#     print(name, age)
 

# employee = student;
# employee("Kelvin", 26)




# 6. Generate a Python list of all the even numbers between 2 to 50.
# my_list=[];
# for i in range(2, 50,2):
#     my_list.append(i);
    
# print(my_list)
    


# 7. Find the largest number from the given list [4, 28, 97, 56, 16].

# my_list =[4, 28, 97, 56, 16]
# print(max(my_list))




# Part B 
# 1. Write the following program to find sum of two numbers using a function.
# Sample input/output:
# Enter first number: 23
# Enter second number: 7
# Sum of the given two numbers is: 30

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print(f"The sum of given two numbers is: {num1 + num2}")





# 2. Write a Python program to read name of student, TP Number and enter his/her all subject marks in list. Compute the total and percentage (Average) of a student. At the end display Name of Programming with Python Lab6student, TP Number, Total, Percentage and Grade of that semester by using function as defined
# below. Score Grade
# 80-100 A+
# 75-79 A
# 70-74 B+
# 65-69 B
# 60-64 C+
# 55-59 C
# 50-54 C
# 40-49 D
# 0-39 F
# a) Use Display function to print output.
# b) Use mark function to accept parameter and return total to Display function.
# c) Use average function by passing parameter which is generated in mark function.
# d) Use grade function by passing parameter which is generated in average function.


name =input("Enter the name of student:")
tpNumber = int(input("Enter TP number: "))
marks = input("Enter marks saperated by comma(,): ")
marks = list(marks.split(','))   
    
def mark(marks):
    total = 0;
    for i in marks:
        total = total + int(i)
    return total

def average(total,n):
    return total/n

def grade(av):
   
    g =""
    if(av >=80  and av <=100):
        g = "A+"
    elif(av >=75 and av <=79):
        g = 'A'
    elif(av >=70 and av <=74):
        g = 'B+'
    elif(av >=65 and av <=69):
        g = 'B'
    elif(av >=60 and av <=64):
        g = 'C+'
    elif(av >=55 and av <=59):
        g = 'C'
    elif(av >=50 and av <=54):
        g = 'D+'
    elif(av >=40 and av <=49):
        g = 'D'
    elif(av >=0 and av <=39):
        g = 'F'
    
    return g
    

def display(name, tpNumber, marks):  
    total = mark(marks)
    # print(total)
    av = average(total,len(marks))
    g = grade(av)
    print(f"Programming with Python Lab6student \nName ={name} \nTP Number = {tpNumber} \nTotal = {total} \nAverage = {av} \nGrade = {g}")
    
display(name,tpNumber, marks)
    

