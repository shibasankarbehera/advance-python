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