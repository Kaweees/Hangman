import random
#adding color to the program
from colorama import Fore, Back, Style 
animes = ["naruto", "sailor moon", "one piece", "yu-gi-oh!", "sword art online", "pokemon", "jojo's bizarre adventure", "one-punch man", "attack on titan",  "neon genesis evangelion"] #possible words to be guessed
#also top 11 animes of all time
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
invalidcharacters = ["¤",	"¶",	"§",	"†","!", "#","$","%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "{", "|", "}", "~", "", "Ç", "ü","é", "â", "ä", "ä", "à", "å", "ç", "ê", "ë", "è", "ï", "î", "ì", "æ", "Æ", "ô", "ö", "ò", "û", "ù", "ÿ", "¢", "£", "¥", "P", "ƒ", "á", "í", "ó", "ú", "ñ", "Ñ", "‡", "¿", "¬", "½", "¼", "¡", "«", "»", "¦", "ß", "µ", "±", "°", "•", "·", "²", "€", "„", "…", "†", "‡", "ˆ", "‰", "Š", "‹", "Œ", "‘", "’", "“", "”", "–", "—", "˜", "™", "š", "›", "œ", "Ÿ", "¨", "©", "®", "¯", "³", "´", "¸", "¹", "¾", "À", "Á", "Â", "Ã", "Ä", "Å", "È", "É", "Ê", "Ë", "Ì", "Í", "Î", "Ï", "Ð", "Ò", "Ó", "Ô", "Õ", "Ö", "×", "Ø", "Ù", "Ú", "Û", "Ü", "Ý","Þ","ã", "ð", "õ", "÷", "ø", "þ"]
hint = "Anime"
answer = animes[random.randint(0,len(animes)-1)] #variable for that's to be guessed
#print(answer) ''' turn this line on/off during testing/gameplay'''
notguessedletters = letters # a list of letters player hasn't guessed
guessedletters = [] # a list of letters player has guessed
word = ""
for i in range(len(answer)):
  if str(answer[i]).lower() in letters:
    word += "*"
  else:
    word += str(answer[i])
triesleft = 10 # amount of guesses 15/26 possible letters
changed = False
print(Fore.CYAN + 
""" _    _                                         
| |  | |                                        
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/   """)#+--- big
#bruh
print(Fore.LIGHTRED_EX + " This game is intended to play in full screen. Please follow the following game for a better gaming experience: https://SimpleHangman.miguelvilla.repl.run")
while triesleft != 0: #actual game starts here:
  guessedstring = ', '.join(guessedletters)
  notguessedstring = ', '.join(notguessedletters)
  if triesleft == 10 or triesleft == 9:
    print(Fore.GREEN + '''\n   ____
  |    |      Answer is: %s
  |           Letters guessed: %s 
  |           Letters remaining: %s
  |           Guesses left: %s
  |           Hint: %s 
 _|_
|   |______
|          |
|__________|''' % (word, guessedstring, notguessedstring, triesleft, hint))
  
  elif triesleft == 8 or triesleft == 7:
    print(Fore.GREEN + '''\n   ____
  |    |      Answer is: %s
  |    O      Letters guessed: %s 
  |           Not guessed letters: %s
  |           Guesses left: %s
  |
 _|_
|   |______
|          |
|__________|''' % (word, guessedstring, notguessedstring, triesleft))
  elif triesleft == 6 or triesleft == 5:
    print(Fore.YELLOW + '''\n   ____
  |    |      Answer is: %s
  |    o      Letters guessed: %s 
  |   /|      Not guessed letters: %s
  |           Guesses left: %s
  |
 _|_
|   |______
|          |
|__________|'''
 % (word, guessedstring, notguessedstring, triesleft))
  elif triesleft == 4 or triesleft == 3:
    print(Fore.YELLOW + '''   ____
  |    |      Answer is: %s
  |    o      Letters guessed: %s 
  |   /|\     Not guessed letters: %s
  |           Guesses left: %s
  |
 _|_
|   |______
|          |
|__________|'''
 % (word, guessedstring, notguessedstring, triesleft))
  elif triesleft == 2 or triesleft == 1:
    print(Fore.YELLOW + '''   ____
  |    |      Answer is: %s
  |    o      Letters guessed: %s 
  |   /|\     Not guessed letters: %s
  |    |      Guesses left: %s
  |   /
 _|_
|   |______
|          |
|__________|'''
 % (word, guessedstring, notguessedstring, triesleft))
  guess = str(input("\nGuess a letter: ")).lower()
  guess = guess[0].lower()
  if guess == "":
    print(Fore.RED + "\nYou cannot guess nothing! ")
  elif guess in invalidcharacters:
    print (Fore.RED + "\n You can only guess letters! ")
  elif guess in guessedletters:
      print(Fore.RED + "\nYou already guessed this letter. ")
      changed = False
  elif guess in letters:
    print(guess)
    if guess.lower() in answer.lower():
      changed = True
      a = ""
      for i in range(len(answer)):
        if answer[i].lower() == guess.lower():
          #replace all "-" with the letter if the guessed letter is part of the word
          a += answer[i]
        elif not(word[i] =="-"):
          a += word[i]

        else:
            #when not replacing letters, keep letters in their solved/unsolved state
            a += "-"
          #word[i] = answer[i]
          #a = word[:i] + answer[i] + word[i:] #errors here
          #word = a
        changed = True
      guessedletters += guess
    else:
      if guess.lower() in guessedletters:
        pass
      else:
         guessedletters += guess 
      triesleft -= 1
    notguessedletters.remove(str(guess))

       
    guessedletters.sort()
    
    if changed == True:
      word = a
      a = ""
      changed = False
  else:
    print (Fore.RED + "\nYou can only guess letters! ")
  if answer == word:
    break
  
if answer == word:
  print(Fore.CYAN + '''__   _______ _   _ _    _ _____ _   _ 
\ \ / /  _  | | | | |  | |_   _| \ | |
 \ V /| | | | | | | |  | | | | |  \| |
  \ / | | | | | | | |/\| | | | | . ` |
  | | \ \_/ / |_| \  /\  /_| |_| |\  |
  \_/  \___/ \___/ \/  \/ \___/\_| \_/
                                        \nAnswer: %s''' % (answer))
elif triesleft == 0:
  print(Fore.RED + '''\n   ____
  |    |      Answer : %s
  |    o      Guesses left : Too late             
  |   /|\     Game Over 
  |    |      Good luck next time 
  |   / \
 _|_
|   |______
|          |
|__________|'''%(answer))
  print('''  _____                       ____                 
 / ____|                     / __ \                
| |  __  __ _ _ __ ___   ___| |  | |_   _____ _ __ 
| | |_ |/ _` | '_ ` _ \ / _ \ |  | \ \ / / _ \ '__|
| |__| | (_| | | | | | |  __/ |__| |\ V /  __/ |   
 \_____|\__,_|_| |_| |_|\___|\____/  \_/ \___|_|   ''')
  
