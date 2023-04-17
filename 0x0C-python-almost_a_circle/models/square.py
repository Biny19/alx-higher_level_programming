#!/usr/bin/python3
"""
   Define Rectangle Class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
"""
   Module Representation of Square
"""

    def __init__(self, size, x=0, y=0, id=None):
        """
           Initialization a Square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ 
            module string represation of square
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
    @property
    def size(self):
        """
            module Square size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            module Square size setter
        """
        self.width = value
        self.height = value

   def update(self, *args, **kwargs):
        """
            module update square
        """
        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.size = arg
                elif i == 1:
                    self.x = arg
                elif i == 2:
                    self.y = arg
                elif i == 3:
                    self.id = arg
        else:
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
            if "id" in kwargs:
                self.id = kwargs["id"]

    def to_dictionary(self):
        """
            retrun dictonary
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
            }
