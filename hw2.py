from MCTSBase import MCTSBase, TreeNode


class GomokuNode(TreeNode):
    '''
    Base class for MCT node. The node has to support the following four methods.
    '''
    def is_terminal(self):
        '''
        :return: True if this node is a terminal node, False otherwise.
        '''
        pass

    def value(self):
        '''
        :return: the value of the node form the current player's point of view
        '''
        pass

    def find_action(self):
        '''
        Find the action with the highest upper confidence bound to take from the state represented by this MC tree node.
        :return: action as a tuple (x, y), i.e., putting down a piece at location x, y
        '''
        pass

    def update(self, v):
        '''
        Update the statistics/counts and values for this node
        :param v: value backup following the action that was selected in the last call of "find_action"
        :return: None
        '''
        pass



class MCTS(MCTSBase):
    """
    Monte Carlo Tree Search
    Note the game board will be represented by a numpy array of size [2, board_size[0], board_size[1]]
    """
    def __init__(self, game):
        '''
        Your subclass's constructor must call super().__init__(game)
        :param game: the Gomoku game
        '''
        self.game = game

    def reset(self):
        '''
        Clean up the internal states and make the class ready for a new tree search
        :return: None
        '''
        pass

    def get_visit_count(self, state):
        '''
        Obtain number of visits for each valid (state, a) pairs from this state during the search
        :param state: the state represented by this node
        :return: a board_size[0] X board_size[1] matrix of visit counts. It should have zero at locations corresponding to invalid moves at this state.
        '''
        pass

    def get_treenode(self, standardState):
        '''
        Find and return the node corresponding to the standardState in the search tree
        :param standardState: board state
        :return: tree node (None if the state is new, i.e., we need to expand the tree by adding a node corresponding to the state)
        '''
        pass

    def new_tree_node(self, standardState, game_end):
        '''
        Create a new tree node for the search
        :param standardState: board state
        :param game_end: whether game ends after last move, takes 3 values: None-> game not end; 0 -> game ends with a tie; 1-> player who made the last move win
        :return: a new tree node
        '''
        pass