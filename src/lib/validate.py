# validate.py
from enum import Enum
from typing import Union
class BusStatus(Enum):
    """Перечисление возможных состояний автобуса"""
    IN_PARK = "На парковке"
    ON_ROUTE = "На маршруте"
    REPAIR = "В ремонте"
    ACCIDENT = "Авария"

# Константы для валидации
MIN_SPEED = 1
MAX_SPEED = 120
MIN_CAPACITY = 5
MAX_CAPACITY = 150
MAX_PASSENGER_OVERLOAD = 1.2
MIN_FUEL_FOR_ROUTE = 20

# Функции валидации
def val_route_number(value):
    """Проверка номера маршрута"""
    if not isinstance(value, str):
        raise TypeError(f"Номер маршрута должен быть строкой, получен {type(value).__name__}")
    value = value.strip()
    if not value:
        raise ValueError("Номер маршрута не может быть пустым")
    if len(value) > 10:
        raise ValueError(f"Номер маршрута слишком длинный (макс. 10 символов), получено {len(value)}")
    return value

def val_capacity(value):
    """Проверка вместимости"""
    if not isinstance(value, int):
        raise TypeError(f"Вместимость должна быть целым числом, получен {type(value).__name__}")
    
    if not (MIN_CAPACITY <= value <= MAX_CAPACITY):
        raise ValueError(
            f"Вместимость должна быть от {MIN_CAPACITY} до {MAX_CAPACITY}, "
            f"получено {value}"
        )
    return value

def val_speed(value):
    """Проверка скорости"""
    if not isinstance(value, (int, float)):
        raise TypeError(f"Скорость должна быть числом, получен {type(value).__name__}")
    
    if not (MIN_SPEED <= value <= MAX_SPEED):
        raise ValueError(
            f"Скорость должна быть от {MIN_SPEED} до {MAX_SPEED} км/ч, "
            f"получено {value}"
        )
    return float(value)

def val_driver_name(value):
    """Проверка имени водителя"""
    if not isinstance(value, str):
        raise TypeError(f"Имя водителя должно быть строкой, получен {type(value).__name__}")
    value = value.strip()
    if not value:
        raise ValueError("Имя водителя не может быть пустым")
    
    if len(value) < 2:
        raise ValueError(f"Имя водителя должно содержать минимум 2 символа, получено {len(value)}")
    
    if len(value) > 50:
        raise ValueError(f"Имя водителя слишком длинное (макс. 50 символов), получено {len(value)}")
    
    # Проверяем, что имя содержит только буквы, пробелы и дефисы
    for char in value:
        if not (char.isalpha() or char.isspace() or char == '-'):
            raise ValueError(
                f"Имя водителя может содержать только буквы, пробелы и дефис, "
                f"найден недопустимый символ: '{char}'"
            )
    return value

def val_passenger_count(current_count, add_count, capacity, status):
    """Проверка количества пассажиров с учетом состояния"""
    if not isinstance(add_count, int):
        raise TypeError(f"Количество пассажиров должно быть целым числом, получен {type(add_count).__name__}")
    if add_count < 0:
        raise ValueError(f"Количество пассажиров не может быть отрицательным, получено {add_count}")
    
    new_count = current_count + add_count
    
    # Проверяем состояние автобуса
    if status == BusStatus.REPAIR:
        raise ValueError("Нельзя сажать пассажиров в автобус в ремонте")
    
    if status == BusStatus.ACCIDENT:
        raise ValueError("Нельзя сажать пассажиров в автобус после аварии")
    
    # Проверяем вместимость (с учетом перегруза)
    max_allowed = int(capacity * MAX_PASSENGER_OVERLOAD)
    if new_count > max_allowed:
        raise ValueError(
            f"Нельзя превысить максимальную вместимость {max_allowed} "
            f"(вместимость: {capacity}, перегрузка макс. {MAX_PASSENGER_OVERLOAD*100:.0f}%)"
        )
    
    return new_count