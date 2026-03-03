# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
# show(5)     

#factorial using recursion.............

# def fact(n):
#     if(n==1 or n==0):
#         return 1
#     return fact(n-1)*n
# print(fact(4))

#write a recursion function to calculate the sum of first n natural no:............

# def sum(n):
#     if(n==0):
#         return 0
#     print(n)
#     return sum(n-1)+n

# val=sum(5)
# print("value is:",val)    

#write a recursive function to print all element in a list.........

ele=[1,2,3,4,5]
def val(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    val(list,idx+1)
    return
val(ele)    