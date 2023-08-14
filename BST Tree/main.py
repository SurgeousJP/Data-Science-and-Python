
class node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = node(value)
        else:
            if self.root.value < value:
                if self.root.left is None:
                    self.root.left = node(value)
                else:
                    self.root.left.insert(value)
            else:
                if self.root.right is None:
                    self.root.right = node(value)
                else:
                    self.root.right.insert(value)

    def printTree(self):
        if self.root.left is not None:
            self.root.left.printTree()
        print(self.root, end=' ')
        if self.root.right is not None:
            self.root.right.printTree()


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(6)
    bst.insert(8)
    bst.insert(7)
    bst.printTree()
