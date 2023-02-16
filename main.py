class Auto:
    """
    Подготовка к работе класса "Auto"
    """
    def __init__(self, power: int, volume: float, fuel_type: str, carrying: int):
        """
        Конструктор класса "Auto"
        :param power: Мощность
        :param volume: Объем двигателя
        :param fuel_type: Тип топлива
        :param carrying: Грузоподъемность
        """
        self.power = power
        self.volume = volume
        self.fuel_type = fuel_type
        self.carrying = carrying

    def __str__(self) -> str:
        """
        Содержит в себе информацию о машине
        """
        return f'Автомобиль мощностью {self.power} лошадиных сил, объемом двигателя {self.volume} л. и типом топлива {self.fuel_type} грузоподъемностью {self.carrying} кг'

    def __repr__(self) -> str:
        """
        Возвращает валидную Python-строку для данного класа "Auto"
        """
        return f'{self.__class__.__name__}(power={self.power}, volume={self.volume}, fuel_type={self.fuel_type!r}, carrying={self.carrying})'

    def loading_auto(self,  weigth: int) -> str:
        """
        3агрузка автомобиля
        :param weigth: Масса груза
        """
        if weigth > self.carrying:
            return f'Грузоподъемность превышена , смените автомобиль на грузовой!!!'
        return f'Машина загружена!'

    def start_auto(self) -> None:
        """
        Запуск автомобиля
        """
        ...

class Truck(Auto):
    """
    Подготовка к работе дочернего класса "Truck"
    """
    def __init__(self, power: int, volume: float, fuel_type: str, carrying: int):
        """
        Конструктор дочернего класса, унаследует все аргументы базового класса. Новых не имеет.
        """
        super().__init__(power, volume, fuel_type, carrying)

    def __str__(self) -> str:
        """
        Был перегружен магический метод __str__ из-за другой информации
        """
        return f'Грузовой автомобиль мощностью {self.power} лошадиных сил, объемом двигателя {self.volume} л. и типом топлива {self.fuel_type} грузоподъемностью {self.carrying} кг'

    def loading_auto(self,  weigth) -> str:
        """
        Метод "loading_auto" был перегружен из-за другого вида информации, которая ведет к другому решению.
        """
        if weigth > self.carrying:
            return f'Эта машина не подходит для транспортировки этого груза!!!'
        return f'Машина загружена!'


if __name__== "__main__":

    pass
