from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any
from ..Types import Type
from pygame import Vector2

class Builder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_type(self) -> None:
        pass

    @abstractmethod
    def produce_position(self) -> None:
        pass

    @abstractmethod
    def produce_speed(self) -> None:
        pass
    
    @abstractmethod
    def produce_sprite(self) -> None:
        pass
    
    @abstractmethod
    def produce_surface(self) -> None:
        pass