def raise_exception_msg(message=""):
    """Raise a name exception with a custom message.

    Args:
        message (str): The custom message for the exception.

    Raises:
        NameError: The exception with the specified message.
    """
    try:
        raise NameError(message)
    except NameError as e:
        raise e
