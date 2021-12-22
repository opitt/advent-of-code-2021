# https://adventofcode.com/2021/day/17
import os
from rich import print


class Probe:
    def __init__(self, velo_y, velo_x, min_y, max_y, min_x, max_x) -> None:
        # The probe's x,y position starts at 0,0.
        self.y = 0
        self.x = 0
        self.y_velo_init = self.y_velo = velo_y
        self.x_velo_init = self.x_velo = velo_x
        # target area
        self.y_min = min_y
        self.y_max = max_y
        self.x_min = min_x
        self.x_max = max_x
        # save the highest trajectory point
        self.y_high = self.y

    def _update_velocity(self):
        # Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
        # Due to gravity, the probe's y velocity decreases by 1.
        if self.x_velo > 0:
            self.x_velo = max(self.x_velo - 1, 0)
        self.y_velo -= 1

    def move_a_step(self):
        # Then, it will follow some trajectory by moving in steps. On each step, these changes occur in the following order:
        # The probe's x position increases by its x velocity.
        self.x += self.x_velo
        # The probe's y position increases by its y velocity.
        self.y += self.y_velo
        self.y_high = max(self.y_high, self.y)
        # update gravity
        self._update_velocity()

    def is_in_target(self):
        return self.x_min <= self.x <= self.x_max and self.y_min <= self.y <= self.y_max

    def can_reach_target(self):
        if (
            self.y < self.y_min
        ):  # e.g. -11 for:  y=-10..-5 ... while -3 is still ok # if beyond arget y ... stop
            return False
        if (
            self.x > self.x_max
        ):  # and self.x_direction > 0:  # if beyond target x ... stop
            return False
        if (
            self.x < self.x_min and self.x_velo == 0
        ):  # if before target, but no movement ... stop
            return False
        return True


def solve1(target_ymin, target_ymax, target_xmin, target_xmax):
    target_velos = set()
    for vx in range(target_xmax + 1):
        for vy in range(target_ymin, abs(target_ymin) * 10):
            probe = Probe(vy, vx, target_ymin, target_ymax, target_xmin, target_xmax)
            while True:
                probe.move_a_step()
                if probe.is_in_target():
                    target_velos.add((vx, vy, probe.y_high))
                    break
                if not probe.can_reach_target():break
    return max(target_velos, key=lambda x: x[2])[2], len(target_velos)


def main(input_name, use_line=0):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, input_name), encoding="utf-8") as input:
        lines = input.readlines()
    # target area: x=20..30, y=-10..-5
    line = lines[use_line]
    x, y = line[line.find(":") + 2 :].split()
    xmin, xmax = map(int, x.replace(",", "").split("=")[1].split(".."))
    ymin, ymax = map(int, y.split("=")[1].split(".."))
    res1, res2 = solve1(ymin, ymax, xmin, xmax)
    print(f"Result 1: {res1}")
    print(f"Result 2: {res2}")
    
if __name__ == "__main__":
    # for i in range(1):
    #    main("test.txt", i)
    main("input.txt", 0)
