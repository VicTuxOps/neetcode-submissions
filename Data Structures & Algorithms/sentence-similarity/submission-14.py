class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        similar = []
        for a, b in similarPairs:
            similar.append([a,b])
            similar.append([b,a])

        for a, b in zip(sentence1, sentence2):
            if a == b:
                continue
            if [a, b] not in similar:
                return False

        return True
