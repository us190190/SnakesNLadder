class Board:
    def __init__(self, snakes, ladders, max_size):
        self.__snakes = snakes
        self.__ladders = ladders
        self.__max_size = max_size

    def get_next_location(self, current_location, move_by):

        # out of board location
        new_location = current_location + move_by
        if new_location > self.__max_size:
            print("Out of board")
            return current_location

        # check ladders on board
        for start, end in self.__snakes:
            if start == new_location:
                print("Snake")
                return end

        # check snakes on board
        for start, end in self.__ladders:
            if start == new_location:
                print("Ladder")
                return end

        return new_location

    def is_last_location(self, current_location):
        return current_location == self.__max_size

