from lab03.models import CityBus, TouristBus, ElectricBus
from lab06.container import TypedCollection, DisplayCollection, ScoreCollection
from lab01.model import Bus

def create_buses():
    b1 = CityBus("10", 50, 50, "Иванов", 20, 50)
    b2 = TouristBus("20", 30, 80, "Петров", "Анна", 200)
    b3 = ElectricBus("30", 45, 55, "Сидоров", 300, 5)
    return [b1, b2, b3]


# СЦЕНАРИЙ 1 (типизация)

def scenario_1():
    print("\n--- Сценарий 1 ---")

    c: TypedCollection[CityBus] = TypedCollection()

    bus = CityBus("10", 50, 60, "Иванов", 20, 50)
    c.add(bus)

    # c.add("not a bus")  #  покажет ошибку типов

    for b in c.get_all():
        print(b)



# СЦЕНАРИЙ 2 (find/filter/map)

def scenario_2():
    print("\n--- Сценарий 2 ---")

    c: TypedCollection[Bus] = TypedCollection()

    for b in create_buses():
        c.add(b)

    # find
    found = c.find(lambda x: x.speed > 70)
    print("Найден:", found)

    not_found = c.find(lambda x: x.speed > 200)
    print("Не найден:", not_found)

    # filter
    fast = c.filter(lambda x: x.speed > 60)
    print("Быстрые автобусы:", fast)

    # map
    names = c.map(lambda x: x.driver_name)
    print("Имена:", names)

    speeds = c.map(lambda x: x.speed)
    print("Скорости:", speeds)



# СЦЕНАРИЙ 3 (Protocol)

def scenario_3():
    print("\n--- Сценарий 3 ---")

    buses = create_buses()

    # Displayable
    dc = DisplayCollection()
    for b in buses:
        dc.add(b)

    print("Display:")
    dc.show_all()

    # Scorable
    sc = ScoreCollection()
    for b in buses:
        sc.add(b)

    print("Scores:", sc.get_scores())



# MAIN
def main():
    scenario_1()
    scenario_2()
    scenario_3()


if __name__ == "__main__":
    main()