# In[]:
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from memoization_efforts import *
from run import root
from functions import *

# In[]: sainty check, should be 1
root.minimax_score
n_of_colors = 3
n_of_chips_per_color = 3



# In[]: extract 1st layer to [1] and [-1] 
layer_0 = root
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


# turn matrices to np.array
lose_moves_1stlayer_np = np.array(uniqe_1st_layer_losing_moves[0])
win_moves_1stlayer_np = np.array(uniqe_1st_layer_winning_moves[0])



# In[]: Create a tree graph for 1st layer

# dont forget the root node!
start_state_matrix = np.array(map_game_state_to_matrix(layer_0.state, n_of_colors,n_of_chips_per_color))

# Define a function to format the node labels
def matrix_to_str(matrix):
    return "\n".join([" ".join(map(str, row)) for row in matrix])






# In[]: extract 2nd layer to [1] and [-1]  # score 1 - win condition
# take the first 1 score
for child in root.children:
    if child.minimax_score==1:
        layer_1_win = child
        break

winning_moves = []
losing_moves = []
# extract moves by score
for state in layer_1_win.children:
    if state.minimax_score==1:
        winning_moves.append(map_game_state_to_matrix(state, n_of_colors,n_of_chips_per_color))
    elif state.minimax_score==-1:
        losing_moves.append(map_game_state_to_matrix(state, n_of_colors,n_of_chips_per_color))


# distil uniqe move-matrices

uniqe_layer_2_winning_moves = distil_list_of_moves(winning_moves)
uniqe_layer_2_losing_moves = distil_list_of_moves(losing_moves)


# turn matrices to np.array

#win_moves_layer_2win_np = np.array(uniqe_layer_2_winning_moves)
# there are 8
lose_moves_layer_2win_np = np.array(uniqe_layer_2_losing_moves)


# In[]: extract 2nd layer to [1] and [-1]  # score -1
# take the first -1 score
for child in root.children:
    if child.minimax_score==-1:
        layer_1_lose = child
        break

winning_moves = []
losing_moves = []
# extract moves by score
for state in layer_1_lose.children:
    if state.minimax_score==1:
        winning_moves.append(map_game_state_to_matrix(state, n_of_colors,n_of_chips_per_color))
    elif state.minimax_score==-1:
        losing_moves.append(map_game_state_to_matrix(state, n_of_colors,n_of_chips_per_color))


# distil uniqe move-matrices

uniqe_layer_2lose_winning_moves = distil_list_of_moves(winning_moves)
uniqe_layer_2lose_losing_moves = distil_list_of_moves(losing_moves)


# turn matrices to np.array
win_moves_layer_2lose_np = np.array(uniqe_layer_2lose_winning_moves[0])
#lose_moves_layer_2lose_np = np.array(uniqe_layer_2lose_losing_moves)
# there are 4


# %%
# Draw the tree graph
G = nx.DiGraph()

# make a node for every matrix
G.add_node("start", matrix=start_state_matrix)
G.add_node("win", matrix=win_moves_1stlayer_np)
G.add_node("lose", matrix=lose_moves_1stlayer_np)
G.add_node("win_lose", matrix=lose_moves_layer_2win_np)
G.add_node("lose_win", matrix=win_moves_layer_2lose_np)

for i, move in enumerate(uniqe_layer_2lose_losing_moves):
    move_name = "lose_lose_"+str(i)
    G.add_node(move_name, matrix=np.array(move))
    G.add_edge("lose", move_name, weight=-1)

for i, move in enumerate(uniqe_layer_2_winning_moves):
    move_name = "win_win_"+str(i)
    G.add_node(move_name, matrix=np.array(move))
    G.add_edge("win", move_name, weight=1)


# add edges with +-1 weights on them
G.add_edge("start", "win", weight=1)
G.add_edge("start", "lose", weight=-1)
G.add_edge("win", "win_lose", weight=-1)
G.add_edge("lose", "lose_win", weight=1)


# Define edges to create the tree structure
G.add_edges_from([("start", "win"), ("start", "lose"),
                  ("win", "win_win_0"),("win", "win_win_1"),("win", "win_win_2"), ("win", "win_win_3"),("win", "win_win_4"),("win", "win_win_5"),("win", "win_win_6"),("win", "win_win_7"),
                  ("lose", "lose_win"), ("lose", "lose_lose_0"), ("lose", "lose_lose_1"), ("lose", "lose_lose_2"), ("lose", "lose_lose_3")])

# Define positions for the nodes
pos = {
    "start": (0, 2),

    "win": (-15, 1.5),
    "lose": (15, 1.5),

    "win_lose": (-30, 1),
    "lose_win": (30, 1),

    "win_win_0": (-30, 0),
    "win_win_1": (-25, 0.5),
    "win_win_2": (-20, 0),
    "win_win_3": (-15, 0.5),
    "win_win_4": (-10, 0),
    "win_win_5": (-5, 0.5),
    "win_win_6": (0, 0),
    "win_win_7": (5, 0.5),
    "lose_lose_0": (10, 0),
    "lose_lose_1": (15, 0.5),
    "lose_lose_2": (20, 0),
    "lose_lose_3": (25, 0.5),
    "lose_lose_4": (30, 0)
}

# Draw the nodes, edges, and labels

labels = {n: matrix_to_str(d['matrix']) for n, d in G.nodes(data=True)}
edge_labels = nx.get_edge_attributes(G, "weight")

nx.draw(G, pos, with_labels=True, labels=labels, node_shape="s",  node_color="none", bbox=dict(facecolor="skyblue", edgecolor='black', boxstyle='round,pad=0.2'), font_size=7, font_color='black')
nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=10, rotate=False, bbox=dict(facecolor="olive", edgecolor='black', boxstyle='round,pad=0.2'))

# Display the plot
plt.title("Two first layers of 3-Colored Babylon")
plt.show()
# %%
