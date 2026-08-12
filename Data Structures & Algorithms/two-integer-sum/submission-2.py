class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #dictionary
        dict1 = {}
        end_list = []
        for i in range(len(nums)):
            elem = target - nums[i]
            
            if (elem in dict1):
                return [dict1[elem], i]

            #if not found
            dict1[nums[i]] = i
        
    
            
                