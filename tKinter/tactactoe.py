import tkinter as tk
from tkinter import messagebox

# Global variables
current_player = "X"
board = [""] * 9
game_over = False


def draw_grid():
    """Draw the 3x3 grid on the canvas"""
    # Vertical lines
    canvas.create_line(100, 0, 100, 300)
    canvas.create_line(200, 0, 200, 300)

    # Horizontal lines
    canvas.create_line(0, 100, 300, 100)
    canvas.create_line(0, 200, 300, 200)


def handle_click(event):
    """Handle mouse click events on the canvas"""
    global current_player, game_over

    if game_over:
        return

    # Calculate which cell was clicked
    col = event.x // 100
    row = event.y // 100
    position = row * 3 + col

    # If cell is already occupied, do nothing
    if board[position] != "":
        return

    # Update board and draw the mark
    board[position] = current_player

    # Draw mark (X or O)
    x = col * 100
    y = row * 100

    if current_player == "X":
        canvas.create_text(x + 50, y + 50, text="X", font=("Arial", 36, "bold"))
    else:
        canvas.create_text(x + 50, y + 50, text="O", font=("Arial", 36, "bold"))

    # Check for win
    if check_winner():
        messagebox.showinfo("Game Over", f"Player {current_player} wins!")
        game_over = True
    elif "" not in board:
        messagebox.showinfo("Game Over", "It's a draw!")
        game_over = True
    else:
        # Switch player
        current_player = "O" if current_player == "X" else "X"


def check_winner():
    """Check if the current player has won"""
    # Define winning combinations
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]

    # Check each winning combination
    for combo in win_combinations:
        if (board[combo[0]] == board[combo[1]] == board[combo[2]] == current_player):
            return True
    return False


def reset_game():
    """Reset the game to the initial state"""
    global current_player, board, game_over
    current_player = "X"
    board = [""] * 9
    game_over = False

    # Clear canvas and redraw grid
    canvas.delete("all")
    draw_grid()


# Set up the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create canvas
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

# Draw grid
draw_grid()

# Bind click event
canvas.bind("<Button-1>", handle_click)

# Reset button
reset_button = tk.Button(root, text="Reset", command=reset_game)
reset_button.pack()

# Start the game
root.mainloop()