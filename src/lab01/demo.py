from model import Bus
import time
def print_separator(part_name):
    # функция для вывода разделителей
    print("\n" + "=" * 60)
    print(f" {part_name}")
    print("=" * 60)

def demonstrate_grade5():
    #ЧАСТЬ 1: СОЗДАНИЕ ОБЪЕКТОВ
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
    
    # ЧАСТЬ 2: ДЕМОНСТРАЦИЯ ВАЛИДАЦИИ
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
    
    # ЧАСТЬ 3: ДЕМОНСТРАЦИЯ СВОЙСТВ И СЕТТЕРОВ
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
    
    #ЧАСТЬ 4: БИЗНЕС-МЕТОДЫ И СОСТОЯНИЯ
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
    
    # ЧАСТЬ 5: МАГИЧЕСКИЕ МЕТОДЫ
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
    
    # ЧАСТЬ 6: ИТОГИ
    print_separator("Итоги")
    print(f"\n Статистика:")
    print(f"  Всего создано автобусов: {Bus.total_buses}")
    print(f"  Всего перевезено пассажиров: {Bus.total_passengers_transported}")
    print("\n Финальное состояние всех автобусов:")
    for i, bus in enumerate([bus1, bus2, bus3, bus4, bus5, bus6], 1):
        print(f"  {bus}")

if __name__ == "__main__":
    demonstrate_grade5()
