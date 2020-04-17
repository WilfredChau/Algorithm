"""
选择排序的实现
"""


# 用于找出数组中最小元素的函数
def find_smallest(arr):
    smallest = arr[0]  # 存储最小值
    smallest_index = 0  # 存储最小值的索引
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


# 使用上面的函数实现选择排序算法
def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        # 找出数组中最小的元素，并将其加入到新数组中
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))

    return new_arr


print(selection_sort([5, 3, 6, 2, 10]))
