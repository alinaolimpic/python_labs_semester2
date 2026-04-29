from lab02.model import Bus
from lab04.interfaces import Printable, Comparable
class CityBus(Bus, Printable, Comparable):
    def __init__(self, route_number, capacity, speed, driver_name,
                 stops_count, ticket_price):
        super().__init__(route_number, capacity, speed, driver_name)
        self.__stops_count = stops_count
        self.__ticket_price = ticket_price

    def calculate_income(self):
        return self.passenger_count * self.__ticket_price

    def process(self):
        return f"Городской автобус: доход = {self.calculate_income()}"

    # ===== Printable =====
    def to_string(self):
        return f"[CityBus] Маршрут {self.route_number}, пассажиры: {self.passenger_count}"

    # ===== Comparable =====
    def compare_to(self, other):
        return self.calculate_income() - other.calculate_income()
    def __str__(self):
        return f"[Городской] {super().__str__()} | остановок: {self.__stops_count}"


class TouristBus(Bus, Printable, Comparable):
    def __init__(self, route_number, capacity, speed, driver_name,
                 guide_name, tour_price):
        super().__init__(route_number, capacity, speed, driver_name)
        self.__guide_name = guide_name
        self.__tour_price = tour_price

    def calculate_income(self):
        return self.passenger_count * self.__tour_price

    def process(self):
        return f"Туристический автобус: доход = {self.calculate_income()}"

    def to_string(self):
        return f"[TouristBus] Гид: {self.__guide_name}, пассажиры: {self.passenger_count}"

    def compare_to(self, other):
        return self.calculate_income() - other.calculate_income()

    def __str__(self):
        return f"[Туристический] {super().__str__()} | гид: {self.__guide_name}"


class ElectricBus(Bus, Printable, Comparable):
    def __init__(self, route_number, capacity, speed, driver_name,
                 battery_capacity, eco_level):
        super().__init__(route_number, capacity, speed, driver_name)
        self.__battery_capacity = battery_capacity
        self.__eco_level = eco_level

    def calculate_income(self):
        return self.passenger_count * 20 + self.__eco_level * 10

    def process(self):
        return f"Электробус: доход = {self.calculate_income()}"

    def to_string(self):
        return f"[ElectricBus] ECO={self.__eco_level}, пассажиры: {self.passenger_count}"

    def compare_to(self, other):
        return self.calculate_income() - other.calculate_income()

    @property
    def eco_level(self):
        return self.__eco_level

    def __str__(self):
        return f"[Электробус] {super().__str__()} | батарея: {self.__battery_capacity}"