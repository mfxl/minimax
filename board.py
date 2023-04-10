from __future__ import annotations
from typing import NewType, List
from abc import ABC, abstractmethod


class bcolors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

Move = NewType("Move", int)  # Data Type Move represents a move in a game

class Piece:
    """
    Base class for any gaming tile or pawn on the board in a game
    """
    @property
    def opposite(self) -> Piece:
        raise (NotImplementedError("Replace with sub class"))


class Board(ABC):
    """
    Abstract class to manage the states in a game
    """
    @property
    @abstractmethod
    def turn(self) -> Piece:
        ...

    @abstractmethod
    def move(self, location: Move) -> Board:
        ...

    @property
    @abstractmethod
    def legal_moves(self) -> List[Move]:
        """
        A list of legal moves
        """
        ...

    @property
    @abstractmethod
    def is_win(self) -> bool:
        ...

    @property
    def is_draw(self) -> bool:
        return (not self.is_win) and (len(self.legal_moves) == 0)

    @abstractmethod
    def evaluate(self, player: Piece) -> float:
        """
        Evaluates the position
        """
        ...
