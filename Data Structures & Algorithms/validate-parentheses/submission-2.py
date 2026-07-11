class Solution:
  def isValid(self,s:str)->bool:
    array = []
    hashmap = {")":"(","]":"[","}":"{"}
    for c in s:
      if c in hashmap:
        if array and array[-1] == hashmap[c]:
          array.pop()
        else:
          return False
      else:
        array.append(c)
    return True if not array else False
