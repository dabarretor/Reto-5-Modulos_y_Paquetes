import math

class Point:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    def get_x(self) -> int:
        return self._x

    def set_x(self, new_x: int):
        self._x = new_x

    def get_y(self) -> int:
        return self._y

    def set_y(self, new_y: int):
        self._y = new_y

    def compute_distance(self, other_point: "Point") -> float:
        length = math.sqrt(
            ((other_point.get_x() - self.get_x()) ** 2)
            + ((other_point.get_y() - self.get_y()) ** 2)
        )
        return length


class Line:
    def __init__(self, start_point: Point, end_point: Point):
        self._start_point = start_point
        self._end_point = end_point
        self._length = self._start_point.compute_distance(self._end_point)

    def get_start_point(self) -> Point:
        return self._start_point

    def set_start_point(self, new_start: Point):
        self._start_point = new_start

    def get_end_point(self) -> Point:
        return self._end_point

    def set_end_point(self, new_end: Point):
        self._end_point = new_end

    def get_length(self) -> float:
        return self._length

    def compute_slope(self) -> float:
        dy = self._end_point.get_y() - self._start_point.get_y()
        dx = self._end_point.get_x() - self._start_point.get_x()
        radians = math.atan2(dy, dx)
        angle = math.degrees(radians)
        return angle

    def compute_horizontal_cross(self) -> bool:
        if (self._end_point.get_y() * self._start_point.get_y()) <= 0:
            return True
        else:
            return False

    def compute_vertical_cross(self) -> bool:
        if (self._end_point.get_x() * self._start_point.get_x()) <= 0:
            return True
        else:
            return False


class Shape:
    def __init__(
        self,
        is_regular: bool,
        vertices: list[Point],
        edges: list[Line],
        inner_angles: list[float],
    ):
        self._is_regular = is_regular
        self._vertices = vertices
        self._edges = edges
        self._inner_angles = inner_angles

    def get_is_regular(self) -> bool:
        return self._is_regular

    def set_is_regular(self, regular: bool):
        self._is_regular = regular

    def get_vertices(self) -> list[Point]:
        return self._vertices

    def set_vertices(self, vertices: list[Point]):
        self._vertices = vertices

    def get_edges(self) -> list[Line]:
        return self._edges

    def set_edges(self, edges: list[Line]):
        self._edges = edges

    def get_inner_angles(self) -> list[float]:
        return self._inner_angles

    def set_inner_angles(self, angles: list[float]):
        self._inner_angles = angles

    def compute_area(self):
        raise NotImplementedError

    def compute_perimeter(self):
        perimeter = 0
        for line in self._edges:
            perimeter += line.get_length()
        return perimeter
