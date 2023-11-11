# 攻撃力
class AttackPower:
    def __init__(self, power: int):
        self._power = power

    @property
    def power(self) -> int:
        return self._power
