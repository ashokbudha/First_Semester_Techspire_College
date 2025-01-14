# Practice Question Set 1
# Part A:
# 1. Print numbers from 1 to 10 using a for loop.
# 2. Write a function to add two numbers and return the result.
# 3. Use a while loop to print the first 5 even numbers.
# 4. Write a program to calculate the sum of numbers from 1 to 20 using a for loop.
# 5. Create a function to check if a number is positive or negative.
# 6. Write a program to print the multiplication table for the number 11.
# 7. Write a program to print all numbers between 1 and 10 except 5 (use an if condition).
# 8. Create a function that returns the square of a given number.
# 9. Use a for loop to print each character in the string "Python".
# 10. Write a program to find the smallest number in a list using a for loop.


# 1. Print numbers from 1 to 10 using a for loop.
# Solution
# for i in range(1,11):
#     print(i)
    
    
    
# 2. Write a function to add two numbers and return the result.
# Solution
# def add_two_num(a,b):
#     return a+b
# result = add_two_num(4,5)
# print(f"Result is {result}")



# 3. Use a while loop to print the first 5 even numbers.
# Solution
# num = 0 
# count = 1 
# while count<=5:
#     if num%2==0:
#         print(num)
#         count = count + 1 
#     num +=1




# 4. Write a program to calculate the sum of numbers from 1 to 20 using a for loop.
# Solution
# sum =0
# for i in range(1,21):
#     sum += i
# print(f"sum is {sum}")



# 5. Create a function to check if a number is positive or negative.
# Solution

# def check_positive_negative(n):
#     if n>0:
#         print("Positive")
#     elif n<0:
#         print("Negative")
#     else:
#         print("Zero")

# check_positive_negative(-3)




# 6. Write a program to print the multiplication table for the number 11.
# Solution
# num = 11
# for i in range(1,11):
#     print(f"{num} * {i} = {num * i}")




# 7. Write a program to print all numbers between 1 and 10 except 5 (use an if condition).
# Solution
# for i in range(1,11):
#     if i == 5:
#         continue
#     print(i)
    



# 8. Create a function that returns the square of a given number.
# Solution
# def find_square(n):
#     return n*n

# result = find_square(5)
# print(f"Square is {result}")




# 9. Use a for loop to print each character in the string "Python".
# Solution
# for i in "Python":
#     print(i)




# 10. Write a program to find the smallest number in a list using a for loop.
# Solution
# my_list = [1,5,3,8,0,4,-5,9]

# smallest = my_list[0]
# for i in range(len(my_list)):
#     if my_list[i] < smallest:
#         smallest = my_list[i]
# print(f"smallest number in list is {smallest}")





# Part B:
# 1. Write a program that prints all numbers between 1 and 50 that are divisible by 3.
# 2. Use a while loop to print the sum of all even numbers from 1 to 100.
# 3. Create a program that prints the reverse of a given string using a for loop.
# 4. Write a program to count how many times the number 7 appears in a list using a while
# loop.
# 5. Use a for loop to print the multiplication table for a given number.
# 6. Write a program to print the first 10 terms of the Fibonacci sequence using a while loop.
# 7. Create a program that prints all prime numbers between 1 and 100 using a for loop.
# 8. Use a while loop to find the factorial of a number entered by the user.
# 9. Write a program that finds the sum of digits in a number using a while loop.
# 10. Create a program that prints a pattern of stars in the following format using a for loop:
# *
# **
# ***
# ****
# *****



# 1. Write a program that prints all numbers between 1 and 50 that are divisible by 3.
# Solution
# for i in range(1,51):
#     if i % 3 == 0:
#         print(i)




# 2. Use a while loop to print the sum of all even numbers from 1 to 100.
# Solution
# num = 1
# sum = 0
# while (num <= 100):
#     if num % 2 == 0:
#         sum += num
#     num +=1
# print(f"Sum of all number is {sum}")
    
    




# 3. Create a program that prints the reverse of a given string using a for loop.
# Solution
# my_string = "Ashok Budha"
# for i in range(1, len(my_string)+1):
#     print(my_string[-i], end ="")




# 4. Write a program to count how many times the number 7 appears in a list using a while
# my_list = [1,5,6,7,89,7,4,7,4,7]
# count = 0
# for i in my_list:
#     if i == 7:
#         count +=1

# print(f"7 is repeated {count} times")




# loop.
# 5. Use a for loop to print the multiplication table for a given number.
# Solution
# user_input = int(input("Enter a number:"))
# for i in range(1,11):
#     print(f"{user_input} * {i} = {user_input * i}")





# 6. Write a program to print the first 10 terms of the Fibonacci sequence using a while loop.
# Solution
# a = 0
# b = 1
# count = 0
# while count < 10:
#     print(a)
#     a,b = b,a+b
#     count +=1





# 7. Create a program that prints all prime numbers between 1 and 100 using a for loop.
# Solution
# prime_list =[]
# for i in range(1,101):
#     count = 0
#     for j in range(2,i//2):
#         if i % j == 0:
#             count +=1
    
#     if count ==0 and i !=1:
#         prime_list.append(i)
        
# print(prime_list) 


# Alternative method 





# 8. Use a while loop to find the factorial of a number entered by the user.
# Solution
# num = int(input("Enter a number: "))
# fact = 1
# if num<0:
#     print("We cannot calculate factorial of negative number")
# else:
#     while num >0:
#         fact *=num
#         num -=1
#     print(f"Factorial is {fact}")




# 9. Write a program that finds the sum of digits in a number using a while loop.
# Solution
# num = int(input("Enter a number: "))
# sum = 0
# for i in str(num):
#     sum += int(i)
# print(f"Sum is {sum}")




# 10. Create a program that prints a pattern of stars in the following format using a for loop:
# *
# **
# ***
# ****
# *****

# Solution
# for i in range(5):
#     for i in range(i+1):
#         print("*", end = "")
#     print("\n")





# Practice Question Set 2
# 1. Write a Python function to calculate the sum of all numbers in a given list using a for
# loop.
# 2. Write a function that prints all even numbers between 1 and 20 using a while loop.
# 3. Create a function that accepts a number as an argument and prints all its divisors using a
# for loop.
# 4. Write a function to count how many times the letter 'a' appears in a given string using a
# for loop.
# 5. Write a Python function that returns the factorial of a given number using a for loop.
# 6. Create a function that prints the Fibonacci sequence up to a given number using a while
# loop.
# 7. Write a function that calculates the average of all numbers in a list and returns the result
# using a for loop.
# 8. Create a function to check if a number is prime, using a for loop to iterate through
# possible divisors.
# 9. Write a function that prints the multiplication table of a given number up to 10 using a
# for loop.
# 10. Create a function that prints all numbers from 1 to 100 that are divisible by both 3 and 5
# using a while loop.
# 11. Write a Python function to reverse a given string.
# 12. Write a Python program to generate a list of squares of numbers from 1 to N.
# 13. Create a program that asks the user to input the depth of a well in meters. If the depth is
# above 10 meters, display 'The well is deep.' If it is 10 meters or less, display 'The well is
# shallow.' Keep asking for the depth until the user inputs -1 to exit.
# 14. Create a program that prompts the user to enter a number and determines whether it is
# divisible by 3, 5, or neither. Continue asking for input until the user enters "exit".
# 15. Write a Python program that generates the squares and cubes of numbers from 1 to 5. Use
# a loop to iterate through the numbers and print the results in the format: a2 = b, a3 = c.
# 16. Create a Python program that converts temperatures.
# o Ask the user to input a temperature in Celsius or Fahrenheit and the desired
# conversion (e.g., C to F or F to C).
# o Use a function to perform the conversion.

# o Keep asking for conversions until the user types "Stop."
# 17. Write a Python program which accepts the radius of a circle from the user and computes
# the area.


# 1. Write a Python function to calculate the sum of all numbers in a given list using a for
# loop.
# 2. Write a function that prints all even numbers between 1 and 20 using a while loop.
# 3. Create a function that accepts a number as an argument and prints all its divisors using a
# for loop.
# 4. Write a function to count how many times the letter 'a' appears in a given string using a
# for loop.
# 5. Write a Python function that returns the factorial of a given number using a for loop.
# 6. Create a function that prints the Fibonacci sequence up to a given number using a while
# loop.
# 7. Write a function that calculates the average of all numbers in a list and returns the result
# using a for loop.
# 8. Create a function to check if a number is prime, using a for loop to iterate through
# possible divisors.
# 9. Write a function that prints the multiplication table of a given number up to 10 using a
# for loop.
# 10. Create a function that prints all numbers from 1 to 100 that are divisible by both 3 and 5
# using a while loop.
# 11. Write a Python function to reverse a given string.
# 12. Write a Python program to generate a list of squares of numbers from 1 to N.
# 13. Create a program that asks the user to input the depth of a well in meters. If the depth is
# above 10 meters, display 'The well is deep.' If it is 10 meters or less, display 'The well is
# shallow.' Keep asking for the depth until the user inputs -1 to exit.
# 14. Create a program that prompts the user to enter a number and determines whether it is
# divisible by 3, 5, or neither. Continue asking for input until the user enters "exit".
# 15. Write a Python program that generates the squares and cubes of numbers from 1 to 5. Use
# a loop to iterate through the numbers and print the results in the format: a2 = b, a3 = c.
# 16. Create a Python program that converts temperatures.
# o Ask the user to input a temperature in Celsius or Fahrenheit and the desired
# conversion (e.g., C to F or F to C).
# o Use a function to perform the conversion.

# o Keep asking for conversions until the user types "Stop."
# 17. Write a Python program which accepts the radius of a circle from the user and computes
# the area.



# PRACTISE QUESTIONNS SET 3
# Section A:
# 1. What type of variable assignment does Python support?
# a. Static
# b. Dynamic
# c. Manual
# d. Implicit
# 2. What is the correct syntax for an if statement in Python?
# a. if x > 5 then:
# b. if x > 5:
# c. if (x > 5) {
# d. if x > 5 do:
# 3. What is the output of this code bool(“Hello”)?
# a. True
# b. False
# c. None
# d. Error
# 4. What will happen if the following code is executed?
# for i in range(1, 10, -3):
# print(i)
# a. It will print numbers from 1 to 10 with a step of -3.
# b. It will throw a ValueError because the step is negative and the start is less
# than the end.
# c. It will throw a SyntaxError.
# d. It will print nothing.
# 5. What is the output of this code print("Hello" + 1530)?
# a. Hello1530
# b. Error
# c. None
# d. 1530Hello
# 6. Which of these is NOT true about a compiler?
# a. It generates machine code.
# b. It is slower than an interpreter during the first execution.
# c. It executes the program line by line.
# d. Errors are displayed after the entire code is compiled.
# 7. What happens if the following code is executed and the user inputs "ten"?

# number = int(input("Enter a number: "))
# print(f"The double of the number is {number * 2}")
# a. It will print "The double of the number is ten".
# b. It will throw a ValueError.
# c. It will print 20.
# d. It will throw a TypeError.

# 8. What will be the output if the user enters 10, 20, and 30?

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))
# print("The average is:", (a + b + c) / 3)

# a. The average is 20
# b. The average is 20.0
# c. 20
# d. 60
# 9. What does the “is” operator compare?
# a. The values of two objects
# b. The memory locations (identity) of two objects
# c. Both values and memory locations
# d. The type of two objects
# 10. What will the following code output?

# a = 0
# b = 0
# print(a > b)

# a. True
# b. False
# c. Error
# d. None

# Section B:
# 1. Write a Python function to reverse a given string.
# 2. Write a function that prints all even numbers between 1 and 20 using a while loop.
# 3. Write a Python program to determine whether the speed limit exceeds 110 km per
# hour. If the speed exceeds 110, then fine = 300, otherwise fine = 0. Display fine.
# 4. Draw a Flowchart and Write a Python Program for Multiplication Tables up to 10.
# 5. Write a program that prompts the user to prints all numbers between 1 and 50 that
# are divisible by 3.
# 6. Ask the user to enter a number. If the number is even, print "The number is even." If
# the number is odd, print "The number is odd." Continue asking for a number until
# the user enters 0.
# 7. Write a program to count how many times the number 7 appears in a list using a while
# loop.
# 8. Write a program that finds the sum of digits in a number.
# 9. Write a python program to ask for the score input and print the respective grade as
# follow:

# Score Grade
# Above 80 A
# 60 - 79 B
# 40 – 59 C
# Below 40 D
# 10. Accept 2 input values from user and do arithmetic operation. (+, -, *, /, %). (HINT: simple
# calculator)



# 1. Write a Python function to reverse a given string.
# 2. Write a function that prints all even numbers between 1 and 20 using a while loop.
# 3. Write a Python program to determine whether the speed limit exceeds 110 km per
# hour. If the speed exceeds 110, then fine = 300, otherwise fine = 0. Display fine.
# 4. Draw a Flowchart and Write a Python Program for Multiplication Tables up to 10.
# 5. Write a program that prompts the user to prints all numbers between 1 and 50 that
# are divisible by 3.
# 6. Ask the user to enter a number. If the number is even, print "The number is even." If
# the number is odd, print "The number is odd." Continue asking for a number until
# the user enters 0.
# 7. Write a program to count how many times the number 7 appears in a list using a while
# loop.
# 8. Write a program that finds the sum of digits in a number.
# 9. Write a python program to ask for the score input and print the respective grade as
# follow:

# Score Grade
# Above 80 A
# 60 - 79 B
# 40 – 59 C
# Below 40 D
# 10. Accept 2 input values from user and do arithmetic operation. (+, -, *, /, %). (HINT: simple
# calculator)