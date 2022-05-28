from progression import Progression

class ArithmeticProgression(Progression):
    """Iterator producing an arithmetic progression."""

    def __init__(self, increment=1, start=0):
        """
        Create a new arithmetic progression.

        increment the fixed constant to add to each term (default 1)
        start the first term of the progression (default 0)
        """
        
        super().__init__(start)
        self._increment = increment
    
    def _advance(self): # override inherited version
        """Update current value by adding the fixed increment."""
        self._current += self._increment


if __name__ == "__main__" :
    print(" Default progression: ")
    Progression().print_progression(10)

    print("Arithmetic progression with increment 5: ")
    ArithmeticProgression(5).print_progression(10)

    print("Arithmetic progression with increment 5 and start 2: ")
    ArithmeticProgression(5, 2).print_progression(10)
