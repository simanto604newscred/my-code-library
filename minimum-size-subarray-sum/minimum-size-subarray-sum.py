class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        end = len(nums)
        cur_sum = 0
        start = 0
        
        for i in range(end):
            cur_sum += nums[i]
            while cur_sum >= target:
                ans = min(ans, i+1 - start)
                cur_sum -= nums[start]
                start+=1
        
        
        return ans if ans != float('inf') else 0
        