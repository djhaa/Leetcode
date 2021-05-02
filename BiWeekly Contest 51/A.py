class Solution:
    def get(self, c, length):
        return chr(ord(c) + length)

    def replaceDigits(self, s: str) -> str:
        nums = list(s)
        for i in range(len(s)):
            if i&1:
                nums[i] = self.get(nums[i-1], int(nums[i]))
        return "".join(nums)