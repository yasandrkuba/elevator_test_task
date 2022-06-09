from random import randint


class Building:
    def __init__(self):
        self.num_of_floors = randint(5, 20)
        self.persons_on_floors = {i: randint(0, 10) for i in range(self.num_of_floors)}
        self.destination_floors = dict()

        for floor_num, persons in enumerate(self.persons_on_floors):
            self.destination_floors[floor_num] = list()
            for i in range(persons):
                destination = self.make_random_destination(floor_num)
                self.destination_floors[floor_num].append(destination)

    def make_random_destination(self, current_floor: int) -> int:
        destination = current_floor
        while destination == current_floor:
            destination = randint(1, self.num_of_floors - 1)
        return destination
