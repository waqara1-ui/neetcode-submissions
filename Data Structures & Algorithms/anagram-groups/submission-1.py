class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict ={}
        for i in range(len(strs)):
            string = "".join(sorted(strs[i]))
            if string in myDict:
                myDict[string].append(strs[i])
            else:
                myDict[string] = [strs[i]]
        return list(myDict.values())


            


        