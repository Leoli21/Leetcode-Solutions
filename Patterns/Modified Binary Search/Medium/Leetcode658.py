def findClosestElements(arr, k, x):
    '''
    So the main idea of it is to find out the lower bound of that k length range. The numbers between "left" and "right" are the candidates
    of the lower bound.

    The if condition "x - A[mid] > A[mid + k] - x" is used to compare A[mid] and A[mid+k], see which is closer to x.

    If A[mid] is closer to x, then A[mid+k] can never be in the k length range. So we can confidently remove all
    (A[mid+1], A[mid+2], A[mid+3]...) from the candidates list by set right=mid.


    If A[mid+k] is closer to x, then A[mid] can never be in the k length range. So we can confidently remove all
    (...A[mid-2], A[mid-1], A[mid]) from the candidates list by set left=mid+1.
    

    Once we remain only one candidate, that is left==right, we got our final lower bound.
    '''

    # Valid start for our closest elements would be from
    # 0 (start of array) to len(arr) - k (inclusive) or else
    # we risk getting elements that are out of bounds.
    l, r = 0, len(arr) - k
    # Once l and r reach the same element in the arr, this means
    # we have converged on our final candidate, which will be our answer
    while l < r:
        # Finding the left endpoint (start) of our window
        m = (l + r) // 2

        # Check if the distance from our target to the start of
        # our window is farther away from than from the element just
        # right outside of our window (to the right). If it is, then we
        # know that we can find a window that includes elements closer to
        # the target starting from m + 1
        if x - arr[m] > arr[m + k] - x:
            # If this is True, then 'x' must lie near arr[m + k] and thus a
            # window starting at [m + 1] would always be a better answer then the
            # windows starting from (...arr[m - 2], arr[m - 1], arr[m])
            l = m + 1

        else:
            # This means that the distance to our target starting from 'mid' is closer
            # than the element just outside of our window. This means that our target lies
            # closer to the element at mid then the element at 'mid + k'.

            # 'x' is closer to arr[m] then arr[m + k]
            # Thus, a window starting at arr[m] would always be a better answer then a
            # a window starting from arr[m + 1], arr[m + 2], arr[m + 3]... b/c these
            # would lead to values farther from 'x'

            # This also takes care of the edge case where we have two elements that have the
            # same distance to target. This condition makes sure that the element that is smaller
            # is counted as closer to the target.
            r = m

    return arr[l: l + k]

# O(n) Solution (Not Optimized but good starting)
def findClosestElements(arr, k, x):
    # Intuition: Use 2 pointers to rule out the furthest element in the current
    # array for each iteration.
    # The reason this works is because it will always be 'True' that either the
    # leftmost or rightmost element in the subarray (eliminated some elements from
    # ends) are the furthest from 'x'.
    # When the size of the window [l, r] becomes k, then we have found the solution
    # If n is the total number of elements, we just need to eliminate 'n - k' elements.
    l, r = 0, len(arr) - 1

    # Keep on elminating elements as long as our range [l, r] still contains
    # more than 'k' elements.
    while r - l >= k:
        # If our current leftmost element is the furthest away from 'x', eliminate
        # it from our answer, by increasing our left pointer.
        if x - arr[l] > arr[r] - x:
            l += 1

        # If our rightmost element is the furthest away from 'x', eliminate it from
        # our answer OR if the distances are the same, eliminate element at 'r'.
        # EDGE CASE:
        # If our target, 'x', is smaller than our smallest element in 'arr', eliminate
        # our rightmost element.
        else:
            r -= 1

    # Return our window as an array.
    return arr[l:r + 1]

arr = [1,2,3,4,5]
k = 4
x = -1
print(findClosestElements(arr,k,x))