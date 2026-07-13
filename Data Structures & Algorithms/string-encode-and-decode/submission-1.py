class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s  # append length
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            # locate delimiter '#' for the current segment
            while s[j] != "#":
                j += 1
            # parse length value from i to j
            length = int(s[i:j])
            # extract actual string using parsed length
            res.append(s[j + 1 : j + 1 + length])
            # move pointer to the start of next segment
            i = j + 1 + length
        return res
