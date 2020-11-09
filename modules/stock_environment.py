from modules.environment import Environment
from catagories.actions import Action

class StockEnvironment(Environment):
    def __init__(self, data):
        super(Environment, self).__init__()
        self._data = data
        self._data_length = len(data)

    def start(self, init_amount):
        self._count = 0
        self._amount = init_amount
        self._number_of_share = 0
        self._state = self._data[0].extend([self._amount])

    def step(self, action):
        previous_data = self._data[self._count]
        previous_valuation = self._calculate_valueation(previous_data[0])

        self._count += 1
        current_data = self._data[self._count]
        self._trade(current_data[0], action)

        current_valuation = self._calculate_valueation(current_data[0])
        rewards = current_valuation - previous_valuation
        next_state = current_data

        done  = self.is_done()
        return next_state, rewards, done
    
    def _trade(self, current_share_value, action):
        if action == Action.BUY:
            buying = True
            while buying:
                if self._amount >= current_share_value:
                    self._amount -= current_share_value
                    self._number_of_share += 1
                else:
                    buying = False

        elif action == Action.SELL:
            self._amount += self._number_of_share * current_share_value
            self._number_of_share = 0

        elif action == Action.HOLD:
            pass

    def _calculate_valueation(self, share_value):
        return self._number_of_share * share_value + self._amount

    def is_done(self):
        if self._count == self._data_length - 1:
            return True
        else: 
            return False

    def get_init_state(self):
        return self._state
