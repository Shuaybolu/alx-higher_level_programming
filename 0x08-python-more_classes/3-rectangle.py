#!/usr/bin/python3
"""This module defines a Rectangle class."""


class Rectangle:
   """A class that defines a rectangle."""

   def __init__(self, width=0, height=0):
       """Initialize the Rectangle.

       Args:
           width (int): The width of the rectangle.
           height (int): The height of the rectangle.
       """
       self.width = width
       self.height = height

   @property
   def width(self):
       """Get the width of the Rectangle."""
       return self.__width

   @width.setter
   def width(self, value):
       """Set the width of the Rectangle.

       Args:
           value (int): The width value to set.

       Raises:
           TypeError: If width is not an integer.
           ValueError: If width is less than 0.
       """
       if not isinstance(value, int):
           raise TypeError("width must be an integer")
       if value < 0:
           raise ValueError("width must be >= 0")
       self.__width = value

   @property
   def height(self):
       """Get the height of the Rectangle."""
       return self.__height

   @height.setter
   def height(self, value):
       """Set the height of the Rectangle.

       Args:
           value (int): The height value to set.

       Raises:
           TypeError: If height is not an integer.
           ValueError: If height is less than 0.
       """
       if not isinstance(value, int):
           raise TypeError("height must be an integer")
       if value < 0:
           raise ValueError("height must be >= 0")
       self.__height = value

   def area(self):
       """Return the area of the Rectangle."""
       return self.__width * self.__height

   def perimeter(self):
       """Return the perimeter of the Rectangle."""
       if self.__width == 0 or self.__height == 0:
           return 0
       return 2 * (self.__width + self.__height)

   def __str__(self):
       """Return string representation of the Rectangle.

       Returns:
           str: The string representation of the Rectangle.
       """
       if self.__width == 0 or self.__height == 0:
           return ""
       rect = []
       for i in range(self.__height):
           rect.append("#" * self.__width)
       return "\n".join(rect)
