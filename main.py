import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard, FinishLine, Game_Over

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

scoreboard = Scoreboard()
finish_line = FinishLine()
player = Player()

car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True


game_count = 0
increase_level = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()
    game_count += 1

    if game_count == 6:
        car_manager.create_car()
    elif game_count > 6:
        game_count = 0

    if increase_level == 0:
        car_manager.move_cars()
    else:
        car_manager.move_faster(increase_level)

    if player.ycor() >= 180:
        increase_level += 1
        print(increase_level)
        player.complete_race()


        player.go_to_start()
        scoreboard.add_point()

    for i in car_manager.segments:
        if i.distance(player) < 20:
            game_is_on = False
            game_over = Game_Over()




screen.exitonclick()