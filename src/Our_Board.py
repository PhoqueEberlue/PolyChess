import chess


class Our_Board:
    """
    Gère l'affichage dans le terminal
    """

    def __init__(self, emojiMode=True):
        self.board: chess.Board = chess.Board()
        self.emojiMode = emojiMode

    def get_base_display(self):
        """
        Remplace l'affichage des pions avec les lettres par un affichage avec des emojis
        :return:
        """
        res = str(self.board)
        if self.emojiMode:
            res = res.replace("R", "♜")
            res = res.replace("B", "♝")
            res = res.replace("Q", "♛")
            res = res.replace("K", "♚")
            res = res.replace("P", "♟")
            res = res.replace("N", "♞")
            res = res.replace("r", "♖")
            res = res.replace("b", "♗")
            res = res.replace("q", "♕")
            res = res.replace("k", "♔")
            res = res.replace("p", "♙")
            res = res.replace("n", "️♘")
            return res
        else:
            return res

    def display_board(self):
        """
        Affiche les numéros de lignes et de colonnes
        :return:
        """
        res = '  a b c d e f g h \n'
        x = self.get_base_display().split('\n')

        for i in range(8, 0, -1):
            res += f'{i} {x[abs(i - 8)]}\n'

        return res
