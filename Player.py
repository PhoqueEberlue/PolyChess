import chess
from typing import List


class Player:
    """
    Gère les joueurs
    """

    def __init__(self, nom, color, isIA):
        self.nom = nom
        self.color: bool = color  # False = Noir, True = Blanc
        self.isIA: bool = isIA
        self.graveyard = []

    def get_move(self, legal_moves) -> str:
        """

        :return: coordonnées sous forme 'a1b2'
        """
        print(f"C'est le tour {self.nom} ({self.color})")
        pos_init = input("Entrez la coordonnée de la pièce à déplacer : ")
        pos_fin = input("Entrez la coordonnée de destination : ")
        while chess.Move.from_uci(pos_init + pos_fin) not in legal_moves:
            print("Le coup rentré est incorrect")
            pos_init = input("Entrez la coordonnée de la pièce à déplacer : ")
            pos_fin = input("Entrez la coordonnée de destination : ")

        return pos_init + pos_fin
