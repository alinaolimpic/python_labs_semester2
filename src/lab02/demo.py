# demo.py
from lab02.model import Bus
from lab02.collection import BusFleet
def print_sep(title):
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)

def main():
    fleet = BusFleet()

    print_sep("СОЗДАНИЕ ОБЪЕКТОВ")
    b1 = Bus("10", 40, 60, "Иван Иванов")
    b2 = Bus("20", 30, 55, "Петр Петров")
    b3 = Bus("30", 50, 65, "Сергей Сергеев")

    print_sep("ДОБАВЛЕНИЕ В КОЛЛЕКЦИЮ")
    fleet.add(b1)
    fleet.add(b2)
    fleet.add(b3)

    print("Все автобусы:")
    for bus in fleet:
        print(bus)

    print_sep("LEN И ИТЕРАЦИЯ")
    print("Количество автобусов:", len(fleet))

    print_sep("ИНДЕКСАЦИЯ")
    print("Первый автобус:")
    print(fleet[0])

    print_sep("ПОИСК")
    found = fleet.find_by_id(1)
    print("Поиск по id=1:")
    print(found)

    print_sep("СОРТИРОВКА")
    fleet.sort_by_capacity()
    print("Отсортировано по вместимости:")
    for bus in fleet:
        print(bus)

    print_sep("ФИЛЬТРАЦИЯ (СЦЕНАРИЙ 1)")
    b1.start_route()
    active = fleet.get_active()
    print("Автобусы на маршруте:")
    for bus in active:
        print(bus)

    print_sep("СЦЕНАРИЙ 2 (УДАЛЕНИЕ)")
    fleet.remove_at(1)
    print("После удаления:")
    for bus in fleet:
        print(bus)

    print_sep("СЦЕНАРИЙ 3 (ДУБЛИКАТ)")
    try:
        fleet.add(b1)
    except ValueError as e:
        print("Ошибка:", e)


if __name__ == "__main__":
    main()