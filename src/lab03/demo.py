from lab03.models import CityBus, TouristBus, ElectricBus
from lab03.base import BusCollection


print(" -------------------- Сценарий 1: Проверка корректности и создание объектов --------------------")
print("Цель: показать создание объектов и базовую валидацию")
try:
    bus1 = CityBus("12A", 50, 60, "Иванов", 20, 50)
    bus1.board_passengers(30)

    bus2 = TouristBus("T1", 40, 70, "Петров", "Гид Анна", 200)
    bus2.board_passengers(20)

    bus3 = ElectricBus("E5", 30, 50, "Сидоров", 300, 5)
    bus3.board_passengers(15)

    print("Автобусы успешно созданы:\n")
    print(bus1)
    print(bus2)
    print(bus3)

except ValueError as e:
    print("Ошибка:", e)


# Сценарий 2: Полиморфизм и проверка типов 
# Цель: показать polymorphism + isinstance
print("Сценарий 2: Полиморфизм и проверка типов ")
print("\n--- Полиморфизм и isinstance ---")

print("bus2 является TouristBus:", isinstance(bus2, TouristBus))
print("bus2 является CityBus:", isinstance(bus2, CityBus))

print("\nПолиморфный вызов метода process():")
for bus in [bus1, bus2, bus3]:
    print(bus.process())


print("\n---Сценарий 3: Коллекция и работа с объектами---")
collection = BusCollection()
collection.add(bus1)
collection.add(bus2)
collection.add(bus3)

print("\nВсе автобусы:")
for b in collection:
    print(b)

print("\nТолько CityBus:")
for b in collection.get_by_type(CityBus):
    print(b)

# запуск маршрута
bus1.start_route()
bus2.start_route()

print("\nАктивные автобусы:")
for b in collection.get_active():
    print(b)

print("\nДоход (переопределение методов):")
for b in collection:
    print(b.calculate_income())