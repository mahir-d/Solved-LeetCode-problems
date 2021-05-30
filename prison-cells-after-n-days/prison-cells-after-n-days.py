class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        
        my_dict = dict()
        
        
        for i in range(n):
            
            tuple_set = tuple(cells)
            
            if tuple_set not in my_dict:
                my_dict[tuple_set] = i
                cells = self.next_state(cells)
            else:
                
                diff = i - my_dict[tuple_set]
                remain = (n - i) % diff
                return self.prisonAfterNDays(cells, remain)
                
        return cells
            
        
        
        
        
        
    
    
    def next_state(self, cells: List[int]) -> List[int]:
        
        next_cell = [0] * len(cells)
        
        for i in range(1, len(cells)-1):
            
            if cells[i-1] == cells[i+1]:
                next_cell[i] = 1
            else:
                next_cell[i] = 0
                
        next_cell[-1] = 0
        
        return next_cell
        