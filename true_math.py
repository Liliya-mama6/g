import urban
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        a=urban.Runner('turtle')
        for i in range(10):
            a.walk()
        self.assertEqual(a.distance, 50)
    def test_run(self):
        a=urban.Runner('frog')
        for i in range(10):
            a.run()
        self.assertEqual(a.distance, 100)
    def test_challenge(self):
        a=urban.Runner('pomidurov')
        b=urban.Runner('oguchok')
        for i in range(10):
            a.run()
            b.walk()
        self.assertNotEqual(a.distance, b.distance)
    
