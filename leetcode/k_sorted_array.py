from heapq import heapify, heappop, heappush


def sort_k_messed_array(arr, k):
  n = len(arr)
  h = arr[:k+1]
  heapify(h)
  for i in range(k+1, n):
    arr[i-(k+1)] = heappop(h)
    heappush(h, arr[i])
    
  i= 0
  while i <= k and h: 
    ax = heappop(h)
    arr[n-k-1 + i] = ax
    i+=1

  
  return arr
print(sort_k_messed_array(
[1,4,5,2,3,7,8,6,10,9], 2)
)
