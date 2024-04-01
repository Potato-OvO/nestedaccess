from nestedaccess.lang import lang_messages


def error_message(msg_key, lang="en", **kwargs):
    if lang not in lang_messages:
        raise ValueError("Unsupported language. Supported languages are 'en' and 'zh'.")

    message = lang_messages[lang].get(msg_key)
    if message is None:
        raise ValueError(f"Message key '{msg_key}' not found for language '{lang}'.")

    return message.format(**kwargs)


def get(data, keys, default=None, lang="en"):
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
                if key in data:
                    data = data[key]
                else:
                    error_msg = error_message("KeyError", lang=lang, key=key)
                    raise KeyError(error_msg)
            elif isinstance(data, list):
                try:
                    index = int(key)
                    if 0 <= index < len(data):
                        data = data[index]
                    else:
                        error_msg = error_message("IndexError", lang=lang, key=key)
                        raise IndexError(error_msg)
                except TypeError:
                    error_msg = error_message("TypeError", lang=lang)
                    raise TypeError(error_msg)
            else:
                error_msg = error_message(
                    "GeneralError", lang=lang, data_type=type(data).__name__, key=key
                )
                raise ValueError(error_msg)

        # 如果循环完毕没有抛出异常，则返回数据
        return data
    except Exception as e:
        if default is not None:
            return default
        else:
            raise
