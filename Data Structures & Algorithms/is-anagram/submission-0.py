class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            collectionS = {}
            collectionT = {}
            for i in s:
                if i not in collectionS:
                    collectionS[i] = 1
                else:
                    collectionS[i] += 1
            for i in t:
                if i not in collectionT:
                    collectionT[i] = 1
                else:
                    collectionT[i] += 1
            if collectionS == collectionT:
                return True
            else:
                return False
        else:
            return False