from time import time
import game_board as hxg
from tkinter import filedialog, Tk
import inspect
import numpy as np

if __name__ == "__main__":
    # root = Tk()
    # root.withdraw()
    # dirname = filedialog.askopenfilename(title = "Select config file to use")
    # root.destroy()

    board = hxg.GameBoard("default_settings.yaml")

    # print(inspect.getmro(hxg.GameBoard))

    tile_test = board[np.array([-9, 13])][0]
    # for coords, tile in board.items():
    #     print("{:5s}: {}".format(coords, tile))

    # print()

    # print("Information stored in {}:\n".format(tile_test))
    # for item, info in tile_test.__dict__.items():
    #     print("{}: {}".format(item, info))

    # piece_info = tile_test.get_piece()

    # print()

    # print("Information stored in {}:\n".format(piece_info))
    # for item, info in piece_info.__dict__.items():
    #     print("{}: {}".format(item, info))


    # # Move piece to a new direction
    # old = np.array([1, -1])
    # new_dir = "NE"
    # print(board.move_piece(old, old, new_dir))


    # print("Information stored in {}:\n".format(piece_info))
    # for item, info in piece_info.__dict__.items():
    #     print("{}: {}".format(item, info))
