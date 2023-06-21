# README.md
<a href="./README.md">English document</a>

# Nestedaccess

Nestedaccess是一个简单、优雅的获取深层次的字典的嵌套数据。字段不存在可以自定义返回默认值，也可以选择是否输出错误信息。


```python

import nestedaccess

data = {
    'foo': {
        'bar': [1, 2, 3],
        'baz': {
            'qux': 'hello',
            'quux': {
                'corge': True,
                'grault': [4, 5, 6]
            }
        }
    },
    'empty_list': [],
    'empty_dict': {}
}

# 正常数据测试
print(nestedaccess.get(data, ['foo', 'baz', 'quux', 'grault', 1]))  # Output: 5

# 返回默认值数据测试
print(nestedaccess.get(data, ['nonexistent'], default='Not found'))  # Output: 'Not found'

# 字段不存在，不返回错误信息数据测试
print(nestedaccess.get(data, ['foo', 'baz', 'quux', 'corge', 'invalid']))  # Output: None

# 字段不存在返回错误信息测试
test_key = ['foo', 'baz', 'quux', 'corge', 'invalid']
print(nestedaccess.get(data, test_key, error_info=True))  # Output: None (dictionary key does not exist)
print(nestedaccess.get(data, test_key, error_info=True, default='Not found'))  # Output: 'Not found'
```

# 安装 Nestedaccess 和支持的版本

## Nestedaccess is available on PyPI:

```python
$ python -m pip install nestedaccess
```

Nestedaccess officially supports Python 3.7+.

# 支持的功能和最佳实践

-   用于获取嵌套数据，在嵌套结构很深的情况下，通过列表的方式获取数据，使得代码更优雅。
-   采用嵌套数据对象（可以是字典或列表）、键或索引列表以及可选的默认值。
-   它将尝试以给定的键或索引顺序获取嵌套数据，如果获取失败则返回默认值。
-   如果字段不存在则输出不存在的字段名，并返回默认值。
-   选择是否输出错误信息（默认不输出错误信息）。