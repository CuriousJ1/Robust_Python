class Rectangle:
    def __init__(self, height: int, width: int):
            self._height = height
            self._width = width
    def set_width(self, new_width):
        self._width = new_width
    def set_height(self, new_height):
        self._height = new_height
    def get_width(self) -> int:
        return self._width
    def get_height(self) -> int:
        return self._height

class Square(Rectangle):
    # super calls Rectangles constructor and calls the base class
    def __init__(self, length: int):
        super().__init__(length, length)
    def set_side_length(self, new_length):
        super().set_width(new_length)
        super().set_height(new_length)
    def set_width(self, new_width):
        self.set_side_length(new_width)
    def set_height(self, new_height):
        self.set_side_length(new_height)