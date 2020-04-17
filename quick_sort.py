"""
快速排序的实现
"""


def quick_sort(arr):
    if len(arr) < 2:
        return arr  # 当数组为空或仅有一个元素时不用排序直接返回

    pivot = arr[int(len(arr) / 2)]
    less_arr = []
    more_arr = []

    arr.remove(pivot)
    for i in arr:
        # 大于基准值放进右边的子数组
        if i > pivot:
            more_arr.append(i)
        # 小于基准值放进左边的子数组
        else:
            less_arr.append(i)

    #  左右两边的子数组递归进行快排操作
    return quick_sort(less_arr) + [pivot] + quick_sort(more_arr)


print(quick_sort([16, 9, 27, 55, 37, 22, 6, 24]))
