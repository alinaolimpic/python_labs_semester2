from lab03.models import CityBus, TouristBus, ElectricBus
from lab05.collection05 import AdvancedBusCollection
import lab05.strategies as st



def print_all(title, collection):
    print(f"\n--- {title} ---")
    for b in collection:
        print(b)


def create_collection():
    """Создание коллекции (используется в каждом сценарии)"""
    c = AdvancedBusCollection()
    b1 = CityBus("10", 50, 60, "Иванов", 20, 50)
    b2 = TouristBus("20", 30, 80, "Петров", "Анна", 200)
    b3 = ElectricBus("30", 45, 55, "Сидоров", 300, 5)
    b4 = CityBus("40", 60, 70, "Алексеев", 25, 60)
    b5 = TouristBus("50", 35, 65, "Николаев", "Олег", 150)

    for b in [b1, b2, b3, b4, b5]:
        c.add(b)

    return c


# СЦЕНАРИЙ 1

def scenario_1():
    print("\n------- СЦЕНАРИЙ 1 -------")
    print("Цепочка: filter → sort → apply") 

    c = create_collection()
    print_all("Исходная коллекция", c)

    # FILTER
    filtered = c.filter_by(st.is_large)
    print_all("После filter (вместимость > 40)", filtered)

    # SORT
    sorted_c = filtered.sort_by(st.by_speed)
    print_all("После sort (по скорости)", sorted_c)

    # APPLY
    applied = sorted_c.apply(st.increase_speed)
    print_all("После apply (увеличение скорости)", applied)


# СЦЕНАРИЙ 2
def scenario_2():
    print("\n--------СЦЕНАРИЙ 2 ----------")
    print("Замена стратегии сортировки")

    c = create_collection()
    print_all("Исходная коллекция", c)

    # стратегия 1
    sorted_by_capacity = c.sort_by(st.by_capacity)
    print_all("Сортировка по вместимости", sorted_by_capacity)

    # стратегия 2 
    sorted_by_driver = c.sort_by(st.by_driver)
    print_all("Сортировка по имени водителя", sorted_by_driver)

    # стратегия 3 
    sorted_by_speed = c.sort_by(st.by_speed)
    print_all("Сортировка по скорости", sorted_by_speed)

# СЦЕНАРИЙ 3
def scenario_3():
    print("\n-------- СЦЕНАРИЙ 3 --------")
    print("Callable-объект как стратегия + map + фабрика")

    c = create_collection()
    fast = list(filter(st.is_fast, c)) 
    print_all("Исходная коллекция", c)

    # CALLABLE

    # стратегия 1
    strategy = st.UpgradeStrategy()
    upgraded = c.apply(strategy)
    print_all("После применения callable стратегии (апгрейд)", upgraded)

    # стратегия 2
    strategy2 = st.DiscountSpeedStrategy()
    discounted = c.apply(strategy2)
    print_all("После применения callable стратегии (уменьшение скорости)", discounted)



    # MAP 
    names = c.map(lambda x: x.driver_name) 
    print("\nРезультат map (имена водителей):", names)

    # ФАБРИКА demo 4
    slow_filter = st.make_speed_filter(65)
    slow_buses = c.filter_by(slow_filter)
    print_all("Фильтр через фабрику (скорость <= 65)", slow_buses)



#------MAIN------

def main():
    scenario_1()
    scenario_2()
    scenario_3()


if __name__ == "__main__":
    main()
