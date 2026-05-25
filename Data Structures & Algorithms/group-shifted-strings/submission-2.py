class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        sizeStr = {}
        for word in strings:
            idx = self.hashFunction(word)
            sizeStr.setdefault(idx, []).append(word)
        
        return list(sizeStr.values())

    def hashFunction(self, word):
        res = ()
        if len(word) >= 1:
            for i in range(1,len(word)):
                temp = (ord(word[i]) - ord(word[i-1]))%26
                res = res + (temp,)
        res = res + (len(word),)
        return res
