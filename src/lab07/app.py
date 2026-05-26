from typing import List

from lab05.collection05 import AdvancedBusCollection
from lab03.models import CityBus, TouristBus, ElectricBus
from lab02.model import Bus

from lab07.exceptions import BusNotFoundError, DuplicateBusError
from lab07.storage import save_buses, load_buses


class BusApp:
    """Бизнес-логика приложения."""

    def __init__(self) -> None:
        self.collection = AdvancedBusCollection()
        self._load()

    def _load(self) -> None:
        """Автозагрузка данных."""
        buses = load_buses()

        for bus in buses:
            self.collection.add(bus)

    def save(self) -> None:
        """Сохранение данных."""

        save_buses(self.collection.get_all())

    def add_city_bus(
        self,
        route: str,
        capacity: int,
        speed: float,
        driver: str,
        stops: int,
        price: float
    ) -> None:
        """Добавление городского автобуса."""


        for bus in self.collection:
            if bus.route_number == route and bus.driver_name == driver:
                raise DuplicateBusError("Автобус уже существует")

        bus = CityBus(route, capacity, speed, driver, stops, price)
        self.collection.add(bus)


    def add_tourist_bus(
        self,
        route: str,
        capacity: int,
        speed: float,
        driver: str,
        guide: str,
        price: float
    ) -> None:
        """Добавление туристического автобуса."""

        bus = TouristBus(route, capacity, speed, driver, guide, price)
        self.collection.add(bus)
    def add_electric_bus(
        self,
        route: str,
        capacity: int,
        speed: float,
        driver: str,
        battery: int,
        eco: int
    ) -> None:
        """Добавление электробуса."""

        bus = ElectricBus(route, capacity, speed, driver, battery, eco)
        self.collection.add(bus)

    def get_all(self) -> list[Bus]:
        """Получение всех автобусов."""

        return self.collection.get_all()

    def remove_bus(self, bus_id: int) -> None:
        """Удаление автобуса."""

        bus = self.find_by_id(bus_id)
        self.collection.remove(bus)

    def find_by_id(self, bus_id: int) -> Bus:
        """Поиск автобуса по id."""

        bus = self.collection.find_by_id(bus_id)

        if bus is None:
            raise BusNotFoundError(f"Автобус с id={bus_id} не найден")

        return bus
    def filter_fast_buses(self, min_speed: float) -> list[Bus]:
        """Фильтр быстрых автобусов."""

        return self.collection.filter_by(lambda b: b.speed >= min_speed).get_all()

    def sort_by_speed(self) -> list[Bus]:
        """Сортировка по скорости."""

        return self.collection.sort_by(lambda b: b.speed).get_all()

    def sort_by_capacity(self) -> list[Bus]:
        """Сортировка по вместимости."""

        return self.collection.sort_by(lambda b: b.capacity).get_all()

    def sort_by_driver(self) -> list[Bus]:
        """Сортировка по водителю."""
        
        return self.collection.sort_by(lambda b: b.driver_name).get_all()