import unittest

from person import Person


class TestPerson(unittest.TestCase):

    def test_number(self):
        p1 = Person('AAA', 'BBB')
        p2 = Person('Ccc', 'Dddd')
        p3 = Person('Ddd', 'Hhh')

        self.assertEqual(Person.number_of_person, 3)

    def test_email(self):

        person = Person('aaa', 'bbb')

        self.assertEqual( person.get_email(), 'aaa.bbb@gmail.com')