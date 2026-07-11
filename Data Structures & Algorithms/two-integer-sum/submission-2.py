class Solution:
    def twoSum(self,nums:List[int],target:int)->List[int]:
        map = {}
        for i,n in enumerate(nums):
            result = target - n
            if result in map:
                return[map[result],i]
            map[n] = i