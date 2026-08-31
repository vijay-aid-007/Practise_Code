class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list = sorted(nums1 + nums2)  
        length = len(merged_list)     
        mid_val = length // 2 
        
        if length % 2 == 0:
            return (merged_list[mid_val-1] + merged_list[mid_val]) / 2
        else:
            return merged_list[mid_val]