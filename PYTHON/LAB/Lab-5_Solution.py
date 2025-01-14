# part A
# 1. Convert the program design for Question 1, 5 and 6 from previous Lab 2 – Problem Solving Control Structure lab exercise.

# 1. Using a while loop, asks the user to enter a number, and prints a countdown from the number entered by the user to zero.
# a=10
# while a>=0:
#     print(a)
#     a-=1    
        
# 5. Print odd number(s).
# for i in range(1,50):
#     if i%2!=0:
#         print(i)

# 6. Guess if the number that user enter is in a range or not.
# iscontinue=True
# while iscontinue:
#     user_input = int(input("Enter a number: "))
#     if user_input in range(10,20):
#         print("Your Guess is correct.")
#         iscontinue=False
#     else:
#         print("Your Guess is incorrect.")
#         iscontinue = input("Do you want to continue? (yes/no): ").lower() == "yes"

    
    
# 2. Write a program that able to print the even number that in the between of 2 to 50.
# for i in range(2,50):
#     if i%2==0:
#         print(i)

# part B
# 1. Write a Python program to display numbers from 1 to 20. Note: use all types of repetitive structures

# using for loop
# for i in range (1,21):
#     print(i)

# using while loop
# i=1
# while i<=20:
#     print(i)
#     i+=1


# 2. Write a Python program to create a multiplication table of 7.
# for i in range(1,11):
#     print(f"7 x {i} = {7*i}")


# 3. Use a proper iterative structure to write a program that will read names and exam scores of students. The class average is to be calculated and printed at the end of the report. Score can range from 0 to 100. Score out of the range is not to be included in the calculations.

# isContinue = True
# total = 0
# count = 0
# while isContinue:
#     name = input("Enter student name: ")
#     score = float(input("Enter exam score: "))
#     if score >= 0 and score <= 100:
#         total += score
#         count += 1
#     else:
#         print("Invalid score. Score should be between 0 and 100.")
#     isContinue = input("Do you want to continue? (yes/no): ").lower() == "yes"

# if count > 0:
#     print(f"Class average: {total / count}")    
# else:
#     print("No valid scores entered.")


# 4. Write a Python program to construct the following pattern, using a nested for loop. 
# * 
# * * 
# * * *
# * * * *
# * * * * *

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
