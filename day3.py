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

        self.dx = self.dy = 1
        self.grid_part_b = {}

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

    def set_square_value(self):
        n = self.grid_part_b.get((self.x, self.y - 1), 0)
        ne = self.grid_part_b.get((self.x + 1, self.y - 1), 0)
        e = self.grid_part_b.get((self.x + 1, self.y), 0)
        se = self.grid_part_b.get((self.x + 1, self.y + 1), 0)
        s = self.grid_part_b.get((self.x, self.y + 1), 0)
        sw = self.grid_part_b.get((self.x - 1, self.y + 1), 0)
        w = self.grid_part_b.get((self.x - 1, self.y), 0)
        nw = self.grid_part_b.get((self.x - 1, self.y - 1), 0)
        self.grid_part_b[(self.x, self.y)] = n + ne + e + se + s + sw + w + nw
        return self.grid_part_b.get((self.x, self.y))

    def traverse_spiral(self):
        self.x = 0
        self.y = 0
        self.runner = 1

        # Add the first and second square
        self.grid_part_b[(self.x, self.y)] = self.runner

        self.x += 1
        self.grid_part_b[(self.x, self.y)] = self.runner

        # Spiral out
        while self.runner <= self.square:
            # Go up by 2*dy - 1
            for delta_y in range(0, 2 * self.dy - 1):
                if self.runner <= self.square:
                    self.y -= 1
                    self.runner = self.set_square_value()
                else:
                    return self.runner

            # Go left by 2*dx
            for delta_x in range(0, 2 * self.dx):
                if self.runner <= self.square:
                    self.x -= 1
                    self.runner = self.set_square_value()
                else:
                    return self.runner

            # Go down by 2*dy
            for delta_y in range(0, 2 * self.dy):
                if self.runner <= self.square:
                    self.y += 1
                    self.runner = self.set_square_value()
                else:
                    return self.runner

            # Go right by 2*dx
            for delta_x in range(0, 2 * self.dx):
                if self.runner <= self.square:
                    self.x += 1
                    self.runner = self.set_square_value()
                else:
                    return self.runner

            # Go to the right one
            if self.runner <= self.square:
                self.x += 1
                self.runner = self.set_square_value()
            else:
                return self.runner

            # Increment dx, dy
            self.dx += 1
            self.dy += 1

    def solve_part_b(self):
        print(self.traverse_spiral())


def main():
    day3 = Day3()
    day3.solve_part_a()
    day3.solve_part_b()

if __name__ == "__main__":
    main()
