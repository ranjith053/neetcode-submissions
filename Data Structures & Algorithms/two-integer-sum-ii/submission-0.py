class Solution:
    def twoSum(self,numbers:List[int],target:int)->List[int]:
        left = 0 
        right = len(numbers) - 1  # creating two pointers
        while left < right:
            count = numbers[left] + numbers[right] # creating temp variable count to calculate and store
            if count == target:
                return [left+1, right+1]   # comparing
            elif count > target:
                right -=1    # if count is greater remove right subtract
            else:
                left += 1   # if count is small add from left
