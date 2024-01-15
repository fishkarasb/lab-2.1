class Building:
    def __init__(self, number_of_apartments: int, number_of_residents: int):
        """
        Создание и подготовка к работе объекта "Здание"

        :param number_of_apartments: Количество квартир
        :param number_of_residents: Количество жильцов

        Примеры:
        >>> building = Building(500, 800)
        """
        if not isinstance(number_of_apartments, int):
            raise TypeError("Количество квартир должно быть int")
        if number_of_apartments <= 0:
            raise ValueError("Количество квартир должно быть положительным числом")
        self.number_of_apartments = number_of_apartments

        if not isinstance(number_of_residents, int):
            raise TypeError("Количество жильцов должно быть int")
        if number_of_residents < 0:
            raise ValueError("Количество жильцов не может быть отрицательным числом")
        if number_of_residents <= number_of_apartments:
            raise ValueError("Количество жильцов должно быть больше или равно количеству квартир")
        self.number_of_residents = number_of_residents

    def remove_resident_from_building(self, homeless: int) -> None:
        """
        Выселение жильцов из здания.

        :param homeless: Количество выселенцов
        :raise ValueError: Если количество выселяемых людей больше чем живёт в доме,
        то возвращается ошибка.

        :return: количество ревльно выселеных людей

        Примеры:
        >>> building = Building(500, 700)
        >>> building.remove_resident_from_building(200)
        """
        if not isinstance(homeless, int):
            raise TypeError("Выселяемые жильцы должны быть типа int")
        if homeless < 0:
            raise ValueError("Выселяемые жильцы должны положительным числом")
        ...

    def add_resident_to_building(self, resident: int) -> None:
        """
        Заселение жильцов в здание.
        :param resident: количество заселяемых людей

        Примеры:
        >>> building = Building(500, 800)
        >>> building.add_resident_to_building(200)
        """
        if not isinstance(resident, int):
            raise TypeError("Добавляемые жильцы должны быть типа int")
        if resident < 0:
            raise ValueError("Добавляемые жильцы должны положительным числом")
        ...


class Bouquet:
    def __init__(self, number_of_leaves: int, number_of_buds: int):
        """
        Создание и подготовка к работе объекта "Букет"

        :param number_of_leaves: Количество листочков
        :param number_of_buds: Количество бутнов

        Примеры:
        >>> bouquet = Bouquet(75, 25)
        """
        if not isinstance(number_of_leaves, int):
            raise TypeError("Количество листочков должно быть int")
        if number_of_leaves <= 0:
            raise ValueError("Количество листочков должно быть положительным числом")
        self.number_of_leaves = number_of_leaves

        if not isinstance(number_of_buds, int):
            raise TypeError("Количество бутонов должно быть int")
        if number_of_buds <= 0:
            raise ValueError("Количество бутонов не может быть отрицательным числом")
        self.number_of_buds = number_of_buds

    def price_per_bud(self, price: float) -> None:
        """
        Расчёт цены за букет.

        :param price: цена за один бутон
        :return: цена за букет

        Примеры:
        >>> bouquet = Bouquet(75, 25)
        >>> bouquet.price_per_bud(80)
        """
        if not isinstance(price, (int, float)):
            raise TypeError("Цена за бутон долна быть типа int или float")
        if price < 0:
            raise ValueError("Цена за бутон долна быть положительным числом")
        ...

    def add_other_flowers_to_bouquet(self, flowers: int) -> None:
        """
        Добовление других цветов в букет.
        :param flowers: количество добовляемых цветов

        Примеры:
        >>> bouquet = Bouquet(75, 25)
        >>> bouquet.add_other_flowers_to_bouquet(35)
        """
        if not isinstance(flowers, int):
            raise TypeError("Добавляемые цветы должны быть типа int")
        if flowers < 0:
            raise ValueError("Добавляемые цветы должны быть положительным числом")
        ...


class Hair:
    def __init__(self, hair_density: int, hair_length: float):
        """
        Создание и подготовка к работе объекта "Волосы"

        :param hair_density: Количестов волос на голове
        :param hair_length: Длина волос на голове

        Примеры:
        >>> hair = Hair(90000, 27.5)
        """
        if not isinstance(hair_density, int):
            raise TypeError("Количество волос должно быть int")
        if hair_density <= 0:
            raise ValueError("Количество волос должно быть положительным числом")
        self.hair_density = hair_density

        if not isinstance(hair_length, (int, float)):
            raise TypeError("Длина волос должна быть int или float")
        if hair_length <= 0:
            raise ValueError("Длина волос не может быть отрицательным числом")
        self.hair_length = hair_length

    def haircut(self, length: int) -> None:
        """
        Стрижка.

        :param length: Длина на которую укорачивают волосы
        :raise ValueError: Если длина на которую укорачивают волосы больше чем длина до стрижки,
        то возвращается ошибка.

        :return: длина волос

        Примеры:
        >>> hair = Hair(90000, 27.5)
        >>> hair.haircut(15)
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина на которую укорачивают волосы должна быть int или float")
        if length < 0:
            raise ValueError("Длина на которую укорачивают волосы должна положительным числом")
        ...

    def hair_transplant(self, number_of_hairs: int) -> None:
        """
        Пересадка волос.
        :param number_of_hairs: количество пересаживаемы волос

        Примеры:
        >>> hair = Hair(90000, 27.5)
        >>> hair.hair_transplant(20000)
        """
        if not isinstance(number_of_hairs, int):
            raise TypeError("Количество пересаживаемых волос должно быть типа int")
        if number_of_hairs < 0:
            raise ValueError("Количество пересаживаемых волос должно быть положительным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()
