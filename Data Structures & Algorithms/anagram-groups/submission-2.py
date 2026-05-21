class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newDict = defaultdict(list)
        for e in strs:
            sortedE = self.hashing(e)
            newDict[sortedE].append(e)
        
        print(newDict.keys())
        return list(newDict.values())

    def hashing(self,key):
        text = "".join(sorted(key))
        return text