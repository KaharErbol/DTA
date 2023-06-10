class MinHeap:
    def __init__(self):
        self.heap = [None]
        self.size = 0

    def insert(self, val):
        self.heap.append(val)
        self.size += 1
        self._swap(self.size)

    def _swap(self, idx):
        while idx // 2 > 0:
            if self.heap[idx] < self.heap[idx // 2]:
                self.heap[idx // 2], self.heap[idx] = self.heap[idx], self.heap[idx // 2]
            idx = idx // 2

    def sort(self):
        result = []
        while len(self.heap) > 1:
            result.append(self.remove())
        return result
    
    def min_child(self, idx):
        # if right child is out of idex range
        if idx * 2 + 1 > self.size:
            return idx * 2 # left child
        else:
            if self.heap[idx * 2] < self.heap[idx * 2 + 1]:
                return idx * 2 # left child
            else:
                return idx * 2 + 1 # right child

    def _swap_down(self, idx):
        # while left child is within index range
        while (idx * 2) <= self.size:
            mc = self.min_child(idx)
            if self.heap[idx] > self.heap[mc]:
                self.heap[idx], self.heap[mc] = self.heap[mc], self.heap[idx]
            idx = mc

    def remove(self):
        smallest = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        self._swap_down(1)
        return smallest

    def build_heap(self, arr):
        i = len(arr) // 2
        self.size = len(arr)
        self.heap = [0] + arr[:]
        while i > 0:
            self._swap_down(i)
            i -= 1

    def sort(self):
        result = []
        i = self.size
        while i > 0:
            result.append(self.remove())
            i -= 1
        return result


# min_heap = MinHeap()
# min_heap.insert(20)
# min_heap.insert(19)
# min_heap.insert(22)
# min_heap.insert(17)
# min_heap.insert(21)
# min_heap.insert(15)
# min_heap.insert(23)
# min_heap.insert(25)
# min_heap.insert(26)


# print("Heap: ", min_heap.heap)
# print("Size: ", min_heap.size)
# removed = min_heap.remove()
# print("Removed: ", removed)
# print("New Heap: ", min_heap.heap)
# print("New Size: ", min_heap.size)

arr_heap = MinHeap()
arr = [9,6,5,2,3]

arr_heap.build_heap(arr)
print(arr_heap.heap)

print("Sorted: ", arr_heap.sort())