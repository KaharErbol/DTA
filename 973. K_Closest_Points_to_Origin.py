class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(x ** 2 + y ** 2) ** 0.5 for x, y in points]
        min_heap = []
        for i in range(len(points)):
            min_heap.append((distances[i], points[i]))
        min_heap.sort()
        return [ min_heap[i][1] for i in range(k)]


### 2nd Solution used heapq
# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         min_heap = []
#         for i in range(len(points)):
#             dst = (points[i][0] ** 2 + points[i][1] ** 2) ** 0.5
#             heapq.heappush(min_heap, (dst, points[i]))
        
#         return [ heapq.heappop(min_heap)[1] for _ in range(k)]