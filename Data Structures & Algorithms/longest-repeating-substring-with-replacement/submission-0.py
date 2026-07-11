class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        result = 0
        max_freq = 0
        for r in range(len(s)):
            a = s[r]
            if a in count:
                count[a] += 1
            else:
                count[a] = 1
            max_freq = max(count[a],max_freq)
            windowl = r - left + 1
            if  windowl - max_freq > k:
                count[s[left]] -= 1
                left += 1
            result = max(result, r - left + 1)
        return result


