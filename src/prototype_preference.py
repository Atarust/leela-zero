# Prototype of preference learning cost
# preference learning is basically throwing away the assumption, that 
#   "reward_a > reward_b" is giving more information as "reward_a >> reward_b"

# given a state, we have for multiple actions their expected value. 

# avgDominance = (sum for all a (but ai): P(ai > a)) / (nr_of_actions - 1)
# we can calculate P(ai > a), by counting how many actions a have a better value than ai.


## values of action 0 to 4. values[a] is count and value of action a
import numpy as np


def avg_dominance(action, values):
    # calculate average dominance of action action, given value, a list of all rewads of all action
    actions = range(len(values))
    
    probs = 0
    for a in actions:
        if a == action:
            continue
        probs += prob_higher(values[action], values[a])
    return probs/(len(actions)-1)

def prob_higher(rewards_a,rewards_b):
    # P(Reward(a) > Reward(b)) : probability that reward of action a is higher than reward of action b
    comparisons = 0
    if len(rewards_a) == 0 or len(rewards_b) == 0:
        return np.NaN # TODO
    for r_a in rewards_a:
        for r_b in rewards_b:
            if r_a > r_b:
                comparisons += 1
            #print("{} > {} -> comparison={}".format(r_a, r_b, comparisons))
    return comparisons/(len(rewards_a)*len(rewards_b))

# values[action] is collected reward action
values = [[-1, -1, 0.6,0.6,0.6,0.6,0.6,0.6,0.6,0.6],
            [0.4, 0.4,0.4, 0.4,0.4, 0.4,0.4, 0.4,0.4, 0.4]]

nr_of_actions = 5
visits = 1000 # max
values = np.random.rand(nr_of_actions,np.random.randint(1,visits))
print('values:', values)
print('ave_dominance:', [avg_dominance(a, values) for a in range(len(values))])
print('average reward:', [np.mean([values[a]]) for a in range(len(values))])
print('average median:', [np.median([values[a]]) for a in range(len(values))])

