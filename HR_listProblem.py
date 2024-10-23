#LIST
#Problem Statement: https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true


if __name__ == '__main__':
    n = int(input())  # Read number of commands
    lst = []          # Initialize an empty list
    
    for _ in range(n):
        operation = input().split()  # Read the command and split into operation and values
        op = operation[0]            # The command (e.g., "insert", "print", etc.)

        # Handle different operations based on the input command
        if op == "insert":
            i = int(operation[1])
            val = int(operation[2])
            lst.insert(i, val)  # Insert val at index i
        elif op == "print":
            print(lst)          # Print the list
        elif op == "remove":
            val = int(operation[1])
            lst.remove(val) # Remove the first occurrence of val
        elif op == "append":
            val = int(operation[1])
            lst.append(val) # Append val to the end of the list
        elif op == "sort":
            lst.sort()           # Sort the list
        elif op == "pop":
            lst.pop()            # Remove the last element
        elif op == "reverse":
            lst.reverse()        # Reverse the list
