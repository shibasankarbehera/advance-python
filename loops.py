# ...............while loop...............

count = 1
while count<=5:
    print("hello")
    count+=1
print(count)    

# i=1
# while i<=10:
#     print("shiba",i)
#     i+=1

# print num  fromm 1 to 5..

# i=1
# while i<=5:
#     print(i)
#     i+=1
# print("loop ended",i)    

# ..............practice question...........

# 1.print a num from 1 to 100.

# i=1
# while i<=100:
#     print(i)
#     i+=1

#2.print num from 100 to 1.
# i=100
# while i>=1:
#     print(i)
#     i-=1 

# 3. print the multiplication table  of num N.

# n=int(input("enter a no:"))
# i = 1
# while i<=10:
#     print(n*i)
#     i+=1

# 4.print the elements of the following list using a loop.
# [1,4,9,16,25,36,49,64,81,100]

# num =[1,4,9,16,25,36,49,64,81,100]
# i=0
# while i<len(num):
#     print(num[i])    #num[i] means num[0]=1,num[1]=4,num[2]=9,num[3]=16..........
#     i+=1

# ...............2nd example............

# name = ["shiba","shyam","arpan","sameer","pratap","prateek"]
# i=0
# while i<len(name):
#     print(name[i])
#     i+=1

# 5.search for num x in this tuple using loop.
# (1,4,9,16,25,36,49,64,81,100)

# num= (1,4,9,16,25,36,49,64,81,100)
# x=int(input("enter a no:"))
# i=0
# while i<(len(num)):
#     if(num[i]==x):
#         print("the i value is:",x)
#     else:
#         print("still finding")    
#     i+=1

# break statement:::

# num= (1,4,9,16,25,36,49,64,81,100)
# x=int(input("enter a no:"))
# i=0
# while i<(len(num)):
#     if(num[i]==x):
#         print("the index value is:",i,"and the value is:",x)
#         break
#     else:
#         print("still finding")    
#     i+=1
# print("end of loop")    

#continue statement::::

# i=0
# while i<=10:
#     if(i==5):
#         i+=1        #this means skip the no.5.......
#         continue
#     print(i)
#     i+=1

#print odd num........

# i=1
# while i<=10:
#     if(i%2==0):
#         i+=1
#         continue
#     print(i)
#     i+=1

#print even num..........

# i=1
# while i<=10:
#     if(i%2!=0):
#         i+=1
#         continue
#     print(i)
#     i+=1

#................ for loop ....................

# friends = ["shiba","arpan","sameer","pratik","sidhu"]

# for name in friends:
#     print(name)

# tup = ("shiba",2,3,5,"shyam")

# for name in tup:
#     print(name)

# str="shibasankar behera"
# for char in str:
#     if(char=='n'):
#         print("n found")
#         break
#     print(char)
# else:
#     print("end")

# num=(1,4,9,16,25,36,49,64,81,100)
# x=int(input("enter a no:"))
# i=0
# for val in num:
#     if(val==x):
#         print("found at idx",i)
#         break
#     i+=1
# else:
#     print("not found")

# check fibonacci or not..........

# n=int(input('enter a no:'))
# a,b=0,1
# while b<n:
#     a,b=b,a+b
# if b==n:
#     print("fibonacci")
# else:
#     print("not fibonacci")    

# check fatorial no.......

# n=int(input("enter a no:"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# # print("factorial=",fact

# wap to find the sum of first n numbers(using for)........

# n=int(input("enter a no:"))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print("sum is:",sum)

# wap to find the sum of first n numbers(using while)........

# n=int(input("enter a no:"))
# sum=0
# i=1
# while i<=n:
#     sum+=i
#     i+=1
# print("sum is:",sum)

# wap to find the factorial of first n number (using for loop)..........

# n=int(input("entera no:"))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print("factorial is:",fact)    

# n=5
# fact=1
# i=1
# while i<=n:
#     fact*=i
#     i+=1
# print("fact is:",fact)    
