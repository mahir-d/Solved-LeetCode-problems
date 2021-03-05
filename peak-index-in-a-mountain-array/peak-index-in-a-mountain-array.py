class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left = 0
        right = n-1

        while left <= right:
            mid = (left+right) // 2
            if mid < right and arr[mid] > arr[mid-1] and arr[mid+1] < arr[mid]:
                return mid
            elif mid == right:
                return mid
            elif mid < right and arr[mid] < arr[mid+1]:
                left = mid+1
            else:
                right = mid-1

        return -1