class Group:

    def __init__(self):
        self.__persons = []
        self.__number = 0

    def add(self, person):
        self.__persons.append(person)
        self.__number += 1

    def remove(self, person):
        self.__persons.remove(person)
        self.__number -= 1

    def __len__(self):
        return self.__number


    def __add__(self, other):
        self.__persons.append(other)
        self.__number += 1
        return self


    def __str__(self):
        value=''
        for person in self.__persons:
            value = value + str(person) + '\n'
        return value


