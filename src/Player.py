import chess
from typing import List


class Player:
    """
    Gère les joueurs
    """

    def __init__(self, nom, color, is_pc):
        self.nom = nom
        self.color: bool = color  # False = Noir, True = Blanc
        self.is_pc: bool = is_pc
        self.graveyard = []

    def get_move(self, legal_moves, board) -> str:
        """

        :return: coordonnées sous forme 'a1b2'
        """
        if self.is_pc:
            return self.get_move_from_pc(legal_moves, board)
        else:
            return self.get_move_from_player(legal_moves)

    def get_move_from_player(self, legal_moves) -> str:
        """
        Renvoie un déplacement choisi par un joueur humain
        :param legal_moves: la liste des coups possibles pour ce joueur
        :return: les coordonnées de déplacement sous forme 'a1b2'
        """
        print(f"C'est le tour {self.nom} ({self.color})")
        pos_init = input("Entrez la coordonnée de la pièce à déplacer : ")
        pos_fin = input("Entrez la coordonnée de destination : ")
        while chess.Move.from_uci(pos_init + pos_fin) not in legal_moves:
            print("Le coup rentré est incorrect")
            pos_init = input("Entrez la coordonnée de la pièce à déplacer : ")
            pos_fin = input("Entrez la coordonnée de destination : ")

        return pos_init + pos_fin

    def get_move_from_pc(self, legal_moves, board: chess.Board) -> str:
        """
        Renvoie un déplacement choisi par l'ordinateur
        :param legal_moves: la liste des coups possibles pour ce joueur
        :param board: l'instance du plateau
        :return: les coordonnées de déplacement sous forme 'a1b2'
        """
        pass
