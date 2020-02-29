from Exceptions.Error import Error


# Not Supported connector exception
class NotSupportedException(Error):
    """Raised when wrong connector is passed"""
    pass
