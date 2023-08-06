#string menthods
string = 'Hello Word'
length = len(string)
print('length of the string is:', length)

upper = string.upper()
print('uppercase string:',upper)

lower = string.lower()
print('lowercase string:',lower)

count = string.count('o')
print('count of string:', count)

#list methods
list = [1,2,3,4]
length = len(list)
print('length of the string:',length)

list.append(5)
print('appended list:', list)

list.reverse()
print('reverse of list:', list)

list.sort()
print('sorted list is', list)

#dictionary methods
dict = {'name': 'john', 'age': 25, 'city': 'new york'}
length = len(dict)
print('length of the dictionary is', length)

keys = dict.keys()
print('dictionary keys', keys)

values = dict.values()
print('dictionary values:',values)

key_exist = 'age' in dict
print('does exist in dict',key_exist)

dict.pop('age')
print('dictionary',dict)
