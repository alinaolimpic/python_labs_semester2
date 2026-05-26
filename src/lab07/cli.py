from typing import Callable

from lab07.app import BusApp
from lab07.exceptions import BusError


app = BusApp()


def print_menu() -> None:
    """Вывод меню."""

    print("\n" + "=" * 60)
    print("СИСТЕМА УПРАВЛЕНИЯ АВТОБУСНЫМ ПАРКОМ")
    print("=" * 60)

    print("1. Добавить городской автобус")
    print("2. Добавить туристический автобус")
    print("3. Добавить электробус")
    print("4. Показать все автобусы")
    print("5. Найти автобус по ID")
    print("6. Удалить автобус")
    print("7. Фильтр по скорости")
    print("8. Сортировка")
    print("0. Выход")

def print_buses(buses: list) -> None:
    """Красивый вывод автобусов."""

    if not buses:
        print("Коллекция пуста")
        return

    print("\n" + "-" * 120)

    for bus in buses:
        print(bus)

    print("-" * 120)



def add_city_bus() -> None:
    """Добавление городского автобуса."""

    route = input("Маршрут: ")
    capacity = int(input("Вместимость: "))
    speed = float(input("Скорость: "))
    driver = input("Водитель: ")
    stops = int(input("Количество остановок: "))
    price = float(input("Цена билета: "))

    app.add_city_bus(route, capacity, speed, driver, stops, price)

    print("Городской автобус успешно добавлен")


def add_tourist_bus() -> None:
    """Добавление туристического автобуса."""

    route = input("Маршрут: ")
    capacity = int(input("Вместимость: "))
    speed = float(input("Скорость: "))
    driver = input("Водитель: ")
    guide = input("Имя гида: ")
    price = float(input("Цена тура: "))

    app.add_tourist_bus(route, capacity, speed, driver, guide, price)

    print("Туристический автобус успешно добавлен")



def add_electric_bus() -> None:
    """Добавление электробуса."""

    route = input("Маршрут: ")
    capacity = int(input("Вместимость: "))
    speed = float(input("Скорость: "))
    driver = input("Водитель: ")
    battery = int(input("Ёмкость батареи: "))
    eco = int(input("Эко-уровень: "))

    app.add_electric_bus(route, capacity, speed, driver, battery, eco)

    print("Электробус успешно добавлен")

def find_bus() -> None:
    """Поиск автобуса."""

    bus_id = int(input("Введите ID автобуса: "))

    bus = app.find_by_id(bus_id)

    print("\nНайден автобус:")
    print(bus)



def delete_bus() -> None:
    """Удаление автобуса."""

    bus_id = int(input("Введите ID автобуса: "))

    bus = app.find_by_id(bus_id)

    confirm = input(f"Удалить автобус {bus.route_number}? (y/n): ")

    if confirm.lower() == "y":
        app.remove_bus(bus_id)
        print("Автобус удалён")
    else:
        print("Удаление отменено")



def filter_buses() -> None:
    """Фильтрация автобусов."""

    speed = float(input("Минимальная скорость: "))

    buses = app.filter_fast_buses(speed)

    print_buses(buses)

def sort_buses() -> None:
    """Сортировка автобусов."""

    print("\n1. По скорости")
    print("2. По вместимости")
    print("3. По водителю")

    choice = input("Выберите вариант: ")

    if choice == "1":
        buses = app.sort_by_speed()

    elif choice == "2":
        buses = app.sort_by_capacity()

    elif choice == "3":
        buses = app.sort_by_driver()

    else:
        print("Неверный пункт")
        return

    print_buses(buses)

def run_cli() -> None:
    """Главный цикл CLI."""

    while True:
        try:
            print_menu()

            choice = input("\nВыберите пункт меню: ")

            if choice == "1":
                add_city_bus()

            elif choice == "2":
                add_tourist_bus()

            elif choice == "3":
                add_electric_bus()

            elif choice == "4":
                print_buses(app.get_all())

            elif choice == "5":
                find_bus()

            elif choice == "6":
                delete_bus()

            elif choice == "7":
                filter_buses()

            elif choice == "8":
                sort_buses()

            elif choice == "0":
                app.save()
                print("Данные сохранены")
                print("Выход из программы")
                break

            else:
                print("Ошибка: неверный пункт меню")

        except ValueError as error:
            print(f"Ошибка ввода: {error}")

        except BusError as error:
            print(f"Ошибка приложения: {error}")

        except Exception as error:
            print(f"Неожиданная ошибка: {error}")