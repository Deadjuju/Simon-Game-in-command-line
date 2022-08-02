from random import randint


class Simon:

    INITIAL_CHARACTERS_NUMBER: int = 3

    def __init__(self) -> None:
        self.sequence: str = ""
        self._initial_sequence()
        self.score: int = 0

    @classmethod
    def _generate_random_sequence_piece(cls) -> str:
        """ Generates a random number between 0 and 9 in string format """
        return str(randint(0, 9))

    def _initial_sequence(self) -> None:
        for _ in range(Simon.INITIAL_CHARACTERS_NUMBER):
            self.update_sequence()

    def update_sequence(self) -> None:
        self.sequence += Simon._generate_random_sequence_piece()
    
    def update_score(self) -> None:
        self.score += 1

    def initialize_simon(self) -> None:
        self.sequence = ""
        self._initial_sequence()
        self.score = 0
