class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dicS1, dicS2 = {}, {}
        for i in nums1:
            dicS1[i] = dicS1.get(i, 0) + 1
        for i in nums2:
            dicS2[i] = dicS2.get(i, 0) + 1
        interSection = set(nums1).intersection(set(nums2))
        ans = []
        for i in interSection:
            ans += [i] * min(dicS1[i], dicS2[i])
        return ans
