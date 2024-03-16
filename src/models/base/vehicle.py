from typing import Self

from src.enumerations.brand import Brand
from src.enumerations.color import Color
from src.enumerations.fuel import Fuel
from src.enumerations.gearshift_type import Gearshift
from src.enumerations.model import Model
from src.models.abstraction.abstract_vehicle import AbstractVehicle


class Vehicle(AbstractVehicle):

    def __init__(self, brand: Brand, model: Model, color: Color) -> None:
        self.__brand: Brand = brand
        self.__model: Model = model
        self.__color: Color = color
        self.__gearshift = None
        self.__fuel = None

    def __str__(self) -> str:
        return (f"{self.__color} {self.__brand} {self.__model} "
                f"with {self.__gearshift} gearshift, "
                f"running on {self.__fuel}.")

    def __to_dict__(self) -> dict:
        return {
            "brand": self.__brand,
            "model": self.__model,
            "color": self.__color,
            "gearshift_type": self.__gearshift,
            "fuel_source": self.__fuel,
        }

    def manual(self) -> Self:
        self.__gearshift = Gearshift.MANUAL
        return self

    def automatic(self) -> Self:
        self.__gearshift = Gearshift.AUTOMATIC
        return self

    def diesel(self) -> Self:
        self.__fuel = Fuel.DIESEL
        return self

    def petrol(self) -> Self:
        self.__fuel = Fuel.PETROL
        return self

    def electric(self) -> Self:
        self.__fuel = Fuel.ELECTRIC
        return self

    def start(self) -> None:
        print(f"{self.__color} {self.__brand} {self.__model} turned its engine on.")

    def drive(self, distance: int) -> None:
        print(f"{self.__color} {self.__brand} {self.__model} is driving straight for {distance} kilometers.")

    def turn(self, direction: str) -> None:
        print(f"{self.__color} {self.__brand} {self.__model} is turning {direction}.")

    def accelerate(self, target: int) -> None:
        print(f"{self.__color} {self.__brand} {self.__model} is speeding up to {target} km/h.")

    def brake(self, target: int) -> None:
        print(f"{self.__color} {self.__brand} {self.__model} is slowing down to {target} km/h.")

    def change_gear(self, current_gear: int, target_gear: int) -> None:
        print(f"{self.__color} {self.__brand} {self.__model} is changing gear from {current_gear} to {target_gear}.")

    def cruise_control(self, set_speed: int) -> None:
        print(f"{self.__color} {self.__brand} {self.__model} is using cruise control set to {set_speed} km/h.")

    def stop(self) -> None:
        print(f"{self.__color} {self.__brand} {self.__model} turned its engine off.")
