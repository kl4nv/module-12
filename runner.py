import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        run = Runner('Bob')
        for _ in range(1, 11):
            run.walk()
        self.assertEqual(run.distance, 50)

    def test_run(self):
        run = Runner('Karl')
        for _ in range(1, 11):
            run.run()
        self.assertEqual(run.distance, 100)

    def test_challenge(self):
        run1 = Runner('Alice')
        run2 = Runner('Max')
        for _ in range(1, 11):
            run1.run()
            run2.walk()
        self.assertNotEqual(run1.distance, run2.distance)

if __name__ == '__main__':
    unittest.main()