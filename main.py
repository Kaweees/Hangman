import random
import math

letters_left = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
answer = [""]

#picking an anime
def animeanswer():
  animes = ["naruto", "sailor moon", "one piece", "yu-gi-oh!", "sword art online", "pokemon", "jojo's bizarre adventure", "one-punch man", "attack on titan",  "neon genesis evangelion"]
  global answer
  anime_answer_number = random.randint(1,10)
  answer[0] = str(animes[anime_answer_number - 1])
  return answer

#picking a tv show

def tvshowanswer():
 global answer
 tvshows = ["the 100", "criminal minds", "game of thrones", "grey's anatomy", "the big bang theory", "this is us", "the good doctor", "america’s got talent", "the simpsons",  "the flash"]
 tvshownumber = random.randint(1,10)
 answer = str(tvshows[tvshownumber - 1])
 return answer

def start_sequence():
  topic = input("\nWhat topic would you like to pick? ")
  if topic.lower() == "anime":
      animeanswer()
  elif topic.lower() == "tv show" or topic.lower() == "tv" or  topic.lower() == "television show" or  topic.lower() == "television shows" or        topic.lower() == "tv shows":
    tvshowanswer()
  else:
    print("\nI'm not sure what that means. ")
word = ""
start_sequence()
letters_left_in_answer = []
for letter in answer:
  letters_left_in_answer.append(letter)
  word += " _ "
gameresult = "not defined"
while gameresult == "not defined":
  guessesleft = 10
  guessedletters = []
  hangman = '''   ____
  |    |      Guesses left: %s left
  |           Guessed : %s 
  |           Average :  50%
  |           Word: %s
  |   
 _|_
|   |______
|          |
|__________|'''% (str(guessesleft), str(guessedletters), word)
while True:
  guess = input("Guess a letter: ")
  if guess[0] in letters_left:
    guessedletters.append(guess[0])
    guessesleft -= 1
    if guess[0] in letters_left_in_answer:
      letters_left_in_answer.remove(guess[0])
  elif guess[0] in guessedletters:
    print("you already guessed that letter")
  else:
    print("That is not a letter")
  
  win = False
  