from model.base.attribute import Attribute


class TequniqueRepojitory:
    def __init__(self) -> None:
        self.tequniques = {
            "tequniqu_id1": {
                "name": "体当たり",
                "power": 50,
                "attribute": Attribute.NORMAL,
            },
            "tequniqu_id2": {
                "name": "10万ボルト",
                "power": 60,
                "attribute": Attribute.DENKI,
            },
            "tequniqu_id3": {
                "name": "はねる",
                "power": 0,
                "attribute": Attribute.NORMAL,
            },
        }

    def get_tequnique(self, id: str):
        return self.tequniques.get(id)
