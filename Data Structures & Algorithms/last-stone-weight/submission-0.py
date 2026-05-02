class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # Heandling edge cases
        if len(stones) == 1:
            return stones[0]
        if len(stones) == 2:
            return abs(stones[0] - stones[1])

        stones.append(stones[0])
        stones[0] = 0

        # Converting the input array to max heap
        self.heapify(stones)

        # Looping the heap until there are atleast 2 elements in the heap
        while len(stones) > 2:
            a, b = 0, 0

            # Getting first max element
            a = self.heapPop(stones)

            # Checking if we can get the second max element and retriving it
            if len(stones) > 2:
                b = self.heapPop(stones)
            # If only one element left in heap then get the remaining element
            else:
                b = stones.pop()

            # Pushing the result weight back to the heap if the difference is not 0
            if abs(a - b) != 0:
                self.heapPush(stones, abs(a - b))

        # returning the remaining element in the heap as result
        return stones[-1]

    def heapPush(self, arr, val):
        arr.append(val)
        i = len(arr) - 1

        while i // 2 > 0 and arr[i] > arr[i // 2]:
            arr[i], arr[i // 2] = arr[i // 2], arr[i]
            i = i // 2

    def heapify(self, arr):
        curr = (len(arr) - 1) // 2
        while curr > 0:
            self.precolateDown(curr, arr)
            curr -= 1

    def heapPop(self, arr):
        currMax = arr[1]
        arr[1] = arr.pop()
        self.precolateDown(1, arr)
        return currMax

    def precolateDown(self, ind, arr):
        i = ind

        while 2 * i < len(arr):
            if (2 * i) + 1 < len(arr) and arr[(2 * i) + 1] > arr[2 * i] and arr[(2 * i) + 1] > arr[i]:
                arr[(2 * i) + 1], arr[i] = arr[i], arr[(2 * i) + 1]
                i = (2 * i) + 1
            elif arr[2 * i] > arr[i]:
                arr[2 * i], arr[i] = arr[i], arr[2 * i]
                i = 2 * i
            else:
                break