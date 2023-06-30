from abc import ABC,abstractmethod


class Shape(ABC):

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):

    def draw(self):
        return f'This is a Circle '


class Square(Shape):

    def draw(self):
        return f'This is a Square '


class ShapeFactory:

    @staticmethod
    def create_shape(shape_type):
        shapes = dict(circle = Circle(), square = Square())
        response = shapes.get(shape_type)
        if response is not None:
            return response
        raise ValueError(f'shape {shape_type} not in the factory')


shape = ShapeFactory.create_shape('square')
shape = shape.draw()
print(shape)