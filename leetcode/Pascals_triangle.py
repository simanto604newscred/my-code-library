__author__ = 'MAK'



class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []

        current_list = [1]

        for i in range(numRows):

            result.append(current_list)

            new_list = []
            new_list.append(current_list[0])

            for j in range(len(current_list)-1):
                new_list.append(current_list[j]+current_list[j+1])

            new_list.append(current_list[-1])
            current_list = new_list
        print(result)
        return result

if __name__ == '__main__':
    Solution().generate(5)
