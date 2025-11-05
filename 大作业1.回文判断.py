"""
# 基础测试用例
>>> is_palindrome("abcba")
'Yes'
>>> is_palindrome("Abcba")
'Yes'
>>> is_palindrome("1233221")
'No'
>>> is_palindrome("a")
'Yes'
>>> is_palindrome("Ia,aI")
'Yes'
>>> is_palindrome("Noon")
'Yes'
>>> is_palindrome("Python")
'No'
"""

# 自定义测试用例
"""
>>> is_palindrome("Noon")
'Yes'
>>> is_palindrome("python")
'No'
"""

import re


def is_palindrome(s: str) -> str:
    """判断字符串是否为回文串（忽略大小写与符号）"""
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return "Yes" if s == s[::-1] else "No"


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    print("软工2班-2415304206,黄思绮")
