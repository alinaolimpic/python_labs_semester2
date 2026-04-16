"""
strategies.py
Функции-стратегии и callable-объекты для работы с автобусами
"""

# ===== СОРТИРОВКА =====

def by_capacity(bus):
    """Сортировка по вместимости"""
    return bus.capacity


def by_speed(bus):
    """Сортировка по скорости"""
    return bus.speed


def by_driver(bus):
    """Сортировка по имени водителя"""
    return bus.driver_name


def by_capacity_and_speed(bus):
    """Сортировка по вместимости и скорости"""
    return (bus.capacity, bus.speed)


# ===== ФИЛЬТРЫ =====

def is_fast(bus):
    """Быстрые автобусы (> 60)"""
    return bus.speed > 60


def is_large(bus):
    """Большая вместимость (> 40)"""
    return bus.capacity > 40


def is_city_bus(bus):
    """Фильтр по типу"""
    from lab03.models import CityBus
    return isinstance(bus, CityBus)


# ===== ФАБРИКА ФУНКЦИЙ =====

def make_speed_filter(max_speed):
    """Фабрика фильтров по скорости"""
    def filter_fn(bus):
        return bus.speed <= max_speed
    return filter_fn


# ===== APPLY ФУНКЦИИ =====

def increase_speed(bus):
    """Увеличить скорость"""
    bus.speed += 5
    return bus


def start_route(bus):
    """Запуск маршрута"""
    try:
        bus.start_route()
    except:
        pass
    return bus


# ===== СТРАТЕГИИ (CALLABLE) =====

class DiscountSpeedStrategy:
    """Стратегия уменьшения скорости (например, износ)"""

    def __call__(self, bus):
        bus.speed *= 0.9
        return bus


class UpgradeStrategy:
    """Стратегия улучшения автобуса"""

    def __call__(self, bus):
        bus.speed += 10
        return bus