class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
         self._name = name
         self._author = author
    @property
    def name(self):
        return self._name
    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга: {self.name}\nАвтор: {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Бумажная книга """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError('Количество страниц должно быть типа int')
        if pages > 0:
            self.pages = pages
        else:
            raise ValueError('Количество страниц - положительное число')

    def __str__(self):
        return f"Книга: {self.name}\nАвтор: {self.author}\nКоличество страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """ Аудиокнига """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)

        if not isinstance(duration, float):
            raise TypeError('Продолжительность аудиокниги должна быть типа float')
        if duration > 0:
            self.duration = duration
        else:
            raise ValueError('Продолжительность аудиокниги - положительное число')

    def __str__(self):
        return f"Книга: {self.name}\nАвтор: {self.author}\nПродолжительность аудиокниги: {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


