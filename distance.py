class Distance:

    def __init__(self, distance = 0):
        self.__distance = distance

    def __add__(self, other):
        return Distance(len(self) + other)

    def __eq__(self, other):
        return self.__distance == len(other)

    def __str__(self):
        return 'Distance is ' + str(self.__distance)

    def get_distance(self):
        return self.__distance

    def __len__(self):
        return self.__distance




