import chess


class Our_Board:
    
    
    """
    Gère l'affichage dans le terminal
    """
    
    
    
    def __init__(self):
        
        self.board: chess.Board = chess.Board()
        

    def display_board(self):
        
        res='  a b c d e f g h \n'
        #x=self.board.__repr__()
        x=str(self.board).split('\n')    
        
        
        for i in range(1,9):
            res+=f'{i} {x[i-1]}\n'
            
            
        return res
            
        
        
        