from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(0)
        self.pencolor("white")
        self.penup()
        self.hideturtle()

    def scoring(self, count):
        self.goto(-175, 275)
        self.write("000", align="center", font=("Just my type", 72, "bold"))
        self.clear()
        self.count = count
        if count >= 10:
            self.write("0{}".format(self.count), align="center", font=("Just my type", 72, "bold"))
        elif count < 10:
            self.write("00{}".format(self.count), align="center", font=("Just my type", 72, "bold"))

    def attempts(attempt, att):
        attempt.goto(175, 275)
        attempt.write("000", align="center", font=("Just my type", 72, "bold"))
        attempt.clear()
        attempt.write("00{}".format(att), align="center", font=("Just my type", 72, "bold"))

        