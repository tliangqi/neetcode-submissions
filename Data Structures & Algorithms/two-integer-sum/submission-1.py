class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap={} #create empty Hash map, value:index

        for i, n in enumerate(nums): #Tuple Unpacking
            diff=target - n
            if diff in prevMap:
                return[prevMap[diff], i]
            #If complement not found, store current number
            prevMap[n]=i
        return