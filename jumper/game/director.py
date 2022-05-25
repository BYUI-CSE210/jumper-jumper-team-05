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
        _letter (string): The letter typed by the user 
        _wrong_guesses (int): Do the count of the wrongs when the gamer try to guess the word
        _parachute: Draw the parachute and keep track the lifes
        _puzzle: Get one word to guess from the list 
        _word: This variable save the word obtained by Puzzle class
        _show_word : one list of every letter of the chosen word 
        _word_list: one list with the "_" dashes when the letters are not guessed
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
        self._terminal_service = TerminalService()

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
        """This function is when the game start, shows the board of the word to guess, 
        and draw the parachute. 

        Args:
            self (Director): An instance of Director.
        """

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
        valid = False
        while not valid:

            self._letter = input('Type one letter (a-z): ').lower()
            valid = "a" <= self._letter <= "z" and len(self._letter) == 1
            if not valid:
                print("Error the letter should be from a to z. Type only one letter")

    def _do_updates(self):
        """This method change the "_" by the letters guessed, keep one count
        of the wrongs guessed and keep playing or end it

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

        if self._wrong_guesses >= 5:
            self._is_playing = False

        elif "_" not in self._show_word:
            self._is_playing = False

    def _do_outputs(self):
        """This method shows the parachute when the gamer lose the opportunities to guess or when is with life yet


        Args:
            self (Director): An instance of Director.
        """
        if self._wrong_guesses >= 5:
            print()
            for i in self._show_word:
                print(f"{i}", end=" ")

            print("\n\n")
            print("   X\n  /|\\\n  / \\")
            print("Sorry, you lose the game")
            print("\n^^^^^^^")

        else:
            print()
            for i in self._show_word:
                print(f"{i}", end=" ")

            print("\n\n")
            self._parachute.chute(self._wrong_guesses)
            print("   O\n  /|\\\n  / \\")

            if "_" not in self._show_word:
                print("Congrats, You win the game!!")

            print("\n^^^^^^^")
