# val = {
#     "name" : "shiba",
#     "age" : 19,
#     "marks" : [98,76,65,89],
#     "cgpa" : (9.5,8.6,6.13),
#     "topic": ("dictionary","set"),
#     "domain" : "cse(aiml)"
# }
# print(type(val))
# print(len(val))
# print(val)
# print(val["name"])
# print(val["age"])
# print(val["topic"])
# print(val["domain"])

student = {
    "name" : "shiba",
    "friends" : {
        "name1" : "arpan",
        "name2": "sameer",
        "name3" : "prateek"
    }
}
print(student)
print(type(student["friends"]))
print(student["friends"] ["name1"])