'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    first = 1
    second = 1
    third = 2
    if n is 0:
        return first
    elif n is 1:
        return second
    elif n is 2:
        return third
    else:
        for x in range(3, n+1):
            next_num = first + second + third
            first = second
            second = third
            third = next_num
        return third

        # recursive solution. not great at all for large numbers
        # return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
    
