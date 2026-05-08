from lab02.model import Bus
#Переопределение методов — это механизм, при котором дочерний класс заменяет 
#реализацию метода базового класса, сохраняя его интерфейс.
#Полиморфизм = один интерфейс → разные реализации
class CityBus(Bus):
    def __init__(self,route_number: str, capacity: int,speed: float, driver_name: str,stops_count: int, ticket_price: float) -> None:
        super().__init__(route_number, capacity, speed, driver_name)

        self.__stops_count:int = stops_count
        self.__ticket_price: float = ticket_price

    def calculate_income(self)-> float:
        return self.passenger_count * self.__ticket_price

    def process(self)-> str:
        return f"Городской автобус: доход = {self.calculate_income()}"

    def __str__(self)-> str:
        return f"[Городской] {super().__str__()} | остановок: {self.__stops_count}"
    
    def display(self) -> str:
        return str(self)

    def score(self) -> float:
        return float(self.speed)

class TouristBus(Bus):
    def __init__(self, route_number: str, capacity: int, speed: float, driver_name: str, guide_name: str, tour_price: float) -> None:
        super().__init__(route_number, capacity, speed, driver_name)

        self.__guide_name: str = guide_name
        self.__tour_price: float = tour_price

    def calculate_income(self)-> float:
        return self.passenger_count * self.__tour_price

    def process(self)-> str:
        return f"Туристический автобус: доход = {self.calculate_income()}"

    def __str__(self)-> str:
        return f"[Туристический] {super().__str__()} | гид: {self.__guide_name}"
    def display(self) -> str:
        return str(self)

    def score(self) -> float:
        return float(self.speed)

class ElectricBus(Bus):
    def __init__( self,route_number: str, capacity: int, speed: float, driver_name: str, battery_capacity: int, eco_level: int) -> None: 
        super().__init__(route_number, capacity, speed, driver_name)
        self.__battery_capacity: int = battery_capacity
        self.__eco_level: int = eco_level

    def calculate_income(self)-> float:
        # экологический бонус
        return self.passenger_count * 20 + self.__eco_level * 10

    def process(self)-> str:
        return f"Электробус: доход = {self.calculate_income()}, экорейтинг = {self.__eco_level}"

    def __str__(self)-> str:
        return f"[Электробус] {super().__str__()} | батарея: {self.__battery_capacity}"
 
    def display(self) -> str:
        return str(self)

    def score(self) -> float:
        return float(self.speed)

#citybus process(доход) = число пассажиров * цена билета
#touristbus pricess(доход) = число пассажиров* цена тура
#electricbus process(доход) = число пассажиров * 20+ ecobonus
