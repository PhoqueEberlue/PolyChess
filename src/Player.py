import chess
from typing import List
from MovesGenerator import MovesGenerator


class Player:
    """
    Gère les joueurs
    """

    def __init__(self, nom, color, is_pc):
        self.nom = nom
        self.color: bool = color  # False = Noir, True = Blanc
        self.is_pc: bool = is_pc
        self.graveyard: List[str] = []  # Exemple : ['r', 'p', 'p', 'k']
        self.score = 0

        if self.is_pc:
            self.move_generator = MovesGenerator()

    def get_name(self):
        return self.nom

    def get_move(self, legal_moves, board) -> str:
        """
        Renvoie le déplacement d'un joueur ordinateur ou humain
        :return: coordonnées sous forme 'a1b2'
        """
        if self.is_pc:
            return self.get_move_from_pc(board)
        else:
            return self.get_move_from_player(legal_moves)

    def get_move_from_player(self, legal_moves) -> str:
        """
        Renvoie le déplacement choisi par un joueur humain
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

    def get_move_from_pc(self, board: chess.Board) -> str:
        """
        Renvoie le déplacement choisi par l'ordinateur
        :param board: l'instance du plateau
        :return: les coordonnées de déplacement sous forme 'a1b2'
        """
        return self.move_generator.get_move()

    def get_win_number(self) -> int:
        """
        Retourne le nombre de victoire
        :return: int
        """
        return self.score

    def incr_win(self) -> None:
        """
        Incrémente le nombre de victoire du joueur
        """
        self.score += 1

    def add_to_graveyard(self, piece) -> None:
        """
        Ajoute une pièce au cimetière.
        :param piece:
        """
        self.graveyard.append(piece)

    def remove_from_graveyard(self, piece) -> None:
        """
        Retire une piece du cimetière
        :param piece:
        :return:
        """
        if self.is_in_graveyard(piece):
            self.graveyard.remove(piece)

    def is_in_graveyard(self, piece) -> bool:
        """
        Vérifie si une pièce est dans le cimetière
        :param piece:
        :return: un booléen
        """
        for x in self.graveyard:
            if x == piece:
                return True
        return False
