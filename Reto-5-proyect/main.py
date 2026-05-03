from Rectangule import Rectangle # , Square
from shape import Line, Point  # , Shape
from Triangule import Triangle  # , Equilateral, Scalene, Trirectangle, Isosceles

if __name__ == "__main__":
    rectangle = Rectangle(point1=Point(0.5, -3.54), point2=Point(4.5, 0.46))
    area = rectangle.compute_area()
    perimeter = rectangle.compute_perimeter()
    interference = rectangle.compute_interference_point(Point(2, -1))
    interference_line = rectangle.compute_interference_line(
        Line(Point(0, 0), Point(5, 0))
    )

    print("RECTANGLE DATA:")
    print(
        f"Width: {rectangle._width} and Height: {rectangle._height}"
    )  # Output: Width: 4.0 and Height: 4.0
    print(
        f"Center Point: ({rectangle._center_point._x}, {rectangle._center_point._y})"
    )  # Output: Center Point: (2.5, -1.54)
    print(f"Area: {round(area, 2)}")  # Output: Area: 16.0
    print(f"Perimeter: {round(perimeter, 2)}")  # Output: Perimeter: 16.0
    print(f"Interference: {interference}")  # Output: Interference: True
    print(f"Interference Line: {interference_line}")  # Output: Interference Line: False

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
    print(f"Area: {round(rect_from_lines.compute_area(), 2)}")  # Output: Area: 12.0
    print(
        f"Perimeter: {round(rect_from_lines.compute_perimeter(), 2)}"
    )  # Output: Perimeter: 14.0
    print(f"\n{'-' * 30}")

    line = Line(Point(1, 2), Point(4, 6))
    length = line.get_length()
    slope = line.compute_slope()
    horizontal_cross = line.compute_horizontal_cross()
    vertical_cross = line.compute_vertical_cross()

    print("\nLINES DATA: ")
    print(f"Length: {round(line.get_length(), 2)}")  # Output: Length: 5.0
    print(f"Slope: {round(line.compute_slope(), 2)}")  # Output: Slope: 53.13
    # Output: Horizontal cross: False
    print(f"Horizontal cross: {line.compute_horizontal_cross()}")
    # Output: Vertical cross: False
    print(f"Vertical cross: {line.compute_vertical_cross()}")
    print("-" * 30)

    print("\nTRIANGLE DATA:")
    triangle = Triangle(
        start_point=Point(0.0, 2.0),
        height=5.0,
        base=4.25,
        angles=[80.0, 50.0, 50.0],
        top_offset_x=2,
    )
    area = triangle.compute_area()
    perimeter = triangle.compute_perimeter()
    print(f"Area: {round(area, 2)}")  # Output: Area: 10.62
    print(f"Perimeter: {round(perimeter, 2)}")  # Output: Perimeter: 15.12
