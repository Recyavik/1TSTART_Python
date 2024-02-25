import unittest
from mymodule import add, subtract

class TestMyModule(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-3, 5), 2)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)

if __name__ == "__main__":
    unittest.main()
# Здесь мы импортируем класс unittest.TestCase и наши функции из модуля mymodule.
# Затем определяем класс TestMyModule, который наследуется от unittest.TestCase.
# Далее, определяем тестовые методы для каждой функции, с префиксом test_, и добавляем соответствующие проверки.
# Теперь, чтобы выполнить тесты, просто запустите файл «test_mymodule.py»:
