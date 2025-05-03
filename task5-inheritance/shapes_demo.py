from shapes import Circle, Rectangle, Triangle

def show_shape_info(shape):
    print(shape)
    print(f"Area: {shape.area():.2f}\n")

shapes = [
    Circle(4),
    Rectangle(3, 5),
    Triangle(6, 2)
]

for shape in shapes:
    show_shape_info(shape)
