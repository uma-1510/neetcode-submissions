class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for index, val in enumerate(nums):
            hashmap[val] = index

        for index, val in enumerate(nums):
            diff = target - val
            if diff in hashmap and hashmap[diff] != index:
                return [index, hashmap[diff]]

        return []

            