class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxSum = 0
        currSum = 0
        for n in nums:
            if n == 0:
                maxSum = max(maxSum, currSum)
                currSum = 0
            else:
                currSum += n
        
        return max(maxSum, currSum)