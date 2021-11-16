"""
File with custom exceptions
"""

__all__ = [
    "FileAlreadyLoaded"
]


class CustomException(Exception):  # Class for custom exceptions
    def __init__(self, error_msg: str):
        self.error_msg = str(error_msg)

        if not self.error_msg.endswith("."):
            self.error_msg += "."

        super().__init__(self.error_msg)

    def __str__(self):
        return str(self.error_msg)

    def __repr__(self):
        return repr(self.error_msg)


class FileAlreadyLoaded(CustomException):
    pass
