class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # initializing Class variables minHeap and k to access across the class
        self.minHeap, self.k = [0] + nums.copy(), k

        # converting the initial array to a minHeap - O(n)
        self.heapify()

        # Creating a minHeap of size k, to get the kth larget element
        while len(self.minHeap) > self.k + 1:
            self.heapPop()

        # print(self.minHeap)

    def add(self, val: int) -> int:

        # adding the element at the end in minHeap
        self.minHeap.append(val)

        i = len(self.minHeap) - 1

        # precolating up until the inserted value is at correct position
        while i // 2 > 0 and self.minHeap[i] < self.minHeap[i // 2]:
            self.minHeap[i], self.minHeap[i // 2] = self.minHeap[i // 2], self.minHeap[i]
            i = i // 2

        if len(self.minHeap) > self.k + 1:
            self.heapPop()

        return self.minHeap[1]

    def heapify(self):

        # starting from the first parent node to start precolating down
        curr = (len(self.minHeap) - 1) // 2

        # precolating down each node until we reach the first node
        while curr > 0:
            self.precolateDown(curr)
            curr -= 1

    def heapPop(self):

        # repacing the top element with last element
        self.minHeap[1] = self.minHeap.pop()

        # precolating down first element after replacing
        self.precolateDown(1)

    def precolateDown(self, ind):
        i = ind

        # Running the loop until there is atleast a left child for the current node while precolating down
        while 2 * i < len(self.minHeap):

            # checking if there is a right child and if exists, checking if we can swap the current node with the right child.
            if (2 * i) + 1 < len(self.minHeap) and self.minHeap[(2 * i) + 1] < self.minHeap[(2 * i)] and self.minHeap[(2 * i) + 1] < self.minHeap[i]:
                self.minHeap[(2 * i) + 1], self.minHeap[i] = self.minHeap[i], self.minHeap[(2 * i) + 1]
                i = (2 * i) + 1

            # checking if we can swap the current node with the left child
            elif self.minHeap[i] > self.minHeap[(2 * i)]:
                self.minHeap[i], self.minHeap[(2 * i)] = self.minHeap[(2 * i)], self.minHeap[i]
                i = 2 * i

            # no need to swap, as current node is at a valid position. Hence breaking out of loop
            else:
                break



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)