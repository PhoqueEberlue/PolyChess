import chess
from Player import Player
from Game import Game


class Menu:
    """
    Classe permettant de lancer les différents mode de jeu, de modifier les options etc.
    """

    def __init__(self):
        pass

    def start_human_vs_human(self):
        """
        Lance une partie en humain contre humain
        :return:
        """
        player1 = Player("Andrew", False, False)
        player2 = Player("Calvin", True, False)
        board = chess.Board()
        game = Game(board, player1, player2)
        game.start()

    def start_pc_vs_pc(self):
        """
        Lance une
        :return:
        """
        pass

    def start_human_vs_pc(self):
        pass

    def create_player(self):
        """
        Création d'un nouveau joueur en rentrant les informations de ce dernier dans le terminal
        :return:
        """
        pass

    def modify_player(self):
        """
        Modifier les informations d'un joueur
        :return:
        """

    def delete_player(self):
        """
        Supprimer un joueur
        :return:
        """

    def options(self):
        """
        Menu d'options
        :return:
        """
        pass
