import random
from words import word_list


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
game_over = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_len = len(chosen_word)

guess_word = []
for i in range(word_len):
    guess_word += "_"

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in guess_word:
        print(f"You've already guessed {guess}")

    for pos in range(word_len):
        letter = chosen_word[pos]
        if letter == guess:
            guess_word[pos] = letter
    print(f"{' '.join(guess_word)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")
    
    if not "_" in guess_word:
        game_over = True
        print("You win.")

    print(stages[lives])
