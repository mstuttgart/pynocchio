# -*- coding: utf-8 -*-


class PynocchioBaseException(Exception):

    def __init__(self, msg, *args):
        super(PynocchioBaseException, self).__init__(msg, *args)
        self.message = msg.format(args)

    def __str__(self):
        return repr(self.message)


class InvalidTypeFileException(PynocchioBaseException):

    def __str__(self):
        return repr(self.message)


class DependenceNotFoundException(PynocchioBaseException):

    def __str__(self):
        return repr(self.message)


class NoDataFindException(PynocchioBaseException):

    def __str__(self):
        return repr(self.message)


class LoadComicsException(PynocchioBaseException):

    def __str__(self):
        return repr(self.message)
