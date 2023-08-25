'''
Write solutions to 4. New Mouse Release here.

Author:Minjae Kim
SID:530009478
Unikey:mkim9138
'''
from shop import buy_cheese
import unittest
from unittest.mock import patch
from mouse import Mouse
from game import change_cheese


class Testbuy_cheese(unittest.TestCase):
    def testcase1_positive(self):
        # side_effects mock user's inputs in multiple cases with a form of a list.
        with patch('builtins.input', side_effect=['Swiss 1', 'Cheddar 1', 'Cheddar 1', 'Marble 1', 'back']):
            result = buy_cheese(200)
        self.assertEqual(result, (170, (2, 1, 1)))

    def testcase2_positive(self):
        with patch('builtins.input', side_effect=['Swiss 2', 'back']):
            result = buy_cheese(230)
        self.assertEqual(result, (200, ((0, 0, 2))))

    def testcase03_negative(self):
        with patch('builtins.input', side_effect=['1 Swiss', 'back']):
            result = buy_cheese(100)
        self.assertEqual(result, (0, (0, 0, 0)))

    def testcase4_edge(self):
        with patch('builtins.input', side_effect=['', 'back']):
            result = buy_cheese(50)
        self.assertEqual(result, (0, (0, 0, 0)))

    def testcase5_negative(self):
        with patch('builtins.input', side_effect=['Cheddar -5', 'back']):
            result = buy_cheese(125)
        self.assertEqual(result, (0, (0, 0, 0)))

    def testcase6_edge(self):
        with patch('builtins.input', side_effect=['Cheddar 9223372036854775807', 'back']):
            result = buy_cheese(92233720368547758070)
        self.assertEqual(result, (92233720368547758070, (9223372036854775807, 0, 0)))


class Testmouse_probability(unittest.TestCase):
    def test_probability(self):
        expected_prob = [0.5, 0.1, 0.15, 0.1, 0.1, 0.05]
        mouse_occurrence = [["None", 0], ["Brown", 0], ["Field", 0], ["Grey", 0], ["White", 0], ["Tiny", 0]]
        i = 0
        while i < 10000:
            mouse_generate = Mouse()
            mouse_name = mouse_generate.__str__()
            num = 0
            while num < len(mouse_occurrence):
                if mouse_name == mouse_occurrence[num][0]:
                    mouse_occurrence[num][1] += 1
                num += 1
            i += 1
        probability = []
        a = 0
        while a < len(expected_prob):
            occur_prob = mouse_occurrence[a][1]/10000
            probability.append(occur_prob)
            a += 1
        j = 0
        while j < len(expected_prob):
            self.assertAlmostEqual(expected_prob[j], probability[j], 2, f"Incorrect probability for {mouse_occurrence[j][0]}")
            j += 1
        print('Similar probability')


class TestChangeCheese(unittest.TestCase):
    def testcase1positive_case(self):
        with patch('builtins.input', side_effect=["cHeDdAR", "yes", "back"]):
            result = change_cheese('Bob', 'Cardboard and Hook Trap', cheese=(["Cheddar", 10], ["Marble", 0], ["Swiss", 0]))
        self.assertEqual(result, (True, "Cheddar"))
        print('change cheese 1')

    def testcase2positive_case(self):
        with patch('builtins.input', side_effect=["Swiss", "no", "back"]):
            result = change_cheese('Bob', 'Cardboard and Hook Trap', cheese=(["Cheddar", 0], ["Marble", 0], ["Swiss", 1]))
        self.assertEqual(result, (False, None))
        print('change cheese 2')

    def testcase3negative_case(self):
        with patch('builtins.input', side_effect=["23", "back"]):
            result = change_cheese('Bob', 'Cardboard and Hook Trap', cheese=(["Cheddar", 3], ["Marble", 3], ["Swiss", 3]))
        self.assertEqual(result, (False, None))
        print('change cheese 3 number')

    def testcase4negative_case(self):
        with patch('builtins.input', side_effect=[f"{chr(27)}", "back"]):
            result = change_cheese('Bob', 'Cardboard and Hook Trap', cheese=(["Cheddar", 3], ["Marble", 3], ["Swiss", 3]))
        self.assertEqual(result, (False, None))
        print('change cheese 4 ESC')

    def testcase5edge_case(self):
        with patch('builtins.input', side_effect=["", "yes", "back"]):
            result = change_cheese('Bob', 'Cardboard and Hook Trap', cheese=(["", 0],))
        self.assertEqual(result, (True, ""))
        print('change cheese 5 empty')

    def testcase6edge_case(self):
        with patch('builtins.input', side_effect=["Cheddar", "yes", "back"]):
            with self.assertRaises(TypeError):
                change_cheese('Bob', 'Cardboard and Hook Trap', cheese=(["Cheddar", ""], ["Marble", 0], ["Swiss", 1]))


if __name__ == '__main__':
    unittest.main()