import unittest
import logging
from tests_12_3 import RunnerTest
from rt_with_exceptions import Runner

def test_new_walk(self):
    try:
        start = Runner('Bob', speed=-5)
        for _ in range(1, 11):
            start.walk()
        self.assertEqual(start.distance, 50)
        logging.info('"test_walk" выполнен успешно')
    except ValueError:
        logging.warning("Неверная скорость для Runner", exc_info=True)

RunnerTest.test_walk = test_new_walk

def test_new_run(self):
    try:
        start = Runner(['Karl'])
        for _ in range(1, 11):
            start.run()
        self.assertEqual(start.distance, 100)
        logging.info('"test_run" выполнен успешно')
    except TypeError:
        logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

RunnerTest.test_run = test_new_run

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                        encoding='UTF-8', format='%(asctime)s # %(levelname)s # %(message)s')

    unittest.main()
