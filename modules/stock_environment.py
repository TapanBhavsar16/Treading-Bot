from modules.environment import Environment

class StockEnvironment(Environment):
    def __init__(self, data):
        super(Environment, self).__init__()
        self._data = data
        self._data_length = len(data)

    def start(self, init_amount):
        self._count = 0
        self._amount = init_amount
        self._state = self._data[0].extend([self._amount])
    
    def step(self, action):
        pass
    
    def is_done(self):
        if self._count == self._data_length - 1:
            return True
        else: 
            return False