class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def plus(self):
        if isinstance(self.a, (int, float)) and isinstance(self.b, (int, float)):
            return self.a + self.b
        elif isinstance(self.a, str) and isinstance(self.b, str):
            return self.a + ' ' + self.b
        else:
            raise TypeError("Неподдерживаемые типы")

    def minus(self):
        if isinstance(self.a, (int, float)) and isinstance(self.b, (int, float)):
            return self.a - self.b
        elif isinstance(self.a, str) and isinstance(self.b, str):
            return self.a.replace(self.b, '')
        else:
            raise TypeError("Неподдерживаемые типы")



double_str = Calculator("Ивaнов", "Г.П.")
double_float = Calculator(15.2, 10.2)
double_int = Calculator(10, 3)

list_obj = [double_str, double_float, double_int]

for el in list_obj:
    print(el.plus())
    print(el.minus())
