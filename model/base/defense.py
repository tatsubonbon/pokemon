# 防御力
class DefensePower:
    def __init__(self, power: int):
        self._power = power

    @property
    def power(self) -> int:
        return self._power
