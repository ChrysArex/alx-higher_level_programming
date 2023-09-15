import unittest
import sys
from io import StringIO
from models import square


class TestSquare(unittest.TestCase):

    def test_doc_mod(self):
        self.assertEqual(square.__doc__, "Define the Square class "\
                "derived from the Rectangle one")
        self.assertEqual(square.Square.__doc__, "Class Square")
        self.assertEqual(square.Square.__str__.__doc__, "String "\
                "representation of the square instance")
        self.assertEqual(square.Square.__init__.__doc__, "Initialize "\
                "the attributes")
        self.assertEqual(square.Square.size.__doc__, "getter for the size")

    def test_string(self):
        new_std = StringIO()
        sys.stdout = new_std
        s1 = square.Square(5)
        print(s1)
        print(s1.area())
        s1.display()
        self.assertEqual(new_std.getvalue(), "[Square] (" + str(s1.id) + \
                ") 0/0 - 5\n25\n#####\n#####\n#####\n#####\n#####\n")
        new_std.seek(0)
        new_std.truncate()
        s2 = square.Square(2, 2)
        print(s2)
        print(s2.area())
        s2.display()
        self.assertEqual(new_std.getvalue(), "[Square] (" + str(s2.id) + \
                ") 2/0 - 2\n4\n  ##\n  ##\n")
        new_std.seek(0)
        new_std.truncate()
        s3 = square.Square(3, 1, 3)
        print(s3)
        print(s3.area())
        s3.display()
        self.assertEqual(new_std.getvalue(), "[Square] (" + str(s3.id) + \
                ") 1/3 - 3\n9\n\n\n\n ###\n ###\n ###\n")
        new_std.seek(0)
        new_std.truncate()
        sys.stdout = sys.__stdout__

    def test_getter_setter(self):
        s1 = square.Square(5)
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(s1.size, 10)
        with self.assertRaises(TypeError) as e:
            s1.size = "9"
            self.assertEquale(e, "width must be an integer")
        with self.assertRaises(ValueError) as e:
            s1.size = -5
            self.assertEqual(e, "width must be > 0")

    def test_update(self):
        s1 = square.Square(5)
        self.assertEqual(s1.size, 5)
        s1.update(10)
        self.assertEqual(s1.id, 10)
        s1.update(1, 2)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 2)
        s1.update(1, 2, 3)
        self.assertEqual(s1.x, 3)
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.y, 4)
        s1.update(x=12)
        self.assertEqual(s1.x, 12)
        s1.update(size=7, y=1)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.y, 1)
        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.id, 89)

    def test_dict_representation(self):
        r1 = square.Square(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        r2 = square.Square(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(r1_dictionary, {'x': 2, 'y': 1, \
                'id': 9, "size": 10})
        self.assertIs(type(r1_dictionary), dict)
        self.assertNotEqual(r1, r2)
