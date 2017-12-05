import sys


class Day3:
    def __init__(self):
        self.square = int(sys.argv[1])

        # "Build" the grid
        self.grid_size = 1
        while self.grid_size * self.grid_size < self.square:
            self.grid_size += 2

        self.center_x = self.center_y = self.grid_size // 2

        self.runner = self.grid_size * self.grid_size           # the value at your current coordinates in the spiral
        self.grid_size -= 1                                     # treat as max index in the spiral array
        self.x, self.y = self.grid_size, self.grid_size         # your current coordinates in the spiral

    def move_left(self):
        while self.x > 0 and self.runner > self.square:
            self.x -= 1
            self.runner -= 1
        return self.runner == self.square

    def move_right(self):
        while self.x < self.grid_size and self.runner > self.square:
            self.x += 1
            self.runner -= 1
        return self.runner == self.square

    def move_up(self):
        while self.y > 0 and self.runner > self.square:
            self.y -= 1
            self.runner -= 1
        return self.runner == self.square

    def move_down(self):
        while self.y < self.grid_size and self.runner > self.square:
            self.y += 1
            self.runner -= 1
        return self.runner == self.square

    def solve_part_a(self):
        """
        When the spiral was "generated", an extra "loop" around it only occurred if the maximum value in the previous
        loop (on the diagonal moving down from 1) was smaller than the number we're searching for. Therefore, we know
        the value we want must be on the outer loop. Move clockwise from the lower right corner to look for it.
        """
        self.move_left() or self.move_up() or self.move_right() or self.move_down()
        print(abs(self.center_x - self.x) + abs(self.center_y - self.y))


def main():
    day3 = Day3()
    day3.solve_part_a()

if __name__ == "__main__":
    main()
