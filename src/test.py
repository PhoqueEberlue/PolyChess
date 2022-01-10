import chess
import chess.engine


"""
engine = chess.engine.SimpleEngine.popen_uci(r"/home/andrewmhdb/Downloads/stockfish_14.1_linux_x64_avx2/stockfish_14.1_linux_x64_avx2"
)

board = chess.Board()
while not board.is_game_over():
    result = engine.play(board, chess.engine.Limit(time=0.1))
    board.push(result.move)
    info = engine.analyse(board, chess.engine.Limit(depth=20))
    print(board)
    print("Score:", info["score"])
    print(result.move)

engine.quit()
"""

print(chess.KING)