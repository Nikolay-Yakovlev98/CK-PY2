import doctest


class Car:
    def __init__(self, type_fuel: str, color: str, horse_power: int):
        """
         Создание и подготовка к работе объекта "Машина"

        :param type_fuel: Тип топлива
        :param color: Цвет
        :param horse_power: Мощность

        Пример:
        >>> car1 = Car("diesel", "Blue", 123)
        """
        if not isinstance(type_fuel, str):
            raise TypeError('Не тот тип данных')
        self.type_fuel = type_fuel
        if not isinstance(color, str):
            raise TypeError('Не тот тип данных')
        self.color = color

        if not isinstance(horse_power, int):
            raise TypeError('Не тот тип данных')
        if horse_power <= 0:
            raise ValueError('Отрицательное число')
        self.horse_power = horse_power

    def on_headlight(self) -> None:
        """
        Включение фар
        """
        ...

    def open_car(self) -> None:
        """
        Открыть машину
        """
        ...


class Phone:
    def __init__(self, model: str, color: str, price: int):
        """
        Создание и подготовка к работе объекта "Телефон"

        :param model: Модель
        :param color: Цвет
        :param price: Цена

         Пример:
        >>> phone1 = Phone("IPhone", "Black", 1000)
        """
        if not isinstance(model, str):
            raise TypeError('Не тот тип данных')
        self.model = model
        if not isinstance(color, str):
            raise TypeError('Не тот тип данных')
        self.color = color

        if not isinstance(price, int):
            raise TypeError('Не тот тип данных')
        if price <= 0:
            raise ValueError('Отрицательное число')
        self.price = price

    def call_phone(self) -> None:
        """
        Звонить по телефону
        """
        ...

    def charging(self) -> None:
        """
        Зарядка телефона
        """
        ...


class Ball:
    def __init__(self, year: int, name: str, weight: int):
        """
        Создание и подготовка к работе объекта "Мяч"

        :param year: Год выпуска
        :param name: Название
        :param weight: Вес

         Пример:
        >>> ball1 = Ball(2014, "Jabulani", 100)
        """
        if not isinstance(year, int):
            raise TypeError('Не тот тип данных')
        if year <= 0:
            raise ValueError('Не тод год')
        self.year = year
        if not isinstance(name, str):
            raise TypeError('Не тот тип данных')
        self.name = name

        if not isinstance(weight, int):
            raise TypeError('Не тот тип данных')
        if weight <= 0:
            raise ValueError('Отрицательное число')
        self.weight = weight

    def hit_ball(self) -> None:
        """
        Удар
        """
        ...

    def swing_ball(self) -> None:
        """
        Накачать мяч
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
