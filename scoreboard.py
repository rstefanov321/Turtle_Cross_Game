from turtle import Turtle


FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto((10, 200))
        self.score = 0
        self.write(f"Game score: {self.score}", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.write(f"Game score: {self.score}", align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()


class FinishLine(Turtle):
    def __init__(self):
        super().__init__()
        # self.hideturtle()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(0.1, 30)
        self.goto(0, 180)


class Game_Over(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto((10, 0))
        self.score = 0
        self.write("Game Over...", align=ALIGNMENT, font=FONT)


