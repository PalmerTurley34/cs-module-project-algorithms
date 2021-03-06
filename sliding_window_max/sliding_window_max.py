'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    from collections import deque
    q = deque(nums[:k])
    maxes = [max(q)]
    for i in range(k, len(nums)):
        q.append(nums[i])
        q.popleft()
        maxes.append(max(q))
    return maxes


    # does not do well with large inputs
    # start = 0
    # stop = k
    # maxes = []
    # while stop <= len(nums):
    #     maxes.append(max(nums[start:stop]))
    #     start += 1
    #     stop += 1
    # return maxes


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
