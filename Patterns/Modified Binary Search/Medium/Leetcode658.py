def findClosestElements(arr, k, x):
    '''
    So the main idea of it is to find out the lower bound of that k length range. The numbers between "left" and "right" are the candidates of the lower bound.

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
    # we have found our answer
    while l < r:
        # Finding the left endpoint (start) of our window
        m = (l + r) // 2

        # Check if the distance from our target to the start of
        # our window is farther away from than from the element just
        # right outside of our window (to the right). If it is, then we
        # know that we can find a window that includes elements closer to
        # the target starting from m + 1
        if x - arr[m] > arr[m + k] - x:
            l = m + 1

        # This means that the distance to our target starting from 'mid' is closer
        # than the element just outside of our window. This means that our target lies
        # closer to the element at mid then the element at 'mid + k'.

        # This also takes care of the edge case where we have two elements that have the
        # same distance to target. This condition makes sure that the element that is smaller
        # is counted as closer to the target.
        else:
            r = m

    return arr[l: l + k]

arr = [1,2,3,4,5]
k = 4
x = -1
print(findClosestElements(arr,k,x))