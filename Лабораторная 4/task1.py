import doctest


class Vehicle:
    def __init__(self, max_speed: float, cost: float, number_of_passengers: int):
        """Базовый класс: 'Транспортное средство'

        :param: max_speed: максимальаня скорость, которую может развивать транспортное средство
        :param: cost: стоимость транспортного средства (в евро)
        :param: number_of_passengers: количество пассажиров, которое может вместить транспортное средство

        Примеры:
        >>> vehicle = Vehicle(230.5, 30000.0, 4)  # Инициализация экземпляров класса
        """
        if not isinstance(max_speed, float):  # Проверяем, что максимальная скорость типа float
            raise TypeError("Максимальная скорость должна быть типа float")  # Вызываем ошибку
        if max_speed < 0:
            raise ValueError('Максимальная скорость должна быть положительная')
        self.max_speed = max_speed

        if not isinstance(cost, float):  # Проверяем, что стоимость типа float
            raise TypeError("Стоимость должна быть типа float")
        if cost < 0:
            raise ValueError('Стоимость должна быть положительная')
        self.cost = cost

        if not isinstance(number_of_passengers, int):  # Проверяем, что число пассажиров типа int
            raise TypeError("Количество пассажиров должно быть типа int")
        if number_of_passengers < 0:
            raise ValueError('Количество пассажиров должно быть положительным')
        self.number_of_passengers = number_of_passengers

    def speed_control(self, speed: float) -> float:
        """ Функция, которая получает максимально допустимую на данном участке дороги скорость,
         и сравнивает ее с максимально возможной скоростью транспортного средства

        :param: speed: максимально допустимая на данном участке дороги скорость
        :return: максимально возможная скорость на дороге, исходя из ограничений на дороге и возможностей
        транспортного средства

        Примеры:
        >>> vehicle = Vehicle(230.5, 30000.0, 4)
        >>> vehicle.speed_control(120.0)
        """

        if not isinstance(speed, float):
            raise TypeError('Скорость, разрешенная на дороге, должна быть типа float')
        if speed < 0:
            raise ValueError('Скорость, разрешенная на дороге, должна быть больше нуля')
        ...

    def sell_cost(self, years: float) -> float:
        """Функция, которая вычисляет цену, за которую можно продать транспортное средство спустя время эксплуатации,
         исходя из его характеристик
         :param: years: период эксплуатации транспортного средства
         :return: стоимость транспортного средства

         Примеры:
        >>> vehicle = Vehicle(230.5, 30000.0, 4)
        >>> vehicle.sell_cost(5.0)
         """
        if not isinstance(years, float):
            raise TypeError('Период эксплуатации должен быть типа float')
        if years < 0:
            raise ValueError('Период эксплуатации должен быть больше нуля')
        ...

    def __str__(self):
        return f"Максимальная скорость: {self.max_speed}\nСтоимость: {self.cost}\n" \
               f"Количество пассажиров: {self.number_of_passengers}"

    def __repr__(self):
        return f"{self.__class__.__name__}(max_speed={self.max_speed!r}, " \
               f"cost={self.cost!r}, number_of_passengers={self.number_of_passengers!r})"


class Car(Vehicle):
    """Дочерний класс: 'Легковой автомобиль'

    :param: max_speed: максимальаня скорость, которую может развивать транспортное средство
    :param: cost: стоимость транспортного средства (в евро)
    :param: number_of_passengers: количество пассажиров, которое может вместить транспортное средство
    :param: type_of_gearbox: тип коробки передач: автоматическая (AT) или механическая (MT)
    :param: type_of_fuel: тип потребляемого топлива (petrol/diesel/electricity)

        Примеры:
        >>> car = Car(230.5, 30000.0, 4, 'AT', 'petrol')
    """
    def __init__(self, max_speed: float, cost: float, number_of_passengers: int,
                 type_of_gearbox: str, type_of_fuel: str):
        """Инициализация экземпляра класса"""
        super().__init__(max_speed, cost, number_of_passengers)
        if not isinstance(type_of_gearbox, str):
            raise TypeError('Вид коробки передач должен быть строкой')
        self.type_of_gearbox = type_of_gearbox

        if not isinstance(type_of_fuel, str):
            raise TypeError('Вид используемого топлива должен быть строкой')
        self.type_of_fuel = type_of_fuel

    def sell_cost(self, years: float, mileage: float) -> float:
        """Функция, которая вычисляет цену, за которую можно продать легковой автомобиль спустя время эксплуатации,
         исходя из его характеристик
         Метод перегружен, так как в случае легкового автомобиля необходимо учитывать больше параметров для расчета цены
         :param: years: период эксплуатации транспортного средства
         :param: mileage: пробег (км)
         :return: стоимость транспортного средства

         Примеры:
         >>> car = Car(230.5, 30000.0, 4, 'AT', 'petrol')
         >>> car.sell_cost(5.0, 90000.0)
         """
        if not isinstance(years, float):
            raise TypeError('Период эксплуатации должен быть типа float')
        if years < 0:
            raise ValueError('Период эксплуатации должен быть больше нуля')

        if not isinstance(mileage, float):
            raise TypeError('Пробег должен быть типа float')
        if mileage < 0:
            raise ValueError('Пробег должен быть больше нуля')
        ...

    def __str__(self):
        return f"Максимальная скорость: {self.max_speed}\nСтоимость: {self.cost}\n" \
               f"Количество пассажиров: {self.number_of_passengers}\nТип коробки передач: {self.type_of_gearbox}\n" \
               f"Тип потребляемого топлива: {self.type_of_fuel}"

    def __repr__(self):
        return f"{self.__class__.__name__}(max_speed={self.max_speed!r}, cost={self.cost!r}," \
               f" number_of_passengers={self.number_of_passengers!r}, type_of_gearbox={self.type_of_gearbox!r} " \
               f"type_of_fuel={self.type_of_fuel!r})"


class Bike(Vehicle):
    """ Дочерний класс: 'Велосипед'

        :param: max_speed: максимальаня скорость, которую может развивать транспортное средство
        :param: cost: стоимость транспортного средства (в евро)
        :param: number_of_passengers: количество пассажиров, которое может вместить транспортное средство
        :param: number_of_wheels: количество колес у велосипеда
        :param: road_type: дорога, для которой предназначен велосипед (mountain/highway)

        Примеры:
        >>> bike = Bike(50.0, 500.0, 1, 2, 'highway')
    """
    def __init__(self, max_speed: float, cost: float, number_of_passengers: int, number_of_wheels: int, road_type: str):
        """Инициализация экземпляра класса"""
        super().__init__(max_speed, cost, number_of_passengers)

        if not isinstance(number_of_wheels, int):
            raise TypeError('Количество колес у велосипеда должно быть типа int')
        if number_of_wheels < 0:
            raise ValueError('Количество колес у велосипеда должно быть положительным числом')
        self.number_of_wheels = number_of_wheels

        if not isinstance(road_type, str):
            raise TypeError('Тип дороги, для которого предназначен велосипед, должен быть строкой')
        self.road_type = road_type

    def sell_cost(self, years: float, frame: float) -> float:
        """Функция, которая вычисляет цену, за которую можно продать велосипед спустя время эксплуатации,
         исходя из его характеристик
         Метод перегружен, так как в случае велосипеда необходимо учитывать больше параметров для расчета цены
         :param: years: период эксплуатации транспортного средства
         :param: frame: состояние рамы велосипеда (оценка повреждений по шкале 1-10)
         :return: стоимость транспортного средства

         Примеры:
         >>> bike = Bike(50.0, 500.0, 1, 2, 'highway')
         >>> bike.sell_cost(2.0, 8.0)
         """
        if not isinstance(years, float):
            raise TypeError('Период эксплуатации должен быть типа float')
        if years < 0:
            raise ValueError('Период эксплуатации должен быть больше нуля')

        if not isinstance(frame, float):
            raise TypeError('Оценка рамы должна быть типа float')
        if frame < 0:
            raise ValueError('Оценка рамы должна быть больше нуля')
        ...

    def __str__(self):
        return f"Максимальная скорость: {self.max_speed}\nСтоимость: {self.cost}\n" \
               f"Количество пассажиров: {self.number_of_passengers}\nКоличество колес: {self.number_of_wheels}\n" \
               f"Тип дороги: {self.road_type}"

    def __repr__(self):
        return f"{self.__class__.__name__}(max_speed={self.max_speed!r}, cost={self.cost!r}," \
               f" number_of_passengers={self.number_of_passengers!r}, number_of_wheels={self.number_of_wheels!r}," \
               f"road_type={self.road_type!r})"


if __name__ == "__main__":
    bike = Bike(50.0, 500.0, 1, 2, 'highway')
    doctest.testmod()
    pass
