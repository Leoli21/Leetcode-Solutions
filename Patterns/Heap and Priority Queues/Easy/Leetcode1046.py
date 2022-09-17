import heapq


def lastStoneWeight(self, stones):
    stones = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        first = -heapq.heappop(stones)

        # Either have equal weight as first or a weight less than the first
        # because when we pop from heap to get first stone, that is the greatest
        second = -heapq.heappop(stones)

        # Weights are negative, so second will be a smaller negative (thus greater than
        # the value of 'first')
        if first > second:
            # We are pushing second - first because we want to add the negative value of
            # the difference since our heap is maintaining the negative values
            heapq.heappush(stones, -1 * (first - second))

    # Deal with edge case where we end up with no stones remaining
    return abs(stones[0]) if stones else 0