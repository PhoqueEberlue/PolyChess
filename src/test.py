import chess
import chess.engine
from datetime import datetime, date, time,timezone


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

timer = datetime.now()
print(timer)
timer2 = time(16, 43)
print(timer2)
print(timer) #JE DEVIENS FOU
timer3 = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
print(timer3)

timer4 = timer.minute
print(timer4)
