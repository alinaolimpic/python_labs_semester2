from abc import ABC, abstractmethod


class Printable(ABC):
    """Интерфейс для вывода"""

    @abstractmethod
    def to_string(self) -> str:
        pass


class Comparable(ABC):
    """Интерфейс для сравнения"""

    @abstractmethod
    def compare_to(self, other) -> int:
        """
        Возвращает:
        < 0 если меньше
        0 если равны
        > 0 если больше
        """
        pass