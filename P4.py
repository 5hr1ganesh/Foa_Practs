# binary tree traversals
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def printInorder(root):
    if root:
        # First recur on left child
        printInorder(root.left)

        # then print node
        print(root.val),

        # now recur on right child
        printInorder(root.right)


# A function to do postorder traversal
def printPostorder(root):
    if root:
        # First recur on left child
        printPostorder(root.left)
        # recur on right child
        printPostorder(root.right)
        # now print data
        print(root.val)


# A function for preorder traversal
def printPreorder(root):
    if root:
        print(root.val)

        printPreorder(root.left)

        printPreorder(root.right)


# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print("Preorder traversal of binary tree is")
printPreorder(root)
print("Inorder traversal of binary tree is")
printInorder(root)
print("postorder traversal of binary tree")
printPostorder(root)
