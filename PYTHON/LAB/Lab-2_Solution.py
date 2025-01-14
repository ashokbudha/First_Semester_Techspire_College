#TODO: 1. Using a while loop, asks the user to enter a number, and prints a countdown from the number entered by the user to zero.

# # Solution
# num = int(input("Enter a number:"))
# while (num >= 0):
#     print(num)
#     num -=1
    

 
#TODO: 2. Check if the number enter is a positive number, negative number or zero.

# # Solution
# num = int(input("Enter a number"))
# if num > 0:
#     print(f"{num} is a positive number.")
# elif num < 0:
#     print(f"{num} is a negative number.")
# else:
#     print(f"{num} is zero.")





#TODO: 3. Find the largest numbers between 3 numbers.

# # Solution
# my_input = input("Enter three number saperated by comma:")
# a,b,c = my_input.split(",")
# if (a >= b) and (a >= c):
#     print(f"{a} is the largest number.")
# elif (b >=a) and (b >= c):
#     print(f"{b} is the largest number.")
# else:
#     print(f"{c} is the largest number.")


#TODO: 4. Check year enter is a leap year or not a leap year.

# # Solution
# year = int(input("Enter a year:"))
# if year % 400 ==0 or (year % 4 == 0 and year % 100 !=0):
#     print(f"{year} is leap year.")
# else:
#     print(f"{year} is not a leap year.")




#TODO: 5. Print odd number(s).

# # Solution
# i = 0 
# for i in range(20):
#     if i % 2 != 0:
#         print(i, end ="," )



#TODO: 6. Guess if the number that user enter is in a range or not.

# # Solution
# num = int(input("Enter a number:"))
# if num in range(10):
#     print("Guess is correct.")
# else:
#     print("Guess is not correct.")