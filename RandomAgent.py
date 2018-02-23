
class RandomAgent:
    '''

    '''

    def choose_action(self, available_actions):
        number_of_actions = len(available_actions)
        random_index = np.random.randint(0, number_of_actions)
        action = available_actions[random_index]
        return action