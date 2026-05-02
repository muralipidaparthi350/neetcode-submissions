class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0, 0, 0]

        for num in nums:
            bucket[num] += 1
        print(bucket)

        i, j = 0, 0

        while i < 3:
            if bucket[i]:
                nums[j] = i
                bucket[i] -= 1
                j += 1
            else:
                i += 1
