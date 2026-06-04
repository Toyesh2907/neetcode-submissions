from typing import List

class Solution:

    def odd_median(
        self,
        len1: int,
        len2: int,
        nums1: list[int],
        nums2: list[int],
        total_len: int
    ) -> float:

        if len1 == 0:
            return nums2[len2 // 2]

        if len2 == 0:
            return nums1[len1 // 2]

        counter = 0
        i, j = 0, 0

        while i < len1 or j < len2:

            if i == len1:
                val = nums2[j]
                j += 1

            elif j == len2:
                val = nums1[i]
                i += 1

            elif nums1[i] < nums2[j]:
                val = nums1[i]
                i += 1

            else:
                val = nums2[j]
                j += 1

            if counter == total_len // 2:
                return val

            counter += 1


    def even_median(
        self,
        len1: int,
        len2: int,
        nums1: list[int],
        nums2: list[int],
        total_len: int
    ) -> float:

        if len1 == 0:
            return (
                nums2[(len2 // 2) - 1] +
                nums2[len2 // 2]
            ) / 2

        if len2 == 0:
            return (
                nums1[(len1 // 2) - 1] +
                nums1[len1 // 2]
            ) / 2

        counter = 0
        median1 = None
        median2 = None
        i, j = 0, 0

        while i < len1 or j < len2:

            if i == len1:
                val = nums2[j]
                j += 1

            elif j == len2:
                val = nums1[i]
                i += 1

            elif nums1[i] < nums2[j]:
                val = nums1[i]
                i += 1

            else:
                val = nums2[j]
                j += 1

            if counter == (total_len // 2) - 1:
                median1 = val

            if counter == total_len // 2:
                median2 = val
                return (median1 + median2) / 2

            counter += 1


    def findMedianSortedArrays(
        self,
        nums1: List[int],
        nums2: List[int]
    ) -> float:

        len1 = len(nums1)
        len2 = len(nums2)
        total_len = len1 + len2

        if total_len % 2 == 0:
            return self.even_median(
                len1=len1,
                len2=len2,
                nums1=nums1,
                nums2=nums2,
                total_len=total_len
            )

        return self.odd_median(
            len1=len1,
            len2=len2,
            nums1=nums1,
            nums2=nums2,
            total_len=total_len
        )