class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
      map1 = {}
      map2 = {}
      left = 0
      for char in s1:
        if char in map1:
          map1[char] += 1
        else:
          map1[char] = 1
      for right in range(len(s2)):
        char = s2[right]
        if char in map2:
          map2[char] += 1
        else:
          map2[char] = 1
        if right - left + 1 > len(s1):
          left_char = s2[left]
          map2[left_char] -= 1
          if map2[left_char] == 0:
            del map2[left_char]
          left += 1
        if map1 == map2:
          return True
      return False
          