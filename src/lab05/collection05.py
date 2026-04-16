from lab03.base import BusCollection


class AdvancedBusCollection(BusCollection):

    # ===== SORT =====
    def sort_by(self, key_func):
        self._buses.sort(key=key_func)
        return self  # для цепочек

    # ===== FILTER =====
    def filter_by(self, predicate):
        new = AdvancedBusCollection()
        for bus in self._buses:
            if predicate(bus):
                new.add(bus)
        return new

    # ===== APPLY =====
    def apply(self, func):
        new = AdvancedBusCollection()
        for bus in self._buses:
            new.add(func(bus))
        return new

    # ===== MAP =====
    def map(self, func):
        return list(map(func, self._buses))