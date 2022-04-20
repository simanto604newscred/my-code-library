class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle or len(needle) > len(haystack):
            return -1
        
        needle_len = len(needle)
        haystack_len = len(haystack)
        
        steps = haystack_len - needle_len +1
        
        for i in range(steps):
            if haystack[i:i+needle_len] == needle:
                return i
        return -1