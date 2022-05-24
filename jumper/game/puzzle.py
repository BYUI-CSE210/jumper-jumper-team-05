import random

class Puzzle:
    """This gets us the random word that the user has to guess
    and it keeps track of the letters.
    """
    def __init__(self):
        self._list_words = ['house', 'fish', 'encapsulation']
        
    def get_word(self):
        word = random.choice(self._list_words).lower()
        return word