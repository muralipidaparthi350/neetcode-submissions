class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        temp = [(nums[i], i) for i in range(l)]
        temp.sort(key = lambda x: x[0])
        
        i = 0
        j = l - 1

        while i < j:
            if temp[i][0] + temp[j][0] == target:
                return [min(temp[i][1], temp[j][1]), max(temp[i][1], temp[j][1])]
            elif temp[i][0] + temp[j][0] > target:
                j -= 1
            else:
                i += 1

