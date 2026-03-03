pin=1237
for i  in range(3):
    p=int(input("Enter your ATM Pin: "))
    if p ==pin:
        print("Acces Granted ")
        break
    else:
        print("Incorrect Pin")
else:
    print("Your card is Block")
