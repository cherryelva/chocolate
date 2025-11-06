def merge(nums1, nums2):
    """
    >>> merge([0,1,2],[4,5,7])  # 基本测试用例
    [0, 1, 2, 4, 5, 7]
    >>> merge([0,2,3],[2,4,6])
    [0, 2, 2, 3, 4, 6]
    >>> merge([1,2,3,4],[])
    [1, 2, 3, 4]
    >>> merge([],[1,3,5])
    [1, 3, 5]
    >>> merge([2,3,6],[1,5,7])
    [1, 2, 4, 5, 6, 7]
    """
    ans = nums1 + nums2
    ans.sort()
    return ans

nums1 = [1, 2, 3, 4, 5]
nums2 = [2, 4, 6, 7, 8]

print(merge(nums1, nums2))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    print("软工2班,2415304206,黄思绮")
