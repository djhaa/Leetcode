class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = float("INF")
        l, r = start, start
        while l > 0 and nums[l] != target:
            l -= 1
        while r < len(nums)-1 and nums[r] != target:
            r += 1
        if nums[l] == target:
            res = min(res, start - l)
        if nums[r] == target:
            res = min(res, r - start)
        return res