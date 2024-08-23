from Board import Board
from Dice import Dice
from Player import Player


class Game:
    def __init__(self, board, players, dice):
        self.__board = board
        self.__players = players
        self.__dice = dice
        self.__current_player = None

    def start_game(self):
        while len(self.__players) > 1:
            self.__current_player = self.get_next_player()
            move_by = self.__dice.roll()
            has_won = self.move_player(move_by)
            if has_won:
                print(self.__current_player.get_name() + " won")
            else:
                self.__players.append(self.__current_player)

    def get_next_player(self):
        return self.__players.pop(0)

    def move_player(self, move_by):
        new_location = self.__board.get_next_location(self.__current_player.get_current_location(), move_by)
        self.__current_player.move_to(new_location)
        print("{} moves to {}".format(self.__current_player.get_name(), new_location))
        return True if self.__board.is_last_location(new_location) else False


p1 = Player("Utkarsh")
p2 = Player("Anjali")
players_list = [p1, p2]
d = Dice()
snakes = ((16, 6), (48, 26), (49, 11))
ladders = ((1, 38), (4, 14), (28, 84))
b = Board(snakes, ladders, 100)

g = Game(b, players_list, d)
g.start_game()
