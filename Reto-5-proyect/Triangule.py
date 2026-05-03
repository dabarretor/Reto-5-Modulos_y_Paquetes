import math
from shape import Shape, Line, Point

class Triangle(Shape):
    def __init__(
        self,
        base: float,
        height: float,
        start_point: Point,
        angles: list[float],
        top_offset_x: float,
    ):
        self._base = base
        self._height = height
        self._start_point = start_point

        p1_vertex = self._start_point
        p2_x = self._start_point.get_x() + self._base
        p2_y = self._start_point.get_y()
        p2_vertex = Point(p2_x, p2_y)
        p3_x = self._start_point.get_x() + top_offset_x
        p3_y = self._start_point.get_y() + self._height
        p3_vertex = Point(p3_x, p3_y)

        self._line1 = Line(p1_vertex, p2_vertex)
        self._line2 = Line(p2_vertex, p3_vertex)
        self._line3 = Line(p3_vertex, p1_vertex)

        self._lines = [self._line1, self._line2, self._line3]

        super().__init__(
            is_regular=False,
            vertices=[p1_vertex, p2_vertex, p3_vertex],
            edges=self._lines,
            inner_angles=angles,
        )

    def get_base(self) -> float:
        return self._base

    def set_base(self, base: float):
        self._base = base

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float):
        self._height = height

    def get_start_point(self) -> Point:
        return self._start_point

    def set_start_point(self, start_point: Point):
        self._start_point = start_point

    def compute_area(self):
        return (self._base * self._height) / 2


class Isosceles(Triangle):
    def __init__(self, height: float, start_point: Point, side_length: float):
        super().__init__(
            base=side_length,
            height=height,
            start_point=start_point,
            angles=[80.0, 50.0, 50.0],
            top_offset_x=int(side_length / 2),
        )


class Equilateral(Triangle):
    def __init__(self, side_length: float, start_point: Point):
        height = (math.sqrt(3) / 2) * side_length
        super().__init__(
            base=side_length,
            height=height,
            start_point=start_point,
            angles=[60.0, 60.0, 60.0],
            top_offset_x=int(side_length / 2),
        )


class Scalene(Triangle):
    def __init__(
        self, base: float, height: float, start_point: Point, top_offset_x: float
    ):
        super().__init__(
            base=base,
            height=height,
            start_point=start_point,
            angles=[100.0, 50.0, 30.0],
            top_offset_x=top_offset_x,
        )


class Trirectangle(Triangle):
    def __init__(self, base: float, height: float, start_point: Point):
        super().__init__(
            base=base,
            height=height,
            start_point=start_point,
            angles=[90.0, 45.0, 45.0],
            top_offset_x=0,
        )
