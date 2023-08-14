

class Tree:
    """Abstract base class representing tree data structures"""
    # ---------------------------nested Position class------------------------------------
    class Position:
        """An abstraction representing the location of a single element"""
        def element(self):
            """Return the element store at this Position"""
            raise NotImplementedError('This method must be implemented by subclass')

        def __eq__(self, other):
            """Return true if self and other representing the same location"""
            raise NotImplementedError('Must be implemented by subclass')

        def __ne__(self, other):
            """Return true if self and other not representing the same location"""
            return not self == other

    # -------------------abstract methods that concrete subclasses must support-----------
    def root(self):
        """Return the Position representing the tree's root"""
        raise NotImplementedError('Must be implemented by subclass')

    def parent(self, p):
        """Return the Position representing the p's parent position"""
        raise NotImplementedError('Must be implemented by subclass')

    def children(self, p):
        """Generate an iteration of Positions representing p's children position"""
        raise NotImplementedError('Must be implemented by subclass')

    def num_children(self, p):
        """Return the number of children that p's position has"""
        raise NotImplementedError('Must be implemented by subclass')

    def __len__(self):
        """Return the number of elements in tree"""
        raise NotImplementedError('Must be implemented by subclass')

    # ------------------concrete methods implemented in this class-------------------------
    def is_root(self, p):
        """Return true if p's position representing the root's position"""
        return p == self.root()

    def is_leaf(self, p):
        """Return true if p's position has no children"""
        return self.num_children(p) == 0

    def is_empty(self, p):
        """Return true if tree has no element"""
        return len(self) == 0

    def depth(self, p):
        """Return the number of levels separating p with the root"""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.children(p))

    def height(self, p):
        """Return the height of node p"""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + self.height(self.parent(p))


class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure"""
    # ----------------------additional abstract methods--------------------------
    def left(self, p):
        """Return the Position representing p's left child position, return None if p doesn't have it"""
        raise NotImplementedError('Must be implemented by subclass')

    def right(self, p):
        """Return the Position representing p's right child position, return None if p doesn't have it"""
        raise NotImplementedError('Must be implemented by subclass')

    # ---------------------concrete methods implemented in this class-------------
    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        """Generate an iteration of Position representing p's children"""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)



