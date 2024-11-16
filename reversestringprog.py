"""
WAP to reverse a string
"""

s = "I am Anand and I can speak and understand 6 languages"
sent = []
for each in s:
    s1 = ' '.join(s.split()[::-1])
    
print(s1)
