from model.base.attack import AttackPower
from model.base.damage import Damage
from model.base.pokemon import Pokemon


class Garura(Pokemon):
    def pokemon_id(self) -> str:
        return "pokemon_id4"

    # 2回攻撃
    def attack(self, tequniqueIndex: int, targetPokemon: "Pokemon") -> None:
        print(self.name + "の" + self.tequniques[tequniqueIndex].name)
        damage = Damage(
            self.attackPower,
            self.tequniques[tequniqueIndex],
            targetPokemon.defensePower,
        )
        targetPokemon.damaged(damage)
        # 2回目の攻撃
        print(self.name + "の" + self.tequniques[tequniqueIndex].name + "2回目")
        damage2 = Damage(
            AttackPower(self.attackPower.power / 5),
            self.tequniques[tequniqueIndex],
            targetPokemon.defensePower,
        )
        targetPokemon.damaged(damage2)
