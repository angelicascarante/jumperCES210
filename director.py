from game.terminal_service import TerminalService
from game.secret_word import SecretWord
from game.parachute import Parachute


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    Attributes:
        paraschute (Parachute): The drawings of the skydiver with his parachute.
        is_playing (boolean): Whether or not to keep playing.
        secret_word (SecretWord): the randomly selected secret word of the game.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._parachute = Parachute()
        self._is_playing = True
        self._secret_word = SecretWord()
        self._terminal_service = TerminalService()
        self.num_incorrect_guesses_made = 0
        self.guessed_letters = []

    def start_game(self):
        while self.num_incorrect_guesses_made < 5:
            if len(self.guessed_letters) == 0:
                self._secret_word.display(self.guessed_letters)

            self._parachute.draw(self.num_incorrect_guesses_made)
            letter_guess = self._terminal_service.read_text("Guess a letter [a-z]: ")

            # Don't let them guess a non-alpha letter.
            while letter_guess.isalpha() is False:
                letter_guess = self._terminal_service.read_text("No special characters allowed! Only enter a letter, please: ").lower()

            # Once a valid letter is chosen, add it to guessed_letters
            if letter_guess not in self.guessed_letters:
                self.guessed_letters.append(letter_guess)

                if letter_guess not in self._secret_word.word:
                    self.num_incorrect_guesses_made += 1
                    self._parachute.draw(self.num_incorrect_guesses_made)

                else:
                    self._parachute.draw(self.num_incorrect_guesses_made)

            else:
                self._terminal_service.write_text("You've already guessed the letter '%s', please choose a new letter." % letter_guess)

            current_word = self._secret_word.display(self.guessed_letters)

            print("These are the letters you've already guessed: ", self.guessed_letters)

            if "_" not in current_word:
                self._terminal_service.write_text("Congratulations! You've won!\n")
                break
