## Лаба 1
#### model
``` python
# model.py
from validate import *
class Bus:
    # Атрибуты класса
    total_buses = 0
    total_passengers_transported = 0
    
    def __init__(self, route_number, capacity, speed, driver_name):
        """
        Конструктор класса Bus
        Параметры:
            route_number: номер маршрута (str)
            capacity: вместимость (int)
            speed: средняя скорость (int,float)
            driver_name: имя водителя (str)
        """
        # Валидация через имп фун-ии из validate.py
        self._route_number = val_route_number(route_number)
        self._capacity = val_capacity(capacity)
        self._speed = val_speed(speed)
        self._driver_name = val_driver_name(driver_name)
        
        # Инициализация остальных атрибутов
        self._passenger_count = 0
        self._status = BusStatus.IN_PARK
        self._mileage = 0.0
        self._fuel_level = 100.0
        
        Bus.total_buses += 1
        self._id = Bus.total_buses
        print(f"Создан автобус #{self._id}: маршрут {self._route_number}")
    
    # СВОЙСТВА
    @property
    def route_number(self):
        return self._route_number
    @property
    def capacity(self):
        return self._capacity
    @property
    def speed(self):
        return self._speed
    @property
    def driver_name(self):
        return self._driver_name
    
    @driver_name.setter
    def driver_name(self, new_name):
        old_name = self._driver_name
        self._driver_name = val_driver_name(new_name)
        print(f"Водитель автобуса #{self._id} изменен: {old_name} -> {self._driver_name}")
    @property
    def passenger_count(self):
        return self._passenger_count  
    @property
    def status(self):
        return self._status.value 
    @property
    def fuel_level(self):
        return self._fuel_level
    @property
    def mileage(self):
        return self._mileage
    @property
    def id(self):
        return self._id
    @speed.setter
    def speed(self, new_speed):
        if self._status == BusStatus.REPAIR:
            raise ValueError("Нельзя изменить скорость автобуса в ремонте")
        if self._status == BusStatus.ACCIDENT:
            raise ValueError("Нельзя изменить скорость автобуса после аварии")
        self._speed = val_speed(new_speed)
        print(f"Скорость автобуса #{self._id} изменена на {self._speed} км/ч")


    # БИЗНЕС-МЕТОД 1: Посадка пассажиров
    def board_passengers(self, count):
        print(f"\nПосадка в автобус #{self._id} ({self._passenger_count}/{self._capacity} пассажиров)")
        
        try:
            new_count = val_passenger_count(self._passenger_count, count, self._capacity, self._status)
        except ValueError as e:
            print(f" Ошибка: {e}")
            return {
                'bus_id': self._id,
                'boarded': 0,
                'left': count,
                'total_passengers': self._passenger_count,
                'free_seats': self._capacity - self._passenger_count,
                'is_full': self._passenger_count == self._capacity
            }
        
        free_seats = self._capacity - self._passenger_count
        
        if count > free_seats:
            actual_boarded = free_seats
            self._passenger_count = self._capacity
            left = count - free_seats
            print(f"Влезло только {actual_boarded} пассажиров")
            if left > 0:
                print(f"  {left} пассажиров осталось на остановке")
        else:
            self._passenger_count += count
            actual_boarded = count
            left = 0
            print(f"Село {actual_boarded} пассажиров")
        
        return {
            'bus_id': self._id,
            'boarded': actual_boarded,
            'left': left,
            'total_passengers': self._passenger_count,
            'free_seats': self._capacity - self._passenger_count,
            'is_full': self._passenger_count == self._capacity
        }
    
    # БИЗНЕС-МЕТОД 2: Высадка пассажиров
    def disembark_passengers(self, count=None):
        if count is None:
            count = self._passenger_count
        
        if not isinstance(count, int):
            raise TypeError(f"Количество должно быть целым числом, получен {type(count).__name__}")
        if count <= 0:
            raise ValueError(f"Количество должно быть положительным, получено {count}")
        if count > self._passenger_count:
            raise ValueError(f"Нельзя высадить {count} пассажиров, в автобусе только {self._passenger_count}")
        
        self._passenger_count -= count
        Bus.total_passengers_transported += count
        print(f"Высажено {count} пассажиров")
        
        return {
            'bus_id': self._id,
            'disembarked': count,
            'remaining': self._passenger_count
        }
    
    # БИЗНЕС-МЕТОД 3: Выезд на маршрут
    def start_route(self):
        print(f"\nПопытка выезда автобуса #{self._id} на маршрут {self._route_number}")
        
        if self._status != BusStatus.IN_PARK:
            raise ValueError(f"Нельзя выехать на маршрут из состояния '{self._status.value}'")
        if self._fuel_level < MIN_FUEL_FOR_ROUTE:
            raise ValueError(f"Недостаточно топлива для выезда на маршрут (нужно {MIN_FUEL_FOR_ROUTE}%, есть {self._fuel_level:.1f}%)")
        
        self._status = BusStatus.ON_ROUTE
        print(f" Автобус #{self._id} выехал на маршрут {self._route_number}")
        print(f" Пассажиров в автобусе: {self._passenger_count}")
        print(f" Топливо: {self._fuel_level:.1f}%")
        return True
    
    # БИЗНЕС-МЕТОД 4: Завершение маршрута
    def finish_route(self):
        if self._status != BusStatus.ON_ROUTE:
            raise ValueError(f"Автобус не на маршруте (статус: {self._status.value})")
        
        passengers_this_route = self._passenger_count
        Bus.total_passengers_transported += passengers_this_route
        
        route_distance = 50
        self._mileage += route_distance
        fuel_consumed = route_distance * 0.5
        self._fuel_level = max(0, self._fuel_level - fuel_consumed)
        
        self._passenger_count = 0
        self._status = BusStatus.IN_PARK
        
        print(f"\nАвтобус #{self._id} завершил маршрут {self._route_number}")
        print(f"  Перевезено пассажиров за рейс: {passengers_this_route}")
        print(f"  Всего перевезено всеми автобусами: {Bus.total_passengers_transported}")
        print(f"  Пробег увеличен на {route_distance} км (всего: {self._mileage:.1f} км)")
        print(f"  Остаток топлива: {self._fuel_level:.1f}%")
        return True
    
    # БИЗНЕС-МЕТОД 5: Ремонт
    def send_to_repair(self):
        if self._status == BusStatus.REPAIR:
            raise ValueError("Автобус уже в ремонте")
        
        old_status = self._status
        self._status = BusStatus.REPAIR
        print(f"\n Автобус #{self._id} отправлен в ремонт (был: {old_status.value})")
        return True
    
    def complete_repair(self):
        if self._status != BusStatus.REPAIR:
            raise ValueError("Автобус не в ремонте")
        
        self._status = BusStatus.IN_PARK
        self._fuel_level = 100.0
        self._mileage = 0
        print(f"\nРемонт автобуса #{self._id} завершен")
        print(f"  Автобус готов к работе")
        print(f"  Полный бак")
        return True
    
    # БИЗНЕС-МЕТОД 6: Авария
    def accident(self):
        if self._status == BusStatus.REPAIR:
            raise ValueError("Автобус в ремонте")
        if self._status == BusStatus.ACCIDENT:
            raise ValueError("Автобус уже в аварии")
        
        old_status = self._status
        self._status = BusStatus.ACCIDENT
        
        injured = int(self._passenger_count * 0.3)
        self._passenger_count -= injured
        
        print(f"\nАвария! Автобус #{self._id} попал в аварию")
        print(f"  Было: {old_status.value}, стало: {BusStatus.ACCIDENT.value}")
        print(f"  Пострадало пассажиров: {injured}")
        return True
    
    # МАГИЧЕСКИЕ МЕТОДЫ
    def __str__(self):
        return (f"Автобус #{self._id:03d} | "
                f"Маршрут: {self._route_number:<5} | "
                f"Водитель: {self._driver_name:<15} | "
                f"Состояние: {self._status.value} | "
                f"Пассажиры: {self._passenger_count:3d}/{self._capacity:3d} | "
                f"Топливо: {self._fuel_level:5.1f}% | "
                f"Пробег: {self._mileage:6.1f} км")
    
    def __repr__(self):
        return (f"Bus(route_number='{self._route_number}', "
                f"capacity={self._capacity}, "
                f"speed={self._speed}, "
                f"driver_name='{self._driver_name}')")
    
    def __eq__(self, other):
        if not isinstance(other, Bus):
            return False
        return (self._route_number == other._route_number and 
                self._driver_name == other._driver_name)
    
    def __lt__(self, other):
        if not isinstance(other, Bus):
            return NotImplemented
        return self._capacity < other._capacity
```

#### validate
``` python
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
```


#### demo
``` python
from model import Bus
import time
def print_separator(part_name):
    # функция для вывода разделителей
    print("\n" + "=" * 60)
    print(f" {part_name}")
    print("=" * 60)

def demonstrate_grade5():
    # ========== ЧАСТЬ 1: СОЗДАНИЕ ОБЪЕКТОВ ==========
    print_separator("ЧАСТЬ 1: СОЗДАНИЕ ОБЪЕКТОВ")
    
    print("\nСоздаем три автобуса:")
    bus1 = Bus("15", 50, 60.5, "Иван Золо")
    bus2 = Bus("22", 35, 55.0, "Филипп Киркоров")
    bus3 = Bus("33", 45, 58.5, "Леонид Якубович")
    print("\nВсе созданные автобусы:")
    print(bus1)
    print(bus2)
    print(bus3)
    print(f"\nАтрибут класса total_buses = {Bus.total_buses}")
    print(f"Тот же атрибут, но через экземпляр: {bus1.total_buses}")
    
    # ========== ЧАСТЬ 2: ДЕМОНСТРАЦИЯ ВАЛИДАЦИИ ==========
    print_separator("ЧАСТЬ 2: ДЕМОНСТРАЦИЯ ВАЛИДАЦИИ")
    print("\nПытаемся создать автобус с некорректными данными:")
    test_cases = [
        ("15", 50, 60.5, "", "пустое имя водителя"),
        ("15", 1000, 60.5, "Водитель", "слишком большая вместимость"),
        ("15", 50, 300, "Водитель", "слишком большая скорость"),
        ("", 50, 60.5, "Водитель", "пустой номер маршрута"),
        ("15", 50.5, 60.5, "Водитель", "вместимость не целое число"),
    ]
    
    for i, (route, cap, speed, driver, desc) in enumerate(test_cases, 1):
        print(f"\n  Тест {i}: {desc}")
        try:
            bad_bus = Bus(route, cap, speed, driver)
        except (TypeError, ValueError) as e:
            print(f" Ошибка перехвачена: {e}")
    
    # ========== ЧАСТЬ 3: ДЕМОНСТРАЦИЯ СВОЙСТВ И СЕТТЕРОВ ==========
    print_separator("ЧАСТЬ 3: СВОЙСТВА И СЕТТЕРЫ")
    
    print(f"\nИсходный автобус: {bus1}")
    
    # Изменяем скорость
    print("\nИзменяем скорость:")
    print(f"  Текущая скорость: {bus1.speed} км/ч")
    bus1.speed = 75.5
    print(f"  Новая скорость: {bus1.speed} км/ч")
    
    # Изменяем водителя
    print("\nМеняем водителя:")
    print(f"  Текущий водитель: {bus1.driver_name}")
    bus1.driver_name = "Николай Басков"
    print(f"  Новый водитель: {bus1.driver_name}")
    
    # Пробуем некорректное изменение
    print("\nПытаемся установить некорректную скорость:")
    try:
        bus1.speed = 500
    except ValueError as e:
        print(f"Ошибка: {e}")
    
    # ========== ЧАСТЬ 4: БИЗНЕС-МЕТОДЫ И СОСТОЯНИЯ ==========
    print_separator("ЧАСТЬ 4: БИЗНЕС-МЕТОДЫ И СОСТОЯНИЯ")
    
    print("\n--- СЦЕНАРИЙ 1: Обычный рабочий день ---")
    print("Создаем новый автобус:")
    bus4 = Bus("101", 40, 65.0, "Стас Михайлов")
    print(bus4)
    
    # Сажаем пассажиров
    print("\nПосадка пассажиров:")
    result = bus4.board_passengers(25)
    print(f"  Село: {result['boarded']}, свободно: {result['free_seats']}")
    
    # Выезжаем на маршрут
    print("\nВыезд на маршрут:")
    bus4.start_route()
    print(bus4)
    
    # По пути подбираем еще пассажиров
    print("\nПосадка на маршруте:")
    bus4.board_passengers(20)
    
    # Завершаем маршрут
    print("\nЗавершение маршрута:")
    bus4.finish_route()
    print(bus4)
    
    print("\n--- СЦЕНАРИЙ 2: Ситуация с ремонтом ---")
    print("Создаем еще один автобус:")
    bus5 = Bus("202", 30, 50.0, "Данил Колбасенко")
    print(bus5)
    
    # Отправляем в ремонт
    print("\nОтправка в ремонт:")
    bus5.send_to_repair()
    print(bus5)
    
    # Пытаемся выехать на маршрут (должно быть нельзя)
    print("\nПытаемся выехать на маршрут из ремонта:")
    try:
        bus5.start_route()
    except ValueError as e:
        print(f" Ошибка: {e}")
    
    # Завершаем ремонт
    print("\nЗавершение ремонта:")
    bus5.complete_repair()
    print(bus5)
    
    # Теперь можно работать
    print("\nПосле ремонта:")
    bus5.board_passengers(20)
    bus5.start_route()
    
    print("\n--- СЦЕНАРИЙ 3: Аварийная ситуация ---")
    print("Создаем автобус для демонстрации аварии:")
    bus6 = Bus("303", 50, 55.0, "Андрей Малахов")
    bus6.board_passengers(45)  # почти полный
    bus6.start_route()
    print(bus6)
    # Авария
    print("\nПроисходит авария:")
    bus6.accident()
    print(bus6)
    
    # Пытаемся совершить действия после аварии
    print("\nПытаемся изменить скорость после аварии:")
    try:
        bus6.speed = 60.0
    except ValueError as e:
        print(f" Ошибка: {e}")
    
    # Отправляем в ремонт
    print("\nОтправка в ремонт после аварии:")
    bus6.send_to_repair()
    print(bus6)
    
    # ========== ЧАСТЬ 5: МАГИЧЕСКИЕ МЕТОДЫ ==========
    print_separator("ЧАСТЬ 5: МАГИЧЕСКИЕ МЕТОДЫ")
    
    print("\n __str__ (для пользователя):")
    print(str(bus1))
    
    print("\n __repr__ (для разработчика):")
    print(repr(bus1))
    print("(можно использовать для создания копии)")
    
    print("\n Сравнение автобусов (__eq__):")
    bus_same = Bus("15", 50, 60.5, "Дмитрий Гордон")
    bus_diff = Bus("15", 50, 60.5, "Лариса Гузеева")
    
    print(f"bus1 == bus_same: {bus1 == bus_same} (одинаковые маршрут и водитель)")
    print(f"bus1 == bus_diff: {bus1 == bus_diff} (разные водители)")
    
    print("\n Сортировка по вместимости (__lt__):")
    buses = [bus2, bus1, bus3]
    print("До сортировки:")
    for b in buses:
        print(f"  Маршрут {b.route_number}: вместимость {b.capacity}")
    
    buses.sort()
    print("\nПосле сортировки:")
    for b in buses:
        print(f"  Маршрут {b.route_number}: вместимость {b.capacity}")
    
    # ========== ЧАСТЬ 6: ИТОГИ ==========
    print_separator("Итоги")
    print(f"\n Статистика:")
    print(f"  Всего создано автобусов: {Bus.total_buses}")
    print(f"  Всего перевезено пассажиров: {Bus.total_passengers_transported}")
    print("\n Финальное состояние всех автобусов:")
    for i, bus in enumerate([bus1, bus2, bus3, bus4, bus5, bus6], 1):
        print(f"  {bus}")

if __name__ == "__main__":
    demonstrate_grade5()