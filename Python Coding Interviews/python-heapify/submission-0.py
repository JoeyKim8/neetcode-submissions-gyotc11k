import heapq
from typing import List


def heapify_strings(strings: List[str]) -> List[str]:
    heapq.heapify(strings) # rearrange the elements to a valid heap first

    return strings


def heapify_integers(integers: List[int]) -> List[int]:
    heapq.heapify(integers) # rearrange the ints to a valid heap first

    return integers


def heap_sort(nums: List[int]) -> List[int]:
    heapq.heapify(nums) # rearrange the nums to a valid heap first

    sorted_heap = [] # initialize resulting list first
    
    while nums:
        sorted_heap.append(heapq.heappop(nums))

    return sorted_heap


# do not modify below this line
print(heapify_strings(["b", "a", "e", "c", "d"]))
print(heapify_integers([3, 4, 5, 1, 2, 6]))
print(heap_sort([3, 4, 5, 1, 2, 6]))
