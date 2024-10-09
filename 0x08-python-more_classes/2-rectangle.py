#!/usr/bin/python3

"""Module that defines a Rectangle class"""


class Rectangle:
   """Class that defines a rectangle"""

   def __init__(self, width=0, height=0):
       """Initialize rectangle with optional width and height

       Args:
           width (int): width of rectangle
           height (int): height of rectangle
       """
       self.width = width
       self.height = height

   @property
   def width(self):
       """Get the width of rectangle"""
       return self.__width

   @width.setter
   def width(self, value):
       """Set the width of rectangle

       Args:
           value (int): width value to set

       Raises:
           TypeError: if width is not an integer
           ValueError: if width is less than 0
       """
       if not isinstance(value, int):
           raise TypeError("width must be an integer")
       if value < 0:
           raise ValueError("width must be >= 0")
       self.__width = value

   @property
   def height(self):
       """Get the height of rectangle"""
       return self.__height

   @height.setter
   def height(self, value):
       """Set the height of rectangle

       Args:
           value (int): height value to set

       Raises:
           TypeError: if height is not an integer
           ValueError: if height is less than 0
       """
       if not isinstance(value, int):
           raise TypeError("height must be an integer")
       if value < 0:
           raise ValueError("height must be >= 0")
       self.__height = value

   def area(self):
       """Calculate and return the rectangle area

       Returns:
           int: The area of the rectangle
       """
       return self.__width * self.__height

   def perimeter(self):
       """Calculate and return the rectangle perimeter

       Returns:
           int: The perimeter of the rectangle
       """
       if self.__width == 0 or self.__height == 0:
           return 0
       return 2 * (self.__width + self.__height)
