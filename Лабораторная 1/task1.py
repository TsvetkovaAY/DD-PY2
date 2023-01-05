# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class House:
    def __init__(self, year_of_build: int, length: (int, float), width: (int, float), ceiling_height: (int, float)):
        """
        Создание и подготовка к работе объекта "Дом"

        :param year_of_build: Год постройки дома
        :param length: длина дома
        :param width: ширина дома
        :param ceiling_height: высота потлка в доме

        Примеры:
        >>> house = House(2000, 20, 10, 5)  # Инициализация экземпляра класса
        """

        if not isinstance(year_of_build, int):
            raise TypeError('Год постройки должен быть типа int')
        if year_of_build <= 0:
            raise ValueError('Год постройки должен быть положительным числом')
        self.year_of_build = year_of_build

        if not isinstance(length, (int, float)):
            raise TypeError('Длина дома должна быть типа int или типа float')
        if length <= 0:
            raise ValueError('Длина дома должна быть положительным числом')
        self.length = length

        if not isinstance(width, (int, float)):
            raise TypeError('Ширина дома должна быть типа int или типа float')
        if width <= 0:
            raise ValueError('Ширина дома должна быть положительным числом')
        self.width = width

        if not isinstance(ceiling_height, (int, float)):
            raise TypeError('Высота потолков в доме должна быть типа int или типа float')
        if ceiling_height <= 0:
            raise ValueError('Высота потолков в доме должна быть положительным числом')
        self.ceiling_height = ceiling_height

    def age_of_house(self, year: int) -> int:
        """
        Функция, которая вычисляет, сколько лет дому исполнилось в 2022
        :param year: Текущий год
        :raise ValueError: Если год постройки больше текущего года, то возвращается ошибка
        :return: Возраст дома

        Примеры:
        >>> house = House(2000, 20, 10, 5)
        >>> house.age_of_house(2022)
        """
        if not isinstance(year, int):
            raise TypeError('Текущий год должен быть типа int')
        if year <= 0:
            raise ValueError('Текущий год должен быть положительным числом')
        ...

    def square(self) -> (int, float):
        """
        Функция, вычисляющая площадь дома
        :return: Площадь дома

        Примеры:
        >>> house = House(2000, 20, 10, 5)
        >>> house.square()
        """
        ...

    def ceiling_norm(self, std_height: (int, float)) -> bool:
        """
        Функция, проверяющая, соответвует ли высота потолка строительным нормам
        :param std_height: допустимая минимальная высота потолка
        :raise ValueError: Если высота потолка меньше минимальной допустимой высоты
        :return: Удовлетворяет ли высота строительным нормам

        Примеры:
        >>> house = House(2000, 20, 10, 5)
        >>> house.ceiling_norm(3)
        """
        if not isinstance(std_height, (int, float)):
            raise TypeError('Допустимая минимальная высота потолка должна быть типа int или float')
        if std_height <= 0:
            raise ValueError('Допустимая минимальная высота потолка должна быть положительным числом')
        ...


class Human:
    def __init__(self, name: str, year_of_birth: int):
        """
        Создание и подготовка к работе объекта "Человек"
        :param name: Имя человека
        :param year_of_birth: Год рождения

        Примеры:
        >>> human = Human('Anna', 2002)  # Инициализация экземпляра класса
        """

        if not isinstance(name, str):
            raise TypeError('Имя человека должно быть типа str')
        self.name = name

        if not isinstance(year_of_birth, int):
            raise TypeError('Год рождения должен быть типа int')
        if year_of_birth <= 0:
            raise ValueError('Год рождения должен быть положительным числом')
        self.year_of_birth = year_of_birth

    def human_surname(self, surname: str) -> str:
        """
        Функция, добавляющая к имени человека фамилию
        :param surname: Фамилия человека
        :return: Полное имя человека: имя и фамилия

        Примеры:
        >>> human = Human('Anna', 2002)
        >>> human.human_surname('Tsvetkova')
        """
        if not isinstance(surname, str):
            raise TypeError('Фамилия человека должна быть типа str')
        ...
    def human_age(self, year: int) -> int:
        """
        Функция, вычисляющая возраст человека
        :param year: Текущий год
        :return: Возраст человека

        Примеры:
        >>> human = Human('Anna', 2002)
        >>> human.human_age(2022)
        """
        if not isinstance(year, int):
            raise TypeError('Текущий год должен быть типа int')
        if year <= 0:
            raise ValueError('Текущий год должен быть положительным числом')
        ...


class Lamp:
    def __init__(self, condition: str, color: str, price: (int, float)):
        """
        Создание и подготовка к работе объекта "Лампа"

        :param condition: Состояние лампы: включена/выключена (on/off)
        :param color: Цветовой режим лампы
        :param price: Цена лампы

        Примеры:
        >>> lamp = Lamp('on', 'red', 10)  # инициализация экземпляра класса
        """
        if not isinstance(condition, str):
            raise TypeError('Состояние лампы должно быть типа str')
        self.condition = condition

        if not isinstance(color, str):
            raise TypeError('Цвет лампы должен быть типа str')
        self.color = color

        if not isinstance(price, (int, float)):
            raise TypeError('Цена лампы должна быть типа int или float')
        if price <= 0:
            raise ValueError('Цена лампы должна быть положительным числом')
        self.price = price

    def is_lamp_on(self) -> bool:
        """
        Функция, проверяющая, включена ли лампа
        :return: Является ли лампа включенной

        Примеры:
        >>> lamp = Lamp('on', 'red', 10)
        >>> lamp.is_lamp_on()
        """
        ...

    def change_color(self, new_color: str) -> str:
        """
        Функция, меняющая цветовой режим лампы

        :param new_color: новый цвет свечения лампы
        :raise ValueError: Если цвет лампы не поменялся, вызываем ошибку
        :return: Новый цвет лампы

        Примеры:
        >>> lamp = Lamp('on', 'red', 10)
        >>> lamp.change_color('green')
        """
        if not isinstance(new_color, str):
            raise TypeError('Новый цветовой режим лампы должен быть типа str')
        ...

    def set_lamp_discount(self, discount: (int, float)) -> (int, float):
        """
        Функция, вычисляющая новую цену лампы

        :param discount: Размер скидки в процентах
        :return: Новая цена лампы

        Примеры:
        >>> lamp = Lamp('on', 'red', 10)
        >>> lamp.set_lamp_discount(50)
        """
        if not isinstance(discount, (int, float)):
            raise TypeError('Скидка на лампу должна быть типа int или float')
        if discount > 100 or discount < 1:
            raise ValueError('Скидка на лампу не должнв быть меньше 1% или больше 100%')
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
