class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = []
        m = len(mat)
        n = len(mat[0])
        
        row = col = 0
        direction_up = True
        while row < m and col < n:
            
            # going up
            if direction_up:
                while row > 0 and col < n-1:
                    result.append(mat[row][col])
                    col+=1
                    row-=1
                
                result.append(mat[row][col])
                
                if col == n-1:
                    row+=1
                else:
                    col+=1
                    
            # going down
            else:
                while col > 0 and row < m-1:
                    result.append(mat[row][col])
                    col-=1
                    row+=1
                result.append(mat[row][col])
                if row == m-1:
                    col+=1
                else:
                    row+=1
            direction_up = (not direction_up)
            
        return result
            
                    
                
                
                
            
            
                
            

                
                