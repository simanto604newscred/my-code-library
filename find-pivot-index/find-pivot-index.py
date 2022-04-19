'''
724. Find Pivot Index
https://leetcode.com/problems/find-pivot-index/
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

'''

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        length = len(nums)

            
        for idx, item in enumerate(nums):
            right_sum = total_sum - left_sum - item
            if left_sum == right_sum:
                return idx
            left_sum += item 
            
        return -1