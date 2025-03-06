class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        n = len(nums1)
        m = len(nums2)

        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)

        left, right = 0, n
        while left <= right:
            partition1 = (left+right)//2
            partition2 = (n+m+1)//2 - partition1

            max1 = float('-inf') if partition1 == 0 else nums1[partition1-1]
            min1 = float('inf') if partition1 == n else nums1[partition1]

            max2 = float('-inf') if partition2 == 0 else nums2[partition2-1]
            min2 = float('inf') if partition2 == m else nums2[partition2]

            if max1 <= min2 and max2 <= min1:
                if (n+m) % 2 == 0:
                    return (max(max1, max2)+min(min1, min2))/2
                else:
                    return max(max1, max2)
            elif max1 > min2:
                right = partition1-1
            else:
                left = partition1+1
