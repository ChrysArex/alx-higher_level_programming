import unittest
from models import rectangle
import sys
from io import StringIO


class TestRectangle(unittest.TestCase):

    def test_priv_attr(self):
        r1 = rectangle.Rectangle(10, 2)
        r2 = rectangle.Rectangle(2, 10)
        r3 = rectangle.Rectangle(10, 2, 0, 0, 12)
        #self.assertEqual(r1.id, 5)
        #self.assertEqual(r2.id, 6)
        #self.assertEqual(r3.id, 12)

    def test_doc_mod(self):
        self.assertEqual(rectangle.__doc__, "Define a Rectangle class "\
                "derived from Base class")
        self.assertEqual(rectangle.Rectangle.__doc__, "Class Rectangle")
        self.assertEqual(rectangle.Rectangle.__init__.__doc__, "Initialize "\
                "the values")
        self.assertEqual(rectangle.Rectangle.area.__doc__, "Compute the "\
                "area of an rectangle instance\n\n        "\
                "Return:\n            the area of the rectangle\n        ")
        self.assertEqual(rectangle.Rectangle.display.__doc__, " Print the "\
                "rectangle instance with #")
        self.assertEqual(rectangle.Rectangle.__str__.__doc__, "Define a "\
                "printable value of the Rectangle instance\n\n        "\
                "Return:\n            the string form of the instance\n        ")
        self.assertEqual(rectangle.Rectangle.update.__doc__, "Update the "\
                "initial data of the Rectangle instance")

    def test__attr_validator(self):
        with self.assertRaises(TypeError) as e:
            rectangle.Rectangle(10, "2")
            self.assertEqual(e, "height must be an integer")
        with self.assertRaises(ValueError) as e:
            r = rectangle.Rectangle(10, 2)
            r.width = -10
            self.assertEqual(e, "width must be > 0")
        with self.assertRaises(TypeError):
            r = rectangle.Rectangle(10, 2)
            r.x = {}
            self.assertEqual(e, "x must be an integer")
        with self.assertRaises(ValueError):
            rectangle.Rectangle(10, 2, 3, -1)
            self.assertEqual(e, "y must be >= 0")

    def test_area(self):
        r5 = rectangle.Rectangle(3, 2)
        r6 = rectangle.Rectangle(2, 10)
        r7 = rectangle.Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r5.area(), 6)
        self.assertEqual(r6.area(), 20)
        self.assertEqual(r7.area(), 56)

    def test_print(self):
        new_std = StringIO()
        sys.stdout =  new_std
        r1 = rectangle.Rectangle(2, 3, 2, 2)
        r2 = rectangle.Rectangle(3, 2, 1, 0)
        r1_ = rectangle.Rectangle(4, 6, 2, 1, 12)
        r2_ = rectangle.Rectangle(5, 5, 1)
        r1.display()
        self.assertEqual(new_std.getvalue(), "\n\n  ##\n  ##\n  ##\n")
        new_std.seek(0)
        new_std.truncate()
        print(r1_)
        self.assertEqual(new_std.getvalue(), "[Rectangle] (" + str(r1_.id) + \
                ") 2/1 - 4/6\n")
        new_std.seek(0)
        new_std.truncate()
        r2.display()
        self.assertEqual(new_std.getvalue(), " ###\n ###\n")
        new_std.seek(0)
        new_std.truncate()
        print(r2_)
        self.assertEqual(new_std.getvalue(), "[Rectangle] (" + str(r2_.id) + ") "\
                "1/0 - 5/5\n")
        sys.stdout = sys.__stdout__

    def test_update(self):
        new_std = StringIO()
        sys.stdout = new_std
        r1 = rectangle.Rectangle(10, 10, 10, 10)
        print(r1)
        self.assertEqual(new_std.getvalue(), "[Rectangle] (" + str(r1.id) + \
                ") 10/10 - 10/10\n")
        new_std.seek(0)
        new_std.truncate()
        r1.update(89)
        print(r1)
        self.assertEqual(new_std.getvalue(), "[Rectangle] (" + str(r1.id) + \
                ") 10/10 - 10/10\n")
        new_std.seek(0)
        new_std.truncate()
        r1.update(89, 2)
        print(r1)
        self.assertEqual(new_std.getvalue(), "[Rectangle] (" + str(r1.id) + \
                ") 10/10 - 2/10\n")
        new_std.seek(0)
        new_std.truncate()
        r1.update(89, 2, 3)
        print(r1)
        self.assertEqual(new_std.getvalue(), "[Rectangle] (" + str(r1.id) + \
                ") 10/10 - 2/3\n")
        new_std.seek(0)
        new_std.truncate()
        r1.update(89, 2, 3, 4)
        print(r1)
        self.assertEqual(new_std.getvalue(), "[Rectangle] (" + str(r1.id) + \
                ") 4/10 - 2/3\n")
        new_std.seek(0)
        new_std.truncate()
        r1.update(89, 2, 3, 4, 5)
        print(r1)
        self.assertEqual(new_std.getvalue(), "[Rectangle] (" + str(r1.id) + \
                ") 4/5 - 2/3\n")
        new_std.seek(0)
        new_std.truncate()
        r1 = rectangle.Rectangle(10, 10, 10, 10)
        print(r1)
        self.assertEqual(new_std.getvalue(), "[Rectangle] (" + str(r1.id) + \
                ") 10/10 - 10/10\n")
        new_std.seek(0)
        new_std.truncate()
        r1.update(height=1)
        print(r1)
        self.assertEqual(new_std.getvalue(), "[Rectangle] (" + str(r1.id) + \
                ") 10/10 - 10/1\n")
        new_std.seek(0)
        new_std.truncate()
        r1.update(width=1, x=2)
        print(r1)
        self.assertEqual(new_std.getvalue(), "[Rectangle] (" + str(r1.id) + \
                ") 2/10 - 1/1\n")
        new_std.seek(0)
        new_std.truncate()
        r1.update(y=1, width=2, x=3, id=89)
        print(r1)
        self.assertEqual(new_std.getvalue(), "[Rectangle] (" + str(r1.id) + \
                ") 3/1 - 2/1\n")
        new_std.seek(0)
        new_std.truncate()
        r1.update(x=1, height=2, y=3, width=4)
        print(r1)
        self.assertEqual(new_std.getvalue(), "[Rectangle] (" + str(r1.id) + \
                ") 1/3 - 4/2\n")
        new_std.seek(0)
        new_std.truncate()
        r1.update(45, 33, x=55, y=22)
        print(r1)
        self.assertEqual(new_std.getvalue(), "[Rectangle] (" + str(r1.id) + \
                ") 1/3 - 33/2\n")
        sys.stdout = sys.__stdout__

    def test_dict_representation(self):
        r1 = rectangle.Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        r2 = rectangle.Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(r1_dictionary, {'x': 1, 'y': 9, \
                'id': r1.id, 'height': 2, 'width': 10})
        self.assertIs(type(r1_dictionary), dict)
        self.assertNotEqual(r1, r2)


