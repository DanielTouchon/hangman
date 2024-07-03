# Write your code below this line 👇
import re

class Hangman:
  def __init__(self,word,level):
    self.word = word
    self.placeholder = "*" * len(self.word)
    self.out_letters = []
    self.game_result = "You win!"
    if level == "hard":
      self.lives = 1
    elif level == "medium":
      self.lives = 3
    elif level == "easy":
      self.lives = 5

  def u_replacer(self,letter,position):
    return self.placeholder[:position] + letter + self.placeholder[position+1:]

  def check_letter(self,letter):
    success = [m.start() for m in re.finditer(letter,self.word)]
    if len(success) == 0:
      if letter not in self.out_letters:
        self.lives -= 1
        self.out_letters.append(letter)
      else:
        return False
    return success

  def replace_all(self,letter,success=[]):
    for position in success:
      self.placeholder = self.u_replacer(letter,position)

  def get_lives(self):
    return str(self.lives)

  def check_game_result(self):
    if self.lives == 0:
      self.game_result = "You lose!\nThe word was: " + self.word
      return True
    if self.placeholder == self.word:
      self.game_result = "You win!"
      return True
      
cls = lambda: print("\033c\033[3J", end='')      
      
def input_letter():
  letter = input("Typer in a letter: ").strip()
  if len(letter) > 1:
    print("Please type in a single letter")
  return letter

def game_loop():
  hangman = Hangman("parallelism","medium")

  while hangman.placeholder != hangman.word:
    print(hangman.placeholder)
    print("Lives left: " + hangman.get_lives())
    print("Wrong letters: " + str(hangman.out_letters))
    print(" --------------- ")
    new_letter = input_letter()
    cls()
    check = hangman.check_letter(new_letter)
    if check:
      hangman.replace_all(new_letter,check)
    else:
      print("Wrong letter!")
    is_game_over = False
    is_game_over = hangman.check_game_result()
    if is_game_over == True:
      print(hangman.game_result)
      break