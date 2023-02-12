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
        super().__init__(max_speed, cost, number_of_passengers)
        if not isinstance(type_of_gearbox, str):
            raise TypeError('Вид коробки передач должен быть строкой')
        self.type_of_gearbox = type_of_gearbox

        if not isinstance(type_of_fuel, str):
            raise TypeError('Вид используемого топлива должен быть строкой')
        self.type_of_fuel = type_of_fuel

    def refueling(self, fuel: str) -> str:
        """ Функция, которая принимает тип топлива, который есть на заправке и возвращает ответ, подходит ли это топливо
         для данной машины

        :param: fuel: тип топлива на заправке
        :return: подходит ли эта заправка для данной машины

        Примеры:
        >>> car = Car(230.5, 30000.0, 4, 'AT', 'petrol')
        >>> car.refueling('petrol')
        """

        if not isinstance(fuel, str):
            raise TypeError('название топлива на заправке должно быть типа str')
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
        super().__init__(max_speed, cost, number_of_passengers)

        if not isinstance(number_of_wheels, int):
            raise TypeError('Количество колес у велосипеда должно быть типа int')
        if number_of_wheels < 0:
            raise ValueError('Количество колес у велосипеда должно быть положительным числом')
        self.number_of_wheels = number_of_wheels

        if not isinstance(road_type, str):
            raise TypeError('Тип дороги, для которого предназначен велосипед, должен быть строкой')
        self.road_type = road_type

    def __str__(self):
        return f"Максимальная скорость: {self.max_speed}\nСтоимость: {self.cost}\n" \
               f"Количество пассажиров: {self.number_of_passengers}\nКоличество колес: {self.number_of_wheels}\n" \
               f"Тип дороги: {self.road_type}"

    def __repr__(self):
        return f"{self.__class__.__name__}(max_speed={self.max_speed!r}, cost={self.cost!r}," \
               f" number_of_passengers={self.number_of_passengers!r}, number_of_wheels={self.number_of_wheels!r}," \
               f"road_type={self.road_type!r})"


if __name__ == "__main__":
    doctest.testmod()
    pass
