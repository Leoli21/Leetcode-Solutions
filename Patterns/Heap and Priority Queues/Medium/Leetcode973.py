import heapq


def kClosest(points, k):
    distances = []
    for x, y in points:
        dist = -(x * x + y * y)
        if len(distances) == k:
            heapq.heappushpop(distances, (dist, x, y))
        else:
            heapq.heappush(distances, (dist, x, y))

    res = []

    for (x, y, dist) in distances:
        res.append([x, y])
    return res

points = [[1,3],[-2,2]]
k = 1
print(kClosest(points,k))