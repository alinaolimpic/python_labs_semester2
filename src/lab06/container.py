from typing import TypeVar, Generic, Callable, Optional, Protocol

# ===== БАЗОВЫЕ TYPEVAR =====
T = TypeVar('T')
R = TypeVar('R')


# ===== PROTOCOL =====

class Displayable(Protocol):
    def display(self) -> str:
        ...


class Scorable(Protocol):
    def score(self) -> float:
        ...


# Ограниченные типы
D = TypeVar('D', bound=Displayable)
S = TypeVar('S', bound=Scorable)


# ===== GENERIC КОЛЛЕКЦИЯ =====

class TypedCollection(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def add(self, item: T) -> None:
        self._items.append(item)

    def remove(self, item: T) -> None:
        self._items.remove(item)

    def get_all(self) -> list[T]:
        return list(self._items)

   

    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for item in self._items:
            if predicate(item):
                return item
        return None

    def filter(self, predicate: Callable[[T], bool]) -> list[T]:
        return [item for item in self._items if predicate(item)]

    def map(self, transform: Callable[[T], R]) -> list[R]:
        return [transform(item) for item in self._items]


# КОЛЛЕКЦИЯ С ПРОТОКОЛОМ 

class DisplayCollection(TypedCollection[D]):
    def show_all(self) -> None:
        for item in self._items:
            print(item.display())


class ScoreCollection(TypedCollection[S]):
    def get_scores(self) -> list[float]:
        return [item.score() for item in self._items]