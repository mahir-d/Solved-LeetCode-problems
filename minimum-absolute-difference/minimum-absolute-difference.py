class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        my_dict: Dict[int, List[List[int]]] = {}
        
        arr.sort()
        min_dif: int =  float('inf')
            
        for i in range(0, len(arr) - 1):
            
            abs_dif: int = abs(arr[i+1] - arr[i])
            if abs_dif in my_dict:
                curr_list: List[List[int]] = my_dict[abs_dif]
                curr_list.append([arr[i], arr[i+1]])
                my_dict[abs_dif] = curr_list
            else:
                new_list: List[List[int]] = []
                new_list.append([arr[i], arr[i+1]])
                my_dict[abs_dif] = new_list
                min_dif = min(abs_dif, min_dif)
                
                
        
        return my_dict[min_dif] 
