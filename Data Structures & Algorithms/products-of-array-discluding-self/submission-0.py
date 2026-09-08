class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)

        output = [1] * n

        # Product of everything to the left
        prefix = 1

        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        # Product of everything to the right
        suffix = 1

        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output