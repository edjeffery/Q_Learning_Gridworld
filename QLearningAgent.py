import random

class QLearningAgent:
    '''Q-Learning Agent player and functionality

    Attributes:
        alpha:
        gamma: Discount factor
        epsilon: Exploring parameter

    '''

    def __init__(self, alpha, gamma, epsilon):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def choose_action(self, available_actions, agent_position, q):
        q_values = [q.get_q_values(agent_position, available_actions.index(action)) for action in available_actions]
        # print(q)
        maxQ = max(q_values)
        #count = q_values.count(maxQ)

        if random.random() < self.epsilon:  # or count > 1
            best = [i for i in range(len(available_actions)) if q_values[i] == maxQ]
            i = random.choice(best)
        else:
            i = q_values.index(maxQ)
        # print(maxQ)
        action = available_actions[i]
        return action
