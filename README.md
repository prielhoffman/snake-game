# 🐍 Snake Game

This project is a simple implementation of the classic Snake Game using Python's `turtle` module. The game consists of a snake that moves around the screen, eating food to grow and avoiding collisions with the walls or its own tail. The score increases each time the snake eats food.

## 📂 Project Structure

* **`main.py`** - The main game file that runs the game loop and handles user input, collisions, and game-over logic.
* **`food.py`** - The file responsible for generating the food that the snake consumes. It randomly places the food on the screen.
* **`scoreboard.py`** - Displays the player's current score on the screen and handles the "Game Over" message when the game ends.
* **`snake.py`** - Contains the logic for the snake's movement, direction control, and growing the snake as it eats food.

## 🛠️ How to Run the Game

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/snake-game.git
   ```

2. **Navigate to the project folder:**
     ```bash
      cd snake-game
      ```

3. **Run the game:**
   ```bash
   python main.py
   ```

## 🎮 Controls

* **Up Arrow** - Move up.
* **Down Arrow** - Move down.
* **Left Arrow** - Move left.
* **Right Arrow** - Move right.
