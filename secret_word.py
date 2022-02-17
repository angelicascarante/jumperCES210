import random

class SecretWord:
    """
    Read the words from an outside file and return one of those words, randomly chosen
    """

    def __init__(self):

        with open("words.txt", "r") as f:
            words_list = []

            for line in f:
                words_list.append(line.rstrip('\r\n'))

            self.word = random.choice(words_list)

    def display(self, guessed_letters_list):
        """
        Function to display the secret word with the letters that have been correctly guessed.
        """

        word_to_display = ""

        for letter in self.word:
            if letter in guessed_letters_list:
                word_to_display += " " + letter + " "

            else:
                word_to_display += " _ "
        print()
        print(word_to_display)
        print()
        return word_to_display
