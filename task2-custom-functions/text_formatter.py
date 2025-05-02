def format_text(text, prefix="", suffix="", capitalize=False, max_length=None):
    """
    Formats the input text with optional prefix, suffix, capitalization, and max length.

    Parameters:
    - text (str): The main text to format (required).
    - prefix (str): Text to add before the main text. Default is empty.
    - suffix (str): Text to add after the main text. Default is empty.
    - capitalize (bool): If True, capitalize the text. Default is False.
    - max_length (int or None): If set, trim the final result to this length.

    Returns:
    - str: The formatted text.

    Raises:
    - TypeError: If inputs are not of expected types.
    - ValueError: If max_length is not positive.

    Examples:
    >>> format_text("okay", prefix=">> ", suffix=" <<", capitalize=True)
    '>> Okay <<'

    >>> format_text("technology", max_length=5)
    'techn'
    """
    # Validation
    if type(text) is not str:
        raise TypeError("The 'text' argument must be a string.")
    if type(prefix) is not str:
        raise TypeError("The 'prefix' must be a string.")
    if type(suffix) is not str:
        raise TypeError("The 'suffix' must be a string.")
    if type(capitalize)is not bool:
        raise TypeError("The 'capitalize' flag must be True or False.")
    if max_length is not None:
        if not isinstance(max_length, int):
            raise TypeError("The 'max_length' must be an integer.")
        if max_length < 1:
            raise ValueError("The 'max_length' must be a positive number.")

    # Process text
    if capitalize:
        text = text.capitalize()
    result = prefix + text + suffix

    if max_length is not None:
        result = result[:max_length]

    return result


# Example usage
if __name__ == "__main__":
    print(format_text("i'm legend", prefix="[/*", suffix="*/]", capitalize=True))  # Output: [/*I'm legend*/]
    print(format_text("information", max_length=6))                             # Output: inform
