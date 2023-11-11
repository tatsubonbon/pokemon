from model.base.damage import Damage


# HP
class HP:
    def __init__(self, hp: int, max_hp: int):
        self._hp = hp
        self._max = max_hp

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def max(self) -> int:
        return self._max

    # 回復
    def heal(self, heal_point) -> "HP":
        hp = self._hp + heal_point
        if hp > self._max:
            hp = self._max
        return HP(hp, self._max)

    # ダメージを受ける
    def damaged(self, damage: Damage) -> "HP":
        hp = self._hp - damage.value
        if hp <= 0:
            raise ValueError("HPが0になりました。")
        return HP(hp, self._max)
