class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}
        for i, n in enumerate(nums):
            if n in dictionary:
                return True
            else:
                dictionary[n] = i
        return False

        