def get(data, keys, error_info=False, default=None):
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
        value = get(data, ['foo', 'bar', 1])
        print(value)  # Output: 2
    """
    try:
        for key in keys:
            if isinstance(data, dict):
                data = data.get(key, default)
                if data is default:
                    raise KeyError(f"field '{key}' does not exist")
            elif isinstance(data, list):
                if isinstance(key, int):
                    if -len(data) <= key < len(data):
                        data = data[key]
                    else:
                        raise IndexError(f"list index '{key}' out of range")
                else:
                    raise TypeError("list indices must be integers")
            else:
                raise TypeError(
                    f"cannot fetch nested data because object of type {type(data).__name__} has no key or index"
                )
    except (KeyError, IndexError, TypeError) as e:
        if error_info:
            print(f"an error occurred: {str(e)}")
        else:
            pass
        return default
    return data