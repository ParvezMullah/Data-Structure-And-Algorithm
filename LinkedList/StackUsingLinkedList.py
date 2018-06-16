class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self, head):
        self.head = head
        self.tail = head

    def __len__(self):
        size = 0
        head = self.head
        while head:
            size += 1
            head = head.next
        return size

    def traverse(self):
        head = self.head
        while head:
            print(head.data, end = ' ')
            head = head.next
        print()

    def push(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node
            self.tail = node
            return 1
        node = Node(data)
        self.tail.next = node
        self.tail = self.tail.next

    def pop(self):
        if self.tail is None:  # (if len(stack) == 0:)
            print('stack is empty')
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            head = self.head
            previous = self.head
            while head.next:
                previous = head
                head = head.next
            previous.next = None
            self.tail = previous


    
a = Node(0)
stack = Stack(a)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print('length of stack is ',len(stack))
stack.traverse()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.push(2)
print('length of stack is ',len(stack))
stack.traverse()