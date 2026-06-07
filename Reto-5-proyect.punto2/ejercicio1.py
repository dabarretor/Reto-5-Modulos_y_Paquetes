import math


class Point:
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    def get_x(self) -> float:
        return self._x

    def set_x(self, new_x: float):
        self._x = new_x

    def get_y(self) -> float:
        return self._y

    def set_y(self, new_y: float):
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

    def compute_slope(self) -> float:
        dy = self._end_point._y - self._start_point._y
        dx = self._end_point._x - self._start_point._x
        radians = math.atan2(dy, dx)
        angle = math.degrees(radians)
        return angle

    def compute_horizontal_cross(self) -> bool:
        if (self._end_point._y * self._start_point._y) <= 0:
            return True
        else:
            return False

    def compute_vertical_cross(self) -> bool:
        if (self._end_point._x * self._start_point._x) <= 0:
            return True
        else:
            return False

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


class Rectangle(Shape):
    def __init__(self, **kwargs):
        # The rectangle can be created using different combinations of parameters using the **kwargs syntax.
        # In case 1, the rectangle is created using the width, height, and bottom left corner.
        if "width" in kwargs and "height" in kwargs and "bottom_left_corner" in kwargs:
            self._width = kwargs["width"]
            self._height = kwargs["height"]
            bottom_left_corner = kwargs["bottom_left_corner"]

            center_x = bottom_left_corner.get_x() + (self._width / 2)
            center_y = bottom_left_corner.get_y() + (self._height / 2)

            self._center_point = Point(center_x, center_y)

        # In case 2, the rectangle is created using the width, height, and center point.
        elif "width" in kwargs and "height" in kwargs and "center_point" in kwargs:
            self._width = kwargs["width"]
            self._height = kwargs["height"]
            self._center_point = kwargs["center_point"]

        # In case 3, the rectangle is created using two opposite corners.
        elif "point1" in kwargs and "point2" in kwargs:
            self.point1 = kwargs["point1"]
            self.point2 = kwargs["point2"]
            width = abs(self.point2._x - self.point1._x)
            height = abs(self.point2._y - self.point1._y)
            center_x = (self.point1._x + self.point2._x) / 2
            center_y = (self.point1._y + self.point2._y) / 2

            self._width = width
            self._height = height
            self._center_point = Point(center_x, center_y)
        # In case 4, the rectangle is created using the four lines that form it.
        elif (
            "bottom_line" in kwargs
            and "top_line" in kwargs
            and "left_line" in kwargs
            and "right_line" in kwargs
        ):
            self._bottom_line = kwargs["bottom_line"]
            self._top_line = kwargs["top_line"]
            self._left_line = kwargs["left_line"]
            self._right_line = kwargs["right_line"]

            width = self._bottom_line.get_length()
            height = self._left_line.get_length()

            # We calculate the center point of the rectangle using the midpoint formula
            b_start = self._bottom_line.get_start_point()
            b_end = self._bottom_line.get_end_point()
            l_start = self._left_line.get_start_point()
            l_end = self._left_line.get_end_point()

            center_x = (b_start.get_x() + b_end.get_x()) / 2
            center_y = (l_start.get_y() + l_end.get_y()) / 2

            self._center_point = Point(center_x, center_y)
            self._width = width
            self._height = height

        min_x = self._center_point.get_x() - (self._width / 2)
        max_x = self._center_point.get_x() + (self._width / 2)
        min_y = self._center_point.get_y() - (self._height / 2)
        max_y = self._center_point.get_y() + (self._height / 2)

        p_bottom_left = Point(min_x, min_y)
        p_bottom_right = Point(max_x, min_y)
        p_top_left = Point(min_x, max_y)
        p_top_right = Point(max_x, max_y)

        self._bottom_line = Line(p_bottom_left, p_bottom_right)
        self._top_line = Line(p_top_left, p_top_right)
        self._left_line = Line(p_bottom_left, p_top_left)
        self._right_line = Line(p_bottom_right, p_top_right)

        self._lines = [
            self._bottom_line,
            self._top_line,
            self._left_line,
            self._right_line,
        ]
        super().__init__(
            is_regular=False,
            vertices=[p_bottom_left, p_bottom_right, p_top_left, p_top_right],
            edges=self._lines,
            inner_angles=[90.0, 90.0, 90.0, 90.0],
        )

    def compute_interference_point(self, point: Point):
        """This function determines if a point is inside the rectangle or not.
        For this, the maximum and minimum values of x and y
        that a point can have to be inside the rectangle are calculated.
        """
        Min_x = self._center_point._x - (
            self._width / 2
        )  # Represents the entire left edge.
        Max_x = self._center_point._x + (
            self._width / 2
        )  # Represents the entire right edge.
        Min_y = self._center_point._y - (
            self._height / 2
        )  # Represents the entire bottom edge.
        Max_y = self._center_point._y + (
            self._height / 2
        )  # Represents the entire top edge.

        """ If the given point has coordinates x and y that are within 
        the calculated maximum and minimum values, then the point is inside
        the rectangle and the function returns True. 
        Otherwise, it returns False.
        """

        if Max_x >= point._x >= Min_x and Max_y >= point._y >= Min_y:
            return True
        else:
            return False

    def compute_interference_line(self, line: Line):
        """Use the compute_interference_point function to determine
        if at least one point is inside the rectangle.
        If so, the line segment interferes with the rectangle,
        and the function returns True. Otherwise, it returns False."""

        is_start_inside = self.compute_interference_point(line.get_start_point())
        is_end_inside = self.compute_interference_point(line.get_end_point())
        if is_start_inside or is_end_inside:
            return True
        else:
            return False

    def get_width(self) -> float:
        return self._width

    def set_width(self, width: float):
        self._width = width

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float):
        self._height = height

    def get_center_point(self) -> Point:
        return self._center_point

    def set_center_point(self, center_point: Point):
        self._center_point = center_point

    def compute_area(self):
        return self._width * self._height


class Square(Rectangle):
    def __init__(self, side_length: float, center_point: Point):
        super().__init__(
            height=side_length, width=side_length, center_point=center_point
        )


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
            top_offset_x=side_length / 2,
        )


class Equilateral(Triangle):
    def __init__(self, side_length: float, start_point: Point):
        height = (math.sqrt(3) / 2) * side_length
        super().__init__(
            base=side_length,
            height=height,
            start_point=start_point,
            angles=[60.0, 60.0, 60.0],
            top_offset_x=side_length / 2,
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


if __name__ == "__main__":
    rectangle = Rectangle(point1=Point(5, -3), point2=Point(4, 0))
    area = rectangle.compute_area()
    perimeter = rectangle.compute_perimeter()
    interference = rectangle.compute_interference_point(Point(2, -1))
    interference_line = rectangle.compute_interference_line(
        Line(Point(0, 0), Point(5, 0))
    )

    print("RECTANGLE DATA:")
    print(
        f"Width: {rectangle._width} and Height: {rectangle._height}"
    )  # Output: Width: 1 and Height: 3
    print(
        f"Center Point: ({rectangle._center_point._x}, {rectangle._center_point._y})"
    )  # Output: Center Point: (4.5, -1.5)
    print(f"Area: {round(area, 2)}")  # Output: Area: 3
    print(f"Perimeter: {round(perimeter, 2)}")  # Output: Perimeter: 8.0
    print(f"Interference: {interference}")  # Output: Interference: False
    print(f"Interference Line: {interference_line}")  # Output: Interference Line: True

    print("---  test of point 2: New method with four lines (method_4) ---")
    p1 = Point(0, 0)
    p2 = Point(4, 0)
    p3 = Point(0, 3)
    p4 = Point(4, 3)

    # A new rectangle is created using 4 lines
    rect_from_lines = Rectangle(
        bottom_line=Line(p1, p2),
        top_line=Line(p3, p4),
        left_line=Line(p1, p3),
        right_line=Line(p2, p4),
    )
    print(f"Area: {rect_from_lines.compute_area()}")  # Output: Area: 12.0
    print(
        f"Perimeter: {rect_from_lines.compute_perimeter()}"
    )  # Output: Perimeter: 14.0
    print(f"\n{'-' * 30}")

    line = Line(Point(1, 2), Point(4, 6))
    length = line.get_length()
    slope = line.compute_slope()
    horizontal_cross = line.compute_horizontal_cross()
    vertical_cross = line.compute_vertical_cross()

    print("\nLINES DATA: ")
    print(f"length: {round(length, 2)}")  # Output: length: 5.0
    print(f"slope: {round(slope, 2)}")  # Output: slope: 53.13
    # Output: horizontal cross: False
    print(f"horizontal cross: {line.compute_horizontal_cross()}")
    # Output: vertical cross: False
    print(f"vertical cross: {line.compute_vertical_cross()}")
    print(f"\n{'-' * 30}")

    print("\nTRIANGLE DATA:")
    triangle = Triangle(
        start_point=Point(0, 2),
        height=5.0,
        base=4.25,
        angles=[80.0, 50.0, 50.0],
        top_offset_x=2.0,
    )
    area = triangle.compute_area()
    perimeter = triangle.compute_perimeter()
    print(f"Area: {round(area, 2)}")  # Output: Area: 10.62
    print(f"Perimeter: {round(perimeter, 2)}")  # Output: Perimeter: 15.12
