class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == k:
            return points
        points.append(points[0])
        points[0] = [0, 0]

        self.heapify(points)
        ret = []
        while len(ret) < k:
            ret.append(self.heapPop(points))

        return ret

    def heapify(self, points):
        curr = (len(points) - 1) // 2

        while curr > 0:
            self.precolateDown(curr, points)
            curr -= 1

    def heapPop(self, points):
        ret = points[1]
        points[1] = points.pop()
        self.precolateDown(1, points)
        return ret

    def precolateDown(self, ind, points):
        i = ind

        while 2 * i < len(points):
            if (2 * i) + 1 < len(points) and self.dist(points[(2 * i) + 1]) < self.dist(points[i]) and self.dist(points[(2 * i) + 1]) < self.dist(points[2 * i]):
                points[(2 * i) + 1], points[i] = points[i], points[(2 * i) + 1]
                i = (2 * i) + 1
            elif self.dist(points[2 * i]) < self.dist(points[i]):
                points[2 * i], points[i] = points[i], points[2 * i]
                i = 2 * i
            else:
                break

    def dist(self, point):
        return ((point[0] ** 2) + (point[1] ** 2)) ** 0.5