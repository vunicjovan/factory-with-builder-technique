from abc import ABC, abstractmethod


class AbstractVehicle(ABC):

    @abstractmethod
    def start(self) -> None:
        ...

    @abstractmethod
    def drive(self, distance: int) -> None:
        ...

    @abstractmethod
    def turn(self, direction: str) -> None:
        ...

    @abstractmethod
    def accelerate(self, target: int) -> None:
        ...

    @abstractmethod
    def brake(self, target: int) -> None:
        ...

    @abstractmethod
    def change_gear(self, current_gear: int, target_gear: int) -> None:
        ...

    @abstractmethod
    def cruise_control(self, set_speed: int) -> None:
        ...

    @abstractmethod
    def stop(self) -> None:
        ...
