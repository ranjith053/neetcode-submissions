class Solution:
  def hasDuplicate(self,nums):
    store = set() # creating a set named store
    for num in nums:
      if num in store:
        return True
      store.add(num)
    return False