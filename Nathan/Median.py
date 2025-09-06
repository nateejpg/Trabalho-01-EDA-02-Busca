class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        half_len = (m + n + 1) // 2

        while low <= high:
            partition1 = (low + high) // 2
            partition2 = half_len - partition1

            maxLeft1 = nums1[partition1 - 1] if partition1 != 0 else float('-inf')
            minRight1 = nums1[partition1] if partition1 != m else float('inf')

            maxLeft2 = nums2[partition2 - 1] if partition2 != 0 else float('-inf')
            minRight2 = nums2[partition2] if partition2 != n else float('inf')

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (m + n) % 2 == 1:
                    return float(max(maxLeft1, maxLeft2))
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            elif maxLeft1 > minRight2:
                high = partition1 - 1
            else:
                low = partition1 + 1