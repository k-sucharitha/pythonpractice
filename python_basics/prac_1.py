"""
string (lower, upper, capitalize, count, find, format, join, split, strip, islower, isupper, isalpha, isalnum, isdigit, isnumeric, replace)
lists (append, extend, insert, pop, index, sort, sorted, remove, count, sum, len, max, min)
tuple (index, count, sum, len, max, min)
dictionaries (items, keys, values, update, get)
"""


string = """Contrary to popular belief, Lorem Ipsum is not simply random text. 
It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. 
Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, 
looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, 
and going through the cites of the word in classical literature, discovered the undoubtable source. 
Lorem Ipsum comes from sections 1.10.32 and 1.10.32 of "de Finibus Bonorum et Malorum" 
(The Extremes of Good and Evil) by Cicero, written in 45 BC. 
This book is a treatise on the theory of ethics, very popular during the Renaissance. 
The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32"""


# print(string.lower()) # All letters in the given string can be converted to lower-Case
# print(string.upper()) # All letters in the given string can be converted to UPPER-Case
# print(string.capitalize()) # Fisrt letter of the string becomes Capital Letter

## split() function returns list of strings. This function helps us to split the given string based on the delimeter.
# print(string.split()) # default parameter: ' ' (whitespace) {string.split(' ')}
# print(len(string.split())) ## returns how many words present in the given string
# print(string.split('.')) # splitting the paragraph with delimeter: '.' (pointer/full-stop)
# print(len(string.split('.'))) # retruns how many sentences in the given string
# print(string.split('1.10.32')) # splits the string with the given delimeter

# name = 'Vinay Kumar Reddy' # ['Vinay', 'Kumar', 'Reddy']
# print(name.split('a')) # ['Vin', 'y Kum', 'r Reddy']
# print(name.split('Vinay')) # ['', ' Kumar Reddy']
# print(name.split('V')) # ['', 'inay Kumar Reddy']
# print(name.split('Suchi')) # ['Vinay Kumar Reddy']
# print(name.split('vinay')) # ['Vinay Kumar Reddy']

## Strip() fucntion returns String by removing passed parameter-characters from the given string at both start & end.
# name = '   Kumar   '
# name1 = 'vivvvnaykumarreddyiviiii'
# print(name.strip()) # 'Kumar'
# print(name.strip('a')) # '   Kumar   '
# print(name1.strip('vi')) # 'naykumarreddy'

## rstrip() fucntion returns String by removing passed parameter-characters from the given string at the end
## lstrip() fucntion returns String by removing passed parameter-characters from the given string at the start
# name1 = 'vivvvnaykumarreddyiviiii'
# print(name1.rstrip('vi')) # 'vivvvnaykumarreddy'
# print(name1.lstrip('vi')) # 'naykumarreddyiviiii'

## find() used to return the lowest index value of the first occurrence of the substring from the input string; else it returns -1. 
# name = 'vivvvnaykumarreddyiviiii'
# print(name.find('iv'))


## format() is a technique of the string category permits you to try and do variable substitutions and data formatting.
# string = '{} is a good option for beginners in python'
# v = [1, 2, 3] # int/str/list/tuple/dict any type can be replaced in the {} while using format()
# print(string.format(v))

# string = '{} is a good option for {} in python'
# v = [1, 2, 3] # int/str/list/tuple/dict any type can be replaced in the {} while using format()
# print(string.format(v)) # error must pass two args to replace two {} in string
# print(string.format(v,v))

## positional vs named args
# --------------------------
# 1) positional formatting
# string = '{} is a good option for {} in python'
# a = "dash_1"
# b = "dash_2"
# print(string.format(a,b)) # dash_1 is a good option for dash_2 in python
# print(string.format(b,a)) # dash_2 is a good option for dash_1 in python

# 2) named formatting
# string = '{x1} is a good option for {x2} in python'
# a = "dash_1"
# b = "dash_2"
# print(string.format(x1="vinay",x2="hdsbhdsbs")) # vinay is a good option for hdsbhdsbs in python
# print(string.format(x2=a,x1=b)) # dash_2 is a good option for dash_1 in python

# suchi_details = {"name":"Suchi", "age":23}
# vinay_details = {"name":"Vinay", "age":27}
# bharathi_details = {"name":"Bharathi", "age":51}

# # print("Hi, MY name is Suchi I am 23 years old") # static print (values are hard-coded)
# # dynamic print (using string format())
# print("Hi, MY name is {name} I am {age} years old".format(name=bharathi_details['name'], age=bharathi_details['age'])) 

# join() is an inbuilt string function in Python used to join elements of the sequence separated by a string separator
# list = ["1","2","3","4"] # an iterable object
# string = "vinaykumar" # an iterable object
# tuple = ("vinay", "kumar", ) # an iterable object
# dict = {"mobile":"one plus", "price":"40,999"} # an iterable object
# object = 23 # not an iterable object

# print(" --> ".join(list)) # 1 --> 2 --> 3 --> 4
# print(" --> ".join(string)) # v --> i --> n --> a --> y --> k --> u --> m --> a --> r
# print(" --> ".join(tuple)) # vinay --> kumar
# print(" --> ".join(dict)) # mobile --> price
# print(" --> ".join(object)) # TypeError: can only join an iterable


## isalnum() returns Bool type values (True/False)
""" alpha-numeric means string contains either alphabets or numbers or mix of alphabets and numbers """
# string = "abc123"
# print(string.isalnum()) # True
# print("abc".isalnum()) # True
# print("123".isalnum()) # True
# print("abc$%".isalnum()) # False
# print("".isalnum()) # False {empty strings are not considered as alpha-numerics}


## isalpha() returns Bool type values (True/False)
""" alpha means string contains only alphabets """
# string = "abc"
# print(string.isalpha()) # True
# print("123".isalpha()) # False
# print("abc123".isalpha()) # False
# print("".isalpha()) # False


## isnumeric() returns Bool type values (True/False)
""" numeric means string contains only numbers """
# string = "123"
# print(string.isnumeric()) # True
# print("abc".isnumeric()) # False
# print("abc123".isnumeric()) # False
# print("".isnumeric()) # False


## isdigit() returns Bool type values (True/False)
""" digit means string contains only numbers """
# string = "123"
# print(string.isdigit()) # True
# print("abc".isdigit()) # False
# print("abc123".isdigit()) # False
# print("".isdigit()) # False

## islower() returns Bool type values (True/False)
""" lower means string contains only lower-case alphabets (a, b, c, .., z) """
# string = "vinay"
# print(string.islower()) # True
# print("Vinay".islower()) # False
# print("".islower()) # False


## isupper() returns Bool type values (True/False)
""" upper means string contains only upper-case alphabets (A, B, C, D, ..., Z) """
# string = "vinay"
# print(string.isupper()) # False
# print("Vinay".isupper()) # False
# print("VINAY".isupper()) # True
# print("".isupper()) # False

## replace() method replaces a specified phrase with another specified phrase
""" replace() takes two args 1) which value to be replaced 2) what is the new value we are replacing with """
# string = "vinay" 
# print(string[0], string[-1]) # v y
# string[0] = 'k' # cannot make item assignment 
# string.replace("vin", "ab")
# print(string) # abay (WRONG expected output)?
# Ans: Strings are immutable. that means we cannot change the value ***directly***.
# new_string = string.replace("vin", "ab")
# print(new_string) # abay 
# (old variable string is not modified directly but the value is getting replaced and we are saving into new variable new_string)

########################################################################################
## My Practice 
# name= "vinay"
# print(name)
# print(name.lower())
# print(name.upper())
# print(name.find("na"))
# print(name.count("vi"))
# print(name.strip())
# print(name.strip("nay"))
###################################################################################

# Tuple data type is an immutable data type 
# that means values/elements in the tuple containers cannot be changed.
tup = (4,5,3, 2,1,3,3) 
# print(tup.count(3)) # 3
# print(tup.index(3)) # 2 returns the index of First occurence element
# print(sum(tup)) # 21
# print(len(tup)) # 7
# print(min(tup)) # 1
# print(max(tup)) # 5

# tup.sort() # throws error: AttributeError: 'tuple' object has no attribute 'sort'
###################################################################################

# Dictionaries acts like HashMap that means 
# Dict object does not allow having duplicate Keys. (*** Important Note)
# If we try to update/add an existing key with new value again to the dictionary, then value for the key gets overrided.
# Note: Dictionary keys should be always of type immutable that means dict allows str, tuple, int as their keys. 
# We cannot keep list data type as a Dict key. 

# d = {} # empty dict
# # d.update([1,2]) # update function accepts only dictionary object as an arg
# d.update({"name": "vinay"}) 
# print(d) # d = {"name": "vinay"}

# d.update({"age":24})
# print(d) # d = {"name": "vinay", "age":24}

# d.update({"name":"kumar"}) 
# print(d) # d = {"name": "kumar", "age":24}

# print(d.items()) # [('name', 'kumar'), ('age', 24)] items() returns key:val in tuples
# print(d.keys()) # ['name', 'age'] keys() returns in list
# print(d.values()) # ['kumar', 24] values() returns in list

# for key in d: # iteration occurs on dict keys() by default 
#     print(key) # returns key for each iteration

# for item in d.items(): # performing iteration on dict ietms()
#     print(item) # returns (key, value) in form of tuple for each iteration. Eg: ('name', 'kumar')
#     print(item[0]) # to see the key Eg: name
#     print(item[1]) # to see the val Eg: kumar


# for key, val in d.items(): # performing iteration on dict ietms()
#     print(key) # unpacks the (key, val) tuple to key, value for each iteration Eg: name 
#     print(val) # Eg: kumar

## Testing what data types allowed as dict keys (List and Dict data types are not allowed as dict keys)
# d = {"name":"vinay", (1,2):45, 3:"hyd", {"a":"n"}:678, [1,2]:8, None:"NA", True:67} # Not allowed
# d = {"name":"vinay", (1,2):45, 3:"hyd", [1,2]:8, None:"NA", True:67} # Not allowed
# d = {"name":"vinay", (1,2):45, 3:"hyd", None:"NA", True:67} # Allowed
# d = {"name":"vinay", (1,2):45, 3:"hyd"} # Allowed
# print(d)


## 1) Dict object does not allow having duplicate Keys. (your keys shouldn't get modified at run time)
# d = {1:{"a":[]}, 3:4, 1:5} # key 1 is duplicated so it considers the last occurence val that means {1:5}

## 2) Dict cannot allow unhashable data types (like Lists and Dictionaries) as its keys
# li = ['vinay', 2, 4, 'hyd']
# d = {li:56} # why Lists are not considered as dict keys? (unhashable type: 'list')
# Ans: you can modify the list. Lists are mutable. We can make the item assignemnt in List data types. 
# li[3]='bang' --> ['vinay', 2, 4, 'bang']
# if your List->li is modified then what if the purpose of keeping this one as your dict key

# dict = {'vinay': 'hyd', 'sree':'bang'}
# d = {dict:56} # why Dicts are not considered as dict keys? (unhashable type: 'dict')
# Ans: you can modify the dictionary. Dicts are mutable. dict['sree']='pune' --> dict = {'vinay': 'hyd', 'sree':'pune'}
# if your List->li is modified then what if the purpose of keeping this one as your dict key


## 3) you can only read the elements with the help of index position from immutbale objects.
# We cannot make item assignment on immutable objects like strings, tuples.
# string = "vinay" 
# print(string[0]) # v
# print(string[-1]) # y
# string[0] = 'k' # Correct or Wrong statement ?
# # Ans: Strings are Immutable. TypeError: 'str' object does not support item assignment

# tu = (2,3,4)
# tu[0] = 5 # TypeError: 'tuple' object does not support item assignment

## get() in dict
# dict = {"city":"HYD", "country":'IND'}
# dict.items() # [("city", "HYD"), ("country", 'IND')]
# dict.keys() # ['city', 'country']
# dict.values() # ['HYD', "IND"]
# # print(dict.get()) # get() takes one arg i.e. we need to pass key
# print(dict.get('city'), dict['city']) # 'HYD''HYD'

## why do we use get() if we can access the value by calling the key name in square bracket format??
# print(dict['state']) # KeyError: 'state' i.e  state key is not defined/found in the dict
# print(dict.get('state')) # None (No Error)
# print(dict.get('state', "NO state provided")) # NO state provided (No Error)

## Ans: suppose let's say we have list of dictionaries. 
# Find all the state values provided in the list. If state is not provided print 'Not Available'
l = [
    {"city":"Bang", "country":'IND', 'state':'karnataka'}, 
    {"city":"Pune", "country":'IND', 'state':'Maharashtra'}, 
    {"city":"HYD", "country":'IND'}, 
    {"city":"Chennai", "country":'IND'}
    ]

# print(l[0].get('state')) # karnataka
# print(l[1].get('state')) # Maharashtra
# print(l[2].get('state')) # None
# print(l[3].get('state')) # None

# for obj in l:
#     print(obj.get('state', "Not Provided"))

## sorting the list of dictionaries. sort() function plays with '<' and '>'
# l = [1,2,3,8,7,0,54,23]
# l.sort() # arrange the elements in ascending order by default
# print(l) # [0, 1, 2, 3, 7, 8, 23, 54] # 1<2? 1<3? 1<8? 1<0?(swap) 


## Know the operation/usage of '<', '>' on which Data Types (cannot apply on dict types)
## 1) We can apply < on same types of int, str, list, tuple, bool instances
# print(4<5) # True
# print("vinay"<"kumar") # False (if you apply < on str objects it arranges the strings in alphabetical order)
# print([1,2]<[3,4]) # True
# print((1,2)<(3,4)) # True
# print(True<False) # False # (1<0)

# print({"a":1}<{"a":2}) # TypeError: '<' not supported between instances of 'dict' and 'dict'

## 2) We cannot apply < on different types of instances
# print(4<"5") # TypeError: '<' not supported between instances of 'int' and 'str'
# print("vinay"<[1,2]) # TypeError: '<' not supported between instances of 'str' and 'list'
# print([1,2]<(3,4)) # TypeError: '<' not supported between instances of 'str' and 'list'
# print((1,2)<{"a":(3,4)}) # TypeError: '<' not supported between instances of 'tuple' and 'dict'
# print(True<"vinay") # TypeError: '<' not supported between instances of 'bool' and 'str'

## We cannot apply sort() on a list which are having different types of elements
# l = [2, "vinay", [], (), True] # 2<"vinay"? (int<str)
# l.sort() # TypeError: '<' not supported between instances of 'str' and 'int'

## We cannot apply sort() directly on a list of dictionaries

l = [
    {"city":"Bang", "country":'IND', 'state':'karnataka', 'cases':3456}, 
    {"city":"Pune", "country":'IND', 'state':'Maharashtra', 'cases':9876}, 
    {"city":"HYD", "country":'IND', 'cases':78}, 
    {"city":"Chennai", "country":'IND', 'cases':12345}
    ]

# print("Input list to be sorted:: \n", l)
l.sort(key=lambda x:x['cases'], reverse=True) # list of dict gets sorted as per cases in asc order
print(l)
sorted_l = sorted(l, key=lambda i: i['cases'], reverse=True)
print(sorted_l)

# city - cases
# for x in sorted_l:
#     print(x['city'], x['cases']) # x={'city': 'Chennai', 'country': 'IND', 'cases': 12345}

# l=[5,3,2,4,1]

# a = l.sort()
# print(sorted(l))
