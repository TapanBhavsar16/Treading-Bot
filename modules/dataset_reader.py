import abc

class DatasetReader(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def read_file(self, file):
        pass
