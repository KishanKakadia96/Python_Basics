# No duplicate key is allowed 
# values can be of any type, while the keys must be immutable like numbers, tuples, or strings
# keys are case sensitive

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}   
print (Dict['Tiffany'])

# We can copy the entire dictionary to a new dictionary

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}	
studentX=Boys.copy()
studentY=Girls.copy()
print(studentX)
print(studentY)


# Dictionary items() Method
# Doing a normal for loop in the dict will only get the keys
for k, v in Dict.items():
    print(k, v)

# Preferably use .get method, because it will return None if the item isn't in the dictionary
# Instead of Dict['Charlie'], you can set the default value for keys that don't exist by setting an extra parameter
print(Dict.get('Charlie'))
print(Dict.get('Kishan', 'NOOOO'))

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print("Students Name: %s" % list(Dict.items()))

# Check if a given key already exists in a dictionary

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
for key in list(Boys.keys()):
    if key in list(Dict.keys()):
        print(True)
    else:       
        print(False)

# Sorting the Dictionary

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
Students = list(Dict.keys())
Students.sort()
for S in Students:
      print(":".join((S,str(Dict[S]))))

# Merging Dictionaries
# Merge two dictionaries using update() method

my_dict1 = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}

my_dict2 = {"firstName" : "Nick", "lastName": "Price"}

my_dict1.update(my_dict2)

print(my_dict1)

# Merging dictionaries using ** method 

my_dict1 = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}

my_dict2 = {"firstName" : "Nick", "lastName": "Price"}

my_dict =  {**my_dict1, **my_dict2} 

print(my_dict)


# Update, Delete, Append, Accessing elements

# Accessing elements

my_dict = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Gujarat"}
print("username :", my_dict['username'])
print("email : ", my_dict["email"])
print("location : ", my_dict["location"])


my_dict = {"Name":[],"Address":[],"Age":[]}

# Append elements to a key of dictionary

my_dict["Name"].append("Kishan")
my_dict["Address"].append("Gujarat")
my_dict["Age"].append(26)	
print(my_dict)

my_dict = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Gujarat"}
my_dict['name']='Nick'
print(my_dict)

# Deleting element in a dictionary

my_dict = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Gujarat"}

del my_dict['username']  # it will remove "username": "XYZ" from my_dict
# my_dict.pop("username")
print(my_dict)
my_dict.clear()  # will make the my_dict empty
print(my_dict)
# del my_dict (will delete the dictionary my_dict)

# Updating existing element in a dictionary

my_dict = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Gujarat"}

my_dict["username"] = "ABC"
print(my_dict)

# Insert a dictionary into another dictionary

my_dict = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Washington"}

my_dict1 = {"firstName" : "Nick", "lastName": "Price"}

my_dict["name"] = my_dict1

print(my_dict)