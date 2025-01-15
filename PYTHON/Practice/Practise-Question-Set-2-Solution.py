# Practice Question Set 2


# 1. Write a Python function to calculate the sum of all numbers in a given list using a for loop.
# Solution
# my_list = [1,2,4,5,6]
# sum = 0
# for i in my_list:
#     sum +=i
# print(f"The sum of item is {sum}")





# 2. Write a function that prints all even numbers between 1 and 20 using a while loop.
# Solution
# for i in range(1,21):
#     if i % 2 == 0:
#         print(i)




# 3. Create a function that accepts a number as an argument and prints all its divisors using a for loop.
# Solution
# num = int(input("Enter a number: "))
# for i in range(1,num+1):
#     if num %i == 0:
#         print(i)



# 4. Write a function to count how many times the letter 'a' appears in a given string using a for loop.
# Solution
# my_str = "Ashok"
# count = 0
# for i in my_str.lower():
#     if i == "a":
#         count +=1
# print(f"a is repeated {count} time.")




# 5. Write a Python function that returns the factorial of a given number using a for loop.
# Solution
# def fact(n):
#     result = 1
#     for i in range(1, n+1):
#         result *=i
#     return result
        
# output = fact(5)
# print(f"Factorial of 5 is {output}")



# 6. Create a function that prints the Fibonacci sequence up to a given number using a while loop.
# Solution
# def fibo(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         print(a)
#         a,b = b, a+b

# fibo(10)
    





# 7. Write a function that calculates the average of all numbers in a list and returns the result using a for loop.
# Solution
# def average(my_list):
#     sum = 0
#     for i in my_list:
#         sum +=i
#     return sum/len(my_list)

# result = average([1,2,3,5,4])
# print(f"Average is {result}")




# 8. Create a function to check if a number is prime, using a for loop to iterate through possible divisors.
# Solution
# def check_prime(n):
#     isPrime = True
#     for i in range(2,n):
#         if n % i == 0:
#             isPrime = False
#             return isPrime
#     return isPrime

# result = check_prime(4)
# if result:
#     print("Prime")
# else:
#     print("Not Prime")
    





# 9. Write a function that prints the multiplication table of a given number up to 10 using a for loop.
# Solution
# def table(n):
#     for i in range(1,11):
#         print(f"{n} * {i} = {n*i}")
        
# num = int(input("Enter a number: "))
# table(num)
    




# 10. Create a function that prints all numbers from 1 to 100 that are divisible by both 3 and 5 using a while loop.
# Solution

# num = 1
# while num <= 100:
#     if num % 3 ==0 and num % 5 == 0:
#         print(num)
#     num +=1 
    





# 11. Write a Python function to reverse a given string.
# Solution
# def reverse_string(my_str):
#     return my_str[::-1]

# result = reverse_string("Ashok")
# print(f"Reverse of Ashok is {result}")





# 12. Write a Python program to generate a list of squares of numbers from 1 to N.
# Solution
# my_list = []
# num = int(input("Enter a number: "))
# for i in range(1,num+1):
#     my_list.append(i**2)
    
# print(my_list)







# 13. Create a program that asks the user to input the depth of a well in meters. If the depth is above 10 meters, display 'The well is deep.' If it is 10 meters or less, display 'The well is shallow.' Keep asking for the depth until the user inputs -1 to exit.
# Solution
# depth = float(input(" Enter the depth of well: "))
# isContinue = True
# while isContinue:
#     if depth >10:
#         print("The well is deep.")
#     else:
#         print("The well is shallow.")
    
#     depth = float(input("Enter the depth or enter -1 to exit: "))
#     if depth == -1:
#         isContinue = False






# 14. Create a program that prompts the user to enter a number and determines whether it is divisible by 3, 5, or neither. Continue asking for input until the user enters "exit".
# Solution
# user_input = int(input("Enter a number:"))
# isContinue = True
# while isContinue:
#     if user_input % 3 == 0 and user_input % 5 == 0:
#         print("Divisible by both 3 and 5")
#     elif user_input % 3 == 0:
#         print("Divisible by 3 only.")
#     elif user_input % 5 == 0:
#         print(" Divisible by 5 only.")
#     else:
#         print("Divisible by none.")
    
#     user_input = int(input("Enter a number or -1 to exit: "))
#     if user_input == -1:
#         isContinue = False
    






# 15. Write a Python program that generates the squares and cubes of numbers from 1 to 5. Use a loop to iterate through the numbers and print the results in the format: a2 = b, a3 = c.
# Solution
# for i in range(1,6):
#     print(f"{i}2 = {i**2}, {i}3 = {i**3}");





# 16. Create a Python program that converts temperatures.
# o Ask the user to input a temperature in Celsius or Fahrenheit and the desiredconversion (e.g., C to F or F to C). 
# o Use a function to perform the conversion.
# o Keep asking for conversions until the user types "Stop."
# Solution
# def FtoC():
#     f = float(input("Enter temperature in fahrenheit: "))
#     c = (f-32)/1.8
#     print(f" {f}F = {c}C")

# def CtoF():
#     c = float(input("Enter a temperature in celsius: "))
#     f = 1.8*c +32
#     print(f"{c}C = {f}F")
    
# def temp_converter():
#     user_input = int(input("Enter 1 to conver Celsius to Fahrenheit and 2 to convert Fahrenheit to celsius: "))
#     isContinue = True
#     while isContinue:
#         if user_input == 1:
#             CtoF()
#         elif user_input == 2:
#             FtoC()
#         else:
#             print("Invalid input.")
        
#         user_input = int(input("Enter 1 to conver Celsius to Fahrenheit and 2 to convert Fahrenheit to celsius and 3 to exit: "))
        
#         if user_input == 3:
#             isContinue = False
        
# temp_converter()
    


# 17. Write a Python program which accepts the radius of a circle from the user and computes the area.
# Solution
# radius = float(input("Enter a radius: "))
# area = (22/7)*radius**2
# print(f"Area is {area}")

