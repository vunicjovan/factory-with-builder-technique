from random import choice
from typing import Any

from src.enumerations.brand import Brand
from src.enumerations.color import Color
from src.enumerations.fuel import Fuel
from src.enumerations.gearshift_type import Gearshift
from src.enumerations.model import Model
from src.factories.vehicle_factory import VehicleFactory
from src.models.base.vehicle import Vehicle


class Randomizer:

    @classmethod
    def __random_choice(cls, collection: Any) -> Any:
        if not isinstance(collection, list):
            collection = list(collection)

        return choice(collection)

    @classmethod
    def __produce_random_vehicle(cls) -> Vehicle:
        random_brand = cls.__random_choice(Brand)
        random_model = cls.__random_choice(Model.models_for_brand(random_brand))
        random_color = cls.__random_choice(Color)

        random_vehicle = VehicleFactory.create_vehicle(random_brand, random_model, random_color)

        random_gearshift_type = cls.__random_choice(Gearshift)
        match random_gearshift_type:
            case Gearshift.MANUAL:
                random_vehicle = random_vehicle.manual()
            case Gearshift.AUTOMATIC:
                random_vehicle = random_vehicle.automatic()

        random_fuel_source = cls.__random_choice(Fuel)
        match random_fuel_source:
            case Fuel.DIESEL:
                random_vehicle = random_vehicle.diesel()
            case Fuel.PETROL:
                random_vehicle = random_vehicle.petrol()
            case Fuel.ELECTRIC:
                random_vehicle = random_vehicle.electric()

        return random_vehicle

    @classmethod
    def produce_random_vehicles(cls, number_of_vehicles: int) -> list[Vehicle]:
        random_vehicles = []

        while number_of_vehicles > 0:
            random_vehicle = Randomizer.__produce_random_vehicle()
            random_vehicles.append(random_vehicle)
            number_of_vehicles -= 1

        return random_vehicles
