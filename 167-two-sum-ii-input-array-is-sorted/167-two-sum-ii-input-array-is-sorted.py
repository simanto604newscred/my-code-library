class Solution:
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0 
        high = len(numbers) -1
        
        while low < high:
            cur_sum = numbers[low] + numbers[high]
            
            if cur_sum == target:
                return (low+1, high+1)
            elif cur_sum < target:
                low+=1
            else:
                high-=1
                
        return (-1, -1)
            
        
                