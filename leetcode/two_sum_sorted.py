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

                return look_for[value], current_index

            except KeyError:

                look_for.setdefault(target-value, current_index)

    def twoSum_1(self, numbers, target):
        length = len(numbers)
        i = 0
        j = length -1
        while i < j:
            summary = numbers[i] + numbers[j]
            if summary == target:
                return [i + 1, j + 1]
            if summary < target:
                i += 1
            else:
                j -= 1
        return []

if __name__ == '__main__':

     asd = Solution().twoSum([2,7,11,15],9)

     print(asd)