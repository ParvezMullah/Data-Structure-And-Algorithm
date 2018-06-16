class Node:

    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

class DoublyLinkedList:
    
    def __init__(self, head):
        self.head = head

    def traversal(self):
        head = self.head
        while head:
            print(head.data, end = ' ')
            head = head.next
        print()

    def reverse_traversal(self):
        head = self.head
        while head.next:
            head = head.next
        while head:
            print(head.data, end = ' ')
            head = head.previous


a = Node(0)
b = Node(1)
c = Node(2)

a.next = b
b.previous = a
b.next = c
c.previous = b

doubly_linked_list = DoublyLinkedList(a)
doubly_linked_list.traversal()
doubly_linked_list.reverse_traversal()