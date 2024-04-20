# my_number = 5
# user_input = int(input("What number am I thinking of?"))


# while (user_input != my_number):
#     print("nope! try again... ")
# print("yes!")


# pin_number= 1234
# input_pin = int(input("enter your pin number"))

# # the below is read as; while the input pin does not equal the pin number,print wrong number, try again.
# while (input_pin != pin_number):
#     print("wrong number, try again!")
# #     # input_pin = int(input())
# # print("your balance is 500")

# my_number = 5
# value = int(input("What number am I thinking of? "))
# while (value != my_number):
#  if (value > my_number):
#     print("too high")
#  else:
#     print("too low")
#  value = int(input("try again... "))
# print("yes!")

# # loops.py
# numbers = [1, 2, 3, 4, 5]
# total = 0
# for number in numbers:
#    total = sum(numbers)
# print(total)

# result = 0
# while 7465 > 0:
#  n = n // 10
#  result += 1
#  print(result)

# The Fibonacci numbers form a sequence of integers defined recursively in the
# following way. The first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two. The first few elements in this sequence are: 0,
# 1, 1, 2, 3, 5, 8, 13. Let’s write a program that prints all the Fibonacci numbers, not exceeding
# a given integer n.
# We can keep generating and printing consecutive Fibonacci numbers until we exceed n.
# In each step it’s enough to store only two consecutive Fibonacci numbers.



def fibonacci_numbers_not_exceeding_n(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=" ")  # Print the current Fibonacci number
        a, b = b, a + b    # Calculate the next Fibonacci number

# Input the value of 'n'
n = int(input("Enter an integer 'n': "))

# Print Fibonacci numbers not exceeding 'n'
print("Fibonacci numbers not exceeding", n, "are:")
fibonacci_numbers_not_exceeding_n(n)
