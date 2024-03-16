from src.enumerations.brand import Brand
from src.enumerations.color import Color
from src.enumerations.model import Model
from src.models.base.vehicle import Vehicle


class VehicleFactory:

    @staticmethod
    def create_vehicle(brand: Brand, model: Model, color: Color) -> Vehicle:
        return Vehicle(brand, model, color)
