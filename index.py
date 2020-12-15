from game import *
import os

board = Board()

player1 = Player(input("Player 1, pick a symbol: "), 1)
player2 = Player(input("Player 2, pick a symbol: "), 2)

while player2.get_symbol() == player1.get_symbol():
  print("\n" + Messages.symbol_taken.value)
  player2 = Player(input("Player 2, pick a symbol: "), 2)

while board.is_running():
  os.system("clear")
  board.ask_for_move(player1, False)
  os.system("clear")
  board.ask_for_move(player2, False)