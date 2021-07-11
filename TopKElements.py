#plan
#generate a priority min heap of size k
#stream the numbers into a hashmap O(n)
#if the incremented number is larger than the smallest number then
#pop the heap and add the new value. O(log k) where K is strictly less then N 
#Return the tree as the answer.
from typing import List
from heapq import heapify, heappush, heappop, heapreplace

def topKFrequent(nums: List[int], k: int) -> List[int]:
    heap = []
    heapify(heap)
    map = dict()
    index = []
    for x in nums:
        if(x not in map):
            map[x] = 1
        else:
            map[x] = map[x] + 1

        if( (map[x]-1, x) in heap):
            heap.remove((map[x]-1,x))
            heappush(heap, (map[x],x))
            heapify(heap)
        elif(len(heap) < k):
            heappush(heap, (map[x],x))
        elif(map[x] > heap[0][0]):
            heapreplace(heap, (map[x],x))
        for x in heap:
            print(x)
        print()
    ret = []
    for x in heap:
        ret.append(x[1])
    return ret


print(topKFrequent([5,-3,9,1,7,7,9,10,2,2,10,10,3,-1,3,7,-9,-1,3,3], 3))


