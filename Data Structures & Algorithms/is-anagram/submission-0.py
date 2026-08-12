class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_len = len(s)
        t_len = len(t)
        
        if s_len != t_len:
            return False

        dictionary1 = {}
        dictionary2 = {}

        for i in range(s_len):
            dictionary1[s[i]] = dictionary1.get(s[i], 0) + 1
            dictionary2[t[i]] = dictionary2.get(t[i], 0) + 1

        if dictionary1 == dictionary2:
            return True
        else:
            return False

            
             

        