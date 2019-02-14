# The Calculator Game Solver

## How it works

To use the solver, from your command line:
`python cli.py` with the following arguments:

`--moves=n` total button presses required in the solution

`--balance=n` the starting balance

`--goal=n` the goal that is reached when the sequence is correct

Once you submit the command with all flags, you will be able to enter each
button one at a time. Once you've entered all buttons simply enter `n` in
order to run the solver. If a solution exists it will be output as the
final line.

Example query:

`python cli.py --goal=30 --moves=3 --balance=0`

buttons = `+3 x5 x2` Each one should be entered on it's own

that will output the following:

`SOLVED!`

`(('add', [3]), ('add', [3]), ('multiply', [5]))`
