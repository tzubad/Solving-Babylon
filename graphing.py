# In[]:
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from memoization_efforts import *
from run import root

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
win_moves_1stlayer_np = np.array(uniqe_1st_layer_losing_moves)
lose_moves_1stlayer_np = np.array(uniqe_1st_layer_winning_moves)



# In[]: Create a tree graph for 1st layer

G = nx.Graph()

# make a node for every matrix

G.add_node(2, matrix=win_moves_1stlayer_np)
G.add_node(3, matrix=lose_moves_1stlayer_np)

# dont forget the root node!
start_state_matrix = np.array(map_game_state_to_matrix(layer_0.state, n_of_colors,n_of_chips_per_color))
G.add_node(1, matrix=start_state_matrix)

# add edges with +-1 weights on them
G.add_edge(1, 2, weight=-1)
G.add_edge(1, 3, weight=1)
    
##### to do list ######
# for every layer:  
#   split to [1] and [-1]
#   convert to move matirces and reduce redundent ones
# graph 3 layers of move matrices usinn nx


# Define a function to format the node labels
def matrix_to_str(matrix):
    return "\n".join([" ".join(map(str, row)) for row in matrix])

# Draw the tree graph
pos = nx.nx_agraph.graphviz_layout(G, prog='dot')  # Positioning the nodes
labels = {n: matrix_to_str(d['matrix']) for n, d in G.nodes(data=True)}

# edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw(G, pos, with_labels=True, labels=labels, node_shape="s",  node_color="none", bbox=dict(facecolor="skyblue", edgecolor='black', boxstyle='round,pad=0.2'), font_size=7, font_color='black')
nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=20, rotate=False, bbox=dict(facecolor="olive", edgecolor='black', boxstyle='round,pad=0.2'))
plt.show()

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
win_moves_layer_2win_np = np.array(uniqe_layer_2_winning_moves)
lose_moves_layer_2win_np = np.array(uniqe_layer_2_losing_moves)

# add nodes
G.add_node(4, matrix=win_moves_layer_2win_np)
G.add_node(5, matrix=lose_moves_layer_2win_np)

# add edges with +-1 weights on them
G.add_edge(2, 5, weight=-1)
G.add_edge(2, 4, weight=1)




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
win_moves_layer_2_np = np.array(uniqe_layer_2lose_winning_moves)
lose_moves_layer_2_np = np.array(uniqe_layer_2lose_losing_moves)


# add nodes
G.add_node(6, matrix=win_moves_layer_2win_np)
G.add_node(7, matrix=lose_moves_layer_2win_np)

# add edges with +-1 weights on them
G.add_edge(3, 7, weight=-1)
G.add_edge(3, 6, weight=1)


# %%
# Draw the tree graph
pos = nx.nx_agraph.graphviz_layout(G, prog='dot')  # Positioning the nodes
# pos = nx.planar_layout(G)  # Positioning the nodes
labels = {n: matrix_to_str(d['matrix']) for n, d in G.nodes(data=True)}

# edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw(G, pos, with_labels=True, labels=labels, node_shape="s",  node_color="none", bbox=dict(facecolor="skyblue", edgecolor='black', boxstyle='round,pad=0.2'), font_size=7, font_color='black')
nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=20, rotate=False, bbox=dict(facecolor="olive", edgecolor='black', boxstyle='round,pad=0.2'))
plt.show()