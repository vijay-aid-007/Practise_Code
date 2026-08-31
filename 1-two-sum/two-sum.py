class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,v in enumerate(nums):
            if target - v in seen:
                inx = seen[target-v], i
                return inx
            seen[v] = i
                