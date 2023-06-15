def nestedaccess(data, keys, default=None):
    """
    get nested data

    Args:
        data (dict or list): Nested data objects, which can be dictionaries or lists
        keys (list): list of keys or indices to fetch nested data
        default (any, optional): The default value, returned when the acquisition fails, the default is None

    Returns:
        any: Nested data value, if the acquisition fails, return the default value

    Example:
        data = {'foo': {'bar': [1, 2, 3]}}
        value = get_nested_data(data, ['foo', 'bar', 1])
        print(value)  # Output: 2
    """
    try:
        for key in keys:
            if isinstance(data, dict):
                data = data.get(key, default)
                if data is default:
                    raise KeyError(f"字段 '{key}' 不存在")
            elif isinstance(data, list):
                if isinstance(key, int):
                    if -len(data) <= key < len(data):
                        data = data[key]
                    else:
                        raise IndexError(f"列表索引 '{key}' 超出范围")
                else:
                    raise TypeError("列表索引必须为整数")
            else:
                raise TypeError(f"无法获取嵌套数据，因为类型为 {type(data).__name__} 的对象没有键或索引")
    except (KeyError, IndexError, TypeError) as e:
        print(f"发生错误: {str(e)}")
        return default

    return data