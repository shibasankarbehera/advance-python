# def cal_sum(a,b):
#     sum=a+b
#     print("sum is :",sum)
#     return sum
# cal_sum(12,15)

# def hello():
#     print("shiba")
# hello()

# def hello():
#     print("shiba")
# output=hello()    
# print(output)

def shiba(a,b):
    mul=a*b
   
    return mul

y=shiba(6,8)
print(y)

#calculate the average of 3 no:

# def val(a,b):
#     sum=a+b
#     avg=sum/2
#     print(avg)
#     return avg
# val(10,10)

# waf to print a list(list is a parameter).............

# name=["shiba","shyam","arpan","sameer","pratik","sidhu"]
# def names(list):
#     print(len(list))
# names(name)    

#waf to print the elements of a list in a single line........

# name=["shiba","shyam","arpan","sameer","sidhu","prateek"]
# def print_list(list):
#     for i in list:
#         print(i,end=" ")
# print_list(name)        

#waf to find the factorial of n ..............

# def print_fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#         i+=1
#     print("factorial is:",fact)
# print_fact(7)        

#waf to convert usd to inr........

# def convert(usd):
#     inr=usd*83
#     print(usd,"USD value is:",inr,"INR")
# convert(2)    

#waf to print even or odd no:............

# def val(n):
#     if(n%2==0):
#         print("EVEN")
#     else:
#          print("ODD")
# cal=int(input("enter a num:"))
# val(cal)

# def sum_and_difference(num1, num2):
#     total_sum = num1 + num2
#     total_difference = num1 - num2
#     return total_sum, total_difference

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# sum_result, diff_result = sum_and_difference(a, b)

# print("Sum =", sum_result)
# print("Difference =", diff_result)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a >= b and a >= c:
#     print(a, "is the largest number")
# elif b >= a and b >= c:
#     print(b, "is the largest number")
# else:
#     print(c, "is the largest number")

# def print_numbers(n):
#     i = 1
#     while i <= n:
#         print(i)
#         i += 1

# n = int(input("Enter a number: "))
# print_numbers(n)

# def factorial(n):
#     fact = 1
#     i = 1
#     while i <= n:
#         fact = fact * i
#         i += 1
#     return fact

# num = int(input("Enter a number: "))
# print("Factorial =", factorial(num))

# def get_even_numbers(lst):
#     even_numbers = []
#     for num in lst:
#         if num % 2 == 0:
#             even_numbers.append(num)
#     return even_numbers

# numbers = [int(x) for x in input("Enter numbers giving space: ").split()]
# print("Even numbers:", get_even_numbers(numbers))

# def count_vowels(s):
#     count = 0
#     for char in s.lower():
#         if char in "aeiou":
#             count += 1
#     return count

# text = input("Enter a string: ")
# print("Number of vowels:", count_vowels(text))

# def reverse_string(s):
#     reversed_str = ""
#     for char in s:
#         reversed_str = char + reversed_str
#     return reversed_str

# text = input("Enter a string: ")
# print("Reversed string:", reverse_string(text))

# def multiplication_table(n):
#     for i in range(1, 11):
#         print(n, "x", i, "=", n * i)

# num = int(input("Enter a number: "))
# multiplication_table(num)

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# num = int(input("Enter a number: "))
# if is_prime(num):
#     print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")

# def sum_of_list(lst):
#     total = 0
#     for num in lst:
#         total += num
#     return total

# numbers = [int(x) for x in input("Enter numbers:").split()]
# print("Sum of all elements:", sum_of_list(numbers))

# def fibonacci_series(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a, end=" ")
#         a, b = b, a + b

# terms = int(input("Enter the number of terms: "))
# fibonacci_series(terms)
