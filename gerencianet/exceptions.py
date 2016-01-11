# encoding: utf-8

class GerencianetError(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)

class MissingParametersError(GerencianetError):

    def __init__(self, parameter):
        self.parameter = parameter
        message = 'Missing required parameter {parameter}'.format(parameter= self.parameter)
        super(MissingParametersError, self).__init__(message)


class UnauthorizedError(GerencianetError):

    def __init__(self, status):
        message = 'Status:'  + str(status) +" Could not authenticate. \n\Please make sure you are using correct credentials and if you are using then in the correct environment."
        super(UnauthorizedError, self).__init__(message)
