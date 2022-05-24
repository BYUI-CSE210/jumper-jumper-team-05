class Parachute:
    """This will display the parachute and keep track of life.
    """
     
    def __init__(self):
        self._missing_pieces = 0
        self._pieces = ["  ___", " /   \\", "  ___", " \\   /", "  \\ /"]

    def chute(self, missing_pieces=0):
        printing = 0 + missing_pieces
        while printing < 5:
            print(self._pieces[printing])
            printing += 1