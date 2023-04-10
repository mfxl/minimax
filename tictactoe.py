from __future__ import annotations
from typing import List
from enum import Enum
from board import Piece, Board, Move, bcolors

class TTTPiece(Piece, Enum):
    X = f"{bcolors.CYAN}X{bcolors.ENDC}"
    O = f"{bcolors.YELLOW}O{bcolors.ENDC}"
    E = " "
    @property
    def opposite(self) -> TTTPiece:
        if self == TTTPiece.X:
            return TTTPiece.O
        elif self == TTTPiece.O:
            return TTTPiece.X
        else:
            return TTTPiece.E

    def __str__(self) -> str:
        return(self.value)


class TTTBoard(Board):
    def __init__(self, position: List[TTTPiece] = [TTTPiece.E] * 9, turn: TTTPiece = TTTPiece.X) -> None:
            self.position: List[TTTPiece] = position
            self._turn: TTTPiece = turn
    @property
    def turn(self) -> Piece:
        return self._turn

    def move(self, location: Move) -> Board:
        temp_position: List[TTTPiece] = self.position.copy()
        temp_position[location] = self._turn
        return TTTBoard(temp_position, self._turn.opposite)


    @property
    def legal_moves(self) -> List[Move]:
        """
        Returns a list of legal moves (e.g. [4, 6, 7]) given all positions
        Filters all positions 0-8 where the Piece is empty
        :return list[Move]:
        """
        return [p for p in range(len(self.position)) if self.position[p] == TTTPiece.E]


    @property
    def is_win(self) -> bool:
        # Check 3 rows, 3 columns and 2 diagonals
        return self.position[0] == self.position[1] and \
            self.position[0] == self.position[2] and \
            self.position[0] != TTTPiece.E or \
            self.position[3] == self.position[4] and \
            self.position[3] == self.position[5] and \
            self.position[3] != TTTPiece.E or \
            self.position[6] == self.position[7] and \
            self.position[6] == self.position[8] and \
            self.position[6] != TTTPiece.E or \
            self.position[0] == self.position[3] and \
            self.position[0] == self.position[6] and \
            self.position[0] != TTTPiece.E or \
            self.position[1] == self.position[4] and \
            self.position[1] == self.position[7] and \
            self.position[1] != TTTPiece.E or \
            self.position[2] == self.position[5] and \
            self.position[2] == self.position[8] and \
            self.position[2] != TTTPiece.E or \
            self.position[0] == self.position[4] and \
            self.position[0] == self.position[8] and \
            self.position[0] != TTTPiece.E or \
            self.position[2] == self.position[4] and \
            self.position[2] == self.position[6] and \
            self.position[2] != TTTPiece.E

    def evaluate(self, player: Piece) -> float:
        if self.is_win and self.turn == player:
            return -1
        elif self.is_win and self.turn != player:
            return 1
        else:
            return 0


    def __repr__(self) -> str:
        return(f"""
        {self.position[0]}|{self.position[1]}|{self.position[2]}
        -----
        {self.position[3]}|{self.position[4]}|{self.position[5]}
        -----
        {self.position[6]}|{self.position[7]}|{self.position[8]}
        """)
