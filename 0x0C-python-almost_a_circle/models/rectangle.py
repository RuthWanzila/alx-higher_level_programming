from models.base import Base


class Rectangle(Base):
    """
    Rectangle subclass, inherited from Base Class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize the Rectangle object.
        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): x-coordinate of the rectangle's position. Defaults to 0.
            y (int, optional): y-coordinate of the rectangle's position. Defaults to 0.
            id (int, optional): Identifier of the rectangle. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter method for the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width of the rectangle."""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Getter method for the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height of the rectangle."""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Getter method for the x-coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for the x-coordinate of the rectangle's position."""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Getter method for the y-coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for the y-coordinate of the rectangle's position."""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Display the rectangle visually."""
        print(self.y * '\n', end='')
        row = self.x * ' ' + self.width * '#'
        print('\n'.join([row for _ in range(self.height)]))

    def __str__(self):
        """Return a string representation of the rectangle."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Update the attributes of the rectangle."""
        if args and len(args) > 0:
            for idx, arg in enumerate(args):
                if idx == 0:
                    super().__init__(arg)
                if idx == 1:
                    self.width = arg
                if idx == 2:
                    self.height = arg
                if idx == 3:
                    self.x = arg
                if idx == 4:
                    self.y = arg
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    super().__init__(value)
                if key == 'width':
                    self.width = value
                if key == 'height':
                    self.height = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """Convert the rectangle object to a dictionary representation."""
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
