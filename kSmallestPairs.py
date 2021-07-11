from heapq import heapify, heappush, heappop;
import heapq

def kSmallestPairs(nums1, nums2, k):
    #print(nums1,nums2,k)
    h = []
    for n1 in nums1 :
        for n2 in nums2:
            if len(h) < k:
                heappush(h, (n1+n2, [n1, n2]))
                continue
            largest = max(h)
            if largest[0] > n1+n2:
                h.remove(largest)
                heappush(h, (n1+n2, [n1, n2]))
                continue
            break
            
        
    
    return [heappop(h)[0] for i in range(len(h))] 


print(kSmallestPairs([1,7,11],[2,4,6],3))

print(kSmallestPairs(nums1 = [1,1,2], nums2 = [1,2,3], k = 2))

print(kSmallestPairs(nums1 = [1,2], nums2 = [3], k = 3))

print(kSmallestPairs([1,2,4,5,6],[3,5,7,9],3))
print(kSmallestPairs([0,0,0,0,0],[-3,22,35,56,76],22))