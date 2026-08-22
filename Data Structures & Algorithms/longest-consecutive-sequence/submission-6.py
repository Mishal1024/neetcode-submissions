class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        length = 1
        max_len = 1
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                length += 1
                max_len = max(max_len,length)
            elif nums[i] - nums[i-1] == 0:
                pass
            else:
                length = 1
        return max_len