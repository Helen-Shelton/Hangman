import hangman_art
import hangman_words
import random
#could also use: from Hangman_art import logo,stages
#this will allow us to use stages and logo without calling hangman_art.logo, etc. instead

#option below is better and shorter
chosen_word = random.choice(hangman_words.word_list)
end_game = False
lives = 6
display = []

#Testing code
print(f'{hangman_art.logo} \n Pssst, the solution is {chosen_word}.')

for letter in chosen_word:
  display += '_'
print(display) 

print(hangman_art.stages[lives])
while not end_game: 
  guess = input("Please guess a letter in the chosen word: ").lower()

  if guess in display:
    print(f" \nYou have already entered '{guess}', please try again. \n")
  else:
    for i in range(len(chosen_word)):
      if guess == chosen_word[i]:
        display[i] = guess

    if guess not in chosen_word:
      lives -= 1
      print(f"\n{guess} is not in the word")
      if lives == 0:
        end_game = True
        print("\nYou Lose :( ")

    if '_' not in display:
      end_game = True
      print("\nYou Win!")
    
  print(f"{hangman_art.stages[lives]} \n{display} \n") 
  
print("Done")