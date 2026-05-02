# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def qSort(self, arr, left, right):
        if left >= right:
            return

        ptr = left

        for i in range(left, right):
            if arr[i].key < arr[right].key:
                arr[i], arr[ptr] = arr[ptr], arr[i]
                ptr += 1

        arr[right], arr[ptr] = arr[ptr], arr[right]
        self.qSort(arr, left, ptr - 1)
        self.qSort(arr, ptr + 1, right)

    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.qSort(pairs, 0, len(pairs) - 1)

        return pairs
