import json
from pathlib import Path
from typing import List

from lab03.models import CityBus, TouristBus, ElectricBus
from lab02.model import Bus


DATA_FILE = "buses.json"


def bus_to_dict(bus: Bus) -> dict:
    """Преобразование автобуса в словарь."""

    data = {
        "type": bus.__class__.__name__,
        "route_number": bus.route_number,
        "capacity": bus.capacity,
        "speed": bus.speed,
        "driver_name": bus.driver_name,
    }

    if isinstance(bus, CityBus):
        data["stops_count"] = bus._CityBus__stops_count
        data["ticket_price"] = bus._CityBus__ticket_price

    elif isinstance(bus, TouristBus):
        data["guide_name"] = bus._TouristBus__guide_name
        data["tour_price"] = bus._TouristBus__tour_price

    elif isinstance(bus, ElectricBus):
        data["battery_capacity"] = bus._ElectricBus__battery_capacity
        data["eco_level"] = bus._ElectricBus__eco_level

    return data
def dict_to_bus(data: dict) -> Bus:
    """Создание автобуса из словаря."""

    bus_type = data["type"]

    if bus_type == "CityBus":
        return CityBus(
            data["route_number"],
            data["capacity"],
            data["speed"],
            data["driver_name"],
            data["stops_count"],
            data["ticket_price"]
        )

    if bus_type == "TouristBus":
        return TouristBus(
            data["route_number"],
            data["capacity"],
            data["speed"],
            data["driver_name"],
            data["guide_name"],
            data["tour_price"]
        )

    if bus_type == "ElectricBus":
        return ElectricBus(
            data["route_number"],
            data["capacity"],
            data["speed"],
            data["driver_name"],
            data["battery_capacity"],
            data["eco_level"]
        )

    raise ValueError(f"Неизвестный тип автобуса: {bus_type}")

def save_buses(buses: List[Bus], filepath: str = DATA_FILE) -> None:
    """Сохранение автобусов в JSON."""

    data = [bus_to_dict(bus) for bus in buses]

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)



def load_buses(filepath: str = DATA_FILE) -> List[Bus]:
    """Загрузка автобусов из JSON."""

    path = Path(filepath)

    if not path.exists():
        return []

    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)

    return [dict_to_bus(item) for item in data]