import sys


def get_ai_file_name() -> str:
    """
    Retourne le nom de l'IA à utiliser pour le système d'opération actuel
    :return: le nom du fichier
    """
    if sys.platform == "win32":
        return "stockfish_14.1_win_x64_popcnt.exe"
    elif sys.platform == "linux":
        return "stockfish_14.1_linux_x64_avx2"
