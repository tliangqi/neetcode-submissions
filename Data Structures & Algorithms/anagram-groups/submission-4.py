class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list) #Create Hash map, mapping charCount to List of Anagrams

        for s in strs: #iterate steing in the input list
            count = [0] * 26 #initialize count array for a...z

            for c in s: #count each character in string
                #Map alphabet to index
                count[ord(c) - ord("a")] += 1

            result[tuple(count)].append(s) #convert list to tuple
        
        return list(result.values()) #return all grouped anagram list