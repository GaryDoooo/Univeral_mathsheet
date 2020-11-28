
import codewars_test as test
from solution import Go
from random import choice, randint


def close_it():
    pass


def close_describe():
    pass

test.describe("Creating go boards")
test.it("9x9")
game = Go(9)
board = [[".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."]]
test.assert_equals(game.board, board, "Should generate a 9 by 9 board.")
close_it()

test.it("13x13")
game = Go(13)
board = [[".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]
test.assert_equals(game.board, board, "Should generate a 13 by 13 board.")
close_it()

test.it("19x19")
game = Go(19)
board = [[".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
             ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
             ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
             ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
             ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
             ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
             ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
             ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
             ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
             ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
             ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
             ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
             ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
             ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
             ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
             ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
             ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".",
             ".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]
test.assert_equals(game.board, board, "Should generate a 19 by 19 board.")
close_it()

test.it("32x32")
test.expect_error(
    "Should throw an error. Board cannot be larger than 25 by 25", lambda: Go(32))
close_it()
close_describe()


test.describe("Placing stones")
test.it("Place a black stone")
game = Go(9)
game.move("3D")
test.assert_equals(game.get_position("3D"), "x")
close_it()

test.it("Place a white stone")
game.move("4D")
test.assert_equals(game.get_position("4D"), "o")
close_it()

test.it("Can take multiple moves at a time")
game.move("4A", "5A", "6A")
test.assert_equals(game.get_position("4A"), "x")
test.assert_equals(game.get_position("5A"), "o")
test.assert_equals(game.get_position("6A"), "x")
close_it()

test.it("Cannot place a stone on an existing stone. Raises an error.")
test.expect_error("3D should be an invalid move", lambda: game.move("3D"))
test.expect_error("4D should be an invalid move", lambda: game.move("4D"))
close_it()

test.it("Cannot place a stone with out of bounds coordinates. Raises an error.")
test.expect_error("3Z should be an invalid move", lambda: game.move('3Z'))
test.expect_error("66 should be an invalid move", lambda: game.move('66'))
close_it()
close_describe()


test.describe("Capturing")
test.it("Black captures single white stone")
game = Go(9)
moves = ["4D", "3D", "4H", "5D", "3H", "4C", "5B", "4E"]
game.move(*moves)
test.assert_equals(game.get_position('4D'), ".")
close_it()

test.it("Black captures multiple white stones")
game = Go(9)
moves = ["6D", "7E", "6E", "6F", "4D", "5E", "5D", "7D",
         "5C", "6C", "7H", "3D", "4E", "4F", "3E", "2E",
         "3F", "3G", "2F", "1F", "2G", "2H", "1G", "1H",
         "4C", "3C", "6H", "4B", "5H", "5B"]
captured = ["6D", "6E", "4D", "5D", "5C",
            "4E", "3E", "3F", "2F", "2G", "1G", "4C"]
game.move(*moves)
for capture in captured:
    test.assert_equals(game.get_position(capture), ".")
close_it()

test.it("Corner capture")
game = Go(9)
moves = ["9A", "8A", "8B", "9B"]
game.move(*moves)
test.assert_equals(game.get_position('9A'), ".")
close_it()

test.it("Multiple captures")
game = Go(9)
moves = ["5D", "5E", "4E", "6E", "7D", "4F", "7E", "3E", "5F", "4D",
         "6F", "6D", "6C", "7F", "4E", "5E"]
captured = ["4E", "6D", "6E"]
game.move(*moves)
for capture in captured:
    test.assert_equals(game.get_position(capture), ".")
close_it()

test.it("Snapback")
game = Go(5)
moves = ["5A", "1E", "5B", "2D", "5C", "2C", "3A",
         "1C", "2A", "3D", "2B", "3E", "4D", "4B",
         "4E", "4A", "3C", "3B", "1A", "4C", "3C"]
captured = ["4A", "4B", "4C", "3B"]
game.move(*moves)
for capture in captured:
    test.assert_equals(game.get_position(capture), ".")
close_it()

test.it("Self-capturing throws an error.")
game = Go(9)
moves = ["4H", "8A", "8B", "9B", "9A"]
test.expect_error("self capturing moves are illegal",
                  lambda: game.move(*moves))
test.assert_equals(game.get_position("9A"), ".",
                   "Illegal stone should be removed")
game.move("3B")
test.assert_equals(game.get_position("3B"), "x",
                   "Black should have another try")
close_it()
close_describe()


test.describe("KO Rule")
test.it("Illegal KO by white")
game = Go(5)
moves = ["5C", "5B", "4D", "4A", "3C", "3B",
         "2D", "2C", "4B", "4C", "4B"]
test.expect_error("Illegal KO move. Should throw an error.",
                  lambda: game.move(*moves))
game.move("2B")
test.assert_equals(game.get_position("2B"), "x",
                   "Black should be given another try to place their stone.")
test.assert_equals(game.get_position("4B"), ".",
                   "Should rollback game before illegal move was made.")
close_it()
close_describe()


test.describe("Handicap stones")
test.it("Three handicap stones on 9x9")
game = Go(9)
finalBoard = [['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', 'x', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', 'x', '.', '.', '.', 'x', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.', '.']]

game.handicap_stones(3)
test.assert_equals(game.board, finalBoard)
close_it()
close_describe()


test.describe("Misc")
test.it("Can get board size")
game = Go(9, 16)
test.assert_equals(game.size, {"height": 9, "width": 16})
close_it()

test.it("Can get color of current turn")
game = Go(9)
game.move("3B")
test.assert_equals(game.turn, "white")
game.move("4B")
test.assert_equals(game.turn, "black")
close_it()

test.it("Can rollback a set number of turns")
game = Go(9)
board = [[".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."]]
game.move("3B", "2B", "1B")
game.rollback(3)
test.assert_equals(game.board, board)
test.assert_equals(game.turn, "black")
close_it()

test.it("Can pass turn")
game = Go(9)
game.pass_turn()
test.assert_equals(game.turn, "white")
close_it()

test.it("Can reset the board")
game = Go(9)
board = [[".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."]]

game.move("3B", "2B", "1B")
game.reset()
test.assert_equals(game.board, board)
test.assert_equals(game.turn, "black")
