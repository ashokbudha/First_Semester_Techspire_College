# TODO TODO TODO BASIC CONCEPT
#  1.Write a Python program to swap two variables without using a third variable.
#  2.Write a program that calculates the area of a circle, given the radius as input.
#  3.Write a program to check if a number is odd or even.
#  4.Write a Python script that converts temperature from Celsius to Fahrenheit.
#  5.Take two inputs from the user (name and age) and print a message like: "Hello, [name], you are [age] years old!".
#  6.Write a Python program to find the square root of a given number using the exponentiation operator (**).
#  7.Write a program that checks if a string is a palindrome (reads the same forward and backward).
#  8.Write a Python program that calculates the remainder when one number is divided by another.

#  9.Write a program to check if a given number is positive, negative, or zero.
#  10.Take a string as input and print its first and last character.
# 11.Write a Python program to take three numbers as input and print the largest one.
#  12.Write a program that calculates the sum of three numbers. If the numbers are equal, return three times their sum.
#  13.Write a Python program that checks whether a given year is a leap year.
#  14.Write a program that accepts a string from the user and prints it in all uppercase and lowercase letters.
#  15.Write a program that asks the user for a number and prints whether it is divisible by 5 or not.
#  16.Write a program to convert a number of seconds into hours, minutes, and seconds.
#  17.Write a Python program that accepts the lengths of three sides of a triangle and checks if it forms a valid triangle.
#  18.Write a Python program to find the largest of four numbers.
#  19.Write a program that reads an integer n and prints the first n multiples of 3.
# 20. Write a program that converts a given number into binary, octal, and hexadecimal.
# 21. Write a Python program to find the maximum and minimum of three numbers without using conditional statements or loops.

#  22.Write a program that checks whether a given character is a vowel or a consonant.
# 23. Write a Python program that takes a number and prints whether it's divisible by 2, 3, or both.
# 24. Write a program to print the ASCII value of a given character.
# 25. Write a Python program to calculate the sum of all digits of a given number.
# 26. Write a program that checks if a given number is within a range (e.g., between 10 and 100).
# 27. Write a Python program to check if a given number is a perfect square.
# 28. Write a Python program to check if a given string is a valid identifier (only contains letters, digits, or underscores and doesn't start with a digit).
# 29. Write a Python program to convert a given string to title case (capitalize the first letter of each word).
# 30. Write a program that reads a number n from the user and prints whether it's a prime number or not.
# 31. Write a program that accepts a number and prints the sum of its factors.











# TODO: 1.Write a Python program to swap two variables without using a third variable.

# Original Code
# x=10
# y=5
# x,y=y,x
# print(x,y)



# Suggested Improvement
# x = 10
# y = 5
# x, y = y, x
# print(f"After swapping: x = {x}, y = {y}")








# TODO: 2.Write a program that calculates the area of a circle, given the radius as input.

# Original Code

# import math
# radius=int(input("Enter the radius: "))
# area = math.pi * radius**2
# print(f"Area is {area:.2f}")



# Suggested Improvement
# import math

# radius = float(input("Enter the radius: "))  # Use float for more precision
# area = math.pi * radius**2
# print(f"Area of the circle with radius {radius} is {area:.2f}")









# TODO: 3.Write a program to check if a number is odd or even.


# Original Code
# num = int(input("Enter a number: "))
# if(num % 2 == 0):
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")








# Suggested Improvement
# num = int(input("Enter a number: "))
# result = "even" if num % 2 == 0 else "odd"
# print(f"{num} is {result}.")









# TODO: 4.Write a Python script that converts temperature from Celsius to Fahrenheit.

# Original Code
# celsius = int(input("Enter a temperature in celcius: "))
# fahrenheit = 1.8 * celsius + 32
# print(f"{celsius} celsius = {fahrenheit} fahrenheit")

# Suggested Improvement
# celsius = float(input("Enter a temperature in Celsius: "))
# fahrenheit = (celsius * 9/5) + 32  # More precise formula
# print(f"{celsius}°C = {fahrenheit:.2f}°F")









# TODO: 5.Take two inputs from the user (name and age) and print a message like: "Hello, [name], you are [age] years old!".

# Original Code
# name = input("Whats your name: ")
# age = int(input("Enter your age: "))
# print(f"Hello, {name}, you are {age} years")

# Suggested Improvement
# name = input("What's your name? ")
# age = int(input("Enter your age: "))
# print(f"Hello, {name}! You are {age} years old.")








# TODO: 6.Write a Python program to find the square root of a given number using the exponentiation operator (**).

# Original Code
# num = int(input("Enter a number: "))
# sqr_root = num ** (1/2)
# print(f"Square root of {num} is {sqr_root}")

# Suggested Improvement
# num = float(input("Enter a number: "))
# sqr_root = num ** 0.5  # More common to use 0.5 for square root
# print(f"Square root of {num} is {sqr_root:.2f}")









# TODO: 7.Write a program that checks if a string is a palindrome (reads the same forward and backward).

# Original Code
# string = input("Enter a string: ")
# rev_string=string[::-1]
# if(string == rev_string):
#     print("palindrome")
# else:
#     print("Not Palindrome")




# Suggested Improvement
# string = input("Enter a string: ")
# rev_string = string[::-1]

# if string.lower() == rev_string.lower():  # Case insensitive check
#     print("Palindrome")
# else:
#     print("Not Palindrome")








# TODO: 8.Write a Python program that calculates the remainder when one number is divided by another.

# Original Code
# num = int(input("Enter a number: "))
# divider = int(input("Enter a divider: "))
# remainder = num % divider
# print(f"{num}/{divider} gives remainder {remainder}")



# Suggested Improvement
# num = int(input("Enter a number: "))
# divider = int(input("Enter a divider: "))

# if divider == 0:  # Handle division by zero
#     print("Divider cannot be zero.")
# else:
#     remainder = num % divider
#     print(f"The remainder of {num} divided by {divider} is {remainder}.")










# TODO: 9.Write a program to check if a given number is positive, negative, or zero.

# Original Code
# num = int(input("Enter a number: "))
# if(num>0):
#     print(f"{num} is positive")
# elif(num<0):
#     print(f"{num} is negative")
# else:
#     print("Zero") 



# Suggested Improvement
# num = int(input("Enter a number: "))
# if num > 0:
#     print(f"{num} is positive.")
# elif num < 0:
#     print(f"{num} is negative.")
# else:
#     print("The number is zero.")

    
    
    
    
    
    
    
    
# TODO: 10.Take a string as input and print its first and last character.

# Original Code
# string = input("Enter a string: ")
# print(f"First string is '{string[0]}' and last string is '{string[-1]}'")



# Suggested Improvement
# string = input("Enter a string: ")

# if string:  # Check if the string is not empty
#     print(f"First character is '{string[0]}' and last character is '{string[-1]}'.")
# else:
#     print("The string is empty.")









# ****
#TODO: Write a Python program to take three numbers as input and print the largest one.
# Original Code
# x,y,z=input("Enter three numbers saperated by comma: ").split(",")
# x, y, z=int(x), int(y), int(z)
# if(x==y==z):
#     print("All are equal.")
# elif(x>=y) and (x >=z):
#     print(f"{x} is largest")
# elif(y>=x) and (y>=z):
#     print(f"{y} is largest")
# else:
#     print(f"{z} is largest")



# Suggested Improvement
# x, y, z = map(int, input("Enter three numbers separated by comma: ").split(","))
# if x == y == z:
#     print("All are equal.")
# else:
#     largest = max(x, y, z)
#     print(f"{largest} is largest.")









# TODO: Write a program that calculates the sum of three numbers. If the numbers are equal, return three times their sum.

# Original Code
# x, y, z = input("Enter theree numbers saperated by comma: ").split(",")
# x, y, z = int(x), int(y), int(z)
# sum = x+y+z
# if(x==y==z):
#     print(f"result is {3*sum}")
# else:
#     print(f"result is {sum}")



# Suggested Improvement
# x, y, z = map(int, input("Enter three numbers separated by comma: ").split(","))
# total = x + y + z
# result = total * 3 if x == y == z else total
# print(f"Result is {result}.")










# TODO: Write a Python program that checks whether a given year is a leap year.

# Original Code
# year = int(input("Enter a year: "))
# if((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
#     print(f"{year} is leap year")
# else:
#     print(f"{year} is not leap year")



# Suggested Improvement
# year = int(input("Enter a year: "))

# if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")









# TODO: Write a program that accepts a string from the user and prints it in all uppercase and lowercase letters.

# Original Code
# string = input("Enter a string: ")
# ucase_string =string.upper()
# lcase_string = string.lower()
# print(f" {string} in uppercase '{ucase_string}' and in lowercase '{lcase_string}'")



# Suggested Improvement
# string = input("Enter a string: ")
# print(f"In uppercase: '{string.upper()}' and in lowercase: '{string.lower()}'.")








# TODO: Write a program that asks the user for a number and prints whether it is divisible by 5 or not.

# Original Code
# num = int(input("Enter a number: "))
# if(num % 5 == 0):
#     print(f"{num} is divisible by 5")
# else:
#     print(f"{num} is not divisible by 5")



# Suggested Improvement
# num = int(input("Enter a number: "))
# divisible = "is" if num % 5 == 0 else "is not"
# print(f"{num} {divisible} divisible by 5.")








# TODO: Write a program to convert a number of seconds into hours, minutes, and seconds.
# Original Code
# seconds = int(input("Enter Seconds: "))
# hours = seconds//3600
# seconds = seconds % 3600
# minutes = seconds //60
# seconds = seconds % 60
# print(f"{hours}hr {minutes}min {seconds}sec")



# Suggested Improvement
# seconds = int(input("Enter seconds: "))
# hours = seconds // 3600
# seconds %= 3600
# minutes = seconds // 60
# seconds %= 60

# print(f"{hours} hours, {minutes} minutes, {seconds} seconds.")












# TODO: Write a Python program that accepts the lengths of three sides of a triangle and checks if it forms a valid triangle.

# Original Code
# a, b, c = input("Enter three sides of triangle saperated by comma: ").split(",")
# a, b, c = int(a), int(b), int(c)
# if(a+b>c) or (a+c>b) or (b+c>a):
#     print(f"{a}, {b}, {c} are valid sides of a triangle.")
# else:
#     print(f"{a}, {b}, {c} are not valid sides of a triangle.")

# Suggested Improvement
# a, b, c = map(int, input("Enter three sides of a triangle separated by comma: ").split(","))
# if (a + b > c) and (a + c > b) and (b + c > a):
#     print(f"{a}, {b}, {c} are valid sides of a triangle.")
# else:
#     print(f"{a}, {b}, {c} are not valid sides of a triangle.")











# TODO: Write a Python program to find the largest of four numbers.

# mycode

# a, b, c, d = input("Enter four numbers saperated by comma: ").split(",")
# a, b, c, d = int(a), int(b), int(c), int(d)

# if(a==b==c==d):
#     print("All of them are equal.") 
# elif (a>=b and a>=c and a>=d):
#     print(f"{a} is largest")
# elif (b>=a and b>=c and b>=d):
#     print(f"{b} is largest")
# elif (c>=a and c>=b and c>=d):
#     print(f"{c} is largest")
# else:
#     print(f"{d} is largest")








# improved code

# a, b, c, d = input("Enter four numbers separated by comma: ").split(",")
# a, b, c, d = int(a), int(b), int(c), int(d)

# if a == b == c == d:
#     print("All of them are equal.")
# else:
#     largest = a  # Assume 'a' is the largest
#     if b > largest:
#         largest = b
#     if c > largest:
#         largest = c
#     if d > largest:
#         largest = d
#     print(f"{largest} is largest")











# TODO: 19. Write a program that reads an integer n and prints the first n multiples of 3.

# original code

# num = int(input("Enter a number: "))
# for i in range(1,num+1):
#     print(f" 3 * {i} = {3*i}")


# improved code
# n = int(input("Enter the number of multiples: "))
# multiples = [3 * i for i in range(1, n + 1)]
# print(f"The first {n} multiples of 3: {multiples}")






# TODO:20. Write a program that converts a given number into binary, octal, and hexadecimal.

# original code

# num = int(input("Enter a number: "))

# binary = bin(num)[2:]
# octal = oct(num)[2:]
# hexadecimal = hex(num)[2:]

# print(f"binary representation of {num} is {binary}")
# print(f"octal representation of {num} is {octal}")
# print(f"hexadecimal representation of {num} is {hexadecimal}")



# improved code
# num = int(input("Enter a number: "))
# print(f"Binary: {bin(num)[2:]}, Octal: {oct(num)[2:]}, Hexadecimal: {hex(num)[2:].upper()}")






# TODO:21. Write a Python program to find the maximum and minimum of three numbers without using conditional statements or loops.

# original code

# a, b, c = map(int, input("Enter three numbers saperated by comma:").split(","))
# print(f"minimum number is {min(a,b,c)} and maximum number is {max(a,b,c)}")



# improved code
# numbers = list(map(int, input("Enter three numbers separated by commas: ").split(",")))
# print(f"Min: {min(numbers)}, Max: {max(numbers)}")







# TODO: 22.Write a program that checks whether a given character is a vowel or a consonant.

# original code

# character = input("Enter a character: ")
# check = "is" if (character=='a' or character == 'e' or character == 'i' or character == 'o' or character == 'u') else "is not"
# print(f"'{character}' {check} vowel")
 
 
# inproved code

# char = input("Enter a character: ").lower()
# if char.isalpha():
#     check = "is" if char in 'aeiou' else "is not"
#     print(f"'{char}' {check} a vowel")
# else:
#     print(f"'{char}' is not a valid alphabetic character")
   

 
    
    
    
# TODO:23. Write a Python program that takes a number and prints whether it's divisible by 2, 3, or both.

# original code

# num = int(input("Enter a number: "))
# if (num % 2 == 0 ) and (num % 3 == 0):
#     print(f"{num} is divisible by both 2 and 3")
# elif num % 2 == 0:
#     print(f"{num} is divisible by 2")
# elif num % 3 == 0:
#     print(f"{num} is divisible by 3")
# else:
#     print(f"{num} is not divisible by both 2 and 3")



#inproved code 

# num = int(input("Enter a number: "))
# divisible_by = []

# if num % 2 == 0:
#     divisible_by.append('2')
# if num % 3 == 0:
#     divisible_by.append('3')

# if divisible_by:
#     print(f"{num} is divisible by {', '.join(divisible_by)}")
# else:
#     print(f"{num} is not divisible by 2 or 3")







# TODO:24. Write a program to print the ASCII value of a given character.

# original code

# character = input("Enter a character: ")
# print(f"The ascii of {character} is {ord(character)}")



# improved code

# char = input("Enter a character: ")
# if len(char) == 1:
#     print(f"The ASCII value of '{char}' is {ord(char)}")
# else:
#     print("Please enter a single character.")




# ****
# TODO:25. Write a Python program to calculate the sum of all digits of a given number.

# original code

# num = input("Enter a multi-digit number: ")
# sum = 0 
# for i in num:
#     sum+=int(i)
# print(f"sum of all digits is {sum}")
    


# improved code
# num = input("Enter a multi-digit number: ")
# digit_sum = sum(int(digit) for digit in num)
# print(f"Sum of digits: {digit_sum}")





# TODO:26. Write a program that checks if a given number is within a range (e.g., between 10 and 100).

# original code

# num = int(input("Enter a number: "))
# check = "is" if num in range(10,100) else "is not"
# print(f"{num} {check} in range 10 and 100")



# improved code
# num = int(input("Enter a number: "))
# if 10 <= num <= 100:
#     print(f"{num} is in the range 10 to 100")
# else:
#     print(f"{num} is not in the range 10 to 100")






# TODO:27. Write a Python program to check if a given number is a perfect square.

# original code

# num = int(input("Enter a number: "))
# sqr_root = int(num ** (1/2))
# check = "is" if sqr_root**2 ==num else "is not"
# print(f"{num} {check} perfect square.")


# ímproved code 
# import math
# num = int(input("Enter a number: "))
# sqrt_num = int(math.sqrt(num))
# if sqrt_num * sqrt_num == num:
#     print(f"{num} is a perfect square.")
# else:
#     print(f"{num} is not a perfect square.")





# ****
# TODO:28. Write a Python program to check if a given string is a valid identifier (only contains letters, digits, or underscores and doesn't start with a digit).

# original code

# import sys
# string = input("Enter a string: ")
# print(ord(string[0]))
# # if ord(string[0])>57 or ord(string[0])<48:
# if not(48<=ord(string[0])<=57):
#     for i in string:
#         print(i)
#         if not(90>=ord(i)>=65 or 122>=ord(i)>=97 or 48<=ord(i)<=57 or ord(i)==95):
#             print(f"{string} is not a valid identifier")
#             sys.exit(0)
        
#     print(f"{string} is a valid identifier")       
# else: 
#     print(f"{string} is not a hi hi valid identifier")


# improved code 
# string = input("Enter a string: ")
# if string.isidentifier():
#     print(f"{string} is a valid identifier")
# else:
#     print(f"{string} is not a valid identifier")





# TODO:29. Write a Python program to convert a given string to title case (capitalize the first letter of each word).

# original code

# string = input("Enter a string: ")
# final_string = string.title()
# print(final_string)



# improved code 
# string = input("Enter a string: ")
# print(string.title())




# ****
# TODO:30. Write a program that reads a number n from the user and prints whether it's a prime number or not.

# original code

# num = int(input("Enter a number: "))
# c=0
# for i in range (1,num):
#     if num % i == 0:
#         c+=1

# if(c==1):
#     print(f"{num} is prime")
# else:
#     print(f"{num} is consonant")


# improved code 

# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             print(f"{num} is not prime")
#             break
#     else:
#         print(f"{num} is prime")
# else:
#     print(f"{num} is not prime")






# TODO:31. Write a program that accepts a number and prints the sum of its factors.

# original code
# num = int(input("Enter a number"))
# sum = 0
# for i in range(1,num+1):
#     if num % i == 0:
#         sum += i
# print(f"sum of all factors is {sum}")



# improved code 
# num = int(input("Enter a number: "))
# factors = [i for i in range(1, num + 1) if num % i == 0]
# print(f"Sum of factors: {sum(factors)}")





# TODO TODO TODO : LOOPS
#1. Write a Python program to print all numbers from 1 to 100.
#2. Write a Python program to calculate the factorial of a number using a for loop.
#3. Write a Python program that prints the multiplication table of a given number.
#4. Write a program that sums all the even numbers from 1 to 100 using a loop.
#5. Write a Python program to reverse a given string using a loop.
#6. Write a program to print the Fibonacci series up to a given number.

#7. Write a Python program to count the number of vowels in a given string.
#8. Write a Python program to find the largest element in a list using a loop.
# #9. Write a Python program to calculate the sum of all digits in a number using a while loop.
# #10. Write a Python program to print a pattern of stars in a pyramid shape (e.g., 5 rows).
# 11.Write a Python program to print the sum of all numbers divisible by 3 and 5 between 1 and 100.
#12. Write a Python program that prints the reverse of a given number (e.g., if input is 1234, output should be 4321).
#13. Write a program to print all prime numbers between two given numbers using a loop.
#14. Write a program that takes an integer input n and prints the first n terms of the arithmetic sequence (e.g., 2, 5, 8, 11,... with a difference of 3).
#15. Write a Python program to print the following pattern for n rows:
# 1
# 12
# 123
# 1234
# 12345
# 16.Write a Python program that prints the first 10 numbers of the Fibonacci series using a while loop.
#17. Write a program to print all perfect numbers between 1 and 1000. (A perfect number is one that is equal to the sum of its divisors, excluding itself.)
#18. Write a Python program to find the sum of all numbers in a list using a for loop.
#19. Write a program to calculate the sum of the squares of the first n natural numbers using a loop.
#20. Write a program that continuously asks the user for input until they enter "exit", at which point the program stops.




#TODO:1. Write a Python program to print all numbers from 1 to 100.

# for i in range (1,101):
#     print(i)
    
    
    
    
    
#TODO:2. Write a Python program to calculate the factorial of a number using a for loop.

# num = int(input("Enter a number: "))
# fact = 1
# if num <0:
#     print("Enter a positive number.")
# else:
#     for i in range(1,num+1):
#         fact*=i
#     print(f"factorail fo {num} is {fact}")









#TODO:3. Write a Python program that prints the multiplication table of a given number.

# n = int(input("Enter a number:"))
# print(f"Multiplication table of {n} is given below:-")
# for i in range(1,11):
#     print(f"{n}*{i}={n*i}")
    





#TODO:4. Write a program that sums all the even numbers from 1 to 100 using a loop.

# sum = 0
# for i in range(1,101):
#     if i % 2 == 0:
#         sum+=i

# print(f"sum of all even numbers from 1 to 100 is {sum}")






#TODO:5. Write a Python program to reverse a given string using a loop.


# string = input("Enter a string: ")
# rev_string=""
# for i in range(len(string)-1,-1,-1):
#     rev_string+=string[i]
  
# print(rev_string)    






# ****
#TODO:6. Write a program to print the Fibonacci series up to a given number.

# num = int(input("Enter a number: "))
# x, y = 0, 1
# for i in range(num):
#     print(x, end="," if i <num-1 else "")
#     x,y=x+y,x
    


    
    



#TODO:7. Write a Python program to count the number of vowels in a given string.

# string = input("Enter a string: ")
# count = 0
# for i in string:
#     if i.lower() in "aeiou":
#         count+=1
# print(f"Number of vowel in {string} is {count}")
        





#TODO:8. Write a Python program to find the largest element in a list using a loop.

# mylist = [1,5,9,3,4]
# largest = mylist[0]
# for i in mylist:
#     if i > largest:
#         largest = i
        
# print(f"Largest number in {mylist} is {largest}")






# #TODO:9. Write a Python program to calculate the sum of all digits in a number using a while loop.


# num = int(input("Enter a multi-digit number: "))
# sum = 0 
# while num != 0:
#     r = num % 10
#     sum += r
#     num //= 10
    
# print(f"sum of all digits is {sum}")
    









# #TODO:10. Write a Python program to print a pattern of stars in a pyramid shape (e.g., 5 rows).

# row = int(input("Enter the number of rows: "))
# for i in range(1,row+1):
#     for j in range(row-i):
#         print(" ", end="")
#     for j in range(2*i-1):
#         print("*", end="" if j<2*i-2 else "\n")







# TODO:11.Write a Python program to print the sum of all numbers divisible by 3 and 5 between 1 and 100.

# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i , end="," if i<100 else "")
        
        
        
        
        
        
        
        
        
#TODO:12. Write a Python program that prints the reverse of a given number (e.g., if input is 1234, output should be 4321).

# num = int(input("Enter a number: "))
# rev_num =0
# while num != 0:
#     r = num % 10
#     rev_num = rev_num * 10 + r
#     num //= 10
# print(f"Reverse number is {rev_num}")
    






#TODO:13. Write a program to print all prime numbers between two given numbers using a loop.


# s, e = map(int, input("Enter the start and end number saperated by comma: ").split(","))
# for i in range(s,e+1):
#     c = 0
#     for j in range(1,i):
#         if i % j ==0:
#             c+=1
            
#     if c == 1:
#         print(i,end=" ")













#TODO:14. Write a program that takes an integer input n and prints the first n terms of the arithmetic sequence (e.g., 2, 5, 8, 11,... with a difference of 3).

# num = int(input("Enter a number: "))
# s=3
# for i in range(num):
#     print(s,end="," if i <num-1 else "")
#     s+=3
    







#TODO:15. Write a Python program to print the following pattern for n rows:
# 1
# 12
# 123
# 1234
# 12345


# rows = int(input("Enter the numbers of rows: "))
# for i in range (1,rows+1):
#     for j in range(1,i+1):
#         print(j, end =" " if j<i else "\n")




# TODO:16.Write a Python program that prints the first 10 numbers of the Fibonacci series using a while loop.

# x,y=0,1
# c=0
# while c<10:
#     print(x, end="," if c<9 else "")
#     x,y=x+y,x
#     c+=1






#TODO:17. Write a program to print all perfect numbers between 1 and 1000. (A perfect number is one that is equal to the sum of its divisors, excluding itself.)

# for i in range(1,1001):
#     sum_divider = 0
#     for j in range(1,i):
#         if i % j == 0:
#             sum_divider +=j
        
#     if i == sum_divider:
#         print(i,end=" ")
        
        







#TODO:18. Write a Python program to find the sum of all numbers in a list using a for loop.

# mylist = [1,2,3,4,5,6,4]
# sum = 0
# for i in mylist:
#     sum+=i
# print(f"sum of all item in {mylist} is {sum}")






#TODO:19. Write a program to calculate the sum of the squares of the first n natural numbers using a loop.

# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1,n+1):
#     sum += i**2
# print(f"sum of square of first {n} natural number is {sum} ")










#TODO:20. Write a program that continuously asks the user for input until they enter "exit", at which point the program stops.

# input_text = input("Enter a input: ")
# while input_text !="exit":
#     input_text = input("Enter a input: ")






# TODO TODO TODO : FUNCTIONS

#1. Write a function to check if a number is prime.
#2. Write a function that takes a list of numbers and returns the sum of all even numbers.
#3. Write a function that accepts a string and returns the string in reverse.
#4. Write a function to calculate the greatest common divisor (GCD) of two numbers.
#5. Write a function that takes a list and an element and returns True if the element exists in the list, otherwise False.
#6. Write a function that returns the length of a given string.
#7. Write a function that takes a number as input and returns True if it is a palindrome, otherwise False.
#8. Write a function that calculates the power of a number (without using ** or pow() function).
#9. Write a function that takes two numbers and returns the larger of the two.
#10. Write a function that takes a list of numbers and returns the smallest number.
#11. Write a function that takes two strings and returns True if they are anagrams (contain the same characters in different orders), otherwise False.
#12. Write a function that takes a list of numbers and returns a new list containing only the prime numbers from the original list.
#13. Write a function that takes a string and returns the most frequent character in the string.
#14. Write a recursive function to calculate the factorial of a number.
#15. Write a function that accepts a list of integers and returns the second largest number in the list.
#16. Write a function to check if a given string is a pangram (contains every letter of the alphabet at least once).
#17. Write a function that takes a number and returns True if it is an Armstrong number (e.g., 153 = 1³ + 5³ + 3³), otherwise False.
#18. Write a function that takes a list of numbers and returns the cumulative sum of the list. For example, given [1, 2, 3], return [1, 3, 6].
#19. Write a function to calculate the sum of digits of a number until it reduces to a single digit (e.g., 9875 → 9 + 8 + 7 + 5 = 29 → 2 + 9 = 11 → 1 + 1 = 2).
#20. Write a function that takes a list of strings and returns the longest string in the list.






#TODO:1. Write a function to check if a number is prime.


# def check_prime(n):
#     c=0
#     for i in range(1,n):
#         if n % i == 0:
#             c+=1
#     if c==1:
#         print(f"{n} is prime")
#     else:
#         print(f"{n} is not a prime ")
          
# check_prime(3)









#TODO:2. Write a function that takes a list of numbers and returns the sum of all even numbers.


# my_list = [1,2,3,4,5,6]

# def even_sum(my_list):
#     sum = 0
#     for i in my_list:
#         if i % 2 == 0:
#             sum += i
#     return sum

# print(f"sum of all even number is {even_sum(my_list)} ")        
        







#TODO:3. Write a function that accepts a string and returns the string in reverse.

# string = input("Enter a string: ")

# def rev_string(string):
#     return string[::-1]

# rev_string = rev_string(string)
# print(f"reverse string of {string} is {rev_string}")
















#TODO:4. Write a function to calculate the greatest common divisor (GCD) of two numbers.




















#TODO:5. Write a function that takes a list and an element and returns True if the element exists in the list, otherwise False.


# my_list = [1,5,7,9,4]
# n = int(input("Enter a number: "))

# def check(my_list,n):
#     return True if n in my_list else False


# if check(my_list,n):
#     print(f"{n} is present in list.")
# else:
#     print(f"{n} is not present in list.")









#TODO:6. Write a function that returns the length of a given string.


# string = input("Enter a string: ")

# def len_string(string):
#     return len(string)

# length = len_string(string)
# print(f"length of {string} is {length}")






#TODO:7. Write a function that takes a number as input and returns True if it is a palindrome, otherwise False.

# n = int(input("Enter a number: "))

# def check_palindrome(n):
#     m = n
#     s = 0
#     while n != 0:
#         r = n % 10
#         s = s*10 + r
#         n = n//10
        
#     return True if s == m else False

# if check_palindrome(n):
#     print(f"{n} is a palindrome number.")
# else:
#     print(f"{n} is not a plaindrome number.")








#TODO:8. Write a function that calculates the power of a number (without using ** or pow() function).


# n = int(input("Enter a number: "))
# m = int(input("Enter a power: "))

# def power(n, m):
#     result = 1
#     if m==n==0:
#         return "infinity"
#     else:
#         for i in range(m):
#             result *= n
#         return result

# result = power(n,m)
# print(f"{n} to the power {m} is {result}.")
    
    












#TODO:9. Write a function that takes two numbers and returns the larger of the two.

# n, m = map(int, input("Enter two numbers saperated by comma:").split(","))

# def larger(n,m):
#     if n>m:
#         return n
#     elif m>n:
#         return m
#     else:
#         return "Equal"

# if larger(n,m) != "equal":
#     print(f"{larger(n,m)} is larger")
# else:
#     print("both are equal.")











#TODO:10. Write a function that takes a list of numbers and returns the smallest number.

# my_numbers =input("Enter number saperated by comma: ")
# my_list = [int(item.strip()) for item in my_numbers.split(",")]

# def smallest(my_list):
#     smallest = my_list[0]
#     for i in my_list:
#         if i < smallest:
#             smallest = i
#     return smallest

# smallest = smallest(my_list)   
# print(f"{smallest} is smallest in the list.")     
    














#TODO:11. Write a function that takes two strings and returns True if they are anagrams (contain the same characters in different orders), otherwise False.











#TODO:12. Write a function that takes a list of numbers and returns a new list containing only the prime numbers from the original list.

# my_numbers = input("Enters number saperated by comma: ")
# my_list = [int(item.strip()) for item in my_numbers.split(",")]
# print(my_list)

# def prime_list(my_list):
#     for i in my_list:
#         c = 0 
#         for j in range(1,i):
#             if i % j == 0:
#                 c +=1
#         if c != 1:
#             my_list.remove(i)
            
#     return my_list

# prime_list = prime_list(my_list)
# print(f"list of prime numbers is {prime_list}")












# ***
#TODO:13. Write a function that takes a string and returns the most frequent character in the string.

# string = input("Enter a string: ")

# def frequent_char(string):
#     fc = string[0]
#     fcc = string.count(string[0])
#     for i in string:
#         if string.count(i) > fcc:
#             fc = i
#             fcc = string.count(i)
#     return (fc,fcc)


# frequent_char,frequent_char_count = frequent_char(string)   
# if(frequent_char_count==1) :
#     print("no frequent character")
# else:
#     print(f"frequent character in {string} is {frequent_char}")    
    

















#TODO:14. Write a recursive function to calculate the factorial of a number.


# n = int(input("Enter a number: "))

# def fact(n):
#     if n == 1 or n==0:
#         return 1
#     elif n<0:
#         return 0;
#     else:
#         return n * fact(n-1)
    
# result = fact(n)

# if result:
#     print(f"factorial of {n} is {result}")
# else:
#     print("Error Enter whole number.")













#TODO:15. Write a function that accepts a list of integers and returns the second largest number in the list.


# user_input = input("Enter numbers saperated by comma: ")
# mylist = [int(item.strip()) for item in user_input.split(",")]
# print(mylist)
# largest = mylist[0]
# for i in mylist:
#     if (i > largest):
#         largest = i
        
        
# filtered_number = [num for num in mylist if num != largest]
# second_largest=filtered_number[0]
# for i in mylist:
#     if (i > second_largest) and (i < largest):
#         second_largest = i
        
# print(f"second largest number in {mylist} is {second_largest}")
    









#TODO:16. Write a function to check if a given string is a pangram (contains every letter of the alphabet at least once).








#TODO:17. Write a function that takes a number and returns True if it is an Armstrong number (e.g., 153 = 1³ + 5³ + 3³), otherwise False.

# n = input("Enter a number: ")
# length = len(n)
# result =0
# for i in n:
#     result += int(i)**length
    

# if result == int(n):
#     print (f"{n} is Armstrong number.")
# else:
#     print(f"{n} is not a Armstrong number.")





#TODO:18. Write a function that takes a list of numbers and returns the cumulative sum of the list. For example, given [1, 2, 3], return [1, 3, 6].


# user_input = input("Enter a numbers saperated by comma: ")
# my_list = [int(item.strip()) for item in user_input.split(',')]
# my_clist=[]
# sum = 0 
# for i in my_list:
#     sum +=i
#     my_clist.append(sum)

# print(f"cummulative sum of list is {my_clist}")
    







#TODO:19. Write a function to calculate the sum of digits of a number until it reduces to a single digit (e.g., 9875 → 9 + 8 + 7 + 5 = 29 → 2 + 9 = 11 → 1 + 1 = 2).

# num = int(input("Enter a number:"))

# def sum_of_digit(num):
#     num = str(num)
#     sum = 0
#     for i in num:
#         sum += int(i)
    
#     if sum<10:
#         print(f"Sum is {sum}") 
#     else:
#         sum_of_digit(sum)
    
# sum_of_digit(num)












# TODO:20. Write a function that takes a list of strings and returns the longest string in the list.	


# string_list = ["ashok", "budha", "Techspire", "college","bsc.it"]

# def longest_string_finder(string_list):
#     longest_string=string_list[0]
#     for i in string_list:
#         if len(i)>=len(longest_string):
#             longest_string = i
#     print(f"longest string is {longest_string}")    
    

# longest_string_finder(string_list)










# TODO TODO TODO: List Questions
# Easy
# 1.Create a list of the first 10 natural numbers. Access and print the 5th element.
# 2.Add the number 11 to the list [1, 2, 3, 4, 5] and then remove the number 3.
# Medium
# 3.Reverse the list [10, 20, 30, 40, 50] without using the built-in reverse() method.
# 4.Write a program to find and print all even numbers from the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# Hard
# 5.Write a Python program to remove all duplicates from the list [1, 2, 3, 2, 4, 5, 6, 5, 7] while maintaining order.
# 6.Given a list of integers, find the second largest element without using the max() function.





# 1.Create a list of the first 10 natural numbers. Access and print the 5th element.

# my_list = str(input("Enter 10 numbers saperated by comma:"))
# my_list = my_list.split(",")
# print(f"fifth element in list is {my_list[4]}")








# 2.Add the number 11 to the list [1, 2, 3, 4, 5] and then remove the number 3.

# my_list = [1,2,3,4,5]
# my_list.append(11)
# if 3 in my_list:
#     my_list.remove(3)

# print(my_list)







# 3.Reverse the list [10, 20, 30, 40, 50] without using the built-in reverse() method.

# my_list = [10, 20, 30, 40 , 50]

# def rev_func(my_list):
#     my_list = my_list[::-1]
#     print(my_list)

# rev_func(my_list)






# 4.Write a program to find and print all even numbers from the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

# my_list = [1,2,3,4,5,6,7,8,9,10]
# def check_even(my_list):
#     for i in my_list:
#         if i % 2 == 0:
#             print(i, end=",")

# check_even(my_list)












# 5.Write a Python program to remove all duplicates from the list [1, 2, 3, 2, 4, 5, 6, 5, 7] while maintaining order.

# my_list = [1,2,3,2,4,5,6,5,7]

# for i in my_list:
#     if my_list.count(i)>1:
#         my_list.pop(len(my_list)-1-my_list[::-1].index(i))

# print(my_list)



# 6.Given a list of integers, find the second largest element without using the max() function.

# my_list = [1,2,3,4,7,5,20,19]

# def nth_largest(nth,my_list):
#     list_para = my_list.copy()
#     for i in range(nth):
#         largest = list_para[0]
#         for i in list_para:
#             if i>largest:
#                 largest = i
#         list_para.remove(largest)
#     print(f"{nth} largest is {largest}")

# nth_largest(2,my_list)




















# TODO TODO TODO: Tuple Questions
# Easy
# 1. Create a tuple with 5 elements and print the 3rd element.
# 2. Convert the tuple (1, 2, 3, 4, 5) into a list and modify the second element to 10.
# Medium
# 3. Write a Python program to check if the element 50 exists in the tuple (10, 20, 30, 40, 50, 60).
# 4. Given a tuple (5, 10, 15, 20), calculate and print the sum of all elements.
# Hard
# 5. Write a Python program to sort a tuple of tuples by the second element. Example: [(2, 5), (1, 2), (4, 4)] should become [(1, 2), (4, 4), (2, 5)].
# 6. Given the tuple (1, [2, 3], 4), change the value 3 to 10.






# 1. Create a tuple with 5 elements and print the 3rd element.

# my_tuple = (1,2,3,4,5)
# print(my_tuple[2])



# 2. Convert the tuple (1, 2, 3, 4, 5) into a list and modify the second element to 10.

# my_tuple = (1,2,3,4,5)
# my_list = list(my_tuple)
# my_list[1] = 10
# my_tuple = tuple(my_list)
# print(my_tuple)



# 3. Write a Python program to check if the element 50 exists in the tuple (10, 20, 30, 40, 50, 60).

# my_tuple = (10,20,30,40,50,60)
# if 50 in my_tuple:
#     print(f"50 is present in {my_tuple}")




# 4. Given a tuple (5, 10, 15, 20), calculate and print the sum of all elements.

# my_tuple = (5,10,15,20)
# sum = 0
# for i in my_tuple:
#     sum +=i

# print(f"sum is {sum}")
    





# 5. Write a Python program to sort a tuple of tuples by the second element. Example: [(2, 5), (1, 2), (4, 4)] should become [(1, 2), (4, 4), (2, 5)].


# my_list = [(2, 5), (1, 2), (4, 4)]

# for i in range(len(my_list)):
#     for j in range(len(my_list)):
#         if my_list[i][1]<my_list[j][1]:
#             my_list[i],my_list[j]=my_list[j],my_list[i]

# print(my_list)          
    







# 6. Given the tuple (1, [2, 3], 4), change the value 3 to 10.

# this_tuple = (1,[2,3],4)
# this_list = list(this_tuple)
# this_list[1][1]=10
# this_tuple = tuple(this_list)
# print(this_tuple)




# TODO TODO TODO Dictionary Questions
# Easy
# 1.Create a dictionary with keys name, age, and city and values of your choice. Print the value associated with the key age.
# 2.Add a new key-value pair gender: 'male' to the dictionary {name: 'John', age: 25}.
# Medium
# 3.Write a Python program to merge two dictionaries. Example: d1 = {1: 'a', 2: 'b'}, d2 = {3: 'c', 4: 'd'}.
# 4.Given a dictionary {'a': 10, 'b': 20, 'c': 30}, find the key with the maximum value.
# Hard
# 5.Write a Python program to count the frequency of each word in the string: "hello world hello python".
# 6.Sort a dictionary by its values in ascending order. Example: {'a': 3, 'b': 1, 'c': 2} should become {'b': 1, 'c': 2, 'a': 3}.


# TODO: 1.Create a dictionary with keys name, age, and city and values of your choice. Print the value associated with the key age.

# my_dict = {"name":"Ashok Budha","age":19, "city":"kathmandu"}
# for key in my_dict:
#     print(f"{key}: {my_dict[key]}")


# TODO: 2.Add a new key-value pair gender: 'male' to the dictionary {name: 'John', age: 25}.

# my_dict = dict(name="john", age=25)
# # my_dict["gender"]="male"
# my_dict.update(gender="male")
# print(my_dict)







#TODO: 3.Write a Python program to merge two dictionaries. Example: d1 = {1: 'a', 2: 'b'}, d2 = {3: 'c', 4: 'd'}.

# d1 = {1: 'a', 2: 'b'}
# d2 = {3: 'c', 4: 'd'}
# d = d1 | d2
# print(d)



#TODO: 4.Given a dictionary {'a': 10, 'b': 20, 'c': 30}, find the key with the maximum value.

# d={'a': 10, 'b': 20, 'c': 30}
# for key in d:
#     max_value = d[key]
#     max_key = key
#     if d[key]> max_value:
#         max_value = d[key]
#         max_key = key

# print(f"key with max value is {max_key}")
    


#TODO: 5.Write a Python program to count the frequency of each word in the string: "hello world hello python".



# string = " hello world hello python"
# count_dict = {}
# for i in string:
#     if i not in count_dict and i != " ":
#         count_dict[i] = string.count(i)

# print(count_dict)


#TODO: 6.Sort a dictionary by its values in ascending order. Example: {'a': 3, 'b': 1, 'c': 2} should become {'b': 1, 'c': 2, 'a': 3}.









# TODO TODO TODO: Set Questions
# Easy
# 1.Create a set with elements 1, 2, 3, 4, 5 and check if 3 is in the set.
# 2.Add the element 6 to the set {1, 2, 3, 4, 5} and then remove 2.
# Medium
# 3.Write a program to find the union of two sets {1, 2, 3} and {3, 4, 5}.
# 4.Given two sets {1, 2, 3} and {3, 4, 5}, find their intersection.
# Hard
# 5.Write a Python program to check if one set is a subset of another. Example: Check if {1, 2} is a subset of {1, 2, 3, 4}.
# 6.Given two sets {1, 2, 3, 4} and {3, 4, 5, 6}, find the symmetric difference.




# 1.Create a set with elements 1, 2, 3, 4, 5 and check if 3 is in the set.

# # Solution
# my_set = {1,2,3,4,5}
# if 3 in my_set:
#     print(f"3 is present in {my_set}")
    
    
    

# 2.Add the element 6 to the set {1, 2, 3, 4, 5} and then remove 2.
# Medium

# # Solution
# my_set = {1,2,3,4,5}
# my_set.add(6)
# print(my_set)

# 3.Write a program to find the union of two sets {1, 2, 3} and {3, 4, 5}.

# Solution





# 4.Given two sets {1, 2, 3} and {3, 4, 5}, find their intersection.
# Hard
# 5.Write a Python program to check if one set is a subset of another. Example: Check if {1, 2} is a subset of {1, 2, 3, 4}.
# 6.Given two sets {1, 2, 3, 4} and {3, 4, 5, 6}, find the symmetric difference.




# TODO TODO TODO: Lambda function
# Easy Questions
#1. Write a lambda function to multiply a given number by 3. Test it with 4.
#2. Create a lambda function that checks if a number is greater than 10. Test it with 15 and 8.
#3. Use a lambda function to find the length of a given string. Test it with "hello".
#4. Write a lambda function to convert a temperature from Celsius to Fahrenheit. Formula: f=c * 9/5 +32
#5. Create a lambda function to return the cube of a given number. Test it with 3.

# Medium Questions
#6. Write a lambda function to calculate the sum of squares of two numbers. Test it with 3 and 4.
#7. Use a lambda function with the filter() function to extract vowels from the list ['a', 'b', 'e', 'i', 'o', 'u', 'x'].
#8. Write a lambda function with the map() function to double all the elements in the list [2, 4, 6, 8].
#9. Create a lambda function to find the maximum of three numbers. Test it with 10, 20, and 5.
#10. Use a lambda function to sort a list of tuples based on their sum. Example: [(1, 2), (3, 4), (1, -1)].

# Hard Questions
#11. Write a lambda function to find all palindromic words in the list ["radar", "python", "level", "world"] using filter().
#12. Create a lambda function to group a list of integers into odd and even using a dictionary. Example input: [1, 2, 3, 4].
#13. Write a lambda function to compute x to power y where x and y are inputs 

#14. Use a lambda function to sort a list of dictionaries by multiple keys. Example: [{‘name’: ‘John’, ‘age’: 25}, {‘name’: ‘Jane’, ‘age’: 22}, {‘name’: ‘John’, ‘age’: 20}] sorted by name then age.
#15. Write a lambda function with reduce() to compute the factorial of a number. Test it with 5.








# TODO TODO TODO: CLASS and OBJECTS

#TODO: Question 1. Create Account class with two attributes balance and account no. .Create methods for debit , credit and printing the balance.

# Solution
# class Account:
#     def __init__(self, balance, accno):
#         self.balance = balance
#         self.accno = accno
        
#     def debit(self,debit_amount):
#         self.balance -= debit_amount
#         print(f"{debit_amount} has been withdrawl.")
    
#     def credit(self,credit_amount):
#         self.balance += credit_amount
#         print(f"{credit_amount} has been credited.")
    
#     def show_balance(self):
#         print(f"Your total balance is {self.balance}")
        
# acc1 = Account(10000,1234)
# acc1.debit(5000)
# acc1.credit(10000)
# acc1.show_balance()



#TODO: Question 2. Define a Circle class to create a  circle with radius  r using the constructor. Define an Area() method of a  class which calculates the area of a  circle . Define a Perimeter() method of a class which allows you to claculate the perimeter of a circle.

# Solution
# class Circle:
#     def __init__(self,r):
#         self.r = r
#     @property                         #NOTE: using property decorator to area method
#     def area(self):
#         return (22/7) * self.r **2
    
#     def perimeter(self):
#         return  2 * (22/7) * self.r
    

# c1 = Circle(21)
# print(c1.area)                       #NOTE: using property decorator to area method
# print(c1.perimeter())
        



#TODO: Question 3. Define an Employee class with attribute role, department and salary. This class also has a showDetails() method.
# Create a Engineer calss that inherits properties from Employee and has additional attributes : name and age


# Solution
# class Employee:
#     def __init__(self,role,department ,salary):
#         self.role = role
#         self.department = department 
#         self.salary = salary
    
#     @property
#     def showDetails(self):
#         print(f"The role of employee is {self.role} and department is {self.department} and salary is {self.salary}")
      
      
# class Engineer(Employee):
#     def __init__(self, role,department,salary,name,age):
#         super().__init__(role,department,salary)
#         self.name = name
#         self.age = age
#     @property
#     def showDetails(self):
#         print(f"The role of employee is {self.role} and department is {self.department} and salary is {self.salary} and name is {self.name} and age is {self.age}")
        
        
   
# em1 = Employee("painter","painting",20000)
# en1= Engineer("engineer","en-01",45000,"Ram", 19)
# em1.showDetails
# en1.showDetails



#TODO: Question 4. Create a class called Order which stores item and its price . Use Dunder function __gt__() to convey that : order1>order2 if price of order1 > price of order2


# Solution
# class Order:
#     def __init__(self,item,price):
#         self.item = item
#         self.price = price
    
#     def __gt__(self,another):
#         if (self.price> another.price):
#             return True
#         else:
#             return False

# or1 = Order("iceCream", 100)
# or2 = Order("Chocolate",500)

# print(or1>or2)


