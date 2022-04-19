class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        N = len(digits)
        carry = True
        for i in range(N):
            idx = N - i -1
            item = digits[idx]
            if carry == True:
                if item == 9:
                    result.append(0)
                else:
                    result.append(item+1)
                    carry = False
            else:
                result.append(item)
                
                    
                
        if carry:
            result.append(1)
        
        return result[::-1]
            
        