import unittest

from scr import cartoteka


class TestFindPeopleUnitest(unittest.TestCase):

    def test_find_people(self):
        self.assertEqual(cartoteka.find_people('2207 876234'), "Василий Гупкин")

    def test_add_doc(self):
        self.assertEqual(cartoteka.add_doc('паспорт', '126346', 'Николай Гоголь', '1'),
                         'паспорт с номером 126346 с именем Николай Гоголь добавлен в каталог и перечень полок')

    def test_delete_doc(self):
        self.assertEqual(cartoteka.delete_doc('126346'), 'Документ с номером 126346 удален с полки 1')


if __name__ == '__main__':
    unittest.main()


