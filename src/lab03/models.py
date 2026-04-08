from lab02.model import Bus


class CityBus(Bus):
    def __init__(self, route_number, capacity, speed, driver_name,
                 stops_count, ticket_price):
        super().__init__(route_number, capacity, speed, driver_name)

        self.__stops_count = stops_count
        self.__ticket_price = ticket_price

    def calculate_income(self):
        return self.passenger_count * self.__ticket_price

    def process(self):
        return f"Городской автобус: доход = {self.calculate_income()}"

    def __str__(self):
        return f"[Городской] {super().__str__()} | остановок: {self.__stops_count}"


class TouristBus(Bus):
    def __init__(self, route_number, capacity, speed, driver_name,
                 guide_name, tour_price):
        super().__init__(route_number, capacity, speed, driver_name)

        self.__guide_name = guide_name
        self.__tour_price = tour_price

    def calculate_income(self):
        return self.passenger_count * self.__tour_price

    def process(self):
        return f"Туристический автобус: доход = {self.calculate_income()}"

    def __str__(self):
        return f"[Туристический] {super().__str__()} | гид: {self.__guide_name}"


class ElectricBus(Bus):
    def __init__(self, route_number, capacity, speed, driver_name,
                 battery_capacity, eco_level):
        super().__init__(route_number, capacity, speed, driver_name)

        self.__battery_capacity = battery_capacity
        self.__eco_level = eco_level

    def calculate_income(self):
        # экологический бонус
        return self.passenger_count * 20 + self.__eco_level * 10

    def process(self):
        return f"Электробус: экорейтинг = {self.__eco_level}"

    def __str__(self):
        return f"[Электробус] {super().__str__()} | батарея: {self.__battery_capacity}"