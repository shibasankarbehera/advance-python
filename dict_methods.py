# ............... methods of dictionaries.................. 
# -----------------1. Dict.keys()------------------

# student = {
#     "name" : "shiba",
#     "friends" : {
#         "name1" : "arpan",
#         "name2": "sameer",
#         "name3" : "prateek"
#     }
# }
# print(list(student.keys()))

#----------------2. Dict.values()--------------

# student = {
#     "name" : "shiba",
#     "friends" : {
#         "name1" : "arpan",
#         "name2": "sameer",
#         "name3" : "prateek"
#     }
# }
# print(student.values())
# print(list(student.values()))

# -----------------3. Dict.items()-------------

# student = {
#     "name" : "shiba",
#     "friends" : {
#         "name1" : "arpan",
#         "name2": "sameer",
#         "name3" : "prateek"
#     }
# }
# print(student.items())
# print(list(student.items()))

# # or

# new = (list(student.items()))
# print(new[0])

# -----------------4. Dict.get()-------------

student = {
    "name" : "shiba",
    "friends" : {
        "name1" : "arpan",
        "name2": "sameer",
        "name3" : "prateek"
    }
}
print(student.get("name"))   #In dict methods if we put non deifne keys in print then we get 'none" as a output.. like("name1")
print(student["name"])       # BUT withot methods we get "error"...

# ------------------5. Dict.update()-----------------

# student = {
#     "name" : "shiba",
#     "friends" : {
#         "name1" : "arpan",
#         "name2": "sameer",
#         "name3" : "prateek"
#     }
# }
# new_dict = {"age":18,"domain":"cse"}
# student.update(new_dict)
# print(student)


