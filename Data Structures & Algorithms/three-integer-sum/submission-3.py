class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        length = len(nums)
        for i in range(length):
            target = -nums[i]
            j = i+1
            k = length-1
            while j < k:
                if target < nums[j] + nums[k]:
                    k -= 1
                elif target > nums[j] + nums[k]:
                    j += 1
                else:
                    if ([nums[i],nums[j],nums[k]]) not in out:
                        out.append([nums[i],nums[j],nums[k]])
                    j += 1
        return out