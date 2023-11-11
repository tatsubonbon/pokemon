from abc import ABC, abstractclassmethod
from typing import List

from model.base.attack import AttackPower
from model.base.attribute import Attribute
from model.base.damage import Damage
from model.base.defense import DefensePower
from model.base.hp import HP
from model.base.speed import Speed
from model.base.tequnique import Tequnique
from repojitory.pokemonRepojitory import PokemonRepojitory
from repojitory.tequniqueRepojitory import TequniqueRepojitory


# ポケモンベースクラス
class Pokemon(ABC):
    def __init__(self):
        pokemonRepojitory = PokemonRepojitory()
        tequniqueRepojitory = TequniqueRepojitory()
        pokemon_data = pokemonRepojitory.get_pokemon(self.pokemon_id())

        # 名前
        self._name: str = pokemon_data["name"]
        # タイプ
        self._attribute: List[Attribute] = pokemon_data["attribute"]
        # HP
        self._hp: HP = HP(pokemon_data["hp"], pokemon_data["hp"])
        # 素早さ
        self._speed: Speed = Speed(pokemon_data["speed"])
        # 攻撃力
        self._attackPower: AttackPower = AttackPower(pokemon_data["attack"])
        # 防御力
        self._defensePower: DefensePower = DefensePower(pokemon_data["defense"])
        # 技
        self._tequniques: List[Tequnique] = [
            Tequnique(
                tequniqueRepojitory.get_tequnique(tequnique_id)["name"],
                tequniqueRepojitory.get_tequnique(tequnique_id)["power"],
                tequniqueRepojitory.get_tequnique(tequnique_id)["attribute"],
            )
            for tequnique_id in pokemon_data["tequniques"]
        ]

    @abstractclassmethod
    def pokemon_id(self) -> str:
        raise ValueError("実装してください")

    @property
    def name(self) -> str:
        return self._name

    @property
    def attribute(self) -> List[Attribute]:
        return self._attribute

    @property
    def hp(self) -> HP:
        return self._hp

    @property
    def speed(self) -> Speed:
        return self._speed

    @property
    def attackPower(self) -> AttackPower:
        return self._attackPower

    @property
    def defensePower(self) -> DefensePower:
        return self._defensePower

    @property
    def tequniques(self) -> List[Tequnique]:
        return self._tequniques

    def attack(self, tequniqueIndex: int, targetPokemon: "Pokemon") -> None:
        print(self.name + "の" + self.tequniques[tequniqueIndex].name)
        damage = Damage(
            self._attackPower,
            self._tequniques[tequniqueIndex],
            targetPokemon.defensePower,
        )
        targetPokemon.damaged(damage)

    def damaged(self, damage: Damage) -> None:
        try:
            self._hp = self._hp.damaged(damage)
            print(self.name + " " + "HP: " + str(self.hp.hp))
        except ValueError:
            raise ValueError(self.name + "は倒れた")
