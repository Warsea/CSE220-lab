class Node:
    def __init__(self, d=None):
        self.data = d
        self.next = None

class Mylist:
    def __init__(self, arr=[]):
        # self.head = None
        # current = self.head
        # for i in arr:
        #     new_node = Node(i)
        #     if self.head is None:
        #         self.head = new_node
        #         current = self.head
        #     else:
        #         current.next = new_node
        #         current = current.next
        self.head = Node()
        current = self.head
        for i in arr:
            new_node = Node(i)
            if self.head.next is None:
                self.head.next = new_node
                current = self.head.next
            else:
                current.next = new_node
                current = current.next

    def showList(self):
        current = self.head
        if current.next is None:
            print('Empty list')
            return 0
        while current.next != None:
            current = current.next
            print(current.data)

            
    def isEmpty(self):
        if self.head.next is None:
            return True
        else:
            return False

    def clear(self):
        current = self.head
        while current.next == None:
            current = current.next
            prev = current
            current = None
            current = prev.next

l = Mylist([2,5,4])
l.showList()

print(l.isEmpty())

l4 = Mylist([3,5,3,2,5])
l4.clear()
l4.showList()