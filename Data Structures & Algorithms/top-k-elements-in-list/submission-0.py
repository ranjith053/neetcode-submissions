class Solution:
    def topKFrequent(self,nums:List[int],k:int)->List[int]:
        map = {}
        for n in nums:
            if n in map:
                map[n] += 1
            else:
                map[n] = 1
        return sorted(map,key = lambda x:map[x],reverse = True)[:k]

