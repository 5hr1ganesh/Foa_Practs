# insert elements into binary tree
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class Tree:
    def __init__(self):
        self.root = None

    def add_Node(self, key, node=None):
        if node is None:
            node = self.root

        if self.root is None:
            self.root = Node(key)
            print(key, "root")
        else:
            if key <= node.key:
                if node.left is None:
                    node.left = Node(key)
                    node.left.parent = node
                    print(key, "left")
                    return
                else:
                    return self.add_Node(key, node=node.left)
            else:
                if node.right is None:
                    node.right = Node(key)
                    node.right.parent = node
                    print(key, "right")
                    return
                else:
                    return self.add_Node(key, node=node.right)


t = Tree()
t.add_Node(12)
t.add_Node(14)
t.add_Node(36)
t.add_Node(26)
t.add_Node(39)
