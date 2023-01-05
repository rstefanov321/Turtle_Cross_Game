from turtle import Turtle
import turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 20

turtle.colormode(255)

class CarManager:
    def __init__(self):
        self.segments = []

    def create_car(self):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        car = Turtle("square")
        car.penup()
        car.color((red, green, blue))
        # car.color(COLORS[random.randint(0, len(COLORS))-1])
        car.shapesize(1, 2)
        car.location_y = random.randint(-150, 160)
        car.goto(250, car.location_y)
        self.segments.append(car)

    def move_cars(self):
        for i in self.segments:
            i.backward(STARTING_MOVE_DISTANCE)
            speed = i.backward(STARTING_MOVE_DISTANCE)

    def move_faster(self, level):
        for i in self.segments:
            i.backward(STARTING_MOVE_DISTANCE + (level * MOVE_INCREMENT))




# class CarManager(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.shape("square")
#         self.penup()
#         self.color("white")
#         self.shapesize(1, 2)
#         self.location_y = random.randint(-150, 160)
#         self.goto(250, self.location_y)
#
#     def move(self):
#         self.backward(20)

