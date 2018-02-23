import numpy as np

class QTable:
    '''

    '''

    def __init__(self, cols, rows):
        self.q_table = np.zeros((cols, rows))

    def get_q_values(self, state, action):
        return self.q_table[state][action]
