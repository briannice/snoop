class SnoopException(Exception):
    """
    Custom exception class for application.
    """

    def __init__(self, message):
        super().__init__(message)
