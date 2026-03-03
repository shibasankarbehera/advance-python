import random
c=["rock","paper","scissors"]
user=input("Enter rock,paper or scissor: ").lower()
comp=random.choice(c)
print("Computer chose:",comp)
if user==comp:
    print("Its a tie Better luck next time")
elif(user =="rock"and comp=="scissor")or (user =="paper"and comp=="rock")or (user =="scissors"and comp=="paper"):
    print("You Win")
elif user in c:
    print("Computer Wins")
else:
    print("Invalid Input")