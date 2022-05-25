class Parachute:
    """This will display the parachute and keep track of life.
    """

    def __init__(self):
        """Constructs a new Parachute

        Args:
            self (Parachute): an instance of Parachute.

        Attributes:
            _missing_pieces (int): every number is one lose life.
            _pieces(list): One list of all the pieces for the above part of parachute.

        """
        self._missing_pieces = 0
        self._pieces = ["  ___", " /   \\", "  ___", " \\   /", "  \\ /"]

    def chute(self, missing_pieces=0):
        """This function is to draw the top part of parachute.
    """
        printing = 0 + missing_pieces
        while printing < 5:
            print(self._pieces[printing])
            printing += 1
