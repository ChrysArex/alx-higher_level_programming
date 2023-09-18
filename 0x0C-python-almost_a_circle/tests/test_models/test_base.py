import unittest
from models import base
from models import rectangle
from models import square


class TestBase(unittest.TestCase):

    def test_doc_mod(self):
        self.assertEqual(base.__doc__, "Define the base class of all "\
                "the futur classes")
        self.assertEqual(base.Base.__doc__, "Class Base")
        self.assertEqual(base.Base.__init__.__doc__, "Initialized the "\
                "values of id\n\n        Args:\n            id : "\
                "identifier of the base instance\n        ")
        self.assertEqual(base.Base.from_json_string.__doc__, "returns the "\
                "list of the JSON string representation json_string")
        self.assertEqual(base.Base.create.__doc__, "returns an instance "\
                "with all attributes already set")
        self.assertEqual(base.Base.load_from_file.__doc__, "returns a list "\
                "of instances")

    def test_private_attr(self):
        with self.assertRaises(AttributeError):
            base.Base.__nb_objects

    def test_init_id(self):
        b1 = base.Base()
        b2 = base.Base()
        b4 = base.Base(12)
        b5 = base.Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 3)

    def test_to_json_string(self):
        r1 = rectangle.Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = base.Base.to_json_string([dictionary])
        self.assertIs(type(json_dictionary), str)
        json_dictionary = base.Base.to_json_string([])
        self.assertEqual(json_dictionary, "[]")
        json_dictionary = base.Base.to_json_string(None)
        self.assertEqual(json_dictionary, "[]")

    def test_save_to_file(self):
        r1 = rectangle.Rectangle(10, 7, 2, 8)
        r2 = rectangle.Rectangle(2, 4)
        rectangle.Rectangle.save_to_file([r1, r2])

    def test_from_json_string(self):
        list_input = [
        {'id': 89, 'width': 10, 'height': 4},
        {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = rectangle.Rectangle.to_json_string(list_input)
        list_output = rectangle.Rectangle.from_json_string(json_list_input)
        self.assertIs(type(list_output), list)
        self.assertEqual(list_output, [{'height': 4, 'width': 10, 'id': 89},\
                {'height': 7, 'width': 1, 'id': 7}])
        list_output = rectangle.Rectangle.from_json_string(None)
        self.assertEqual(list_output, [])
        list_output = rectangle.Rectangle.from_json_string("")
        self.assertEqual(list_output, [])

    def test_create(self):
        r1 = rectangle.Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = rectangle.Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_load_from_file(self):
        r1 = rectangle.Rectangle(10, 7, 2, 8)
        r2 = rectangle.Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        list_rectangles_output = rectangle.Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output, [])
        rectangle.Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = rectangle.Rectangle.load_from_file()
        self.assertEqual(str(list_rectangles_input[0]), \
                str(list_rectangles_output[0]))
        self.assertEqual(str(list_rectangles_input[1]), \
                str(list_rectangles_output[1]))
        list_squares_output = square.Square.load_from_file()
        s1 = square.Square(5)
        s2 = square.Square(7, 9, 1)
        list_squares_input = [s1, s2]
        square.Square.save_to_file(list_squares_input)
        list_squares_output = square.Square.load_from_file()
        self.assertEqual(str(list_squares_input[0]), \
                str(list_squares_output[0]))
        self.assertEqual(str(list_squares_input[1]), \
                str(list_squares_output[1]))
