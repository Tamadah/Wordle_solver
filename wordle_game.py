"""
todo: Make it so that the guess word will only include the words from a specific bank
Create a menu for the game to be played multiple time
Store the guesses taken in the round
Improve the looks of the game in terminal to match the nyc wordle site
"""

import random
from colorama import Fore, Back, Style

# this class plays wordle using a word bank in the word_history.txt file
class wordle:
    def __init__(self):
        self.guess = ''
        self.hints_guess = [0] * 5
        self.guesses = []

        self.answer = ''
        self.attempt_count = 0
        self.round_won = False

        self.word_bank = []
        self.__open_word_bank()

    def play_wordle(self):
        pass

    def start_round(self):
        self.start_wordle()
        playing = True
        while playing:
            self.guess_word()
            self.verify_word()
            self.result_from_guess()

            if self.attempt_count >= 5 or self.round_won == True:
                playing = False
        if self.round_won:
            print("you win")
        else:
            print("you lose")



    def start_wordle(self):
        # goes through the word bank (word_history.txt) and choose a random word as the answer 
        choice = random.randint(0, len(self.word_bank) - 1)
        self.answer = self.word_bank[choice]
        print(choice, self.answer)
        self.attempt_count = 0
        self.round_won = False

    def guess_word(self):
        # guess the word and throw it to be verified for conditions
        condition = True
        while condition:
            choice = input("Guess word:")
            if len(choice) != 5:
                print("Error: Guess must be a 5 letter word")
            elif choice.isalpha() == False:
                print("Error: Guess must only include alphabetical characters")
            else:
                condition = False
        self.guess = choice.upper()
        self.attempt_count += 1

    def verify_word(self):
        # takes the guessed word and compare it to the answer.
        self.hints_guess = [0] * 5
        count = 0
        for i in range(len(self.answer)):
            if self.guess[i] in self.answer:
                self.hints_guess[i] = 1
        for i in range(len(self.answer)):
            if self.guess[i] == self.answer[i]:
                self.hints_guess[i] = 2
                count += 1

        if count == 5:
            self.round_won = True

    def result_from_guess(self):
        # shows the result of the guess and hint clues for any correct letter
        for i in range(len(self.guess)):
            match self.hints_guess[i]:
                case 0:
                    print(Style.RESET_ALL + f"{self.guess[i]}", end= '')
                case 1:
                    print(Back.YELLOW + Style.BRIGHT + Fore.WHITE + f"{self.guess[i]}", end= '')
                case 2:
                    print(Back.GREEN + Style.BRIGHT + Fore.WHITE + f"{self.guess[i]}", end= '')
        print(Style.RESET_ALL)

            
    # private method 
    def __open_word_bank(self):
        with open("word_history.txt", 'r') as file:
            for line in file:
                self.word_bank.append(line[:-1])



def main():
    bruh = wordle()
    # print(bruh.word_bank)
    bruh.start_round()
    # print(bruh.guess)
    # print(bruh.hints_guess)
    input("enter to end")

    



if __name__ == "__main__":
    main()



