class Point:
    #point class

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_midpoint(self):
        return Point(self.x, self.y + 0.5)

    def __repr__(self):
        return f'({self.x} | {self.y})'


class LinearFunction:

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        self.delta_y = point_b.y - point_a.y
        self.delta_x = point_b.x - point_a.x
        self.b = self._calculate_b()

    def _calculate_b(self):
        return self.start.y - self.delta_y / self.delta_x * self.start.x

    def point_is_below(self, point: Point):
        return 0 > self.delta_y * point.x - self.delta_x * point.y + self.b * self.delta_x


class MidpointLineAlgorithm:

    def __init__(self, linear_function: LinearFunction):
        self.linear_function = linear_function

    def run(self):
        points = list()

        iterations = linear_function.delta_x
        y = linear_function.start.y
        x = linear_function.start.x

        for x_i in range(iterations):
            current_point = Point(x + x_i, y)
            current_mid_point = current_point.get_midpoint()

            if linear_function.point_is_below(current_mid_point):
                points.append((current_point, "East"))

            else:
                points.append((current_point, "Northeast"))
                y += 1

        return points


if __name__ == "__main__":
    point_a = Point(1, 1)
    point_b = Point(9, 4)
    linear_function = LinearFunction(start=point_a, end=point_b)

    midpoint_line_algorithm = MidpointLineAlgorithm(linear_function=linear_function)

    points = midpoint_line_algorithm.run()

    print(points)
    #runs successfully
