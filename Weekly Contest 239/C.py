class Solution:
    def nextPermutation(self, nums):
        i = len(nums) - 2
        # 找到第一个非降序的数
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        j = len(nums) - 1
        # 找到比nums[i]大的第一个数
        while j >= 0 and nums[i] >= nums[j]:
            j -= 1
        # 交换两数位置
        nums[i], nums[j] = nums[j], nums[i]
            
        # 将nums[i]后面的数反转
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        # 返回下一个序列
        return nums
    
    def getMinSwaps(self, num: str, k: int) -> int:
        num = list(num)
        nums = list(num)
        for i in range(k):
            nums = self.nextPermutation(nums)
        # 模拟
        l = 0
        while l < len(num) and num[l] == nums[l]:
            l += 1
        ans = 0
        for i in range(l, len(num)):
            if num[i] == nums[i]:
                continue
            j = i + 1
            while j < len(num) and num[j] != nums[i]:
                j += 1
            while j > i:
                num[j], num[j-1] = num[j-1], num[j]
                j -= 1
                ans += 1
        return ans
                    
                