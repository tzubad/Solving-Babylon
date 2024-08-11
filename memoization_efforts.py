
from collections import Counter
from functions import GameNode


def compare(s, t):
    '''
    compare between 2 game states
    '''
    return Counter(s) == Counter(t)



def distil_list_of_moves(list_of_moves):
    '''
    grabs a list of matrix moves and distills them to uniqe matrices
    '''
    if list_of_moves==[]:
        return [[0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0]]
    unique_moves = []
    checked_moves = []


    for move in list_of_moves:
        if move in checked_moves:
            continue
        else:
            unique_moves.append(move)
            
        for i in range(len(list_of_moves)):
            if compare(move,list_of_moves[i]):
                checked_moves.append(list_of_moves[i])
            else:
                continue

    return unique_moves[0]

def map_game_state_to_matrix(game_state, n_of_colors,n_of_chips_per_color):
    '''
    map a game state to a n by n matrix such that columns are x[0], rows are x[1], and the values are the number of ('color', int) correspondents in the game state. 
    n is the number of max colors
    returns a list of tuples (why tuples? so we could compare them later)
    [tuple(l) for l in nested_lst]
    
    rows are colors
    cols are heights
    '''
    color_list = ['red','blue','green','yellow','brown','grey','magenta','cyan','orange','pink']
    trimmed_list = color_list[:n_of_colors]
    trimmed_list
    # Initialize a nXn matrix with all zeros
    matrix = [[0 for _ in range(n_of_colors*n_of_chips_per_color)] for _ in range(n_of_colors)]
    
    # Create a dictionary to map colors to row indices
    color_to_row = {color: idx for idx, color in enumerate(trimmed_list)}
    
    # Iterate through the game state
    if isinstance(game_state,GameNode):
        for color, height in game_state.state:
            if color in color_to_row:
                row = color_to_row[color]
                col = height - 1  # Adjust column index (0-based index)
                # Update the matrix cell
                matrix[row][col] += 1
    else:
        for color, height in game_state:
            if color in color_to_row:
                row = color_to_row[color]
                col = height - 1  # Adjust column index (0-based index)
                # Update the matrix cell
                matrix[row][col] += 1


    return [tuple(l) for l in matrix]
