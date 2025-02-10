class Person:

    #class attribute
    city = 'Bishkek'
    num_of_person = 0

    # constructor
    def __init__(self, name, surname, age=0, gender=None):
        self.name = name
        self.surname = surname
        self.__age = age
        self.gender = gender
        self.email = name +'.'+surname+ '@' + 'gmail.com'
        Person.num_of_person +=1

    @classmethod
    def get_number_of_person(cls):
        return cls.num_of_person

    @classmethod
    def get_city(cls):
        print('City = ', cls.city)

    def __str__(self):
        return 'Person name: ' + self.name + ', surname: '+ self.surname + ' age: '+ str(self.__age)

    def get_email(self):
        return self.email

    def info(self):
        print("Person name: ", self.name, ' Surname: ', self.surname, 'Age:', self.__age)