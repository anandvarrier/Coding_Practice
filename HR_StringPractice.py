"""
String Practice
You are given a string S and width w.
You have to wrap the string into a paragraph of width w.
TextWrap: https://docs.python.org/3/library/textwrap.html

Hacker_Rank problem: https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
"""

import textwrap

def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string, max_width))

if __name__ == '__main__':
    string, max_width = input("Enter the string: "), int(input("Enter the num: "))
    result = wrap(string, max_width)
    print(result)
