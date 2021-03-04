class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergelen = len(nums1) + len(nums2)
        # respectively represent the position of two arrays
        i = 0
        j = 0
        # represent the count number of considered elements
        k = 0
        median = 0
        
        while k < int(mergelen/2 - 0.5):
            if i >= len(nums1) or (j < len(nums2) and nums2[j] < nums1[i]):
                j += 1
            else:
                i += 1
            k += 1
        
        if j >= len(nums2) or (i < len(nums1) and nums1[i] < nums2[j]):
            median += nums1[i]
            i += 1
        else:
            median += nums2[j]
            j += 1
        
        if mergelen % 2 == 0:
            if j >= len(nums2) or (i < len(nums1) and nums1[i] < nums2[j]):
                median += nums1[i]
            else:
                median += nums2[j]
            median = float(median) / 2
            
        return median
