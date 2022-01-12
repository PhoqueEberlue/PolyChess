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
        """
        Permet d'afficher le menu dans lequel nous choisissons le mode de jeu.
        :return: Board
        """

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

    def isNotPlayer(self, choice):
        """
        Permet de tester que le nom du joueur en paramètre correspond bien à celui d'un joueur de la liste des joueurs.
        :param choice: bool
        :return:
        """
        for player in self.players:
            if player.get_name() == choice:
                return False
        return True

    def get_index_player(self, choice):
        """
        Méthode permettant d'afficher le nom du joueur.
        :param choice: Choix du joueur.
        :return: Nom joueur.
        """
        for k in range(len(self.players)):
            if self.players[k].get_name() == choice:
                return k
        return -1

    def menu_play(self):

        """
        Demande au joueur le mode de jeu qu'il veut lancer
        :return:
        """

        table_data = [
            ['Quel mode de jeu voulez-vous lancer?'],
            ['H vs H : 0 | H vs IA : 1 | IA vs IA : 2']
            ]
        table = AsciiTable(table_data)
        print(table.table)

        x = input("/:")

        if(x == "0"):
            if(len(self.players) >= 2):
                self.start_human_vs_human()
            else:
                print("Il n'y pas assez de joueur !")

        if(x == "1"):
            if(len(self.players) > 0):
                self.start_human_vs_pc() 
            else:
                print("Il n'y pas assez de joueur !")

        if(x == "2"):
            self.start_pc_vs_pc()

<<<<<<< Updated upstream
    def display_player_list(self):
        """
        Méthode permettant de donner la liste des joueurs.
        :return: liste des joueurs.
        """
        table_data = [
            ['Joueurs']]
        for k in range(len(self.players)):
            name = self.players[k].get_name()
            table_data.append([ str(k) + " : " + name])
        table = AsciiTable(table_data)
        print(table.table)

    def menu_player(self):
        """
        Méthode permettant de créer un nouveau joueur.
        :return: Liste joueurs avec le nouveau joueur.
        """
        self.display_player_list()
        
        table_data2 = [
            ['Que voulez-vous faire ?'],
            ['Créer un nouveau joueur (add Nom | Supprimer un joueur (delete Nom)']
            ]
        table2 = AsciiTable(table_data2)
        print(table2.table)
=======
        self.start()
>>>>>>> Stashed changes

    def start_human_vs_human(self):
        """
        Demande les jouers et lance une partie en humain contre humain
        :return:
        """
        self.display_player_list()

        choiceWhite = ""
        choiceBlack = ""
        while self.isNotPlayer(choiceWhite):
            print("Veuillez choisir le joueur des blancs :")
            choiceWhite = input("")

        while self.isNotPlayer(choiceBlack) or (choiceWhite == choiceBlack):
            print("Veuillez choisir le joueur des noirs :")
            choiceBlack = input("")

        player1 = self.players[self.get_index_player(choiceWhite)]
        player2 = self.players[self.get_index_player(choiceBlack)]
        player1.set_color(True)
        player2.set_color(False)

        board = chess.Board()
        game = Game(board, player1, player2)
        game.start()

    def start_pc_vs_pc(self):
        """
        Lance une partie IA contre IA
        :return:
        """
        board = chess.Board()
        game = Game(board,  Player("PC MASTER RACE 1", True, True), Player("PC MASTER RACE 2", False, True))
        game.start()

    def start_human_vs_pc(self):
        """
        Demande que jouent le joueur et le pc et lance une partie en humain contre IA
        :return:
        """
        self.display_player_list()

        choiceWhite = ""
        choiceBlack = ""

        while self.isNotPlayer(choiceWhite) and choiceWhite != "pc":
            print("Veuillez choisir le joueur des blancs (pc si ce n'est pas le joueur) :")
            choiceWhite = input("")

        while (self.isNotPlayer(choiceBlack) or choiceWhite != "pc") and (choiceBlack != "pc" or choiceWhite == choiceBlack):
            print("Veuillez choisir le joueur des noirs :")
            choiceBlack = input("")

        if(choiceWhite == "pc"):
            player1 = Player("IA", True, True)
            player2 = self.players[self.get_index_player(choiceBlack)]
        else:
            player1 = self.players[self.get_index_player(choiceWhite)]
            player2 = Player("IA", False, True)

        board = chess.Board()
        game = Game(board, player1, player2)
        game.start()

## Menu player

    def menu_player(self):
        """
        Demande au joueur ce qu'il veut faire avec la list des joueurs
        :return:
        """

        self.display_player_list()
        
        table_data2 = [
            ['Que voulez-vous faire ?'],
            ['Créer un nouveau joueur (add Nom | Supprimer un joueur (del Nom)']
            ]
        table2 = AsciiTable(table_data2)
        print(table2.table)

        x = input("/:")

        if(x[0:3] == "add"):
            if(self.isNotPlayer(x[4:])):
                self.players.append(Player(x[4:], None, False))
                print("Le joueur " + x[4:] + " a été ajouté !")

        if(x[0:3] == "del"):
            pass

        self.start()

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

## Menu option

    def options(self):
        """
        Menu d'options
        :return:
        """
        self.start()

