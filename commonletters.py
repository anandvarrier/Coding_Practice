#WAP to find common letter in 2 strings

def common_letters():
    s1 = 'ANAND'
    s2 = 'SHAMBHAVI'

    str1 = set(s1)
    str2 = set(s2)

    common = str1 & str2
    print(common)

common_letters()
