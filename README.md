# README.md
<a href="./README_zh-CN.md">English documentation for Nestedaccess</a>

# Nestedaccess

Nestedaccess is a simple, elegant way to retrieve nested data from deep dictionaries. If the field does not exist, you can customize the return to the default value, and you can also choose whether to output an error message.

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

# normal data test.
print(nestedaccess.get(data, ['foo', 'baz', 'quux', 'grault', 1]))  # Output: 5

# return default data test.
print(nestedaccess.get(data, ['nonexistent'], default='Not found'))  # Output: 'Not found'

# The field does not exist, no error message data test is returned.
print(nestedaccess.get(data, ['foo', 'baz', 'quux', 'corge', 'invalid']))  # Output: None

# The field does not exist and returns an error message test.
test_key = ['foo', 'baz', 'quux', 'corge', 'invalid']
print(nestedaccess.get(data, test_key, error_info=True))  # Output: None (dictionary key does not exist)
print(nestedaccess.get(data, test_key, error_info=True, default='Not found'))  # Output: 'Not found'
```

# Installing Nestedaccess and Supported Versions

## Nestedaccess is available on PyPI:

```python
$ python -m pip install nestedaccess
```

Nestedaccess officially supports Python 3.7+.

# Supported Features & Best–Practices

-   It is used to obtain nested data. In the case of a deep nested structure, the data is obtained through a list, which makes the code more elegant.
-   Takes a nested data object (which can be a dictionary or a list), a list of keys or indices, and an optional default value.
-   It will attempt to fetch nested data in the given key or index order, and fall back to the default value if fetching fails.
-   If the field does not exist, output the non-existent field name and return the default value.
-   Customize the output error message (no error message is output by default).