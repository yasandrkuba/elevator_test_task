from random import randint
from building import Building


class Elevator:
    def __init__(self):
        self.building = Building()
        self.state = "Up"
        self.elevator_cabin = {1: [], 2: [], 3: [], 4: [], 5: []}
        self.elev_floor = 0

    def check_position_elev(self):
        if self.state == "Up":
            self.elev_floor += 1
        elif self.state == "Down":
            self.elev_floor -= 1
        return self.elev_floor

    def check_max_and_min_position_elev(self, build_dist_floor: int):
        if self.elev_floor == 1:
            self.state = "Up"
        elif self.elev_floor == (build_dist_floor):
            self.state = "Down"
        else:
            self.state = self.state
        return self.state

    def check_elevator_direction(self, last_floor: int):
        if self.elev_floor > last_floor:
            self.state = "Down"
            return self.state
        elif self.elev_floor < last_floor:
            self.state = "Up"
            return self.state
        else:
            self.elev_floor = randint(1, (len(self.building.destination_floors) - 1))
            return self.elev_floor

    def check_for_stop(self):
        check_build = any(self.building.destination_floors.values())
        check_elev = any(self.elevator_cabin.values())
        if not check_build and not check_elev:
            return False
        else:
            return True

    def print_elevator(self):
        return print(f" Floor number - {self.elev_floor} \n",
                     f"Elevator direction - {self.state} \n",
                     "=====================\n",
                     f"{self.elevator_cabin.get(1), self.elevator_cabin.get(2), self.elevator_cabin.get(3), self.elevator_cabin.get(4), self.elevator_cabin.get(5)} \n",
                     "=====================\n")
