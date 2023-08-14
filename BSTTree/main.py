class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # truong hop nay ta khong co node root san !!!
    def insert(self, data):
        if self.data is not None:
            if self.data < data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            if self.data > data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
        else:
            self.data = data

    def print_tree(self):
        if self.left is not None:
            self.left.print_tree()
        print(self.data, end=' ')
        if self.right is not None:
            self.right.print_tree()

    # breadth-first traversal
    def height(self, root):
        if root is None:
            return 0
        else:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            return max(left_height, right_height) + 1

    def printCurrentLevel(self, root, level):
        if root is None:
            return
        if level == 1:
            print(root.data, end=' ')
        else:
            self.printCurrentLevel(root.left, level-1)
            self.printCurrentLevel(root.right, level-1)

    def printLevelOrder(self, root):
        h = self.height(root)
        for i in range(1, h+1):
            self.printCurrentLevel(root, i)

    # three traversal below is depth-first traversal
    def inorder_traversal(self, root, lst):
        if root is None:
            return
        self.inorder_traversal(root.left, lst)
        lst.append(root.data)
        self.inorder_traversal(root.right, lst)
        return lst

    def postorder_traversal(self, root, lst):
        if root is None:
            return
        self.postorder_traversal(root.left, lst)
        self.postorder_traversal(root.right, lst)
        lst.append(root.data)
        return lst

    def preorder_traversal(self, root, lst):
        if root is None:
            return
        lst.append(root.data)
        self.preorder_traversal(root.left, lst)
        self.preorder_traversal(root.right, lst)

        return lst


if __name__ == '__main__':
    """tree = Node(27)
    tree.insert(10)
    tree.insert(26)
    tree.insert(73)
    tree.insert(36)
    tree.insert(62)
    tree.print_tree()
    print()
    lst1 = []
    lst2 = []
    lst3 = []
    print(tree.inorder_traversal(tree, lst1))
    print(tree.preorder_traversal(tree, lst2))
    print(tree.postorder_traversal(tree, lst3))
    print(tree.height(tree))
    tree.printLevelOrder(tree)"""
    tree = Node(10)
    tree.insert(7)
    tree.insert(12)
    print(tree.height(tree))
    test = "" in "VX"
    print(test)
    i = 1
    if i in (0,1,2):
        print(True)
