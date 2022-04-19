class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a_set = set()
        for idx, item in enumerate(nums):
            if item in a_set:
                return True
            a_set.add(item)
            
        return False
                                   