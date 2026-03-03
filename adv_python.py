# # def add():
# #     a=50
# #     b=60
# #     c=a+b
# #     print("addition of number is",c)
# # add()

# # l1=["shiba",20,9.5,"btech","chatrapur","cse(aiml)"]
# # l2=["arpan",20,8.7,"bcom"]
# # print(l1[2:])
# # print(l2 * 3)

# # l1=[1,2,3,4,5]
# # l1[1]=9
# # print(l1)

# # l1=[1,2,3,4,5,6,7,8,9]
# # for i in range (10):
# #     if (i%2==0):
# #         print("even no:",i*100)
# #     else:
# #         print("odd no",i*10)
# # print(l1)        
   
# # l1=[0,1,2,3,4,5,6,7,8,9]
# # for i in range (0,10):
# #     if (i%2==0):
# #         l1[i]*=100
# #     else:
# #        l1[i]*=10
# # print(l1)

# # l1 = [1,2,3,4,5]
# # l1.count
# # print(l1)

# # a = int (input(" enter a no.\nwhat  is your name:"))
# # b = int(input("enter a no:"))

# # print("power is:",a ** b ) 
# # n=int(input("Enter the no."))
# # fact=1
# # for i in range(0,n):
# #     fact=fact*(n-i)
# # print(f"Factorial of {n} is {fact}")
# # a="     Shiba      "
# # b="good"
# # print(a.strip)


# # write a program to creat a function func1() that accepts a variable no of arguments & print each of their value
# # def func1(*args):
# #     for value in args:
# #         print(value)
# # func1(10, 20, 30, "hello", 4.5)

# def greet(name="User"):
#     print("Hello,", name)

# # Function calls
# greet("Alice")
# greet()

# # 1. create a function in python...
# # def cal_sum(a,b):
# #     sum=a+b
# #     print("sum is :",sum)
# #     return sum
# # cal_sum(12,15)

# # 2.create a function with variable length of arguments..
# # def val():
# #     name=input("enter a name:")
# #     age=int(input("enter a age:"))
# #     print("name is:",name,"\nage is:",age)
# # val()

# # 3.return multiple values from a function.
# # def cal(a,b):
# #     sum=a+b
# #     sub=a-b
# #     return sum,sub
# # print(cal(40,50))

# # 4.create a function with a default argument
# # def show_employee(name,salary=100000):
# #     print("name=",name)
# #     print("salary=",salary)
# # show_employee("shiba",90000)

# #5. create a inner function
# # def num(a,b):
# #     def sum():
# #         return a+b
# #     return sum()+5
# # print(num(6,7))

# # 6.creatre a recursive function
# def countdown(n):
#     if n == 0:
#         print("found")
#     else:
#         print(n)
#         countdown(n-1)
# countdown(4)

# 7.
# def display_student(name,age):
#     print(name,age)
# show_student=display_student
# show_student("shiba",20)

# #8-
# even_numbers = list(range(4, 31, 2))
# print(even_numbers)

# #9
# def largest():
#  l=[23,24,25,68,544,67,89]
#  return max(l)
# largest()

# #10
# def describe_pet(animal_type,pet_name):
#   print("Animal type= ",animal_type)
#   print("Pet Name ",pet_name)
# describe_pet(animal_type="Dog",pet_name="Tommy")
# print("\n")
# describe_pet("Cat","BilliMC")

# 11.def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(key, "=", value)

# print_info(name="Mukku", age=30)
# print_info(city="Japan", course="BTech", year=2)

# #12
# global_var = 10

# def modify_global():
#     global global_var
#     global_var = global_var + 5

# modify_global()
# print("Global variable value:", global_var)

# #13
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print("Factorial of 5 is:", factorial(5))

# #14
# square = lambda x: x * x
# print(square(5))

# #15
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)

# #16
# numbers = [1, 2, 3, 4, 5]
# doubled_numbers = list(map(lambda x: x * 2, numbers))

# print(doubled_numbers)

# (Q)...create a game between multiple players where:
# each player rolls a dice 5 times.
# the player with the highest total score wins.
# handle ties and allow multiple rounds.

# import random

# def play_round(players):
#     scores = {p: sum(random.randint(1, 6) for _ in range(5)) for p in players}
#     max_score = max(scores.values())
#     winners = [p for p, s in scores.items() if s == max_score]
#     return scores, winners

# players = ["Alice", "Bob", "Charlie"]

# while True:
#     scores, winners = play_round(players)
#     print("Scores:", scores)
#     print("Winner(s):", winners)

#     if input("Play another round? (y/n): ").lower() != "y":
#         break


# import random

# def roll_dice(times=5):
#     """Roll a 6-sided die 'times' times and return the total."""
#     return sum(random.randint(1, 6) for _ in range(times))


# def play_round(players):
#     """Play one round and return the scores."""
#     scores = {}

#     print("\n--- Rolling Dice ---")
#     for player in players:
#         total = roll_dice()
#         scores[player] = total
#         print(f"{player} rolled a total of {total}")

#     return scores


# def determine_winners(scores):
#     """Determine winner(s), handling ties."""
#     highest_score = max(scores.values())
#     winners = [player for player, score in scores.items()
#                if score == highest_score]
#     return winners, highest_score


# def play_game():
#     num_players = int(input("Enter number of players: "))
#     players = [f"Player {i+1}" for i in range(num_players)]

#     round_number = 1

#     while True:
#         print(f"\n=== Round {round_number} ===")
#         scores = play_round(players)
#         winners, high_score = determine_winners(scores)

#         if len(winners) == 1:
#             print(f"\n🏆 {winners[0]} wins with {high_score} points!")
#         else:
#             print(f"\n🤝 It's a tie! Winners: {', '.join(winners)} "
#                   f"with {high_score} points each")

#         again = input("\nPlay another round? (y/n): ").lower()
#         if again != "y":
#             print("\nGame over. Thanks for playing!")
#             break

#         round_number += 1


# if __name__ == "__main__":
#     play_game()


# grade calcuter........


marks=[]
n=int(input("Enter the number of Subject: "))
for i in range(n):
    m = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)
total=sum(marks)
if total>=500:
    print("Grade O")
elif total>=400 and total<500:
    print("Grade E")
elif total>=300 and total<400:
    print("Grade A")
elif total>=200 and total<300:
    print("Grade B")
elif total>=100 and total<200:
    print("Grade C")
elif total>=50 and total<100:
    print("Grade D")
else:
    print("Fail in this Semester")


# ATM pin validation...
    pin=8249
for i  in range(3):
    p=int(input("Enter your ATM Pin: "))
    if p ==pin:
        print("Acces Granted ")
        break
    else:
        print("Incorrect Pin")
else:
    print("Your card is Block")

