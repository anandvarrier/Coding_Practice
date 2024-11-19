"""
Dictionary Practice
Merge two Python dictionaries into one
"""

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = {'Thirtyone': 31, 'Thirtytwo': 32}
dict2['Thirty'] = dict3
dict4 = {**dict1, **dict2}

print(dict4)
print(dict4.get('Thirty'))
