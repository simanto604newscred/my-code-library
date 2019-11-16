from heapq import heapify, heappop, heappush

def sort_k_messed_array1(arr, k):
  '''
  Using insertion sort leading to O(n*k)
  '''
  for i in range(1, len(arr)):
    j=i-1
    key = arr[i]
    while j>=0 and key < arr[j]:
      arr[j+1] = arr[j]
      j-=1
    arr[j+1] = key
  return arr


def sort_k_messed_array(arr, k):
  '''
  Using fixed k+1 size heap leading to O(n * log(k))
  maintaining heap property for i item requires log(k) time and we have do this for n items 
  '''
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
