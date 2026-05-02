class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}

        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                return True

        return False