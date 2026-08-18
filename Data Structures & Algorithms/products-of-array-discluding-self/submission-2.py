class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        if nums.count(0) == 1:
            for num in nums:
                if num != 0:
                    product *= num
            return [int(product) if item == 0 else 0 for item in nums]
        elif nums.count(0) > 1:
            return [0 for item in nums]
        for num in nums:
            product *= num
        return [int(product/item) for item in nums]