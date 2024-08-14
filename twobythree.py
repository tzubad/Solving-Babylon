# In[]:
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from memoization_efforts import *
from functions import *

# In[]: sainty check, should be 1

n_of_colors = 2
n_of_chips_per_color = 3
two_by_three = create_state(n_of_colors,n_of_chips_per_color)
two_by3_root = GameNode(two_by_three, 'Alice')
two_by3_root.generate_children()


# %%
two_by3_root.minimax_score = minimax(two_by3_root, float('-inf'), float('inf'))

# %%
two_by3_root.minimax_score
# %%
layer_0 = two_by3_root
first_layer_winning_moves = []
first_layer_losing_moves = []

for state in layer_0.children:
    if state.minimax_score==1:
        first_layer_winning_moves.append(map_game_state_to_matrix(state, n_of_colors,n_of_chips_per_color))
    elif state.minimax_score==-1:
        first_layer_losing_moves.append(map_game_state_to_matrix(state, n_of_colors,n_of_chips_per_color))


# distil uniqe move-matrices

uniqe_1st_layer_winning_moves = distil_list_of_moves(first_layer_winning_moves)
uniqe_1st_layer_losing_moves = distil_list_of_moves(first_layer_losing_moves)

# %% [(2, 1, 0, 0, 0, 0), (2, 0, 0, 0, 0, 0)] diff color
two_by3_root.children[0]

winning_moves = []
losing_moves = []
# extract moves by score
for state in two_by3_root.children[0].children:
    if state.minimax_score==1:
        winning_moves.append(map_game_state_to_matrix(state, n_of_colors,n_of_chips_per_color))
    elif state.minimax_score==-1:
        losing_moves.append(map_game_state_to_matrix(state, n_of_colors,n_of_chips_per_color))


# distil uniqe move-matrices

uniqe_layer_2_winning_moves = distil_list_of_moves(winning_moves)
uniqe_layer_2_losing_moves = distil_list_of_moves(losing_moves)


# %% [(1, 1, 0, 0, 0, 0), (3, 0, 0, 0, 0, 0)] same color
two_by3_root.children[1]

winning_moves = []
losing_moves = []
# extract moves by score
for state in two_by3_root.children[1].children:
    if state.minimax_score==1:
        winning_moves.append(map_game_state_to_matrix(state, n_of_colors,n_of_chips_per_color))
    elif state.minimax_score==-1:
        losing_moves.append(map_game_state_to_matrix(state, n_of_colors,n_of_chips_per_color))


# distil uniqe move-matrices

uniqe_layer_2_winning_moves = distil_list_of_moves(winning_moves)
uniqe_layer_2_losing_moves = distil_list_of_moves(losing_moves)
# %%
