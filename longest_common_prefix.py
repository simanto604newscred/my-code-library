class Solution:
    def longestCommonPrefix1(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        l_c_p = ""
        i=0

        search_continue = True
        while search_continue:
            for j,word in enumerate(strs):
                if strs[0] and i < len(strs[0]) and i < len(word):
                    if strs[0][i] != word[i]:
                        search_continue = False
                        break
                    else:
                        if j == len(strs) -1:
                            l_c_p = l_c_p + strs[0][i]
                else:
                    return l_c_p
            if search_continue:
                i=i+1
            else:
                return l_c_p

    def longestCommonPrefix2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        lengths = [len(s) for s in strs]
        min_length = min(lengths)
        prefix = ""
        for i in range(min_length):
            current_char = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] != current_char:
                    return prefix
            prefix += current_char
        return prefix

    def longestCommonPrefix3(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs = list(zip(*strs))
        res = ''
        for i in strs:
            if i.count(i[0]) == len(i):
                res += i[0]
            else:
                return res
        return res




if __name__ == '__main__':
    Solution().longestCommonPrefix()
