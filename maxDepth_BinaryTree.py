#WAP to find the maximum depth of a binary tree
#Resource: https://www.youtube.com/watch?v=rN5PhCkauD4&list=PLFV6T8f5WU2FRO_Hu7q9b18yB1P98NSZd&index=6
"""
Algorithm

formula to find the height of bianry tree = 1+no of max edges from root to leaf node
Example:

            [1]
            / \
          [2] [3]
          / \   \
        [4] [5] [6]
          \
          [7]

Here, the height of binary tree would be 4. WHY?
Formula = 1 + 3

The logic is divided in 3 stages
if (A==None)
    return 0
else
1) lDepth = height_tree(A.left)
2) rDepth = height_tree(A.right)
3) if (lDepth > rDepth):
    return (1 + lDepth)
   else:
    return (1 + rDepth)

All 3 stages will be checked for each node in the tree
"""

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def height_tree(A):
    if(A == None):
        return 0
    else:
        #Stage 1
        lDepth = height_tree(A.left)

        #Stage 2
        rDepth = height_tree(A.right)

        #Stage 3
        if(lDepth > rDepth):
            return (1+lDepth)
        else:
            return (1+rDepth)

#creating a Binary Tree
root = Node(1)
root.left  = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.right = Node(7)
root.right.right = Node(6)


print(height_tree(root))
