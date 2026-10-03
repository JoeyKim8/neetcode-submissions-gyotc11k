import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    result_list = [] # initiate the resulting list

    for i in range(len(heap)):
        result_list.append(heapq.heappop(heap)) # first add the smallest priority element to the resulting list
        # heapq.heappop(heap) # and then pop that same element

    return result_list


# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
