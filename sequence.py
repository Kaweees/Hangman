def anime_answer():
  letters_left = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  letters_guessed = []
  guesses_left = 5
  guesses_that_lead_to_answer = []
  if not(anime_answer_name == ""):
    answer = anime_answer_name
  elif not(tv_show_answer_name == ""):
    answer = tv_show_answer_name
    for char in answer:
      guesses_that_lead_to_answer += '-'
  while guesses_left 0:
    guess = input("Guess a letter! ")
    for char in answer:
      if char in guess:
        
        find2('banana', 'a', 2)