# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Book:
    """
    Класс, описывающий книгу.
    """
    def __init__(self, title: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц в книге

        Примеры:
        >>> book = Book("Война и мир", "Лев Толстой", 1225)
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if len(title) == 0:
            raise ValueError("Название книги не может быть пустой строкой")
        self.title = title

        if not isinstance(author, str):
            raise TypeError("Имя автора должно быть строкой")
        if len(author) == 0:
            raise ValueError("Имя автора не может быть пустой строкой")
        self.author = author

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

    def get_reading_time(self, pages_per_hour: int) -> float:
        """
        Расчет времени чтения книги.

        :param pages_per_hour: Количество страниц, которые читатель может прочитать за час
        :return: Время чтения книги в часах

        Примеры:
        >>> book = Book("Война и мир", "Лев Толстой", 1225)
        >>> book.get_reading_time(50)
        """
        if not isinstance(pages_per_hour, int):
            raise TypeError("Скорость чтения должна быть целым числом")
        if pages_per_hour <= 0:
            raise ValueError("Скорость чтения должна быть положительной")

    def is_thick_book(self) -> bool:
        """
        Проверка, является ли книга толстой.
        Считается, что книга толстая, если в ней более 500 страниц.

        :return: True если книга толстая, False в противном случае

        Примеры:
        >>> book = Book("Война и мир", "Лев Толстой", 1225)
        >>> book.is_thick_book()
        """
        ...

    def get_book_info(self) -> str:
        """
        Получение информации о книге в виде строки.

        :return: Строка с информацией о книге

        Примеры:
        >>> book = Book("Война и мир", "Лев Толстой", 1225)
        >>> book.get_book_info()
        """
        ...


class Smartphone:
    """
    Класс, описывающий смартфон.
    """
    def __init__(self, brand: str, model: str, battery_capacity: int):
        """
        Создание и подготовка к работе объекта "Смартфон"

        :param brand: Бренд смартфона
        :param model: Модель смартфона
        :param battery_capacity: Емкость аккумулятора в мАч

        Примеры:
        >>> phone = Smartphone("Apple", "iPhone 14", 3279)
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой")
        if len(brand) == 0:
            raise ValueError("Бренд не может быть пустой строкой")
        self.brand = brand

        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой")
        if len(model) == 0:
            raise ValueError("Модель не может быть пустой строкой")
        self.model = model

        if not isinstance(battery_capacity, int):
            raise TypeError("Емкость аккумулятора должна быть целым числом")
        if battery_capacity <= 0:
            raise ValueError("Емкость аккумулятора должна быть положительным числом")
        self.battery_capacity = battery_capacity

    def calculate_battery_life(self, power_consumption: float) -> float:
        """
        Расчет времени работы аккумулятора.

        :param power_consumption: Потребляемая мощность в мАч/час
        :return: Время работы в часах

        Примеры:
        >>> phone = Smartphone("Apple", "iPhone 14", 3279)
        >>> phone.calculate_battery_life(150)
        """
        if not isinstance(power_consumption, (int, float)):
            raise TypeError("Потребляемая мощность должна быть числом")
        if power_consumption <= 0:
            raise ValueError("Потребляемая мощность должна быть положительной")

    def get_full_name(self) -> str:
        """
        Получение полного названия смартфона.

        :return: Полное название в формате "Бренд Модель"

        Примеры:
        >>> phone = Smartphone("Apple", "iPhone 14", 3279)
        >>> phone.get_full_name()
        """
        ...

    def is_battery_capacity_high(self) -> bool:
        """
        Проверка, является ли емкость аккумулятора высокой.
        Считается высокой емкость более 4000 мАч.

        :return: True если емкость высокая, False в противном случае

        Примеры:
        >>> phone = Smartphone("Apple", "iPhone 14", 3279)
        >>> phone.is_battery_capacity_high()
        """
        ...


class Triangle:
    """
    Класс, описывающий треугольник.
    """
    def __init__(self, side_a: float, side_b: float, side_c: float):
        """
        Создание и подготовка к работе объекта "Треугольник"

        :param side_a: Длина стороны A
        :param side_b: Длина стороны B
        :param side_c: Длина стороны C

        Примеры:
        >>> triangle = Triangle(3, 4, 5)
        """
        for side, value in [("A", side_a), ("B", side_b), ("C", side_c)]:
            if not isinstance(value, (int, float)):
                raise TypeError(f"Сторона {side} должна быть числом")
            if value <= 0:
                raise ValueError(f"Сторона {side} должна быть положительным числом")

        # Проверка неравенства треугольника
        if (side_a + side_b <= side_c or
            side_a + side_c <= side_b or
            side_b + side_c <= side_a):
            raise ValueError("Треугольник с такими сторонами не существует")

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def calculate_perimeter(self) -> float:
        """
        Расчет периметра треугольника.

        :return: Периметр треугольника

        Примеры:
        >>> triangle = Triangle(3, 4, 5)
        >>> triangle.calculate_perimeter()
        """
        ...

    def calculate_area(self) -> float:
        """
        Расчет площади треугольника по формуле Герона.

        :return: Площадь треугольника

        Примеры:
        >>> triangle = Triangle(3, 4, 5)
        >>> triangle.calculate_area()
        """
        ...

    def is_right_triangle(self) -> bool:
        """
        Проверка, является ли треугольник прямоугольным.

        :return: True если треугольник прямоугольный, False в противном случае

        Примеры:
        >>> triangle = Triangle(3, 4, 5)
        >>> triangle.is_right_triangle()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()

    # TODO работоспособность экземпляров класса проверить с помощью doctest

