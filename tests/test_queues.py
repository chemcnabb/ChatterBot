from unittest import TestCase
from chatterbot.utils.queues import ResponseQueue


class ResponseQueueTests(TestCase):

    def setUp(self):
        self.queue = ResponseQueue(maxsize=2)

    def test_append(self):
        self.queue.append(0)
        self.assertIn(0, self.queue)

    def test_contains(self):
        self.queue.queue.append(0)
        self.assertIn(0, self.queue)

    def test_maxsize(self):
        self.queue.append(0)
        self.queue.append(1)
        self.queue.append(2)

        self.assertNotIn(0, self.queue)
        self.assertIn(1, self.queue)
        self.assertIn(2, self.queue)
