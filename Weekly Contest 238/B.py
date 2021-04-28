class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans, sums, left = 0, 0, 0
        for i in range(len(nums)):
            sums += nums[i]
            while left < i and (nums[i] * (i - left + 1) - sums > k):
                sums -= nums[left]
                left += 1
            ans = max(ans, i - left + 1)
        return ans