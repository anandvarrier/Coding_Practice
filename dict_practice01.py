"""
Dictionary Practice
"""

#Convert 2 lists to dictionary
#Using zip method
keys = [1,2,3]
values = ['A','B','C']

zipp = dict(zip(keys, values))

print(zipp)

#==================

#using for update method
keys01 = [4,5,6]
values01 = ['D','E','F']

new_dict = dict()
for i in range(len(keys01)):
    new_dict.update({keys01[i]: values01[i]})

print(new_dict)
