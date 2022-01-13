import chess
import chess.polyglot


class Openings:
    def __init__(self):
        self.filename = "openings/book.bin"

    def get_openings(self, board):
        with chess.polyglot.open_reader(self.filename) as reader:
            return [entry.move.uci() for entry in reader.find_all(board)]




