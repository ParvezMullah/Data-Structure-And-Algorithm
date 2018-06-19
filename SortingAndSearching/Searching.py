class Searching:

    def linear_search(self, arr, value):   # O(n)
        for i in range(len(arr)):
            if arr[i] == value:
                return i
        return 'not found!'


    def binary_search(self, arr, value, start, end): # O(logn) 
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == value:
                return mid
            elif arr[mid] > value:
                end = mid - 1
            else:
                start = mid + 1
        return 'not found!'


        """
            pos = low + [ ((high - low) * (key - a[low]) ) // a[high] - a[low] ]
        """
    def interpolation_search(self, arr, value): # O(log(logn)) if evenly distributed data
        start = 0
        end = len(arr) - 1
        while start <= end and arr[start] <= value and arr[end] >= value:
            pos = start + (( (end - start) *  (value - arr[start]) ) // (arr[end] - arr[start])) 
            if arr[pos] == value:
                return pos
            elif arr[pos] > value:
                end = pos - 1
            else:
                start = pos + 1
        return 'not found!'


    def jump_search(self, arr, value): #O(sqrt(n))
        n = len(arr)
        jump = int(n ** 0.5)
        start = jump
        while start < n and arr[start] <= value :
            start += jump
        begin = start - jump
        while begin < n and begin <= start:
            if arr[begin] == value:
                return begin
            begin += 1
        return 'not found!'

        
    def exponential_search(self, arr, value):
        start, end = 0, 1
        expo = 1
        while arr[end] < value and end < len(arr):
            start, end = end, end + expo**2
            expo += 1
        return self.binary_search(arr, value, start, end)

arr = [2, 2, 4, 6, 8, 21, 21, 32, 34, 37, 50, 53, 57, 89, 90, 675]
value = 37
searching = Searching()
print(searching.linear_search(arr, value))
# print(searching.binary_search(arr, value, 0, len(arr) - 1))
#print(searching.interpolation_search(arr, value))
#print(searching.jump_search(arr, value))
print(searching.exponential_search(arr, value))