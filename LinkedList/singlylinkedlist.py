class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:

    def __init__(self, head):
        self.head = head

    def traverse(self): 
        head = self.head
        while head:
            print(head.data, end = ' ')
            head = head.next
        print()

    def lenght(self):
        head = self.head
        size = 0
        while head:
            size += 1
            head = head.next
        return size

    def insert_at_pos(self, data, position): # 0 based positioning
        head = self.head
        while position  != 1:
            if head:
                position -= 1
                head = head.next
            else:
                print('position is more than the size of linked list.')
                break
        if position == 1:
            node = Node(data)
            node.next = head.next
            head.next = node

    def insert_at_head(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def delete(self,position): # 0 based
        if self.head is None:
            print('no element in linked list') 
        elif position == 0:
            self.head = self.head.next
        else:
            head = self.head
            while position > 1 and head:
                head = head.next
                position -= 1
            if head.next:
                head.next = head.next.next
            else:
                print('elements are less than the position')



a = Node(0)
b = Node(1)
c = Node(2)
d = Node(3)
e = Node(5)
f = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

singly_linked_list = SinglyLinkedList(a)
singly_linked_list.insert_at_pos(4, 4)
singly_linked_list.insert_at_head(-1)
singly_linked_list.insert_at_head(-2)
singly_linked_list.traverse()
#print('size is {}'.format(singly_linked_list.lenght()))
singly_linked_list.delete(9)
singly_linked_list.traverse()

