"""
二分查找的实现
"""


def binary_search(list_search, item):
    low = 0
    high = len(list_search) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = list_search[mid]

        if guess < item:
            print('too low!')
            low = mid + 1
        elif guess > item:
            print('too high!')
            high = mid - 1
        else:
            return 'got it! The position of the number is list[' + str(mid) + '].'

    return None


list1 = [1, 3, 5, 18, 27, 28, 33, 57, 68, 79, 90]
item1 = 28

print(binary_search(list1, item1))




