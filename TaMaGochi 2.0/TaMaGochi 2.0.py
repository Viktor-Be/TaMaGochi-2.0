from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, sex, type1):
        pass

    @abstractmethod
    def Day(self):
        pass

    def AutomaticDay(self):
        pass

    def Sleap(self):
        pass

    def Active(self):
        pass

    def Eat(self):
        pass

    def Wash(self):
        pass


class Dog(Animal):
    def __init__(self, name, sex, type1):
        super().__init__(name, sex, type1)
        self.name = name
        self.type1 = type1
        self.sex = sex
        self.weight = 0.500
        self.emotion = 0

    def Day(self):

        time = int(input("Введите который сейчас час:"))
        if time in range(9,10) or time in range(14,16) or time in range(19,22):
            self.Active()
        elif time in range(10,11) or time in range(13,14) or time in range(18,19):
            self.Eat()
        elif time in range(11,13) or time in range(16,18) or time in range(0,9):
            self.Sleap()
        elif time in range(22,25):
            self.Wash()
        elif self.weight <= 0.300:
            print("Game over")

    def AutomaticDay(self):
        for time in range(0, 25):
            time += 1
            if time in range(9, 10) or time in range(14, 16) or time in range(19, 22):
                self.Active()
            elif time in range(10, 11) or time in range(13, 14) or time in range(18, 19):
                self.Eat()
            elif time in range(11, 13) or time in range(16, 18) or time in range(0, 9):
                self.Sleap()
            elif time in range(22, 25):
                self.Wash()
            elif self.weight <= 0.300:
                print("Game over")

    def Sleap(self):
        print(f"{self.name} сейчас спит.")

    def Active(self):
        acticiti = int(input(f"Как вы будете гулять с {self.name}:\n1.Гулять на улице\n2.Гулять с "
                             f"игрушкой\n3.Дресеровать\n4.Не гулять с питомцем."))
        if acticiti == 1:
            self.emotion += 3
            self.weight -= 0.050
            self.info_emotion()
            self.info_weight()
            self.Deth()
        elif acticiti == 2:
            self.emotion += 2
            self.weight -= 0.025
            self.info_emotion()
            self.info_weight()
            self.Deth()
        elif acticiti == 3:
            self.emotion += 1
            self.info_emotion()
            self.info_weight()
        elif acticiti == 4:
            self.emotion -= 2
            self.weight += 0.050
            self.info_emotion()
            self.info_weight()

    def Eat(self):
        eat = input(f"Выберите что будет есть {self.name}:Мясо,Рыба,Сухой корм,Корм,Каша,Вода:")
        yes_eat = ["Мясо", "Рыба", "Корм"]
        no_eat = ["Сухой корм", "Корм", "Каша"]
        if eat in yes_eat:
            self.emotion += 1
            self.weight += 0.100
            self.info_emotion()
            self.info_weight()
        elif eat in no_eat:
            self.emotion -= 1
            self.weight += 0.050
            self.info_emotion()
            self.info_weight()
        elif eat == "Вода":
            self.emotion += 1
            self.weight -= 0.050
            self.info_emotion()
            self.info_weight()
            self.Deth()

    def Wash(self):
        wash = int(input(f"Вберете как будете ухаживать за {self.name}:"
                         f"1.Помыть"
                         f"2.Расчесать"
                         f"3.Ничего не делать"))
        if wash == 1:
            self.emotion += 1
            self.info_emotion()
        elif wash == 2:
            self.emotion += 2
            self.info_emotion()
        elif wash == 3:
            self.emotion -= 3
            self.info_emotion()

    def info_emotion(self):
        print(f"Настроение вашего питомца - {self.emotion}")

    def info_weight(self):
        print(f"Вес вашего питомца - {self.weight}")

    def Info(self):
        print(f"Ваш питомец {self.type1},{self.sex} по имени {self.name}")

    def Deth(self):
        if self.weight > 0.300:
            pass
        elif self.weight <= 0.300:
            print("Ваш питомец умер :(")




class Cat(Animal):
    def __init__(self, name, sex, type1):
        super().__init__(name, sex, type1)
        self.name = name
        self.type1 = type1
        self.sex = sex
        self.weight = 0.300
        self.emotion = 0

    def Day(self):
        for time in range(0,25):
            time = int(input("Введите который сейчас час:"))
            if time in range(9,10) or time in range(14,16) or time in range(19,22):
                self.Active()
            elif time in range(10,11) or time in range(13,14) or time in range(18,19):
                self.Eat()
            elif time in range(11,13) or time in range(16,18) or time in range(0,9):
                self.Sleap()
            elif time in range(22,25):
                self.Wash()
            elif self.weight <= 0.200:
                print("Game over")

    def AutomaticDay(self):
        for time in range(0, 25):
            time += 1
            if time in range(9, 10) or time in range(14, 16) or time in range(19, 22):
                self.Active()
            elif time in range(10, 11) or time in range(13, 14) or time in range(18, 19):
                self.Eat()
            elif time in range(11, 13) or time in range(16, 18) or time in range(0, 9):
                self.Sleap()
            elif time in range(22, 25):
                self.Wash()
            elif self.weight <= 0.200:
                print("Game over")

    def Sleap(self):
        print(f"{self.name} сейчас спит.")

    def Active(self):
        acticiti = int(input(f"Как вы будете гулять с {self.name}:\n1.Гулять с лазерной указкой\n2.Гулять с "
                             f"игрушкой\n3.Не гулять с питомцем."))
        if acticiti == 1:
            self.emotion += 3
            self.weight -= 0.050
            self.info_emotion()
            self.info_weight()
            self.Deth()
        elif acticiti == 2:
            self.emotion += 2
            self.weight -= 0.025
            self.Deth()
            self.info_emotion()
            self.info_weight()
        elif acticiti == 3:
            self.emotion -= 2
            self.weight += 0.050
            self.info_emotion()
            self.info_weight()

    def Eat(self):
        eat = input(f"Выберите что будет есть {self.name}:Мясо,Рыба,Сухой корм,Корм,Каша,Вода:")
        yes_eat = ["Мясо", "Рыба", "Корм"]
        no_eat = ["Сухой корм", "Корм", "Каша"]
        if eat in yes_eat:
            self.emotion += 1
            self.weight += 0.100
            self.info_emotion()
            self.info_weight()
        elif eat in no_eat:
            self.emotion -= 1
            self.weight += 0.050
            self.info_emotion()
            self.info_weight()
        elif eat == "Вода":
            self.emotion += 1
            self.weight -= 0.050
            self.info_emotion()
            self.info_weight()
            self.Deth()

    def Wash(self):
        wash = int(input(f"Вберете как будете ухаживать за {self.name}:"
                         f"1.Помыть"
                         f"2.Расчесать"
                         f"3.Ничего не делать"))
        if wash == 1:
            self.emotion += 1
            self.info_emotion()
        elif wash == 2:
            self.emotion += 2
            self.info_emotion()
        elif wash == 3:
            self.emotion -= 3
            self.info_emotion()

    def info_emotion(self):
        print(f"Настроение вашего питомца - {self.emotion}")

    def info_weight(self):
        print(f"Вес вашего питомца - {self.weight}")

    def Info(self):
        print(f"Ваш питомец {self.type1},{self.sex} по имени {self.name}")

    def Deth(self):
        if self.weight > 0.200:
            pass
        elif self.weight <= 0.200:
            print("Ваш питомец умер :(")

def Menu():
    type1=""
    sex = ""
    while sex != "Мальчик" and sex != "Девочка":
        sex = int(input("Выберете пол питомца:\n1.Мальчик\n2.Девочка\n"))
        if sex == 1:
            sex = "Мальчик"
        elif sex == 2:
            sex = "Девочка"

    name = input("Введите имя питомца:")
    Dog1 = Dog(name,type1,sex)
    Cat1 = Cat(name, type1, sex)
    while type1 != "Собака" and type1 != "Кот":
        type1 = int(input("""Выберете питомца:
            1.Собака
            2.Кот
            """))
        if type1 == 1:
            type1 = "Собака"
            game = int(input("Выберите режим игры:\n1.Автоматический.\n2.Ручной.\n:"))
            if game == 1:
                Dog1.AutomaticDay()
            elif game == 2:
                Dog1.Day()
        elif type1 == 2:
            type1 = "Кот"
            game=int(input("Выберите режим игры:\n1.Автоматический.\n2.Ручной.\n:"))
            if game == 1:
                Cat1.AutomaticDay()
            elif game == 2:
                Cat1.Day()

Menu()