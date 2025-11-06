"""
基础测试用例
>>> remove_duplicates("12,13,10")
'12,13,10'
>>> remove_duplicates("1,2,4,1,3,5")
'1,2,4,3,5'
>>> remove_duplicates("1,2,3,2,3,5")
'1,2,3,5'

拓展测试用例
>>> remove_duplicates("7,7,7,8,9")
'7,8,9'
>>> remove_duplicates("10,20,10,30,20,40")
'10,20,30,40'
"""


def remove_duplicates(seq_str: str) -> str:
    items = seq_str.split(",")  # 分割字符串为列表
    result = []    # 初始化一个空列表
    seen = set()
    for item in items:
        if item not in seen:
            result.append(item)   # 把未出现过的元素 item 添加到 result 列表中
            seen.add(item)
    return ",".join(result)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    print("软工2班,2415304206,黄思绮")
