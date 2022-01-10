from terminaltables import AsciiTable
import chess
from Player import Player
from Game import Game


class Menu:
    """
    Classe permettant de lancer les différents mode de jeu, de modifier les options etc.
    """

    def __init__(self):
        self.players = []

        player1 = Player("Andrew", False, False)
        player2 = Player("Calvin", True, False)

        self.players.append(player1)
        self.players.append(player2)

        self.start()

    def start(self):

        table_data = [
            ['Que voulez-vous faire ?'],
            ['Jouer (play) | Gérer joueur (player) | Options (opt)']
            ]
        table = AsciiTable(table_data)
        print(table.table)

        x = input("/:")

        if(x == "play"):
            self.menu_play()

        if(x == "player"):
            self.menu_player()

    def menu_play(self):
        table_data = [
            ['Quel mode de jeu voulez-vous lancer?'],
            ['H vs H : 0 | H vs IA : 1 | IA vs IA : 2']
            ]
        table = AsciiTable(table_data)
        print(table.table)

        x = input("/:")

        if(x == "0"):
            if(len(self.players) >= 2):
                self.start_human_vs_human(self.players[0], self.players[1])
            else:
                print("Il n'y pas assez de joueur !")

    def menu_player(self):
        table_data = [
            ['Joueurs']]
        for k in self.players:
            name = k.get_name()
            table_data.append([name])
        table = AsciiTable(table_data)
        print(table.table)
        
        table_data2 = [
            ['Que voulez-vous faire ?'],
            ['Créer un nouveau joueur (add Nom | Supprimer un joueur (delete Nom)']
            ]
        table2 = AsciiTable(table_data2)
        print(table2.table)

    def start_human_vs_human(self, player1, player2):
        """
        Lance une partie en humain contre humain
        :return:
        """
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
        table_data = [
            ['Nouveau joueur !'],
            ['player add Pseudo Color isPC']
            ]
        table = AsciiTable(table_data)
        print(table.table)

    def modify_player(self):
        """
        Modifier les informations d'un joueur
        :return:
        """
        table_data = [
            ['Modifier joueur !'],
            ['player modify Pseudo']
            ]
        table = AsciiTable(table_data)
        print(table.table)

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
