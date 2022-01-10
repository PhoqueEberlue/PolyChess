import chess
import chess.engine


class MovesGenerator:
    """
    Classe qui permet de générer les meilleurs coup à jouer pour l'ordinateur
    plus la partie dure longtemps plus on analyse l'arbre de jeu pour trouver le meilleur coup
    Cette classe est instancié dans la classe joueur
    """

    def __init__(self, game):
        self.engine = None
        self.board = game.board

    def get_move(self):
        machine = self.engine
        print("Machine = ", machine)
        sq = chess.SQUARES
        liste = []
        for i in sq:
            liste.append(i.peace_at())

        if len(liste) > 25:
            moves = machine.play(self.board, chess.engine.Limit(depth=2))
        elif len(liste) > 15:
            moves = machine.play(self.board, chess.engine.Limit(depth=4))
        elif len(liste) > 10:
            moves = machine.play(self.board, chess.engine.Limit(depth=5))
        elif len(liste) > 6:
            moves = machine.play(self.board, chess.engine.Limit(depth=7))
        else:
            moves = machine.play(self.board, chess.engine.Limit(depth=10))

        return moves.move
