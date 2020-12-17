class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        for i in range(0, len(nums1)):
            
            curr = nums1[i]
            
            j = 0
            while nums2[j] != curr:
                j += 1
                
            while j < len(nums2) and nums2[j] <= curr:
                j += 1
            
            nums1[i] = nums2[j] if j < len(nums2) else -1
            
            
        return nums1
            
            
            
            
