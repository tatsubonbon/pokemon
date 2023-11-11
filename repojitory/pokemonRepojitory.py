from model.base.attribute import Attribute


class PokemonRepojitory:
    def __init__(self) -> None:
        self.pokemons = {
            "pokemon_id1": {
                "name": "ピカチュウ",
                "attribute": [
                    Attribute.DENKI,
                ],
                "hp": 100,
                "speed": 100,
                "attack": 30,
                "defense": 30,
                "tequniques": ["tequniqu_id1", "tequniqu_id2"],
            },
            "pokemon_id2": {
                "name": "ヒトカゲ",
                "attribute": [
                    Attribute.HI,
                ],
                "hp": 150,
                "speed": 100,
                "attack": 50,
                "defense": 50,
                "tequniques": ["tequniqu_id1", "tequniqu_id2"],
            },
            "pokemon_id3": {
                "name": "コイキング",
                "attribute": [
                    Attribute.MIZU,
                ],
                "hp": 100,
                "speed": 30,
                "attack": 30,
                "defense": 30,
                "tequniques": ["tequniqu_id3"],
            },
            "pokemon_id4": {
                "name": "ガルーラ",
                "attribute": [
                    Attribute.NORMAL,
                ],
                "hp": 200,
                "speed": 30,
                "attack": 30,
                "defense": 30,
                "tequniques": ["tequniqu_id1"],
            },
        }

    def get_pokemon(self, id: str):
        return self.pokemons.get(id)
