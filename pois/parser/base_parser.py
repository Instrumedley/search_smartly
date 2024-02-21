import abc
class BaseParser(abc.ABC):

    def __init__(self, file_path):
        self.file_path = file_path

    @abc.abstractmethod
    def parse(self):
        """Extract data from a file """
        pass