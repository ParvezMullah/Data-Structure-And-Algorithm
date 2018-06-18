class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, arr):
        self.head = None

        def construct_binary_search_tree(arr):
            node = Node(arr[0])
            self.head = node
            for i in range(1, len(arr)):
                temp_node = self.head
                node = Node(arr[i])
                while True:
                    if arr[i] <= temp_node.data:
                        if temp_node.left:
                            temp_node = temp_node.left
                        else:
                            temp_node.left = node
                            break
                    else:
                        if temp_node.right:
                            temp_node = temp_node.right
                        else:
                            temp_node.right = node
                            break
        construct_binary_search_tree(arr)

    def bst_insertion(self, data):
        node = Node(data)
        temp_node = self.head
        while True:
            if data <= temp_node.data:
                if temp_node.left:
                    temp_node = temp_node.left
                else:
                    temp_node.left = node
                    break
            else:
                if temp_node.right:
                    temp_node = temp_node.right
                else:
                    temp_node.right = node
                    break

    def bst_deletion(self, data):
        previous = self.head
        current = self.head
        while current and current.data != data:
            previous = current
            if data < current.data:
                current = current.left
            else:
                current = current.right
        if not current:
            print('{} not found!'.format(data))
            return
        if current.left is None and current.right is None:
            if current.data <= previous.data:
                previous.left = None
            else:
                previous.right = None
        elif current.left and current.right is None:
            if current.data > previous.data:
                previous.right = current.left
            else:
                previous.left =current.left
        elif current.left is None and current.right:
            if current.data > previous.data:
                previous.right = current.right
            else:
                previous.left = current.right
        else:
            temp_current = current.right
            temp_previous = current.right
            if current.right.left is None:
                temp_data = current.right.data
                current.right = current
                current.right= temp_data
                previous.right = current.right
                current.right = None
                
            while temp_current.left:
                temp_previous = temp_current
                temp_current = temp_current.left
            temp_previous.left = None
            temp_data = temp_current.data
            temp_current = current
            temp_current.data = temp_data
            if current.data > previous.data:
                previous.right = temp_current
            else:
                previous.left = temp_current

    def traversal(self):
        def in_order(head):
            if head:
                in_order(head.left)
                print(head.data, end = ' ')
                in_order(head.right)
        in_order(self.head)
        print()

arr = [50, 40, 30, 45, 42, 48, 60, 55, 65, 63, 67, 61, 64]
bst = BinarySearchTree(arr)
bst.traversal()
# bst.bst_insertion(56)
# bst.bst_insertion(-98)
# bst.bst_deletion(42)
bst.bst_deletion(50)
bst.traversal()

