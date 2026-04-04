from lab02.model import Bus
from lab02.collection import BusFleet


def print_scenario(number, title):
    """Вспомогательная функция для красивого вывода заголовков"""
    print(f"\n{'='*60}")
    print(f"СЦЕНАРИЙ {number}: {title.upper()}")
    print(f"{'='*60}")


def run_lab02_demo():
    # Инициализация коллекции
    fleet = BusFleet()

    # СЦЕНАРИЙ 1
    print_scenario(1, "Создание объектов и наполнение коллекции")
    b1 = Bus("10", 40, 60, "Иван Иванов")
    b2 = Bus("20", 30, 55, "Петр Петров")
    b3 = Bus("30", 50, 65, "Сергей Сергеев")

    fleet.add(b1)
    fleet.add(b2)
    fleet.add(b3)

    print(f"Успешно создано и добавлено {len(fleet)} автобусов.")
    print("Текущее состояние:")
    for bus in fleet:
        print(f"  -> {bus}")

    # СЦЕНАРИЙ 2
    print_scenario(2, "Тест защиты (Дубликаты и Типы)")
    try:
        print("Попытка добавить автобус с существующим id...")
        fleet.add(b1)
    except ValueError as e:
        print(f"Ожидаемая ошибка: {e}")

    try:
        print("\nПопытка добавить некорректный тип данных (строку)...")
        fleet.add("Не автобус")
    except TypeError as e:
        print(f"Ожидаемая ошибка: {e}")

    # СЦЕНАРИЙ 3
    print_scenario(3, "Магические методы (__len__, __iter__)")
    print(f"Количество элементов через len(): {len(fleet)}")
    print("Перебор всей коллекции через цикл for:")
    for bus in fleet:
        print(f"  -> {bus}")

    # СЦЕНАРИЙ 4
    print_scenario(4, "Поиск и индексация (__getitem__)")
    print(f"Прямой доступ к fleet[0]: {fleet[0]}")

    search_id = 2
    found = fleet.find_by_id(search_id)
    print(f"Результат поиска автобуса id={search_id}: {found if found else 'Не найден'}")

    # СЦЕНАРИЙ 5
    print_scenario(5, "Сортировка и фильтрация")
    print("1. Сортировка по вместимости:")
    fleet.sort_by_capacity()
    for bus in fleet:
        print(f"   {bus.capacity:>3} мест | {bus.driver_name}")

    print("\n2. Фильтрация (создание новой коллекции автобусов на маршруте):")
    # Один автобус отправляем на маршрут
    b1.start_route()

    active_fleet = fleet.get_active()
    print(f"Всего автобусов: {len(fleet)}")
    print(f"Автобусов на маршруте в НОВОЙ коллекции: {len(active_fleet)}")
    for bus in active_fleet:
        print(f"   [НА МАРШРУТЕ] {bus}")

    # СЦЕНАРИЙ 6
    print_scenario(6, "Удаление элементов")
    print(f"Удаляем первый элемент (индекс 0)...")
    removed = fleet.remove_at(0)
    print(f"Удален автобус: {removed.driver_name}")
    print(f"Итого осталось в парке: {len(fleet)}")


if __name__ == "__main__":
    run_lab02_demo()