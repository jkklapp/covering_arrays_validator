import unittest
import numpy
from validator import covers
from validator import get_column

class TestGetColumn(unittest.TestCase):

    def setUp(self):
        self.array1 = []
        self.array1.append(["0", "0", "0", "0"])
        self.array1.append(["0", "1", "1", "1"])
        self.array1.append(["1", "1", "0", "1"])
        self.array1.append(["1", "0", "1", "1"])
        self.array2 = []
        self.array2.append(["0", "0", "0", "0"])
        self.array2.append(["0", "1", "1", "1"])
        self.array2.append(["1", "0", "1", "1"])
        self.array2.append(["1", "1", "0", "1"])
        self.array2.append(["1", "1", "1", "0"])

    def test_get_column_from_array(self):
        array = self.array1
        t = get_column(array, 0)
        self.assertEqual(t, ["0", "0", "1", "1"])
        t = get_column(array, 1)
        self.assertEqual(t, ["0", "1", "1", "0"])
        t = get_column(array, 2)
        self.assertEqual(t, ["0", "1", "0", "1"])
        t = get_column(array, 3)
        self.assertEqual(t, ["0", "1", "1", "1"])
        array = self.array2
        t = get_column(array, 0)
        self.assertEqual(t, ["0", "0", "1", "1", "1"])
        t = get_column(array, 1)
        self.assertEqual(t, ["0", "1", "0", "1", "1"])
        t = get_column(array, 2)
        self.assertEqual(t, ["0", "1", "1", "0", "1"])
        t = get_column(array, 3)
        self.assertEqual(t, ["0", "1", "1", "1", "0"])

    def test_covers(self):
        array = self.array2
        is_covering = covers(array, 2, 4, 5)
        self.assertTrue(is_covering)

    def test_not_covers(self):
        array = self.array1
        is_covering = covers(array, 2, 4, 4)
        self.assertFalse(is_covering)

if __name__ == '__main__':
    unittest.main()
