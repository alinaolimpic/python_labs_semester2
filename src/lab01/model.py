# model.py
from lab01.validate import *
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