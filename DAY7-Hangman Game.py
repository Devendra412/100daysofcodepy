import random
import hangman_words
import hangman_art

wordlist = hangman_words.wordlist
chosenword = random.choice(wordlist)
wordlen = len(chosenword)

end_of_game = False
lives = 6

print(hangman_art.logo)
print("Welcome to Hangman! You have 6 lives to guess the word.")

display = []
for i in range(wordlen):
    display += "_"
str1=""
for i in display:
    str1+=i
for i in str1:
    print(i,end=" ")
print("\nThe word is a "+str(wordlen)+" lettered word")



while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("You've already entered", guess)

    for position in range(wordlen):
        letter = chosenword[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosenword:
        print(guess," is not in the word, you lost a life")
        lives -= 1
        print("lives left:",lives)    
        if lives == 0:
            end_of_game = True
            print("YOU LOSE!!")
            print("The word was",chosenword)

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("YOU WIN!!!")

    print(hangman_art.stages[lives])

    
    