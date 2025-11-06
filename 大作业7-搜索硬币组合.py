def coin_change_combinations(coins, amount):
    """
    基础测试用例
    >>> coin_change_combinations([2,3,6,7],7)
    [[2, 2, 3], [7]]
    >>> coin_change_combinations([2,3,5], 8)
    [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    >>> coin_change_combinations([3,7], 11)
    -1

    拓展测试用例
    >>> coin_change_combinations([1,2,5],5)
    [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 2], [5]]
    >>> coin_change_combinations([2,5,10],10)
    [[2, 2, 2, 2, 2], [5, 5], [10]]
    """
    ans = [[] for _ in range(amount + 1)]
    ans[0] = [[]]
    for coin in coins:
        for i in range(coin, amount + 1):
            for comb in ans[i - coin]:
                ans[i].append(comb + [coin])
    if not ans[amount]:
        return -1
    return ans[amount]


coins1 = [1, 2, 5]
amount1 = 5
print(coin_change_combinations(coins1, amount1))
coins2 = [1, 5, 10]
amount2 = 15
print(coin_change_combinations(coins2, amount2))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    print("软工2班,2415304206,黄思绮")
