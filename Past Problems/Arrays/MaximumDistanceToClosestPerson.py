def maxDistToClosest(seats):
    prev = None
    maxDist = 0

    for i, val in enumerate(seats):
        # If we encounter an occupied seat
        if val == 1:
            # 1st Case: encountering first non-empty seat
            if prev is None:
                maxDist = i
            # 2nd Case: encounter another non-empty seat (e.g. [...,1,0,0,0,0,1,...]
            else:
                maxDist = max(maxDist, (i-prev)// 2)

            # Update the previously encountered non-empty seat to new previous index, i
            prev = i

    # 3rd Case: last seat is empty (if it's not, then the calculation len(seats) - 1 - prev will result in 0 because
    # len(seats) - 1 is the last index of seats array and prev will also equal to last index of seats if it is occupied
    maxDist = max(maxDist, len(seats) - 1 - prev)
    return maxDist