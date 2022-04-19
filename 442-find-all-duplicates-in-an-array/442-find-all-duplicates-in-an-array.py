class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hash_set = set()
        result = []
        for idx, item in enumerate(nums):
            if item in hash_set:
                result.append(item)
            else:
                hash_set.add(item)
        return result
                
        
        