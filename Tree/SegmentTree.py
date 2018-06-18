class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.total = 0

class SegmentTree:
    def __init__(self, numbers):
        self.numbers = numbers

        def create_segment_tree(numbers, start, end):
            if start > end:
                return None
            if start == end:
                node = Node(start, end)
                node.total = numbers[start]
                return node
            mid = (start + end) // 2
            node = Node(start, end)
            node.left = create_segment_tree(numbers, start, mid)
            node.right = create_segment_tree(numbers, mid + 1, end)
            node.total = node.left.total + node.right.total
            return node

        self.root = create_segment_tree(numbers, 0, len(arr) - 1)

    def update(self, i, val):

        def update_query(node, i, val):
            if node.start == node.end:
                node.total = val
                return node
            mid = (node.start + node.end) // 2
            if i <= mid:
                update_query(node.left, i, val)
            else:
                update_query(node.right, i, val) 
            node.total = node.left.total + node.right.total
        update_query(self.root, i, val)

    def range(self, i, j):

        def range_query(node, i, j):
            if node.start == i and node.end == j:
                return node.total
            mid = (node.start + node.end) // 2
            if j <= mid:
                return range_query(node.left, i, j)
            elif i >= mid + 1:
                return range_query(node.right, i, j)
            else:
                return range_query(node.left, i, mid) + range_query(node.right, mid + 1, j)
        
        return range_query(self.root, i, j)

    def iterateSegmentTree(self, root):
        queue = [segment_tree.root]
        while queue:
            n = queue.pop(0)
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)
            if not n.left and not n.right:
                print(n.total, end = ' ')
        print()


arr = [1, 2, 4, 1, 6, 7, 9, 2]
segment_tree = SegmentTree(arr)
# segment_tree.update(2,0)
segment_tree.iterateSegmentTree(segment_tree.root)
print(segment_tree.root.total)
#segment_tree.update(2,0)
print(segment_tree.range(0,4))