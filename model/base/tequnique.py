from abc import ABC, abstractmethod

from model.base.attribute import Attribute

# 技ベースクラス
# class Tequnique:
#     @abstractmethod
#     def name(self) -> str:
#         raise NotImplementedError

#     @abstractmethod
#     def power(self) -> int:
#         raise NotImplementedError

#     @abstractmethod
#     def attribute(self) -> "Attribute":
#         raise NotImplementedError


class Tequnique:
    def __init__(self, name: str, power: int, attribute: Attribute) -> None:
        self._name = name
        self._power = power
        self._attribute = attribute

    @property
    def name(self) -> str:
        return self._name

    @property
    def power(self) -> int:
        return self._power

    @property
    def attribute(self) -> Attribute:
        return self._attribute
