import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)



car = CarManager()
scoreboard = Scoreboard()
player = Player()



screen.listen()
screen.onkeypress(player.go_up, "Up")

loop = 1
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.score = player.start_count
    scoreboard.update_scoreboard()
    car.move()
    loop += 1
    if loop % 10 == 0:
        car.make_cars(1)

    #Determine the crush of cars
    for i in car.cars:
        if player.distance(i) < 20:
            scoreboard.game_over()
    # Determine the crush of cars
    if player.is_at_finish_line():
        car.speed_up()
screen.exitonclick()