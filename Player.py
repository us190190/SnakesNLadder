class Player:
    def __init__(self, name):
        self.__name = name
        self.__location = 0

    def move_to(self, new_location):
        self.__location = new_location

    def get_current_location(self):
        return self.__location

    def get_name(self):
        return self.__name
