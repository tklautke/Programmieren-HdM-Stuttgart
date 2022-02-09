class Car:
    def __init__(self, ps, fuel_type, mileage, number_doors):
        self.ps = ps
        self.fuel_type = fuel_type
        self.milage = mileage
        self.number_doors = number_doors
        self.x_cords = 5
        self.y_cords = 5

    def fahren(self, new_y_cords, new_x_cords):
        self.y_cords = new_y_cords
        self.x_cords = new_x_cords


class Sportscar(Car):
    def __init__(self, ps, fuel_type, mileage, number_doors, color, tuned):
        super(Sportscar, self).__init__(ps, fuel_type, mileage, number_doors)
        self.color = color
        self.tuned = tuned


sportscar1 = Sportscar(400, "diesel", 2000, 4, "white", True)

sportscar1.fahren(20, 20)

print(sportscar1.y_cords, sportscar1.x_cords)
