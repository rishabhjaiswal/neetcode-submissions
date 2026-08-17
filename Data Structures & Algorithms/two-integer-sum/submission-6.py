class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, item in enumerate(nums):
            hashmap[item] = index
        for index, item in enumerate(nums):
            if (target - item) in hashmap and hashmap[target - item] != index:
                return sorted([index, hashmap[target - item]])