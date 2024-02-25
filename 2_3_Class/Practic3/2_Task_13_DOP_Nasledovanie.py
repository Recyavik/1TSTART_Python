class Person:

    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def check_full_name(self):
        if self.name.count(" ") >= 1:
            return True
        else:
            return False

    # Добавляет фамилию, если отсутствует
    def add_full_name(self):
        if not(Person.check_full_name(self)):
            surname = input(self.name+", введите фамилию: ")
            while surname == "":
                surname = input("Повторите ввод фамилии: ")
            self.name += (" " + surname)
        else:
            print(f"Имя и Фамилия: {self.name}")

    def info(self):
        print(f"Человек: {self.name}, возраст: {self.age}")

    # Если пользователь забыл инициализировать экземпляр с именем, то заполнить пустое
    # Если данные присутствуют, то выводятся существующие
    def registration(self):
        new = ""
        self.name = self.name.strip()
        while self.name == "" or self.age <= 0:
            if self.name == "":
                self.name = input("Введите Имя: ")
            if self.age <= 0:
                str_age = input("Введите возраст человека: ")
                if not(str_age.isdigit()):
                    self.age = 0
                else:
                    self.age = int(str_age)
            new = "Зафиксированы новые данные: "
        print(f"{new}{self.name} \t- {self.age}")

    def __str__(self):
        return f"{self.name} \t- {self.age}"


class CyberSportsmen(Person):
    def __init__(self, team_name, experience):
        super().__init__(name="", age=0)
        self.team_name = team_name
        self.experience = experience

    @classmethod
    def get_str_year(cls, experience):
        str_y = "лет"
        if experience in [1, 21, 31, 41, 51, 61, 71, 81, 91]:
            str_y = "год"
        elif experience in [2, 22, 32, 42, 52, 62, 72, 82, 92] or \
                experience in [3, 23, 33, 43, 53, 63, 73, 83, 93] or \
                experience in [4, 24, 34, 44, 54, 64, 74, 84, 94]:
            str_y = "годa"
        return str_y

    def info(self):
        if self.experience == 0:
            print(f"Кибер-спортсмен: {self.name}, возраст: {self.age}, играет в команде {self.team_name} "
                  f"- он новичок")
        else:
            str_year = self.get_str_year(self.experience)
            print(f"Кибер-спортсмен: {self.name}, возраст: {self.age}, играет в команде {self.team_name} "
                  f"{self.experience} {str_year}")


class GameDisiner(Person):
    def __init__(self, company_name, experience=0):
        super().__init__(name="", age=0)
        self.company_name = company_name
        self.experience = experience

    @classmethod
    def get_str_year(cls, experience):
        str_y = "лет"
        if experience in [1, 21, 31, 41, 51, 61, 71, 81, 91]:
            str_y = "год"
        elif experience in [2, 22, 32, 42, 52, 62, 72, 82, 92] or \
                experience in [3, 23, 33, 43, 53, 63, 73, 83, 93] or \
                experience in [4, 24, 34, 44, 54, 64, 74, 84, 94]:
            str_y = "годa"
        return str_y

    def info(self):
        if self.experience == 0:
            print(f"Гейм-дизайнер: {self.name}, возраст: {self.age}, работает в компании {self.company_name} "
                  f"- он новичок")
        else:
            str_year = self.get_str_year(self.experience)
            print(f"Гейм-дизайнер: {self.name}, возраст: {self.age}, работает в компании {self.company_name} "
                  f"{self.experience} {str_year}")


p1 = Person()
# Если пользователь забыл инициализировать экземпляр с именем, то заполнить пустое
p1.registration()

# Если данные присутствуют, то выводятся существующие
p1.registration()
p2 = Person("Глеб", 16)
p2.registration()

# Добавляет фамилию, если отсутствует
p2.add_full_name()
p2.registration()

p3 = Person("Татьяна Ларина", 30)
p3.add_full_name()
p3.info()

p3 = CyberSportsmen("Contra", 3)
p3.registration()
p3.info()

p4 = GameDisiner("1T-Start", 15)
p4.registration()
p4.info()
