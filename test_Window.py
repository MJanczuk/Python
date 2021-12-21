from unittest import TestCase


class Test(TestCase):
    def test_end(self):
        print(":(")
        self.fail()
