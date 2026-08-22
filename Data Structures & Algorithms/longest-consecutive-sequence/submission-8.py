class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0
        max_len = 0
        nums = set(nums)
        for num in nums:
            if num-1 not in nums:
                length += 1
                while num+1 in nums:
                    length += 1
                    num += 1
                max_len = max(max_len,length)
                length = 0
        return max_len