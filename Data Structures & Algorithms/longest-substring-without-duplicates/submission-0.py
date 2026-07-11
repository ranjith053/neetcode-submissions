class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      left = 0
      b = set()
      result = 0
      for r in range(len(s)):
        c = s[r]
        while c in b:
            b.remove(s[left])
            left += 1
        b.add(c)
        total = r - left + 1
        result = max(total,result)
      return result

