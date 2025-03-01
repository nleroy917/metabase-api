class MissingParameterException(Exception):
    def __init__(self, parameter_name):
        super().__init__(f"The required parameter '{parameter_name}' is missing.")
        self.parameter_name = parameter_name