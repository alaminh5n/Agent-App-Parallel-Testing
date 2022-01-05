from custom_exception.base_exception import Error


class AppiumConnectionFailException(Error):

    def __init__(self, message):
        self.message = message


class InvalidDeviceTypeException(Error):

    def __init__(self, message):
        self.message = message


class CouldNotFindTheElement(Error):

    def __init__(self, message):
        self.message = message


class CouldNotFindTheXpath(Error):

    def __init__(self, message):
        self.message = message


class CouldNotExecute(Error):

    def __init__(self, message):
        self.message = message

