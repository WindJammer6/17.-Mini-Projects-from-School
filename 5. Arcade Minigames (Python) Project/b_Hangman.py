import random as rd
def main():
    while True:
        dude = ['''
         +-------+
                 |
                 |
                 |
                 |
                 |
               =====''', '''
         +-------+
         |       |
                 |
                 |
                 |
                 |
               =====''', '''    
         +-------+
         |       |
         0       |
                 |
                 |
                 |
               =====''', '''
         +-------+
         |       |
         0       |
         |       |
                 |
                 |
               =====''', '''
         +-------+
         |       |
         0       |
        /|\      |
                 |
                 |
               =====''', '''
         +-------+
         |       |
         0       |
        /|\      |
        / \      |
                 |
               =====''', '''
             +-------+
                     |
                     |
         0           |
        \|  __       |
         |  __       |
        / \        =====''']
        dude.reverse()
        # starting words
        animal = "elephant", "cat", "dog", "penguin"
        movie = "avengers", "star" + "wars", "the" + "conjuring", "toy" + "story"
        SUTD = "jerry", "bernie", "sock", "jackie" + "chan"
        print("Animal,", "Movie,", "SUTD")

        # user input of the category
        category = True
        word = []
        words = input("Choose the category\n")

        # randomise a word based on the category
        while category:
            if words.lower() == "animal":
                word = rd.choice(animal)
                break
            elif words.lower() == "movie":
                word = rd.choice(movie)
                break
            elif words.lower() == "sutd":
                word = rd.choice(SUTD)
                break
            # Ensure only one of the 3 categories are chosen
            else:
                words = (input("Choose a right category\n"))

        # list the word in the alphabet
        letter_list = list(word)
        checking_list = list(word)
        print("It is a", len(letter_list), "letter word")

        # storing of the letter inputs
        wrong_letter = []
        tries = 6
        blanks = ["_"] * len(letter_list)

        # guessing code
        game_over = False
        while not game_over and tries > 0:
            print("You have", tries, "lives")
            # winning condition
            if blanks == checking_list:
                print(dude[0])
                print("You have won, the word is", word)
                break
            # player guess a letter
            guess_letter = input("Guess a letter\n")
            # correct guesses
            if guess_letter in letter_list:
                # prevent repeated guesses
                if guess_letter in (wrong_letter or blanks):
                    print("You have already guessed this letter")
                else:
                    print('You are correct!')
                # replace blanks with the guessed letter
                for i in letter_list:
                    if i == guess_letter:
                        obtained_index = letter_list.index(i)
                        letter_list[obtained_index] = None
                        blanks[obtained_index] = guess_letter
                print(blanks)
            # wrong guesses
            elif guess_letter not in letter_list:
                # prevent repeated guesses
                if guess_letter in (wrong_letter or blanks):
                    print("You have already guessed this letter")
                else:
                    print('You are wrong')
                    wrong_letter.append(guess_letter)
                    print(wrong_letter)
                    tries -= 1
                    print(dude[tries + 1])
                    # last try after numerous wrong letters
                    if tries == 1:
                        last_try = input("You have 1 life, try to guess the full word\n")
                        if last_try == word:
                            print(dude[0])
                            print("You have won, the word is", word)
                            break
                        else:
                            print(dude[tries])
                            print("Game Over")
                            break
        while True:
            answer = str(input("Do you want to play again? (y/n): \n"))
            if answer in ('y', 'n'):
                break
            else:
                print("invalid input")
        if answer == 'y':
            continue
        else:
            print("Goodbye")
            break
            
