from shape import Shape, Line, Point

class Rectangle(Shape):
    def __init__(self, **kwargs):
        # The rectangle can be created using different combinations of parameters using the **kwargs syntax.
        # In case 1, the rectangle is created using the width, height, and bottom left corner.
        if "width" in kwargs and "height" in kwargs and "bottom_left_corner" in kwargs:
            self._width = kwargs["width"]
            self._height = kwargs["height"]
            bottom_left_corner = kwargs["bottom_left_corner"]

            center_x = bottom_left_corner.x + (
                self._width / 2
            )  # The center is sought at x.
            center_y = bottom_left_corner.y + (
                self._height / 2
            )  # The center is sought in y.

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
            self.bottom_line = kwargs["bottom_line"]
            self.left_line = kwargs["left_line"]
            width = self.bottom_line.get_length()
            height = self.left_line.get_length()

            # We calculate the center point of the rectangle using the midpoint formula
            center_x = (
                self.bottom_line.get_start_point().get_x()
                + self.bottom_line.get_end_point().get_x()
            ) / 2
            center_y = (
                self.left_line.get_start_point().get_y()
                + self.left_line.get_end_point().get_y()
            ) / 2

            # The original __init__ is reused to create the rectangle
            self._width = width
            self._height = height
            self._center_point = Point(center_x, center_y)
        min_x = self._center_point.get_x() - int(self.get_width() / 2)
        max_x = self._center_point.get_x() + int(self.get_width() / 2)
        min_y = self._center_point.get_y() - int(self.get_height() / 2)
        max_y = self._center_point.get_y() + int(self.get_height() / 2)

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
        """This fuction determinate if a point is inside the rectangle or not.
        For this, the maximum and minimum values of x and y
        that a point can have to be inside the rectangle are calculated.
        """
        Min_x = self._center_point.get_x() - (
            self._width / 2
        )  # Represents the entire left edge.
        Max_x = self._center_point.get_x() + (
            self._width / 2
        )  # Represents the entire right edge.
        Min_y = self._center_point.get_y() - (
            self._height / 2
        )  # Represents the entire bottom edge.
        Max_y = self._center_point.get_y() + (
            self._height / 2
        )  # Represents the entire top edge.

        """ If the given point has coordinates x and y that are within 
        the calculated maximum and minimum values, then the point is inside
        the rectangle and the function returns True. 
        Otherwise, it returns False.
        """

        if Max_x >= point.get_x() >= Min_x and Max_y >= point.get_y() >= Min_y:
            return True
        else:
            return False

    def compute_interference_line(self, line: Line):
        """Use the compute_interference_point function to determine
        if at least one point is inside the rectangle.
        If so, the line segment interferes with the rectangle,
        and the function returns True. Otherwise, it returns False."""

        is_start_inside = self.compute_interference_point(line._start_point)
        is_end_inside = self.compute_interference_point(line._end_point)
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
