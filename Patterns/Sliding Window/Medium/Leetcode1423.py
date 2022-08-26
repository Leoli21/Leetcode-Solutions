def maxScore(cardPoints, k):
    # The sliding window in this problem represents the cards that you
    # don't end up taking
    # Taking care of first possibility where you only take cards from
    # the left end
    maxScore = currScore = sum(cardPoints[:k])
    windowLength = len(cardPoints) - k
    for i in range(k - 1, -1, -1):
        # Subtracting the point at the start of our window
        currScore -= cardPoints[i]

        # Adding the point that is the element to the right of
        # the window
        currScore += cardPoints[i + windowLength]

        # Compare the current score with our max score and
        # update accordingly
        maxScore = max(maxScore, currScore)

    return maxScore

cardPoints = [4,5,9,16,2,10,26,7,31,5,12,3]
k = 6

print(maxScore(cardPoints, k))