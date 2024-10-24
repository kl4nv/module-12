import unittest
from runner import Runner
import runner_and_tournament as run

class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        start = Runner('Bob')
        for _ in range(1, 11):
            start.walk()
        self.assertEqual(start.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        start = Runner('Karl')
        for _ in range(1, 11):
            start.run()
        self.assertEqual(start.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        start1 = Runner('Alice')
        start2 = Runner('Max')
        for _ in range(1, 11):
           start1.run()
           start2.walk()
        self.assertNotEqual(start1.distance, start2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    def setUp(self):
        self.one_runner = run.Runner('Усэйн', speed=10)
        self.two_runner = run.Runner('Андрей', speed=9)
        self.three_runner = run.Runner('Ник', speed=3)

    @classmethod
    def tearDownClass(cls):
        list_key = cls.all_result.keys()
        if len(list_key) >= 1:
            for numkey in list_key:
                print(cls.all_result[numkey])

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_one(self):
        Usain_Nik = run.Tournament(90, self.one_runner, self.three_runner)
        TournamentTest.all_result[1] = Usain_Nik.start()
        self.assertTrue(TournamentTest.all_result[1][2] == 'Ник', 'Последним должен быть Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_two(self):
         Andrey_Nik = run.Tournament(90, self.two_runner, self.three_runner)
         TournamentTest.all_result[2] = Andrey_Nik.start()
         self.assertTrue(TournamentTest.all_result[2][2] == 'Ник', 'Последним должен быть Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_three(self):
         All_start = run.Tournament(90, self.one_runner, self.two_runner, self.three_runner)
         TournamentTest.all_result[3] = All_start.start()
         self.assertTrue(TournamentTest.all_result[3][3] == 'Ник', 'Последним должен быть Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_false(self):
        # Тестируем забег Усэйна(скорость 10) и Ника(скорость 3) на дистанцию 2. Первый в списке Ник
        false_start = run.Tournament(2, self.three_runner, self.one_runner)
        self.assertTrue(false_start.start()[2] == 'Ник', 'Последним должен быть Ник')
        # Выводит False если не переназначить start в Tournament


