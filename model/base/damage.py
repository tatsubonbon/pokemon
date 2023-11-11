from model.base.attack import AttackPower
from model.base.defense import DefensePower
from model.base.tequnique import Tequnique


class Damage:
    def __init__(
        self, attackPower: AttackPower, tequnique: Tequnique, defensePower: DefensePower
    ) -> None:
        self._damage = attackPower.power * tequnique.power / defensePower.power

    @property
    def value(self) -> float:
        return self._damage
