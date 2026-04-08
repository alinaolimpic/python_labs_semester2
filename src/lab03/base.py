from lab02.model import Bus


class BusCollection:
    def __init__(self):
        self._buses = []

    def _check_type(self, bus):
        if not isinstance(bus, Bus):
            raise TypeError("Можно добавлять только Bus")

    def add(self, bus):
        self._check_type(bus)
        if bus in self._buses:
            raise ValueError("Уже добавлен")
        self._buses.append(bus)

    def get_all(self):
        return self._buses

    def get_active(self):
        new = BusCollection()
        for bus in self._buses:
            if bus.status == "На маршруте":
                new.add(bus)
        return new

    def get_by_type(self, cls):
        new = BusCollection()
        for bus in self._buses:
            if type(bus) == cls:
                new.add(bus)
        return new

    def __iter__(self):
        return iter(self._buses)

    def __len__(self):
        return len(self._buses)

    def __str__(self):
        return "\n".join(str(b) for b in self._buses)