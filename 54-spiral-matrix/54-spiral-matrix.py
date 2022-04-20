class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        changed_directions = 0
        active_direction = 0
        VISITED = 101
        result = []
        row = col = 0
        result.append(matrix[row][col])
        matrix[row][col] = VISITED
        
        while changed_directions < 2:
            while True:
                next_row = row + directions[active_direction][0]
                next_col = col + directions[active_direction][1]
                
                print(f"{next_row}--{next_col}")
                if not(0 <= next_row < rows and 0 <= next_col < cols):
                    break
                    
                if matrix[next_row][next_col] == VISITED:
                    break
                    
                row = next_row
                col = next_col
                
                result.append(matrix[row][col])
                matrix[row][col] = VISITED
                
                changed_directions = 0
                
            active_direction = (active_direction+1) % 4
            changed_directions +=1
            
        return result