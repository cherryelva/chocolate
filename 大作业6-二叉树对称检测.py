def symmetric(tree):
    """
    基础测试用例
    >>> symmetric((1,None,None))
    True
    >>> symmetric((1, (3, (2, None, None), None), (3, (2, None, None), None)))
    False
    >>> symmetric((1, (2, (3, None, None), (4, None, None)), (2, (4, None, None), (3, None, None))))
    True

    拓展测试用例
    >>> symmetric((1, (2, (3, None, None), None), (2, None, (3, None, None))))
    True
    >>> symmetric(None)
    True
    """
    def mirror(t1, t2):   # 判断两棵树是否为镜像
        if not t1 and not t2:
            return True   # 如果两棵树都为空，则返回True
        if not t1 or not t2:
            return False  # 一棵空一棵不空，则返回False
        return t1[0] == t2[0] and mirror(t1[1], t2[2]) and mirror(t1[2], t2[1])
    if tree is None:
        return True
    return mirror(tree[1], tree[2])


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

    tree1 = (1, (2, (3, None, None), (4, None, None)), (2, (4, None, None), (3, None, None)))
    print(f"{symmetric(tree1)}")

    tree2 = (1, (3, (2, None, None), (5, None, None)), (3, (2, None, None), (4, None, None)))
    print(f"{symmetric(tree2)}")
    print("软工2班,2415304206,黄思绮")
