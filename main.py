from building import Building
from elevator import Elevator
import time


def main():
    last_floor = 0
    elevator = Elevator()
    building = Building()
    lst = []
    move = True

    while move:

        elevator.check_position_elev()
        elevator.check_max_and_min_position_elev(build_dist_floor=(len(building.destination_floors) - 1))

        for key_elev, person_elev in elevator.elevator_cabin.items():
            if person_elev is not None:
                for k, person in enumerate(person_elev):
                    if person == elevator.elev_floor:
                        person_elev.remove(person_elev[k])
                        building.destination_floors.get(elevator.elev_floor) \
                            .append(building.make_random_destination(current_floor=elevator.elev_floor))

            if not person_elev:
                if not building.destination_floors.get(elevator.elev_floor):
                    pass
                else:
                    for i in building.destination_floors.get(elevator.elev_floor):
                        if (i > elevator.elev_floor and elevator.state == "Up") or \
                                (i < elevator.elev_floor and elevator.state == "Down"):
                            person_elev.append(i)
                            building.destination_floors.get(elevator.elev_floor).remove(i)
                        break

        for key, value in elevator.elevator_cabin.items():
            for i in value:
                if i is not None:
                    lst.append(i)

        if elevator.state == "Up":
            for i in lst:
                if i is not None:
                    last_floor = max(lst)
            lst.clear()
        elif elevator.state == "Down":
            for i in lst:
                if i is not None:
                    last_floor = min(lst)
            lst.clear()

        elevator.check_elevator_direction(last_floor=last_floor)

        print(building.destination_floors)
        elevator.print_elevator()

        move = elevator.check_for_stop()

        time.sleep(1)


if __name__ == '__main__':
    main()
