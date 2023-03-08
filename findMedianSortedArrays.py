
def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:

    nums1.extend(nums2)
    merged = sorted(nums1)
    length = len(merged)

    if length % 2 == 1:
        return merged[length//2]
    else:
        return (merged[length//2-1] + merged[length//2]) / 2

nums1 = [1,2]
nums2 = [3,4]

print(findMedianSortedArrays(nums1=nums1, nums2=nums2))