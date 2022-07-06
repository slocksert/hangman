import requests
import random
import string


class Game:
    
    def __init__(self):
        self.api = 'https://www.randomlists.com/data/words.json'

    def get_data(self):
        response = requests.get(self.api)
        if response.status_code == 200:
            data = response.json()
            return data['data']

        else:
            print(f"Hello, there's a {response.status_code} error with your request")

    def get_valid_word(self, data):
        self.word = random.choice(data)
        while '-' in self.word or ' ' in self.word:
            self.word = random.choice(data)

        return self.word.upper()

    def hangman(self, word):
        word_letters = set(self.word.upper()) #letters in the word
        alphabet = set(string.ascii_uppercase)
        used_letters = set() #what the user has guessed

        lives = 6

        #getting user input
        while len(word_letters) > 0 and lives > 0:
            print(f'You have {lives} lives left and you have used these letters:', ''.join(used_letters))

            word_list = [letter if letter in used_letters else '-' for letter in word]
            print('\nCurrent word:', ' '.join(word_list))

            user_letter = input('\nGuess a letter: ').upper()
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)

                else:
                    lives -= 1
                    print('\nLetter is not in the word')
            elif user_letter in used_letters:
                print('You have already used that character.')
            
            else:
                print('Invalid character.')
        
        play_again = ''
   
        if lives == 0:
            print(f'\nYou died! the word was {word}')
            play_again = input('\nWanna play again? y/n: ').lower()     
            if play_again !='y':
                quit('Okay Bye!')
            else:
             Game().call_class()

        else:
            print(f'\nYou guessed the word {word}')
            play_again = input('\nWanna play again? y/n: ').lower()
            if play_again !='y':
                quit('Okay Bye!')
            else:
             Game().call_class()

    def call_class(self):
        word = Game()
        data = word.get_data()
        valid_word = word.get_valid_word(data)
        hangman = word.hangman(valid_word)

dashs = '-' * 40







