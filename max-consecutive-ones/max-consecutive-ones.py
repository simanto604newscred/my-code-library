class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_con = 0
        curr_max = 0
        for idx, item in enumerate(nums):
            if item == 1:
                curr_max = curr_max + 1
            else:
                curr_max = 0
            max_con = max(max_con, curr_max)
            
        return max_con
            
                