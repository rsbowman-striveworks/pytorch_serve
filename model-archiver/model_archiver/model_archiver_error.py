
"""
Model Archiver Error
"""


class ModelArchiverError(Exception):
    """
    Error for Model Archiver module
    """
    def __init__(self, message):
        super(ModelArchiverError, self).__init__(message)
