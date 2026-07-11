class Solution:
    def groupAnagrams(self,strs:List[str])->List[str]:
        map = {}
        for w in strs:
            key = "".join(sorted(w))
            if key in map:
                map[key].append(w)
            else:
                map[key] = [w]
        return list(map.values())