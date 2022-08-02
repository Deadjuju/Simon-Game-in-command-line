from time import sleep


class View:
    """ Program views (user interaction) """

    @classmethod
    def welcome(cls) -> None:
        print("---------- Jeu du Simon ----------")
        sleep(1)

    @classmethod
    def display_sequence(cls, sequence: str) -> None:
        print("_" * 30)
        print("Retenez la séquence... ")
        sleep(1)
        print(sequence)
        sleep(3)

    @classmethod
    def prompt_user_sequence(cls) -> str:
        return input("Votre proposition ->| ")

    @classmethod
    def display_congratulation(cls, score: int) -> None:
        print(f"Bonne réponse, votre score est : {score}")
        sleep(2)

    @classmethod
    def display_game_over(cls, correct_sequence: str, score: int) -> None:
        print(f"Mauvaise réponse, la séquence était : {correct_sequence}, votre score final : {score}")
        sleep(2)

    @classmethod
    def prompt_to_user_another_part(cls) -> None:
        print("\nVoulez-vous faire une nouvelle partie?")
        return input("Tappez  'o'  pour oui -->| ")
    
    @classmethod
    def see_you_soon(cls) -> None:
        print("A bientôt!!!")
        sleep(0.5)

    @classmethod
    def display_fake_loader(cls) -> None:
        print("Initialize a part: |_", end="")
        for _ in range(15):
            sleep(0.07)
            print("_", end="", flush="True")
        print(" !!! Nouvelle partie !!!")
        sleep(0.8)
