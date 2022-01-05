import chess
from typing import List
from Player import Player


class Game:
    """
    Classe du jeu. Gère les pions, les joueurs et l'issue de la partie.
    """

    def __init__(self, board):
        # Liste des pièces au cimetière
        self.graveyard: List[chess.Piece] = []
        self.board: chess.Board = board
        self.isTurnBlack = False

    def start(self):
        player1 = Player("Andrew", False, False)
        player2 = Player("Calvin", True, False)

        while not self.board.is_checkmate():

            print(self.board)

            if self.isTurnBlack:
                move = player1.get_move(self.get_legal_move(player1.color), self.board)
                self.board.push_uci(move)
            else:
                move = player2.get_move(self.get_legal_move(player2.color), self.board)
                self.board.push_uci(move)

    def get_legal_move(self, color: bool) -> List[chess.Move]:
        """

        :param color: False = Noir, True = Blanc
        :return:
        """
        res = []
        for move in self.board.legal_moves:
            if self.board.color_at(move.from_square) == color:
                res.append(move)
        return res


