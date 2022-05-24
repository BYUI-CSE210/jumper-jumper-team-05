from game.parachute import Parachute
from game.puzzle import Puzzle

"""
    Update the code and the comments as you change the code for your game.  You will be graded on following the
    Rules listed and your program meets all of the Requirements found on 
    https://byui-cse.github.io/cse210-course-competency/encapsulation/materials/jumper-specification.html
"""


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not to keep playing.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True
        self._letter = ""
        self._wrong_guesses = 0
        self._parachute = Parachute()
        self._puzzle = Puzzle()
        self._word = self._puzzle.get_word()
        self._show_word = []
        self._word_list = []
        for i in self._word:
            self._word_list.append(i)
            self._show_word.append("_")

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._show_board()
            self._get_inputs()
            self._do_updates()

        self._do_outputs()

    def _show_board(self):
        if self._is_playing:
            print()
            for i in self._show_word:
                print(f"{i}", end=" ")

            print("\n\n")
            self._parachute.chute(self._wrong_guesses)
            print("   O\n  /|\\\n  / \\")
            print("\n^^^^^^^")

    def _get_inputs(self):
        """This function is when the user type one letter to guess the hiden word

        Args:
            self (Director): An instance of Director.
        """
        self._letter = input('Type one letter to guess the word: ').lower()

    def _do_updates(self):
        """Update this comment

        Args:
            self (Director): An instance of Director.
        """
        if self._letter in self._word_list:
            for i in range(1, self._word_list.count(self._letter)+1):
                index = self._word_list.index(self._letter)
                self._show_word[index] = self._letter
                self._word_list[index] = "_"

        else:
            self._wrong_guesses += 1

        if self._wrong_guesses >= 5 or "_" not in self._show_word:
            self._is_playing = False

    def _do_outputs(self):
        """This method is when the gamer lose the opportunities to guess

        Args:
            self (Director): An instance of Director.
        """
        if self._wrong_guesses >= 5:
            print()
            for i in self._show_word:
                print(f"{i}", end=" ")

            print("\n\n")
            print("   X\n  /|\\\n  / \\")
            print("\n^^^^^^^")

        else:
            print()
            for i in self._show_word:
                print(f"{i}", end=" ")

            print("\n\n")
            self._parachute.chute(self._wrong_guesses)
            print("   O\n  /|\\\n  / \\")
            print("\n^^^^^^^")
