# Nestedaccess

Nestedaccess is a simple, elegant way to retrieve nested data from deep dictionaries or lists.

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

# normal test
print(get_nested_data(data, ['foo', 'baz', 'quux', 'grault', 1]))  # Output: 5

# default test
print(get_nested_data(data, ['nonexistent'], default='Not found'))  # Output: 'Not found'

# error condition test
print(get_nested_data(data, ['foo', 'baz', 'quux', 'corge', 'invalid']))  # Output: None (dictionary key does not exist)
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