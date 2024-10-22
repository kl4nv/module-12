import runner_and_tournament as run
import unittest
def repr(self):
    return self.name

def start(self):
    finishers = {}
    speed_runners = sorted(self.participants, key=lambda runner: runner.speed, reverse=True)
    for num in range(1, len(self.participants) + 1):
        finishers[num] = speed_runners[num - 1]
    return finishers

run.Runner.__repr__ = repr
run.Tournament.start = start

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    def setUp(self):
        self.one_runner = run.Runner('Усэйн', speed=10)
        self.two_runner = run.Runner('Андрей', speed=9)
        self.three_runner = run.Runner('Ник', speed=3)

    @classmethod
    def tearDownClass(cls):
        for numkey in range(1, 4):
            print(TournamentTest.all_result[numkey])

    def test_one(self):
        Usain_Nik = run.Tournament(90, self.one_runner, self.three_runner)
        TournamentTest.all_result[1] = Usain_Nik.start()
        self.assertTrue(TournamentTest.all_result[1][2] == 'Ник', 'Последним должен быть Ник')

    def test_two(self):
         Andrey_Nik = run.Tournament(90, self.two_runner, self.three_runner)
         TournamentTest.all_result[2] = Andrey_Nik.start()
         self.assertTrue(TournamentTest.all_result[2][2] == 'Ник', 'Последним должен быть Ник')

    def test_three(self):
         All_start = run.Tournament(90, self.one_runner, self.two_runner, self.three_runner)
         TournamentTest.all_result[3] = All_start.start()
         self.assertTrue(TournamentTest.all_result[3][3] == 'Ник', 'Последним должен быть Ник')

    def test_false(self):
        # Тестируем забег Усэйна(скорость 10) и Ника(скорость 3) на дистанцию 2. Первый в списке Ник
        false_start = run.Tournament(2, self.three_runner, self.one_runner)
        self.assertTrue(false_start.start()[2] == 'Ник', 'Последним должен быть Ник')
        # Выводит False если не переназначить start в Tournament


if __name__ == '__main__':
    unittest.main()
