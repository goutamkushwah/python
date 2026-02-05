# dictioary= {
#     "name": "Goutam kushwah",
#     "age": 24,
#     "city": "Indore"
# }
# print(dictioary["name"])
# print(dictioary.get("age"))
# print(dictioary.keys())
# print(dictioary.values())
# print(dictioary.items())
# print(len(dictioary))
# print(type(dictioary))
# print(dictioary)

# update the dictionary
#  
# dictioary["name"]="Shivam"
# print(dictioary)

# Delete the item

# del dictioary["age"]
# print(dictioary)

# delete the dictionary

# del dictioary
# # print(dictioary)


# nested Dictionary
# Student= {
#     "name": "Goutam kushwah",
#     "age": 24,
#     "city": "Indore",
#     "cource":"MCA",
#     "sem":"4 sem",
#     "Sub":{301:"cloud computing",
#            302 : "Advance Python",
#            303 : "Information Security"
#  }
# }
# print(Student)

# use of dict()
# student = dict(name="Goutam", age=22, course="Python")

# print(student)

# Convertin dictionary into datafram

# import pandas as pd

# data = {
#     'Name': ['Goutam', 'Anjali', 'Rohan'],
#     'Age': [24, 22, 27],
#     'City': ['Delhi', 'Mumbai', 'Bangalore']
# }

# df = pd.DataFrame(data)
# print(df)


 

# some try and error

# Genrate memory address of the object


# Object          Type,Hashing Behavior
# Integers,       Usually hash(n) == n. Persistent across sessions.
# Strings,        Salted. Changes every time you restart.
# Floats,         Salted/Algorithm-dependent. Often changes across sessions.
# Tuples,         Salted (because they contain other objects). Changes every time.



# print(hash(3.14))
# print(hash("lorem"))
# print(hash((1, 2, 3)))
# print(hash(3.146545315650564180560))
# print(hash("Lorem ipsum dolor sit amet, consectetur adipisicing elit,"
#  "sed do eiusmod tempor incididunt ut labore et dolore magna"
#  "aliqua. Ut enim ad minim veniam, quis nostrud exercitation"
#  "ullamco laboris nisi ut aliquip ex ea commodo consequat."
#  "Duis aute irure dolor in reprehenderit in voluptate velit"
#  "esse cillum dolore eu fugiat nulla pariatur. Excepteur sint"
#  "occaecat cupidatat non proident, sunt in culpa qui officia"
#  "deserunt mollit anim id est laborum."))
# print(hash("goutam"))
# print(hash("goutam"))
# print(hash("Goutam")==hash("Goutam"))
# print(hash("Goutam")==hash("Go"))

# hashmap = {}
# hashmap["name"] = "Goutam"
# hashmap["age"] = 24
# hashmap["city"] = "Indore"
# print(hashmap)


# import pandas as pd
# emp_details = {'Employee': {'Goutam': {'ID': '001',
#                                      'Salary': 2000,
#                                      'Designation':'Python Developer'},
#                             'Devang': {'ID':'002',
#                                     'Salary': 2300,
#                                     'Designation': 'Java Developer'},
#                             'Diksha': {'ID': '003',
#                                     'Salary': 1843,
#                                     'Designation': 'Hadoop Developer'}}}

# df= pd.DataFrame(emp_details['Employee'])
# print(df)

# def hash_function(text):
#    return sum(ord(character) for character in text)
# print(hash_function("Goutam"))
# print(hash_function("Goutam"))

# def hash_function(key):
#      return sum(ord(character) for character in str(key))

# print(hash_function("Lorem"))
# print(hash_function(3.14))
# print(hash_function(True))
# def hash_function(key):
#     return sum(ord(character) for character in repr(key))

# print(hash_function("Lorem"))
# print(hash_function(3.14))
# print(hash_function(True))
# print(repr(3.14))

