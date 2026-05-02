# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickS(self, arr, left, pivot):
        if left >= pivot:
            return

        ptr = left
        for i in range(left, pivot):
            if arr[i].key < arr[pivot].key:
                arr[ptr], arr[i] = arr[i], arr[ptr]
                ptr += 1

        arr[ptr], arr[pivot] = arr[pivot], arr[ptr]

        self.quickS(arr, left, ptr - 1)
        self.quickS(arr, ptr + 1, pivot)


    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickS(pairs, 0, len(pairs) - 1)

        return pairs