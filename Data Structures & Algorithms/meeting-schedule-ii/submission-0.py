"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        import heapq
        meetingRooms=1
        flat_intervals = []
        for i in intervals:
            flat_intervals.append([i.start, i.end])
        if len(flat_intervals)==1:
            return 1
        elif len(flat_intervals)==0:
            return 0
        flat_intervals.sort()
        minHeap=[flat_intervals[0][1]]
        heapq.heapify(minHeap)
        for i in range(1,len(flat_intervals)):
            if minHeap:
                if flat_intervals[i][0]>=minHeap[0]:
                    heapq.heappop(minHeap)
                
            heapq.heappush(minHeap,flat_intervals[i][1])
        return len(minHeap)
                    



# # Create a sample list and convert it into a min-heap
# my_heap = [42, 10, 18, 5, 23]
# heapq.heapify(my_heap)

# # 1. Peek at the smallest element (Safe lookahead)
# if my_heap:
#     smallest = my_heap[0]
#     print(f"Peek: {smallest}")  # Output: 5
# else:
#     print("Heap is empty")

# # 2. Confirm the element is still there by popping it
# popped_val = heapq.heappop(my_heap)
# print(f"Popped: {popped_val}")  # Output: 5