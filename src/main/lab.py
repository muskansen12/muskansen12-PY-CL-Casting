def int_to_float(value):
    """
    Instead of returning 0, this method should Convert an integer to a float and return that value.

    :param value: The integer value to convert.
    :return: The float value.
    """
    return float(value)

def float_to_int(value):
    """
    Instead of returning 0, this method should Convert a float to an integer and return that value.

    :param value: The float value to convert.
    :return: The integer value.
    """
    return int(value)

def str_to_int(value):
    """
    Instead of returning 0, this method should Convert a string to an integer and return that value.

    :param value: The string value to convert.
    :return: The integer value.
    """
    try:
        return int(value)
    except ValueError:
        print("Invalid input: unable to convert to integer")
        return None

def str_to_float(value):
    """
    Instead of returning 0, this method should Convert a string to a float and return that value.

    :param value: The string value to convert.
    :return: The float value.
    """
    try:
        return float(value)
    except ValueError:
        print("Invalid input: unable to convert to integer")
        return None

def int_to_str(value):
    """
    Instead of returning None, this method should Convert an integer to a string and return that value.

    :param value: The integer value to convert.
    :return: The string value.
    """
    return str(value)

def float_to_str(value):
    """
    Instead of returning None, this method should Convert a float to a string and return that value.

    :param value: The float value to convert.
    :return: The string value.
    """
    return str(value)


