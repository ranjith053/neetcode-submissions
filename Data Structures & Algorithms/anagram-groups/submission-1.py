class Solution:
    def groupAnagrams(self,strs:List[int])->List[int]:
        map = {}
        for w in strs:
            result = "".join(sorted(w))
            if result in map:
                map[result].append(w)
            else:
                map[result] = [w]
        return list(map.values())