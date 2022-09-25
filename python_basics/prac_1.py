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

## find, format, join
# name = 'vivvvnaykumarreddyiviiii'
# print(name.find())


