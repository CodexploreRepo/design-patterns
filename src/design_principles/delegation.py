class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        print("Car started")
        # Delegate the task to the "engine" object
        # i.e: object "car" is not start, but start by "engine" object
        self.engine.start()


if __name__ == "__main__":
    car_engine = Engine()
    my_car = Car(car_engine)

    my_car.start()
