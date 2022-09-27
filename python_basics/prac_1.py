"""
string (lower, upper, capitalize, count, find, format, join, split, strip)
lists (append, extend, insert, pop, index, sort, remove, count, sum, len, max, min)
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

########################################################################################
###################################################################################
name= {}"vinay"{}
print(name)
print(name.lower())
print(name.upper())
print(name.find("na"))
print(name.count("vi"))
print(name.strip())
print(name.strip("nay"))

