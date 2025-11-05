def search_insert(nums, target):
    """
    返回 target 在 nums 中的索引，如果不存在则返回插入位置索引。
    >>> search_insert([1, 3, 5, 6], target=5)    # 基础测试用例
    2
    >>> search_insert([1, 3, 5, 6], target=2)
    1
    >>> search_insert([1, 3, 5, 6], target=7)
    4
    >>> search_insert([], target=1)
    0
    >>> search_insert([2, 4, 6, 7], target=1)    # 自定义测试用例
    0
    >>> search_insert([1, 3, 5, 6], target=2)
    1
    """

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    print("软工2班-2415304206,黄思绮")
