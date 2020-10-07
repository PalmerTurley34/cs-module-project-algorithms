'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    single = set()
    double = set()
    for x in arr:
        if x not in single:
            single.add(x)
        else:
            double.add(x)
    res = single.difference(double)
    return list(res)[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")