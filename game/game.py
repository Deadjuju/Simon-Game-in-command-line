import os

from simon.simon import Simon
from view.view import View


class Game:

    def __init__(self) -> None:
        self.simon: Simon = Simon()
        self.view = View()
    
    @classmethod
    def _clear_screen(cls) -> None:
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')

    def _turn(self) -> bool:
        """ course of a turn """

        Game._clear_screen()
        self.simon.update_sequence()
        self.view.display_sequence(sequence=self.simon.sequence)
        Game._clear_screen()
        user_sequence = self.view.prompt_user_sequence()

        return bool(user_sequence == self.simon.sequence)

    def _congratulate(self) -> None:
        self.simon.update_score()
        self.view.display_congratulation(score=self.simon.score)

    def _game_over(self) -> bool:
        self.view.display_game_over(
                    correct_sequence=self.simon.sequence,
                    score=self.simon.score
                    )
        return False

    def _play_again(self) -> bool:
        user_choice = self.view.prompt_to_user_another_part()
        if user_choice.lower() == "o" or user_choice.lower() == "oui":
            return True
        return False
    
    def _load_new_part(self):
        self.simon.initialize_simon()
        self.view.display_fake_loader()
        self.run()

    def run(self):
        """ course of the game """

        self.view.welcome()
        is_game_running: bool = True
        while is_game_running:
            is_correct_sequence: bool = self._turn()
            if is_correct_sequence:
                self._congratulate()
            else:
                is_game_running = self._game_over()

        if self._play_again():
            self._load_new_part()
        else:
            self.view.see_you_soon()
