def summary_ranges(l: list[int]) -> list[list[int]]:
    """
    >>> summary_ranges([0, 1, 2, 4, 5, 7]) #基本测试用例
    [[0, 2], [4, 5], [7]]
    >>> summary_ranges([0, 2, 3, 4, 6, 8, 9])
    [[0], [2, 4], [6], [8, 9]]
    >>> summary_ranges([1, 2, 3, 4])
    [[1, 4]]
    >>> summary_ranges([])
    []
    >>> summary_ranges([5]) #拓展测试用例
    [[5]]
    >>> summary_ranges([1,3,5,7,8])
    [[1], [3], [5], [7, 8]]
    """

    if not l:
        return []     # 如果输入列表为空，直接返回空列表
    result = []       # 存放区间的列表
    start = end = l[0]   # 当前区间的起点和终点初始化为一个元素
    for num in l[1:]:
        if num == end + 1:
            end = num     # 连续->扩大当前区间
        else:
            result.append([start, end] if start != end else [start])    # 不连续->把之前的区间保存
            start = end = num     # 开始一个新区间
    result.append([start, end] if start != end else [start])   # 循环结束后把最后一个区间加入结果
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    print("软工2班,2415304206,黄思绮")
