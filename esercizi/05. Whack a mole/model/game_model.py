class Hole:
    """Un singolo buco della griglia."""

    def __init__(self) -> None:
        self.is_active = False

    def toggle(self) -> None:
        self.is_active = not self.is_active


class GameModel:
    """Stato complessivo del gioco."""

    NUM_HOLES = 9

    def __init__(self) -> None:
        self.holes = [Hole() for _ in range(GameModel.NUM_HOLES)]

    def toggle_hole(self, index: int) -> None:
        if 0 <= index < GameModel.NUM_HOLES:
            self.holes[index].toggle()
        else:
            print(f"\nIndice {index} non trovato.\n")
