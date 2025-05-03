

class Shape:
   
    """
    Base class for all shapes.

    Attributes:
        name (str): Name of the shape.
    """

    def __init__(self, name):
        """
        Initialize a shape with a name.
        """
        self.name = name

    def area(self):
        """
        Calculate area of the shape. Should be overridden.
        """
        raise NotImplementedError("Subclasses must implement area method.")

    def __str__(self):
        """
        String representation of the shape.
        """
        return f"A shape named {self.name}"


class Circle(Shape):
    """
    Circle shape with a radius.
    """

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        super().__init__("Circle")
        self.radius = radius
         
    def area(self):
        return 3.14 * self.radius ** 2

    def __str__(self):
        return f"{self.name} with radius {self.radius}"


class Rectangle(Shape):
    """
    Rectangle shape with width and height.
    """

    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive.")
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"{self.name} with width {self.width} and height {self.height}"


class Triangle(Shape):
    """
    Triangle shape with base and height.
    """

    def __init__(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive.")
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __str__(self):
        return f"{self.name} with base {self.base} and height {self.height}"