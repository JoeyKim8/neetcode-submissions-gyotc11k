import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    heap = []
    final_heap = []

    for num in nums:
        pair = (-num, num) # start out by making first element in tuple, neg
        heapq.heappush(heap, pair)

    while heap:
        pair = heapq.heappop(heap)
        original_num = pair[1]
        final_heap.append(original_num)
    
    return final_heap



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
