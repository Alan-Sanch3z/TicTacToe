import enum

# Message enums
class Messages(enum.Enum):
  try_again = "Try again"
  move_not_valid = "Move is not valid."

# List of valid moves : index
valid_moves = {
  "A1": 0,
  "A2": 1,
  "A3": 2,
  "B1": 3,
  "B2": 4,
  "B3": 5,
  "C1": 6,
  "C2": 7,
  "C3": 8,
}

# Player class which holds each player's symbol and number
class Player():
  def __init__(self, symbol, index):
    self.symbol = symbol
    self.index = index

  def get_symbol(self):
    return self.symbol

  def get_index(self):
    return self.index

  def get_name(self):
    return "Player " + self.player_index_to_word(self.get_index()).capitalize()

  def player_index_to_word(self, num):
    if num == 1:
      return "one"
    else:
      return "two"

# Move class which holds data on the player and their move location
class Move():
  def __init__(self, Player, slot):
    self.Player = Player
    self.slot = slot

  def get_slot(self):
    return valid_moves.get(self.slot)

  def get_player(self):
    return self.Player

# Board class which handles most of the game logic
class Board():

  # Keeps track of the moves
  moves = [" "," "," "," "," "," "," "," "," "]
  running = True
  winner = None

  def __init__(self):
    pass

  def is_running(self):
    return self.running

  def get_winner(self):
    return self.winner

  # Displays the board as text
  def display_board(self):
    print("\n")
    print("  1   2   3")
    print("A {} | {} | {}".format(self.moves[0], self.moves[1], self.moves[2]))
    print("  --+---+--")
    print("B {} | {} | {}".format(self.moves[3], self.moves[4], self.moves[5]))
    print("  --+---+--")
    print("C {} | {} | {}".format(self.moves[6], self.moves[7], self.moves[8]))
    print("\n")

  # Asks the player for their move
  def ask_for_move(self, player, again):
    self.display_board()
    if self.is_running():
      if not again:
        slot = input("[" + player.get_symbol() + "] " + player.get_name() + ", What move do you want to make?: ")
      else:
        slot = input("\n" + Messages.move_not_valid.value + "\n\n" + Messages.try_again.value + ": ")

      if not slot.capitalize() in valid_moves or not self.make_move(Move(player, slot)):
        self.ask_for_move(player, True)
    else:
      if not self.get_winner == "Tie":
        print(self.get_winner().get_name() + ", has won the game!")
      else:
        print("The game is tied!")

  # Checks if the move is valid and puts it on the board
  def make_move(self, Move):
    if not self.moves[int(Move.get_slot())] == " ":
      pass
    else:
      self.moves[Move.get_slot()] = Move.get_player().get_symbol()
      self.check_for_gameover(Move.get_player())
      return True

  # Checks if there is a tie or a win
  def check_for_gameover(self, player):
    if self.check_for_win():
      self.winner = player
      self.running = False
    elif self.check_for_tie():
      self.winner = "Tie"
      self.running = False

  # Checks if a player has won the game
  def check_for_win(self):
    if self.check_rows() or self.check_columns() or self.check_diagonals():
      return True
    else:
      return False

  # Checks if there is a tie
  def check_for_tie(self):
    for i in self.moves:
      if i == " ":
        return False
      else:
        pass
    return True

  # Checks the rows for a winner
  def check_rows(self):
    row_1 = self.moves[0] == self.moves[1] == self.moves[2] != " "
    row_2 = self.moves[3] == self.moves[4] == self.moves[5] != " "
    row_3 = self.moves[6] == self.moves[7] == self.moves[8] != " "
    if row_3:
      return self.moves[6]
    if row_2:
      return self.moves[3]
    if row_1:
      return self.moves[0]

  # Checks the columns for a winner
  def check_columns(self):
    col_1 = self.moves[0] == self.moves[3] == self.moves[6] != " "
    col_2 = self.moves[1] == self.moves[4] == self.moves[7] != " "
    col_3 = self.moves[2] == self.moves[5] == self.moves[8] != " "
    if col_3:
      return self.moves[0]
    if col_2:
      return self.moves[1]
    if col_1:
      return self.moves[2]


  # Checks the diagonals for a winner
  def check_diagonals(self):
    diag_1 = self.moves[0] == self.moves[4] == self.moves[8] != " "
    diag_2 = self.moves[2] == self.moves[4] == self.moves[6] != " "
    if diag_1:
      return self.moves[0]
    if diag_2:
      return self.moves[2]
