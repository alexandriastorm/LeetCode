class Solution:
    def merge(self, nums1, m, nums2, n):
        temp = nums1.reverse()
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        total = n + m
        if nums1 == None or nums2 == None or len(nums1) == 0 or len(nums2) == 0:
            return
        while m >= 1 and n >= 1:
            if nums1[m - 1] > nums1[n - 1]:
                nums1[total + 1] = nums1[m - 1]
                m-=1
            else:
                nums1[total - 1] = nums2[n - 1]
                n -= 1
        while n >- 1:
            nums1[n - 1] = nums2[n - 1]
            n -= 1
