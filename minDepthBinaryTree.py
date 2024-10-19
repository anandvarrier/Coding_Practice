#WAP to find out the minimum depth of a binary tree

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def min_depth(tree):
    if tree == None:
        return 0
    else:
        lDepth = min_depth(tree.left)

        rDepth = min_depth(tree.right)

        if(lDepth>rDepth):
            return (1+rDepth)
        else:
            return (1+lDepth)
#difference between finding the minimum and maximum depth is the above if-else block

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(7)
root.left.left.right = Node(6)


print(min_depth(root))
