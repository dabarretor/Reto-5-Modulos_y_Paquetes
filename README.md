# Reto 5

---

1. Create a package with all code of class Shape, this exersice should be conducted in two ways:

- A unique module inside of package Shape

- Individual modules that import Shape in inheritates from it.

```mermaid
classDiagram

class Shape {
    +is_regular : bool
    +vertices: list(Point)
    +edges: list(Line)
    +inner_angles: list(float)
    +compute_area(self)
    +compute_perimeter(self)
    +compute_inner_angles(self)
}

class Point {
    +x : int
    +y : int
    +compute_distance(self, Point)
}

class Line {
    +start_point : Point
    +end_point : Point
    +length : float
}


class Rectangle {
}

class Isosceles {
}

class Equilateral { 
}

class Scalene {   
}

class TriRectangle {
}

class Square {
}

Triangle <|-- TriRectangle
Triangle <|-- Isosceles
Triangle <|-- Equilateral
Triangle <|-- Scalene

Rectangle <|-- Square

Shape <|-- Rectangle
Shape <|-- Triangle
Shape *-- Line
Shape *-- Point
```
[Solución_en_python](Reto-5-proyect/main.py)
