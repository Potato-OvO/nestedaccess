# README.md
<a href="./README_zh-CN.md">中文文档</a>

# Nestedaccess

Nestedaccess is a simple, elegant way to retrieve deeply nested data from a dictionary.

Pass in the keys you want to obtain data through lists and tuples in sequence, avoiding the use of overly long if-elif-else judgment statements and making the code more elegant.

In addition, if the field does not exist, it can be customized to return a default value. If there is no default value, an error message will be output. The error message can specify a specific [language](#yuyan).

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

# normal data test.
print(nestedaccess.get(data, ["foo", "baz", "quux", "grault", 1]))  # Output: 5

test_key = ("empty_list", 0, "baz", "qux")
print(get(data, test_key))  # Output: hello

# Field does not exist, return default value data test.
print(nestedaccess.get(data, ["nonexistent"], default="Not found"))  # Output: Not found

# If the field does not exist, an error message is returned.
test_key = ["foo", "baz", "quux", "corge", "invalid"]
res = nestedaccess.get(data, test_key, lang="en")  # Output: ValueError: cannot fetch nested data because object of type bool has no key or index

test1_key = ("foo", "bae", "quux", "corge")
res1 = nestedaccess.get(data, test1_key, lang="en") #Output: KeyError: "field 'bae' does not exist"
```

# Installing Nestedaccess and Supported Versions

## Nestedaccess is available on PyPI:

```python
$ python -m pip install nestedaccess
```

Nestedaccess officially supports Python 3.7+.

# Supported Features & Best–Practices

- Used to obtain nested data. When the nested structure is deep, data can be obtained through lists or tuples to avoid using overly long if-elif-else judgment statements and make the code more elegant.

- Takes a nested data object (can be a dictionary or a list), a list of keys or indexes, and an optional default value.

- It will try to get the nested data in the given key or index order, output the non-existent field name if the field does not exist, and return the default value if a custom default value is set.

- If the field does not exist, the detailed error message returned can optionally be specified in a specific language ("en" is used by default).
  
    <span id="yuyan">Supported languages:</span>
    |language|code|
    | --- | --- |
    | English | en |
    | Chinese | zh |