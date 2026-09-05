class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # s = set()
        # for i in nums:
        #     if i in s:
        #         return True
        #     else:
        #         s.add(i)
        # return False

        if len(nums) != len(set(nums)):
            return True 
        return False