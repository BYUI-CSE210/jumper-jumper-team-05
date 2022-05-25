import random


class Puzzle:
    """This gets us the random word that the user has to guess
    and it keeps track of the letters.
    """

    def __init__(self):
        """Constructs a Puzzle.

        Args:
            self (Puzzle): an instance of Puzzle.

        Attributes:
            _list_words(list): One list with all the words that the game will use
            for the gamer guess it.

        """
        self._list_words = ['house', 'fish', 'encapsulation']

    def get_word(self):
        """
        This function get one word of the list of words and return it
        """

        word = random.choice(self._list_words).lower()
        return word
