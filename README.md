# 15 Puzzle

A [15-puzzle](https://en.wikipedia.org/wiki/15_puzzle) implementation in Python.

This was built to satisfy a brain itch. No vibe coding here. Copilot autocomplete was minimally helpful – led me down wrong paths where I should have trusted myself.

When setting out I was not aware that half of the permutations for a given size are not solvable. So that made the implementation take longer than expected.

## Try it via the CLI:

### Install
```bash
uv tool install git+https://github.com/josmithua/fifteen
```

### Run

```bash
fifteen
```

## Use in your own projects

### Add dependency

```bash
uv add git+https://github.com/josmithua/fifteen
```

### Use

```python
from fifteen import Move, create_random_board, is_solved, make_move

# Have fun...
```
