__author__ = 'MAK'

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        look_for = dict()
        for current_index, value in enumerate(numbers, 1):

            try:

                return look_for[target-value], current_index

            except KeyError:

                look_for.setdefault(target-value, current_index)

if __name__ == '__main__':

     asd = Solution().twoSum([2,7,11,15],9)

     print(asd)