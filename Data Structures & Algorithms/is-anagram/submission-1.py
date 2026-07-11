class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = {}
        td = {}
        for a in s:
            if a in sd:
                sd[a] = sd[a] + 1
            else:
                sd[a] = 1
        for b in t:
            if b in td:
                td[b] = td[b] + 1
            else:
                td[b] = 1
        if sd == td:
            return True
        else:
            return False

            

            

