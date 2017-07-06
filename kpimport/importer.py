"""Base class and functions for importer"""
import abc


class KickpassImporter(metaclass=abc.ABCMeta):
    """Abstract kickpass importer"""
    def __init__(self, inputdata):
        self._inputdata = inputdata

    @abc.abstractmethod
    def getsafes(self):
        """Get list of safes"""
        pass

    @abc.abstractmethod
    def importsafe(self, ctx, safe, elem):
        """Import safe"""
        pass

    @staticmethod
    @abc.abstractmethod
    def magic(inputdata):
        """Try to determine if inputdata is importable"""
        pass
