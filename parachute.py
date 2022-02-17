class Parachute:

    PARACHUTE_STATES = [
        '''
  ___ 
 /___\\
 \   /
  \ /
   O
  /|\\
  / \\
^^^^^^^
        ''',
        '''
   
 /___\\
 \   /
  \ /
   O
  /|\\
  / \\
^^^^^^^
        ''',
        '''
  ___
 \   /
  \ /
   O
  /|\\
  / \\
^^^^^^^
        ''',
        '''
 
 \   /
  \ /
   O
  /|\\
  / \\
^^^^^^^
        ''',
        '''
 
  \ /
   O
  /|\\
  / \\
^^^^^^^
        ''',
        '''
   X
  /|\\
  / \\
^^^^^^^
        ''',
    ]
    def __init__(self):
        self.hangman = self.PARACHUTE_STATES[0]

    def draw(self, num_incorrect_guesses_made):
        """
        Function to display the updated status of the hangman based on the number of incorrect guesses the player has made.
        """

        self.hangman = self.PARACHUTE_STATES[num_incorrect_guesses_made]
        print(self.hangman)
