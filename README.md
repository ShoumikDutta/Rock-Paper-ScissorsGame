# Rock-Paper-Scissors Game

This is a simple Python implementation of the Rock-Paper-Scissors game. The game allows the user to play against the computer and keeps track of the score. The computer's choice is generated randomly, and the user's choice is taken as input.

## Prerequisites

To run this code, you need to have Python installed on your system. This code is compatible with Python 3.x.

## Getting Started

1. Clone the repository or download the script file to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the script using the following command:

```shell
python rock_paper_scissors.py
```

## How to Play

1. When the game starts, you will see the welcome message and the available options:

```
Welcome to Rock-Paper-Scissors Game

1. Rock
2. Paper
3. Scissors
```

2. Enter your choice by typing the corresponding number (1, 2, or 3) and press Enter.

3. The computer will randomly choose its move, and the winner of the round will be determined based on the game rules:

- Rock beats Scissors
- Paper beats Rock
- Scissors beat Paper

4. After each round, the result of the round will be displayed, and the score will be updated accordingly.

5. The game will continue until one of the players reaches a score of 3. If you win the game, you will see the message "Congratulations. You have won the game." If the computer wins, you will see "You Lost the game. Better luck next time."

6. The game will exit automatically after displaying the final result.

## Code Explanation

The code consists of two functions: `main()` and `check_winner(comp, user)`.

The `main()` function is the entry point of the program. It displays the welcome message and the available options. It then enters a loop where it asks the user for their choice, validates the input, and determines the winner of the round. The score is updated based on the result, and the loop continues until one of the players reaches a score of 3.

The `check_winner(comp, user)` function takes the computer's choice (`comp`) and the user's choice (`user`) as parameters and compares them to determine the winner. If the choices are the same, it returns 0 (indicating a tie). If the user wins, it returns 1. Otherwise, it returns -1 (indicating the computer's victory).

## Example Output

```
Welcome to Rock-Paper-Scissors Game

1. Rock
2. Paper
3. Scissors

Enter Your choice (only 1, 2, 3): 1
Tie!

Enter Your choice (only 1, 2, 3): 2
You lost this round

Enter Your choice (only 1, 2, 3): 3
You won this round

Enter Your choice (only 1, 2, 3): 1
You won this round

Congratulations. You have won the game.
```

## Conclusion

You have learned how to play the Rock-Paper-Scissors game against the computer using this Python script. Have fun playing and enjoy!
