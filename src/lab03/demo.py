from lab03.models import CityBus, TouristBus, ElectricBus
from lab03.base import BusCollection

# создание объектов
bus1 = CityBus("12A", 50, 60, "Иванов", 20, 50)
bus2 = TouristBus("T1", 40, 70, "Петров", "Гид Анна", 200)
bus3 = ElectricBus("E5", 30, 50, "Сидоров", 300, 5)

# посадка пассажиров
bus1.board_passengers(30)
bus2.board_passengers(20)
bus3.board_passengers(15)

print(bus1)
print(bus2)
print(bus3)

print("\n--- Полиморфизм ---")
for bus in [bus1, bus2, bus3]:
    print(bus.process())

print("\n--- Доход ---")
for bus in [bus1, bus2, bus3]:
    print(bus.calculate_income())

# коллекция
print("\n--- Коллекция ---")
collection = BusCollection()
collection.add(bus1)
collection.add(bus2)
collection.add(bus3)

for b in collection:
    print(b)

print("\n--- Фильтр по типу (CityBus) ---")
for b in collection.get_by_type(CityBus):
    print(b)

# запуск маршрута
bus1.start_route()
bus2.start_route()

print("\n--- Активные автобусы ---")
for b in collection.get_active():
    print(b)