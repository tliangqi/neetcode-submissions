class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {} #Create empty dictionary

        for i in range(len(s)): #Loop every index
            #Count characters, add 1 update frequency
            countS[s[i]]=1 + countS.get(s[i], 0)
            countT[t[i]]=1 + countT.get(t[i], 0)
        for c in countS: #Iterate character
            if countS[c] != countT.get(c,0):
                return False

        return True