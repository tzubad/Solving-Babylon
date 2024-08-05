# from memoization_efforts import 


initial_state = [
    ('red', 1), ('red', 1), ('red', 1),
    ('blue', 1), ('blue', 1), ('blue', 1),
    ('green', 1), ('green', 1), ('green', 1),
    ('yellow', 1), ('yellow', 1), ('yellow', 1)
]

def create_state(n_of_colors=4,n_of_chips_per_color=3):
    '''
    input: 2 integers - color (up to 10 different colors) & chips per color
    output: list of n_of_colors*n_of_chips_per_color tuples with each tuple as ("color",1)
    '''
    state = []
    color_list = ['red','blue','green','yellow','brown','grey','magenta','cyan','orange','pink']
    for color in range(n_of_colors):
        for chip in range(n_of_chips_per_color):
            state.append((color_list[color],1))
    return state




def generate_legal_moves(state):
    '''
    takes a game state (list with tuples)
    returns a list with possible new game states (a list of lists with tuples)
    '''
    moves = []
    tower_height=1
    tower_color=0
    temp_state = state[:]
    for i in range(len(state)): # the low stack
        for j in range(len(state)): # the top stack
            if i==j:
                continue
                

            # remove all kinds of symmetries
            if (temp_state[i][tower_height] == temp_state[j][tower_height] or temp_state[i][tower_color]==temp_state[j][tower_color]):
                new_state = temp_state[:]
                new_state.append((new_state[j][tower_color], new_state[j][tower_height] + new_state[i][tower_height]))
                if i>j:
                    new_state.remove(new_state[i])
                    new_state.remove(new_state[j])
                else:
                    new_state.remove(new_state[j])
                    new_state.remove(new_state[i])
                
                moves.append(new_state)
                
    moves = list(set(tuple(i) for i in moves))
    moves = [list(tup) for tup in moves] # why tuples? for comparing
    return moves

class GameNode:
    def __init__(self, state, player, parent=None):
        self.state = state
        self.player = player
        self.parent = parent
        self.children = []
        self.is_terminal = False
        self.minimax_score = 0



    def __repr__(self):
        return str(self.state)
    def __str__(self):
        return "Game state of: " + str(self.state)

    # @memoize
    def generate_children(self):
        legal_moves = generate_legal_moves(self.state)
        if legal_moves==[]:
            self.is_terminal = True
        for move in legal_moves:
            child_node = GameNode(move, 'Bob' if self.player == 'Alice' else 'Alice', self)
            self.children.append(child_node)
            child_node.generate_children()
    
    def create_matrix_form(self):
        pass
    




def getUtility(node):
        assert node is not None
        if node.player=='Alice':
            return -1
        else:
            return 1
        





def minimax(position, alpha, beta):
    if position.is_terminal==True:
        position.minimax_score = getUtility(position)
        return getUtility(position)
     
    if position.player=='Alice':
        maxEval = float('-inf')
        for child in position.children:
            eval = minimax(child, alpha, beta)
            # child.minimax_score = eval
            maxEval = max(maxEval, eval)
            position.minimax_score = maxEval
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    
    else:
        minEval = float('inf')
        for child in position.children:
            eval = minimax(child, alpha, beta)
            # child.minimax_score = eval
            minEval = min(minEval, eval)
            position.minimax_score = minEval
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval
 