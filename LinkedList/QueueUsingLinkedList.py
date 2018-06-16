class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def traversal(self):
        if self.head is None:
            print('Queue is emply')
            return
        head = self.head
        while head:
            print(head.data, end = ' ')
            head = head.next

    def __len__(self):
        size = 0
        head = self.head
        while head:
            size += 1
            head = head.next
        return size

    def enqueue(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            return 
        self.tail.next = node
        self.tail = node

    def dequeue(self):
        if self.head is None:
            print('queue is empty ')
            return
        if self.tail == self.head:
            self.tail = None
            self.head = None
        else:
            self.head = self.head.next
        


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print('Length of queue is ', len(queue))
queue.traversal()

queue.dequeue()
queue.dequeue()
print('Length of queue is ', len(queue))
queue.traversal()
