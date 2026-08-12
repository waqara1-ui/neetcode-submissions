class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #smart trick: the key is the count and 
        #the values will be the nums that occur that many count times
        count = {} #hashmap
        freq = [[] for i in range(len(nums)+1)] #sets to the size of num array

        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res





        