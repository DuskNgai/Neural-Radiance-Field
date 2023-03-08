def string_case_insensitive(str1: str, str2: str) -> bool:
    """Compare two strings case-insensitively.
    Args:
        str1 (str): The first string.
        str2 (str): The second string.
    Returns:
        bool: True if the two strings are equal regardless of their case, False otherwise.
    """

    return str1.lower() == str2.lower()
