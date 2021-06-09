
from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
TRAFFIC = 30


class CarManager():

    def __init__(self):

        self.num_of_cars = 5
        self.cars = []
        self.make_cars(self.num_of_cars)
        self.car_speed = STARTING_MOVE_DISTANCE

    def make_cars(self, number_of_cars):
        if len(self.cars) < TRAFFIC:
            for i in range(number_of_cars):
                new_car = Turtle()
                new_car.penup()
                new_car.color(random.choice(COLORS))
                new_car.shape("square")
                new_car.shapesize(stretch_wid=1, stretch_len=2)
                new_y = random.randint(-10, 10) * 25
                new_car.goto(300,new_y)
                new_car.setheading(180)
                self.cars.append(new_car)

    def move(self):

        for car in self.cars:
            car.forward(self.car_speed * random.random())
            if car.xcor() < -310:
                new_y = random.randint(-10, 10) * 25
                car.goto(300,new_y)


    def speed_up(self):
        self.car_speed += MOVE_INCREMENT