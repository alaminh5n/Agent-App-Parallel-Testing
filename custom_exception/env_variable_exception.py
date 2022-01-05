from  custom_exception.base_exception import Error


class EnvVariableNotSetException(Error):

    def __init__(self, message):
        self.message = message
