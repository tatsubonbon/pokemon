# 素早さ
class Speed:
    def __init__(self, speed: int):
        self._speed = speed

    @property
    def speed(self) -> int:
        return self._speed
