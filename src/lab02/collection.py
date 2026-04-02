# collection.py
from lab02.model import Bus
class BusFleet:
    def __init__(self):
        self._items = []

    # ===== БАЗОВЫЕ МЕТОДЫ =====
    def add(self, item: Bus):
        if not isinstance(item, Bus):
            raise TypeError("Можно добавлять только объекты Bus")

        # запрет дубликатов по id
        for bus in self._items:
            if bus.id == item.id:
                raise ValueError(f"Автобус с id={item.id} уже существует")

        self._items.append(item)

    def remove(self, item: Bus):
        self._items.remove(item)

    def remove_at(self, index: int):
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть числом")
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс вне диапазона")
        return self._items.pop(index)

    def get_all(self):
        return list(self._items)


    # ===== ПОИСК =====
    def find_by_id(self, bus_id):
        for bus in self._items:
            if bus.id == bus_id:
                return bus
        return None

    def find_by_route(self, route):
        return [bus for bus in self._items if bus.route_number == route]

    # ===== МАГИЧЕСКИЕ МЕТОДЫ =====
    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    # ===== СОРТИРОВКА =====
    def sort_by_capacity(self):
        self._items.sort(key=lambda bus: bus.capacity)

    def sort_by_speed(self):
        self._items.sort(key=lambda bus: bus.speed)

    # универсальная
    def sort(self, key):
        self._items.sort(key=key)


    # ===== ФИЛЬТРАЦИЯ =====
    def get_active(self):
        """Автобусы на маршруте"""
        new_collection = BusFleet()
        for bus in self._items:
            if bus.status == "На маршруте":
                new_collection.add(bus)
        return new_collection

    def get_in_park(self):
        """Автобусы в парке"""
        new_collection = BusFleet()
        for bus in self._items:
            if bus.status == "На парковке":
                new_collection.add(bus)
        return new_collection