# Practice Question Set 1

# Part A:
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

