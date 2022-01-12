import chess
import chess.engine
from ai_importor import get_ai_file_name


class MovesGenerator:
    """
    Classe qui permet de générer les meilleurs coups à jouer pour l'ordinateur
    plus la partie dure longtemps plus on analyse l'arbre de jeu pour trouver le meilleur coup
    Cette classe est instancié dans la classe joueur
    """

    def __init__(self, niveau: int):
        self.engine = chess.engine.SimpleEngine.popen_uci(f"../ai/{get_ai_file_name()}")
        self.niveau = niveau

    def get_move(self, board):
        """
        Cette fonction permet de retourner le meilleur déplacement à faire en prenant en compte le nombre de coup d'avance que l'IA aura calculé.
        :return: str de la forme 'a1a1'
        """
        machine = self.engine
        print("Machine = ", machine)
        sq = chess.SQUARES
        liste = []
        for i in sq:
            liste.append(board.piece_at(i))

        if self.niveau == 1:
            moves = machine.play(board, chess.engine.Limit(depth=1))

        if self.niveau == 2:
            moves = machine.play(board, chess.engine.Limit(depth=2))

        if self.niveau == 3:
            moves = machine.play(board, chess.engine.Limit(depth=3))

        if self.niveau == 4:
            if len(liste) > 25:
                moves = machine.play(board, chess.engine.Limit(depth=1))
            elif len(liste) > 15:
                moves = machine.play(board, chess.engine.Limit(depth=3))
            elif len(liste) > 10:
                moves = machine.play(board, chess.engine.Limit(depth=4))
            elif len(liste) > 6:
                moves = machine.play(board, chess.engine.Limit(depth=5))
            else:
                moves = machine.play(board, chess.engine.Limit(depth=6))

        return moves.move.uci()
