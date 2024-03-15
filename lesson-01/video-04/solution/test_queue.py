import unittest
from queue import Queue


class TestQueue(unittest.TestCase):

    def test_is_empty(self):
        queue = Queue()
        self.assertTrue(queue.is_empty())

        queue.enqueue(1)
        self.assertFalse(queue.is_empty())

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        self.assertEqual(queue.size(), 3)

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        self.assertIsNone(queue.dequeue())

    def test_size(self):
        queue = Queue()
        self.assertEqual(queue.size(), 0)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        self.assertEqual(queue.size(), 3)


if __name__ == '__main__':
    unittest.main()
