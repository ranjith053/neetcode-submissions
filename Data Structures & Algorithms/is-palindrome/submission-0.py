class Solution:
    def isPalindrome(self,s:str)->bool:
        arr = []
        for n in s:
            if n.isalnum():
                arr.append(n.lower())
        left = 0
        right = len(arr) - 1
        while left < right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1
        return True
