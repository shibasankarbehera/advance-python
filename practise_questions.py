#1.Wap to ask the user to enetr names of their 3 fav cricketer and store them in a list .
# cricketer = []
# cri1=input("enetr  a name :")
# cri2=input("enetr 2nd name:")
# cri3=input("enter 3rd name:")

# cricketer.append(cri1) 
# cricketer.append(cri2)
# cricketer.append(cri3)

# print(cricketer)

# 2.wap to check if a list contains a palindrome of element .(hint:use copy() method)

# list1 =[1,3,1]
# list2 =[1,2,3]
# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1==list1):
#     print("it is a palindrome")
# else:
#     print("it is not palindrome")

# 3. wap to count the number of student with the 'a' grade in the following tuple  

# grade = ['c','d','a','a','b','b','a']
# print(grade.count('a'))

# 4. store the above values ina list and sort them from 'a'to 'b'.

# grade = ["c","d","a","b","b","a"]
# grade.sort()
# print(grade)
# grade.sort(reverse=True)
# print(grade)

# 5. store the following word meaning in a pyton dictionaries.

# table:"a piece of furniture","lists of facts and figure"
# cat:"a small animal"

# ans.....

# dict={
#     "table" : ["a piece of furniture","lists of facts and figure"],
#     "cat":"a small animal"
# }
# print(dict)

# 6. you are a giving a list of sub of student.Assume one classroom in required for 1 sub.How many classroom are needed by all student.
# "python","java","c++","python","javascript","java","python","java","c++","c"

# ans....... 

# subjects ={
#     "python","java","c++","python","javascript","java","python","java","c++","c"
# }
# print("classrooms needed by all students:",len(subjects))
 
# 7.wap to enter marks of 3 subjects from the user and store them in a dictionary.start with an empty dictionary and add one by one. use subject name as key and marks as a value.

# ans..............

# dict ={
#     "subject":{
#         "math" :int(input("enter a no:")),
#         "chem":int(input("enter a no:")),             #this is not exact ans but in simple way......
#         "phy":int(input("enter a no:"))
#     }
# }
# print(dict)

# dict={}

# x=int(input("enter phy marks:"))
# dict.update({"phy":x})

# x=int(input("enter math marks:"))    #this is actual ans............
# dict.update({"math":x})

# x=int(input("enter chem marks:"))
# dict.update({"chem":x})
 
# print(dict)

#8.figure out a way to store 9 & 9.0 as separate value in the set. (you can help of built-in data ).

# ans...........

value = {
    ("float",9.0),
    ("int",9)
}
print(value)