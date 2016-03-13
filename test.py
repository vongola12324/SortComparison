import unittest
import randnum
import bubble
import selection
import insert
import heap
import quick
import copy


class SortTestCase(unittest.TestCase):

    def test_bubblesort(self):
        source = randnum.rand(50)
        target = copy.deepcopy(source)
        bubble.sort(source)
        self.assertEqual(source, sorted(target))

    def test_selectionsort(self):
        source = randnum.rand(50)
        target = copy.deepcopy(source)
        selection.sort(source)
        self.assertEqual(source, sorted(target))

    def test_insertsort(self):
        source = randnum.rand(50)
        target = copy.deepcopy(source)
        insert.sort(source)
        self.assertEqual(source, sorted(target))

    def test_heapsort(self):
        source = randnum.rand(50)
        target = copy.deepcopy(source)
        heap.sort(source)
        self.assertEqual(source, sorted(target))

    def test_quicksort(self):
        source = randnum.rand(50)
        target = copy.deepcopy(source)
        quick.sort(source)
        self.assertEqual(source, sorted(target))


if __name__ == '__main__':
    unittest.main()
