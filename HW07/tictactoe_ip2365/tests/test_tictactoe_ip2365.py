import unittest

  # Adds the src directory to Python's search path
from tictactoe_ip2365.tictactoe_ip2365 import * 

import pytest


def test_initialize_board():

        board = initialize_board()
        # check the board if it has 3 rows
        assert len(board) == 3, "we need 3 rows"
        # check the board if it has 3 columns
        assert all(len(row) == 3 for row in board), "need 3 columns per row"

        assert all(cell == ' ' for row in board for cell in row), "error: some of the cells are not empty"

        print("test_initialize_board passed.")

        """This function tests the initialize_board function to verify that it creates an empty 3x3 board."""
        expected = [[' ', ' ', ' '],
                    [' ', ' ', ' '],
                    [' ', ' ', ' ']]
        result = initialize_board()  # Call the function
        assert result == expected, f"Expected {expected}, but got {result}"
        print("test_initialize_board passed.")


def test_make_move_valid():
                """This function tests the initialize_board function to verify that it creates an empty 3x3 board."""

                start_board=initialize_board()

                for row in range(3):
                    for col in range(3):
                        success = make_move(start_board, row, col, 'X')
                        assert success == True, f"Move should be successful at ({row}, {col})"
                        assert start_board[row][col] == 'X', f"Expected 'X' at ({row}, {col}), but got {start_board[row][col]}"
                start_board=initialize_board()
                for row in range(3):
                    for col in range(3):
                        success = make_move(start_board, row, col, '0')
                        assert success == True, f"Move should be successful at ({row}, {col})"
                        assert start_board[row][col] == '0', f"Expected '0' at ({row}, {col}), but got {start_board[row][col]}"
                print("WOOHOO! all requirements to make a right move have been reached")
