class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):

        # Parking limit of each type of car
        self.limit = [big, medium, small]

        # Count of cars of each type
        self.count = [0, 0, 0]

    def addCar(self, carType: int) -> bool:

        # If space is available, allocate and return True
        if self.count[carType - 1] < self.limit[carType - 1]:
            self.count[carType - 1] += 1
            return True

        # Else, return False
        return False