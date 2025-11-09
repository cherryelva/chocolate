def word_break(s, word_dict):
    """
    >>> word_break("applepenapple", ["apple", "pen"]) # 基础测试用例
    True
    >>> word_break("catsandog", ["cats", "dog", "sand", "and", "cat"])
    False
    >>> word_break("pineapplepenapple", ["pine", "apple", "pen", "apple"]) # 拓展测试用例
    True
    >>> word_break("catsanddogs", ["cats", "dogs", "and", "cat", "dog", "s"])
    True
    """
    word_set = set(word_dict)
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[len(s)]


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

    s1 = "pineapplepenapple"
    wordDict1 = ["apple", "pen", "applepen", "pine", "pineapple"]
    print(f"{word_break(s1, wordDict1)}")

    s2 = "catsanddogs"
    wordDict2 = ["cats", "dogs", "and", "cat", "dog"]
    print(f"{word_break(s2, wordDict2)}")
    print("软工2班,2415304206,黄思绮")
