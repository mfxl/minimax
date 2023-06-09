from __future__ import annotations
from board import Piece, Board, Move

def minimax(board: Board, maximizing: bool, original_player: Piece, max_depth: int = 8) -> float:
    # Termination condition
    if board.is_win or board.is_draw or max_depth == 0:
        return board.evaluate(original_player)

    # Recursion
    if maximizing:
        best_eval: float = float("-inf")
        for move in board.legal_moves:
            result: float = minimax(board.move(move), False, original_player, max_depth - 1)
            best_eval = max(result, best_eval)
        return best_eval
    else:  # minimizing
        worst_eval: float = float("inf")
        for move in board.legal_moves:
            result = minimax(board.move(move), True, original_player, max_depth - 1)
            worst_eval = min(result, worst_eval)
        return worst_eval

def find_best_move(board: Board, max_depth: int = 8) -> Move:
    best_eval: float = float("-inf")
    best_move: Move(-1)
    for move in board.legal_moves:
        result: float = minimax(board.move(move), False, board.turn, max_depth)
        if result > best_eval:
            best_eval = result
            best_move = move
    return best_move