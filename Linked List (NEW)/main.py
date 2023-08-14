
class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def printList(self):
        it = self.head
        while it is not None:
            print(it.value, end=' ')
            it = it.next
        print()

    def add_head(self, e):
        if self.head is None:
            self.head = self.tail = Node(e)
            return
        newest = Node(e)
        newest.next = self.head
        self.head = newest

    def add_tail(self, e):
        if self.head is None:
            self.head = self.tail = Node(e)
            return
        newest = Node(e)
        self.tail.next = newest
        self.tail = newest

    def add_between(self, mid, e):
        if mid is None:
            raise Exception('The mention node is absent')
        else:
            newest = Node(e)
            newest.next = mid.next
            mid.next = newest

    def delete_node(self, key):
        headval = self.head

        if headval is not None:
            if headval.value == key:
                self.head = headval.next
                temp = None
                return

        while headval is not None:
            if headval.value == key:
                break
            prev = headval
            headval = headval.next

        if headval is None:
            return
        prev.next = headval.next
        headval = None

    def find_val(self, val):
        it = self.head
        while it is not None:
            if it.value is val:
                return True
            it = it.next
        return False


if __name__ == '__main__':
    lst = LinkedList()
    for i in range(11):
        lst.add_tail(i)
    lst.printList()
    x = int(input("Enter a value to add head: "))
    lst.add_head(x)
    lst.printList()
    y = int(input("Enter a value to add tail: "))
    lst.add_tail(y)
    lst.printList()
    # add between
    print("Add 1.5 to the linked list:")
    ptr = lst.head.next.next
    lst.add_between(ptr, 1.5)
    lst.printList()
    # delete head
    print("Delete head:")
    print(lst.find_val(-5))
    lst.delete_node(-5)
    lst.printList()
    # delete tail (11)
    print("Delete tail:")
    print(lst.find_val(y))
    lst.delete_node(y)
    lst.printList()
    # delete between (1.5)
    print("Delete between:")
    lst.delete_node(1.5)
    lst.printList()



