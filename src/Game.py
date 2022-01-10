import chess
import chess.engine
from typing import List
from Player import Player


class Game:
    """
    Classe du jeu. Gère les pions, les joueurs et l'issue de la partie.
    """

    def __init__(self, board: chess.Board, player1: Player, player2: Player):
        # Liste des pièces au cimetière
        self.graveyard: List[chess.Piece] = []
        self.board: chess.Board = board
        self.isTurnBlack = False
        self.player1 = player1
        self.player2 = player2
        self.engine = chess.engine.SimpleEngine.popen_uci(r"/home/andrewmhdb/Downloads/stockfish_14.1_linux_x64_avx2/stockfish_14.1_linux_x64_avx2")
        self.turn_count = 0

    def start(self):
        while not self.board.is_checkmate():

            # A remplacer par la fonction d'affichage de la classe CLI
            print(self.board)

            if not self.isTurnBlack:
                move = self.player1.get_move(self.get_legal_move(self.player1.color), self.board)
                self.move_piece(move)
                self.isTurnBlack = True
            else:
                move = self.player2.get_move(self.get_legal_move(self.player2.color), self.board)
                self.move_piece(move)
                self.isTurnBlack = False

            print(self.eval_position())

            self.turn_count += 1

        self.engine.quit()

    def get_legal_move(self, color: bool) -> List[chess.Move]:
        """

        :param color: False = Noir, True = Blanc
        :return: liste de move possibles
        """
        res = []
        for move in self.board.legal_moves:
            if self.board.color_at(move.from_square) == color:
                res.append(move)
        return res

    def move_piece(self, move: str):
        """
        Effectue un coup et l'ajoute à la pile des coups
        """
        self.board.push_uci(move)

    def revert_last_move(self):
        """
        Annule le dernier coup et reviens à la position précédente
        """
        self.board.pop()
        self.turn_count -= 1

    def eval_position(self) -> int:
        """
        Fonction qui évalue la position des deux joueurs.
        Renvoie un int allant de -100 à 100 indiquant respectivement si le joueur est dans une mauvaise ou une bonne
        position.
        :return: int
        """
        info = self.engine.analyse(self.board, chess.engine.Limit(depth=20))
        return info["score"]



