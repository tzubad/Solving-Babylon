# In[9]:
from functions import *
from memoization_efforts import *


# In[9]: build a 3x3
n_colors = 3
n_chips_per_color = 3
three_by_three = create_state(n_colors,n_chips_per_color)
root = GameNode(three_by_three, 'Alice')
root.generate_children()



# In[]: who wins?

root.minimax_score = minimax(root, float('-inf'), float('inf')) # equals 1, Alice wins
root.minimax_score

# In[]: lets scan the first layer
first_layer = []
for gamestate in root.children:
    first_layer.append(minimax(gamestate, float('-inf'), float('inf')))

first_layer # Alice wins in 6 out of 9 possible states.
# [1, 1, -1, -1, 1, 1, 1, -1, 1]

# In[] # a probe at 2nd layer

win_states_1 = []
lose_states_1 = []
for i, gamestate in enumerate(root.children):
    if first_layer[i]==1:
        win_states_1.append(gamestate)
    else:
        lose_states_1.append(gamestate)

lose_states_1 
# [[('red', 1), ('red', 1), ('red', 1), ('blue', 1), ('blue', 1), ('blue', 1), ('green', 1), ('green', 2)],
#  [('red', 1), ('red', 1), ('red', 1), ('blue', 1), ('green', 1), ('green', 1), ('green', 1), ('blue', 2)],
#  [('red', 1), ('blue', 1), ('blue', 1), ('blue', 1), ('green', 1), ('green', 1), ('green', 1), ('red', 2)]]


win_states_1 
# [[('red', 1), ('red', 1), ('red', 1), ('blue', 1), ('blue', 1), ('green', 1), ('green', 1), ('green', 2)],
#  [('red', 1), ('red', 1), ('blue', 1), ('blue', 1), ('blue', 1), ('green', 1), ('green', 1), ('red', 2)],
#  [('red', 1), ('red', 1), ('blue', 1), ('blue', 1), ('green', 1), ('green', 1), ('green', 1), ('red', 2)],
#  [('red', 1), ('red', 1), ('blue', 1), ('blue', 1), ('green', 1), ('green', 1), ('green', 1), ('blue', 2)],
#  [('red', 1), ('red', 1), ('blue', 1), ('blue', 1), ('blue', 1), ('green', 1), ('green', 1), ('green', 2)],
#  [('red', 1), ('red', 1), ('red', 1), ('blue', 1), ('blue', 1), ('green', 1), ('green', 1), ('blue', 2)]]

# In[9] Comparing losing states in the 1st layer
losing_state_1_matrices=[]
for state in lose_states_1:

    losing_state_1_matrices.append(map_game_state_to_matrix(state, n_colors,n_chips_per_color))



compare(losing_state_1_matrices[1],losing_state_1_matrices[2])

losing_state_1_matrices
# [(1, 1, 0, 0, 0, 0, 0, 0, 0), 
#  (3, 0, 0, 0, 0, 0, 0, 0, 0),
#  (3, 0, 0, 0, 0, 0, 0, 0, 0)]

# In[9] Comparing winning states in the 1st layer
wining_state_1_matrices=[]
for state in win_states_1:

    wining_state_1_matrices.append(map_game_state_to_matrix(state, n_colors,n_chips_per_color))



compare(wining_state_1_matrices[0],wining_state_1_matrices[3])

wining_state_1_matrices
# [(2, 1, 0, 0, 0, 0, 0, 0, 0),
#  (2, 0, 0, 0, 0, 0, 0, 0, 0),
#  (3, 0, 0, 0, 0, 0, 0, 0, 0)]



# In[9]: # analyzing the 2nd layer - LOSE CONDITION
second_layer_L = []
for gamestate in lose_states_1:
    for i in range(len(lose_states_1)):
        second_layer_L.append(minimax(gamestate.children[i], float('-inf'), float('inf')))


second_layer_L # [1, 1, 1, -1, 1, 1, 1, 1, 1] This time Bob chooses -1, but it has to be the right choice! IMPORTANT

map_game_state_to_matrix(lose_states_1[1].children[2], n_colors,n_chips_per_color) 
# This is the matrix shape for the -1, the rest are 1
# [(3, 0, 0, 0, 0, 0, 0, 0, 0),
#  (0, 0, 1, 0, 0, 0, 0, 0, 0),
#  (3, 0, 0, 0, 0, 0, 0, 0, 0)]

# In[9]: # analyzing the 2nd layer - WIN
second_layer_W = []
for gamestate in win_states_1:
    for i in range(len(lose_states_1)):
        second_layer_W.append(minimax(gamestate.children[i], float('-inf'), float('inf')))


second_layer_W # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] Out of all 18 options, Bob has no options that favor him
# it doesnt matter what alice chooses in the 2nd layer but one option in second_layer_L 

# In[] # Probing the -1 option (second_layer_L[3]) and one of the other options (second_layer_L[0],second_layer_L[5],second_layer_W)


# In[9]:
## save the 3x3 game

# import pickle

# # Create a large object
# print(root, type(root))
# # <class 'list'> 1000

# # Save to file
# with open('threebythree.pkl', 'wb') as file:
#     pickle.dump(root, file)

# # #


# # In[10]:


# # Load the 2x2 game

# # Load from file
# with open('threebythree.pkl', 'rb') as file:
#     newObj = pickle.load(file)

# print(newObj, type(newObj))
# # <class 'list'> 1000
# newObj.children[0].children==root.children[0].children


# for colors=<3 and chips =<3 i can complie pretty fast
# 

# In[ ]:


# standardGame = GameNode(create_state(), 'Alice')
# standardGame.generate_children()


# In[ ]:


# # started 11:34
# # ended TBA
# # Create a large object
# print(standardGame, type(standardGame))
# # <class 'list'> 1000

# # Save to file
# with open('standardGame.pkl', 'wb') as file:
#     pickle.dump(standardGame, file)


# Step 4: Determine the Winning Condition
# Traverse the game tree to determine the winner at each terminal state:

# In[ ]:


 



# 

# In[ ]:


##########################
###### MINI-MAX A-B ######
##########################

class AlphaBeta:
    # print utility value of root node (assuming it is max)
    # print names of all nodes visited during search
    def __init__(self, game_tree):
        self.game_tree = game_tree  # GameTree
        self.root = game_tree.root  # GameNode
        return

    def alpha_beta_search(self, node):
        infinity = float('inf')
        best_val = -infinity
        beta = infinity

        successors = self.getSuccessors(node)
        best_state = None
        for state in successors:
            value = self.min_value(state, best_val, beta)
            if value > best_val:
                best_val = value
                best_state = state
        print("AlphaBeta:  Utility Value of Root Node: = " + str(best_val))
        print("AlphaBeta:  Best State is: " + best_state.Name)
        return best_state

    def max_value(self, node, alpha, beta):
        print("AlphaBeta->MAX: Visited Node :: " + node.Name)
        if self.isTerminal(node):
            return self.getUtility(node)
        infinity = float('inf')
        value = -infinity

        successors = self.getSuccessors(node)
        for state in successors:
            value = max(value, self.min_value(state, alpha, beta))
            if value >= beta:
                return value
            alpha = max(alpha, value)
        return value

    def min_value(self, node, alpha, beta):
        print("AlphaBeta->MIN: Visited Node :: " + node.Name)
        if self.isTerminal(node):
            return self.getUtility(node)
        infinity = float('inf')
        value = infinity

        successors = self.getSuccessors(node)
        for state in successors:
            value = min(value, self.max_value(state, alpha, beta))
            if value <= alpha:
                return value
            beta = min(beta, value)

        return value
    #                     #
    #   UTILITY METHODS   #
    #                     #

    # successor states in a game tree are the child nodes…
    def getSuccessors(self, node):
        assert node is not None
        return node.children

    # return true if the node has NO children (successor states)
    # return false if the node has children (successor states)
    def isTerminal(self, node):
        assert node.is_terminal==True
        
        return node.children == []

    def getUtility(self, node):
        assert node is not None
        if node.player=='Alice':
            return -1
        else:
            return 1
        


# In[ ]:




