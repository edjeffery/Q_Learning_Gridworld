import numpy as np
from Gridworld import Gridworld
from QLearningAgent import QLearningAgent
from QTable import QTable

alpha = 0.1
gamma = 1
epsilon = 0.05

n_episodes = 500

reward_array = np.empty(n_episodes)

q = QTable(25, 4)

for i in range(n_episodes):
    total_reward = 0
    env = Gridworld()
    # agent = RandomAgent()
    agent = QLearningAgent(alpha, gamma, epsilon)


    while not env.is_terminal(env.agent_position):
        state = env.agent_position
        available_actions = env.get_available_actions()
        chosen_action = agent.choose_action(available_actions, env.agent_position, q)
        reward = env.make_step(chosen_action)
        new_state = env.agent_position  # now updated
        q.q_table[state][available_actions.index(chosen_action)] = (1 - alpha) * q.q_table[state][
            available_actions.index(chosen_action)] + alpha * (reward + gamma * max(q.q_table[new_state, :]))

        total_reward += reward

        grid = np.zeros((5, 5))
        bomb = np.unravel_index([env.bomb_positions], (5, 5))
        gold = np.unravel_index([env.gold_positions], (5, 5))
        pos = np.unravel_index([env.agent_position], (5, 5))
        grid[pos] = 3
        grid[bomb] = 1
        grid[gold] = 2
        # print(grid)
        #plt.matshow(grid)
        #plt.show()
        # plt.plot(reward_array);
        # plt.title("Q-Learning agent")
        # plt.xlabel('Episode')
        # plt.ylabel('Reward')
        #clear_output(wait=True)

    reward_array[i] = total_reward

print(q.q_table)

# plt.plot(reward_array);
# plt.title("Q-Learning agent")
# plt.xlabel('Episode')
# plt.ylabel('Reward')