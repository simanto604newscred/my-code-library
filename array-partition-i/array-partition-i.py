class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        # print(nums)
        
        j = len(nums) - 1
        
        res = 0
        for i in range(0,j,2):
            print(i)
            res = res + nums[i]
            
        return res
            
            