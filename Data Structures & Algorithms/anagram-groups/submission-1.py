class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newDict = {}
        res = []
        for e in strs:
            sortedE = self.hashing(e)
            if sortedE not in newDict:
                newDict[sortedE] = [e]
            else:
                print("append", e)
                newDict[sortedE].append(e)
        #print(newDict)

        for v in newDict.values():
            res.append(v)
        
        #print(res)
        return res

    def hashing(self,key):
        text = "".join(sorted(key))
        return text