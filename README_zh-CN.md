# README.md

<a href="./README.md">English documentation for Nestedaccess</a>

# Nestedaccess

Nestedaccess 是一个简单、优雅的获取深层次的字典的嵌套数据。

通过列表、元组的方式依次传入想要获取数据的键，避免使用过长的 if-elif-else 判断语句，让代码更优雅。

此外，字段不存在可以自定义返回默认值，如果没有默认值，则输出错误信息，错误信息可以指定特定[语言](#yuyan)。

```python

import nestedaccess

data = {
    "foo": {
        "bar": [1, 2, 3],
        "baz": {
            "qux": "hello",
            "quux": {
                "corge": True,
                "grault": [4, 5, 6]
            }
        }
    },
    "empty_list": [
        {
            "baz": {
                "qux": "hello",
                "quux": {
                    "grault": [1, 2, 3]
                }
            }
        },
        {
            "baz": {
                "qux": "hello1",
                "quux": {
                    "grault": [4, 5, 6]
                }
            }
        }
    ],
    "empty_dict": {}
}

# 正常数据测试
print(nestedaccess.get(data, ["foo", "baz", "quux", "grault", 1]))  # Output: 5

test_key = ("empty_list", 0, "baz", "qux")
print(get(data, test_key))  # Output: hello

# 字段不存在，返回默认值数据测试
print(nestedaccess.get(data, ["nonexistent"], default="Not found"))  # Output: "Not found"

# 字段不存在返回错误信息测试
test_key = ["foo", "baz", "quux", "corge", "invalid"]
res = nestedaccess.get(data, test_key, lang="zh")  # Output: ValueError: 无法获取嵌套数据，因为类型为bool的对象没有键或索引

test1_key = ("foo", "bae", "quux", "corge")
res1 = nestedaccess.get(data, test1_key, lang="zh") #Output: KeyError: "字段 'bae' 不存在"
```

# 安装 Nestedaccess 和支持的版本

## Nestedaccess is available on PyPI:

```python
$ python -m pip install nestedaccess
```

Nestedaccess 正式支持 Python 3.7+

# 支持的功能和最佳实践

-   用于获取嵌套数据，在嵌套结构很深的情况下，通过列表或元组的方式获取数据，避免使用过长的 if-elif-else 判断语句，让代码更优雅。
-   采用嵌套数据对象（可以是字典或列表）、键或索引列表以及可选的默认值。
-   它将尝试以给定的键或索引顺序获取嵌套数据，如果字段不存在则输出不存在的字段名，如何设置了自定义的默认值则返回默认值。
-   如果字段不存在，返回的详细错误信息可以选择指定语言(默认使用“en”)。

    <span id="yuyan">支持的语言：</span>
    |语言|代码|
    | --- | --- |
    | 英语 | en |
    | 中文 | zh |
