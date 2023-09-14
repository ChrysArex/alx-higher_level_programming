import unittest
from models import base


class TestBase(unittest.TestCase):
    def test_doc_mod(self):
        self.assertEqual(base.__doc__, "Define the base class of all "\
                "the futur classes")
        self.assertEqual(base.Base.__doc__, "Class Base")
        self.assertEqual(base.Base.__init__.__doc__, "Initialized the "\
                "values of id\n\n        Args:\n            id : "\
                "identifier of the base instance\n        ")
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
