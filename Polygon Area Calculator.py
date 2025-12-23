class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
    def set_width(self, value):
        self.width = value
    
    def set_height(self, value):
        self.height = value
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        shape = ''
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        for _ in range(self.height):
            shape += f'{"*" * self.width}\n'
        return shape

    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)
    

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f'Square(side={self.width})'
    
    def set_side(self, value):
        self.width = value
        self.height = value
    
    def set_width(self, value):
        self.width = value
        self.height = value
    
    def set_height(self, value):
        self.width = value
        self.height = value