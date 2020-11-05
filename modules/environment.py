import abc

class Environment(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def start(self):
        pass
    
    @abc.abstractmethod
    def step(self, action):
        pass
    
    @abc.abstractmethod
    def is_done(self, state):
        pass
