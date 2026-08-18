class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1]*len(nums)
        post = 1
        for i in range(1,len(nums)):
            out[i] = out[i-1] * nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            post = post * nums[i+1]
            out[i] = out[i] * post
        return out