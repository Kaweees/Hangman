def anime_answer():
  global anime_answer_name
  global anime_answer_number
  anime_answer_number = random.randint(1,10)
  if anime_answer_number == 1:
    anime_answer_name = "naruto"
  elif anime_answer_number == 2:
    anime_answer_name = "sailor moon"
  elif anime_answer_number == 3:
    anime_answer_name = "one piece"
  elif anime_answer_number == 4:
    anime_answer_name = "yu-gi-oh!"
  elif anime_answer_number == 5:
    anime_answer_name = "sword art online"
  elif anime_answer_number == 6:
    anime_answer_name = "pokemon"
  elif anime_answer_number == 7:
    anime_answer_name = "jojo's bizarre adventure"
  elif anime_answer_number == 8:
    anime_answer_name = "one-punch man"
  elif anime_answer_number == 9:
    anime_answer_name = "attack on titan"
  elif anime_answer_number == 10:
    anime_answer_name = "neon genesis evangelion"
  return anime_answer_name

animes = ["naruto", "sailor moon", "one piece", "yu-gi-oh!", "sword art online", "pokemon", "jojo's bizarre adventure", "one-punch man", "attack on titan",  "neon genesis evangelion"]

tv_show_answer_name = ""
tv_show_answer_number = 0

def tv_show_answer():
  global tv_show_answer_name
  global tv_show_answer_number
  tv_show_answer_number = random.randint(1,10)
  if tv_show_answer_number == 1:
    tv_show_answer_name = "the 100"
  elif tv_show_answer_number == 2:
    tv_show_answer_name = "criminal minds"
  elif tv_show_answer_number == 3:
    tv_show_answer_name = "game of thrones"
  elif tv_show_answer_number == 4:
    tv_show_answer_name = "grey's anatomy"
  elif tv_show_answer_number == 5:
    tv_show_answer_name = "the big bang theory"
  elif tv_show_answer_number == 6:
    tv_show_answer_name = "this is us"
  elif tv_show_answer_number == 7:
    tv_show_answer_name = "the good doctor"
  elif tv_show_answer_number == 8:
    tv_show_answer_name = "america’s got talent"
  elif tv_show_answer_number == 9:
    tv_show_answer_name = "the simpsons"
  elif tv_show_answer_number == 10:
    tv_show_answer_name = "the flash"
  return tv_show_answer_name