from lab04.models import CityBus, TouristBus, ElectricBus
from lab02.collection import BusFleet
from lab04.interfaces import Printable, Comparable


# универсальные функции
def print_all(items: list[Printable]):
    for item in items:
        print(item.to_string())

def sort_buses(items: list[Comparable]):
    return sorted(items, key=lambda x: x.calculate_income())


def run_demo():

    # =========================
    # СЦЕНАРИЙ 1
    # =========================
    print("\n---Сценарий 1---")
    print("---Создание автобусов---")

    bus1 = CityBus("10", 40, 60, "Иванов", 20, 50)
    bus2 = TouristBus("20", 30, 70, "Петров", "Анна", 200)
    bus3 = ElectricBus("30", 50, 50, "Сидоров", 300, 5)

    print("\n---Данные об автобусах---")
    print(bus1)
    print(bus2)
    print(bus3)

    print("\n---Посадка пассажиров---")
    bus1.board_passengers(20)
    bus2.board_passengers(15)
    bus3.board_passengers(10)

    print("\n---Полиморфизм (process)---")
    print(bus1.process())
    print(bus2.process())
    print(bus3.process())


    # =========================
    # СЦЕНАРИЙ 2
    # =========================
    print("\n---Сценарий 2---")
    print("---Работа через интерфейсы---")

    buses = [bus1, bus2, bus3]

    print("\n---Printable---")
    print_all(buses)

    print("\n---Проверка интерфейсов---")
    for bus in buses:
        print(f"{bus.__class__.__name__}: Printable={isinstance(bus, Printable)}, Comparable={isinstance(bus, Comparable)}")

    print("\n---Сортировка (Comparable)---")
    sorted_buses = sort_buses(buses)
    for bus in sorted_buses:
        print(bus.to_string())


    # =========================
    # СЦЕНАРИЙ 3
    # =========================
    print("\n---Сценарий 3---")
    print("---Коллекция автобусов---")

    fleet = BusFleet()
    fleet.add(bus1)
    fleet.add(bus2)
    fleet.add(bus3)

    print("\n---Все автобусы---")
    for bus in fleet:
        print(bus)

    print("\n---Автобусы на маршруте---")
    bus1.start_route()
    active = fleet.get_active()
    for bus in active:
        print(bus)

    print("\n---Фильтрация по интерфейсу Printable---")
    printable = [b for b in fleet if isinstance(b, Printable)]
    print_all(printable)

    print("\n---Фильтрация по интерфейсу Comparable---")
    comparable = [b for b in fleet if isinstance(b, Comparable)]
    for b in comparable:
        print(b.to_string())


if __name__ == "__main__":
    run_demo()