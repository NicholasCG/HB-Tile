# HBTile

A library for simulating tile based games with separate attacking and directional movement. This library uses
[Hexy](https://github.com/RedFT/Hexy) as a base. 
### Install HBTile via pip
```bash
pip install hbtile
```

# Basic Documentation
## `GameBoard`
```python
hbtile.GameBoard(file_name: str, logs: bool = False)
```
The `GameBoard` class is the main class of the library. All other parts of HBTile work throught `GameBoard`.
To use `GameBoard`, initialize an instance of the class with a path to a valid YAML configuration file, which
an example is given in `default_settings.yaml`. The class keeps track of the turn, which controls which player
can move their piece at that turn.

If no file is provided, or the file is invalid, an error will be raised.

`GameBoard` uses an axial coordinates system, which is inherited from `hexy`.

Example:
```python
board = hbtile.GameBoard("default_settings.yaml")
```
### `GameBoard.move_piece`
```python
board.move_piece(old_coords: np.ndarray, new_coords: np.ndarray, new_direction: str) -> bool
```

The `GameBoard` class allows for pieces to be moved to a new location, given that it is a reachable space,
and there are no other pieces on that space.

`old_coords` and `new_coords` are both 1 dimensional 2 element arrays that correspond to coordinates on the board. 
`old_coords` is used to check for a valid piece at those coordinates, and if they are valid, then `new_coords` is 
used to check if the piece can move to the new coordinates, and does so if possible. `new_direction` is used alongside `new_coords`, as each valid piece will have a direction it is facing, which can changed during movement. 

The function will return whether the move was valid and completed.

### `GameBoard.attack_piece`

```python
board.attack_piece(self, attacker: np.ndarray, target: np.ndarray) -> bool
```

The `GameBoard` class also allows for pieces to attack other pieces independently of movement.
`attacker` and `target` are both 1 dimensional 2 element arrays that correspond to coordinates on the board.
The piece, if it is valid, at `attacker` will attempt to attack the piece at `target`, if there is a valid target there.
If there is a valid target, then the target's health will be subtracted by the attacker's attack power multiplied by 
a random value. The farther away a target is from the attacker, the less damage the attack will do.

### `GameBoard.get_valid_moves`
```python
board.get_valid_moves(hex : GameHex) -> np.ndarray:
```

This function gives you an array of valid tiles to move to, along with the valid possible directions that can be
reached for that tile, depending on the tile given. This function can be used to find what moves are valid before a
move is actually done. This function is used internally for `move_piece()`

This function is going to be reworked soon to make it more efficient. 

### `GameBoard.get_valid_attacks`
```python
board.get_valid_attacks(hex : GameHex) -> np.ndarray:
```

This function gives you an array of valid tiles the piece at the tile can attack, depending on the tile given.
This function can be used to find what tiles are in range before you attack. This function is used internally
for `attack_piece()`

This function is going to be reworked soon to make it more efficient. 

### `GameBoard.end_turn`
```python
board.end_turn() -> int
```

This function ends the current turn of the board. The function allows the next player to move, and checks
to see if a player has won the game (all other players' pieces are gone from the board). If there is a winner,
their player number will be returned. Otherwise, 0 will be returned.

### `GameBoard.dump`
```python
board.dump(name: str)
```

Creates a binary file of the board using the built-in pickle library. The binary can be used to save the game
in its current state.

### `GameBoard.load`
```python
@staticmethod
GameBoard.load(name: str)
```

Loads in a binary file of a board created using `dump()`. Allows for boards that have been previously saved to be reloaded.

## `GameHex`
```python
hbtile.GameHex(axial_coordinates, piece = 0, player = 0, piece_template = EmptyTemplate)
```

An internal class used to hold the information at each coordinate on the board. You should not have a reason to
use one of these objects, as the `GameBoard` object controls all of the `GameHex` objects present. These objects
are created at the initialization of the `GameBoard` object as specified in the YAML configuration file.

The `Piece` and `PieceTemplate` classes will not be documented here, as they are internal classes as well, controlled
by the `GameBoard` object. The `Piece` class is used to specify information about the piece at specific coordinates on the
board. If the coordinates do not hold a piece, then a generic `EmptyPiece` is used. The initial piece locations are specified
in the YAML configuration file.

`PieceTemplate` is used to specify characteristics about a specific type of piece on the board. These templates hold information
about the max health, attack power, attack distance, and movement distance of each piece type. These values are specified
in the YAML configuration file. There is also a special `EmptyTemplate` used for `EmptyPiece`, which has everything set to 0.

If there are any issues, use the issue tracker on [Github](https://github.com/NicholasCG/HBTile/issues).

