"""
Lab7 CIS210 Fall 2014

Class inheritance practice using common shapes which build on a base class called shapes.
Define subclasses using two dimensional shapes (circle, square, rectangle, triangle, parallelogram)

Using the base class Shape, define a subclass for circle.
"""
import math


class Shape:
    """
        The base class Shape defines some common methods that should be implemented in all subclasses
    """


    def __init__(self):
        """
        Define the init method to accept dimensional arguments which will describe the shape.
        """
        pass

    @property
    def area(self):
        """
        Returns the area of the shape
        """
        raise NotImplementedError

    @property
    def circumference(self):
        """
        Returns the circumference of the shape
        """
        raise NotImplementedError


    # Comparison operators. For equality and inequality, we include a check of whether the object is of the same
    # class

    def __eq__(self, other):
        """
        Equality test between two shapes. For a shape to be equal, it must be of the same type and have
        the same dimensions. Use the built-in function isinstance to test if an object is of certain class.
        Overload this method to include dimensional tests
        """
        if isinstance(self, Shape) and isinstance(other, Shape) and self.area == other.area:
            return True
        else:
            return False


    def __ne__(self, other):
        """
        The negation of __eq__()
        """
        if not isinstance(other, Shape):
            return False

        return self.area != other.area


    def __ge__(self, other):
        """
        Returns True if the area this (self) shape is greater than the area of other
        """
        return self.area >= other.area


    def __le__(self, other):
        """
        Returns True if the area of this (self) shape is less than or equal to the area of other
        """
        return self.area <= other.area


    def __gt__(self, other):
        """
        The negation of __le__()
        """
        return not self.__le__(other)


    def __lt__(self, other):
        """
        The negation of __ge__()
        """
        return not self.__ge__(other)


# Math on shapes, build new shapes by combining the area of two different shapes

    def __add__(self, other):
        """
        Add two shapes together (lhs + rhs). The summation should be of the same subclass as the lhs with an
        area equal to the combined area of lhs and rhs. As an example: circle = circle + square, mutates circle by
        increasing the radius such that the area equals circle.area() + square.area().
        """
        raise NotImplementedError


    def __sub__(self, other):
        """
        Subtracts other shape from this shape (lhs - rhs). The result should be of the same subclass as the lhs with
        and area equal to the area of lhs less the area of rhs. If the resulting area would be zero or less than
        None is returned.
    """


    def __str__(self):
        """
        Returns a string representation of the shape in the form of "shape[dimensions ..., area, circumference]"
        """
        return "shape[]"


class Circle(Shape): 


    def __init__(self, radius):
        """
        A circle is defined by its radius
        """
        self.radius = radius


    @property
    def area(self):
        """
        Returns the area of the shape
        """
        
        return math.pi * (self.radius**2)

    @property
    def circumference(self):
        """
        Returns the circumference of the shape
        """

        return math.pi * 2 * self.radius

    # Comparison operators. For equality and inequality, we include a check of whether the object is of the same
    # class

    '''
    def __eq__(self, other):
        """
        Equality test between two shapes. For a shape to be equal, it must have the same 
        area.
        Overload this method to include dimensional tests
        """

        if (super().__eq__(other)) and (self.area == other.area):
            return True

        return False


    def __ge__(self, other):
        """
        Returns True if the area this (self) shape is greater than the area of other
        """

    
        return self.area <= other.area


    def __le__(self, other):
        """
        Returns True if the area of this (self) shape is less than or equal to the area of other
        """

        return self.area <= other.area

    '''
    

# Math on shapes, build new shapes by combining the area of two different shapes

    def __add__(self, other):
        """
        Creates a new instance of circle by increasing the radius such that the area equals circle.area() + other.area().
        """
        new_area = self.area + other.area
        new_radius = math.sqrt(new_area/math.pi)
        new_circle = Circle(new_radius)

        return new_circle



    def __sub__(self, other):
        """
        Subtracts other shape from this shape (lhs - rhs).  If the resulting area would be zero or less, than
        None is return
        """
        if self.area < other.area:
            return None

        new_area = self.area + other.area
        new_radius = math.sqrt(new_area/math.pi)
        new_circle = Circle(new_radius)

        return new_circle


    def __str__(self):
        """
        Returns a string representation of the shape in the form of "shape[dimensions ..., area, circumference]"
        """
        return "circle[{:.1f},{:.1f},{:.1f}]".format(self.radius, self.area, self.circumference)


def main():
    """
    Run some tests
    """

    A = Circle(1)
    B = Circle(2)

    print("A={}".format(A))
    print("B={}".format(B))
    print("(A == A) = {}".format(A == A))
    print("(A == B) = {}".format(A == B))
    print("(A != B) = {}".format(A != B))
    print("(A < B) = {}".format(A < B))
    print("(A > B) = {}".format(A > B))
    print("(A + B) = {}".format(A + B))
    print("(B - A) = {}".format(B - A))

if __name__ == "__main__":
    main()



