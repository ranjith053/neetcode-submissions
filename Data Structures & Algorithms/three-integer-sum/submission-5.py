class Solution:
    def threeSum(self,nums:List[int])->List[int]:
        array = []
        nums.sort()   # sorting and creating array 
        for i,n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:   # comparing duplicate
                continue   # used to skip duplicate values
            left = i + 1
            right = len(nums) - 1   # creating two pointers left and right
            while left < right:
                sum = nums[i] + nums[left] + nums[right]  # creating temp sum to calculate all
                if sum == 0:
                    array.append([nums[i],nums[left],nums[right]]) # here result comes
                    left += 1 
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif sum > 0:
                    right -= 1
                else:
                    left += 1
        return array