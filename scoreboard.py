from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard() # Display the current score
        self.hideturtle() # Only show text

    def update_scoreboard(self):
        # Display the current score on the screen
        self.write(f'Score: {self.score}', align='center', font=('Courier', 24, 'normal'))

    def increase_score(self):
        # Increment the score and update the display
        self.score += 1
        self.clear()
        self.update_scoreboard() # Update the score on the screen

    def game_over(self):
        # Display "Game Over" in the center of the screen
        self.goto(0,0)
        self.write('GAME OVER.', align='center', font=('Courier', 24, 'normal'))