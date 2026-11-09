"""CSC 1001 - Programming Assignment 1: student-written unit tests.

At least two separate unit tests for each of the eight functions in hw1.py.

Run with: python -m unittest hw1_tests.py
"""

import math
import unittest

import data
import hw1


class TestHomework1(unittest.TestCase):

    # Part 1: vowel_count
    def test_vowel_count_case_insensitive(self):
        self.assertEqual(hw1.vowel_count("Apple"), 2)
        self.assertEqual(hw1.vowel_count("AEIOU aeiou"), 10)

    def test_vowel_count_empty_string(self):
        self.assertEqual(hw1.vowel_count(""), 0)

    def test_vowel_count_no_vowels(self):
        self.assertEqual(hw1.vowel_count("rhythm, gym!"), 0)

    def test_vowel_count_sentence(self):
        self.assertEqual(hw1.vowel_count("Cal Poly Engineering"), 7)

    # Part 2: short_lists
    def test_short_lists_mixed_lengths(self):
        items = [[1], [2, 3], [], [4, 5, 6], [7, 8]]
        self.assertEqual(hw1.short_lists(items), [[2, 3], [7, 8]])

    def test_short_lists_no_matching_lengths(self):
        self.assertEqual(hw1.short_lists([[1], [], [4, 5, 6]]), [])

    def test_short_lists_empty_input(self):
        self.assertEqual(hw1.short_lists([]), [])

    def test_short_lists_input_unchanged(self):
        items = [[1], [2, 3], [4, 5, 6]]
        hw1.short_lists(items)
        self.assertEqual(items, [[1], [2, 3], [4, 5, 6]])

    # Part 3: ascending_pairs
    def test_ascending_pairs_reversed_pairs(self):
        items = [[9, 2], [3, 1, 2], [5, 5]]
        self.assertEqual(hw1.ascending_pairs(items), [[2, 9], [3, 1, 2], [5, 5]])

    def test_ascending_pairs_other_lengths_unchanged(self):
        items = [[], [7], [3, 2, 1], [1, 2, 3, 4]]
        self.assertEqual(hw1.ascending_pairs(items),
                         [[], [7], [3, 2, 1], [1, 2, 3, 4]])

    def test_ascending_pairs_already_in_order(self):
        self.assertEqual(hw1.ascending_pairs([[1, 4], [-3, 0]]), [[1, 4], [-3, 0]])

    def test_ascending_pairs_input_unchanged(self):
        items = [[9, 2], [8, 1]]
        hw1.ascending_pairs(items)
        self.assertEqual(items, [[9, 2], [8, 1]])

    # Part 4: add_prices
    def test_add_prices_no_cents_carry(self):
        result = hw1.add_prices(data.Price(3, 20), data.Price(1, 45))
        self.assertEqual(result, data.Price(4, 65))

    def test_add_prices_with_cents_carry(self):
        result = hw1.add_prices(data.Price(3, 75), data.Price(2, 50))
        self.assertEqual(result, data.Price(6, 25))

    def test_add_prices_cents_exactly_100(self):
        result = hw1.add_prices(data.Price(0, 60), data.Price(0, 40))
        self.assertEqual(result, data.Price(1, 0))

    def test_add_prices_max_cents(self):
        result = hw1.add_prices(data.Price(5, 99), data.Price(4, 99))
        self.assertEqual(result, data.Price(10, 98))

    # Part 5: rectangle_area
    def test_rectangle_area_standard_rectangle(self):
        rect = data.Rectangle(data.Point(0, 3), data.Point(4, 0))
        self.assertAlmostEqual(hw1.rectangle_area(rect), 12)

    def test_rectangle_area_negative_coordinates(self):
        rect = data.Rectangle(data.Point(-5, -1), data.Point(-2, -4))
        self.assertAlmostEqual(hw1.rectangle_area(rect), 9)

    def test_rectangle_area_crossing_origin(self):
        rect = data.Rectangle(data.Point(-2.5, 1.5), data.Point(1.5, -0.5))
        self.assertAlmostEqual(hw1.rectangle_area(rect), 8.0)

    # Part 6: books_by_author
    def test_books_by_author_matching_authors(self):
        b1 = data.Book(["Ann Lee"], "First")
        b2 = data.Book(["Bo Diaz", "Ann Lee"], "Second")
        b3 = data.Book(["Cy Park"], "Third")
        self.assertEqual(hw1.books_by_author("Ann Lee", [b1, b2, b3]), [b1, b2])

    def test_books_by_author_no_matches(self):
        books = [data.Book(["Bo Diaz"], "One"), data.Book(["Cy Park"], "Two")]
        self.assertEqual(hw1.books_by_author("Ann Lee", books), [])

    def test_books_by_author_empty_list(self):
        self.assertEqual(hw1.books_by_author("Ann Lee", []), [])

    def test_books_by_author_multiple_authors(self):
        b1 = data.Book(["Ann Lee", "Bo Diaz", "Cy Park"], "Team Book")
        self.assertEqual(hw1.books_by_author("Cy Park", [b1]), [b1])

    # Part 7: circle_bound
    def test_circle_bound_square(self):
        rect = data.Rectangle(data.Point(0, 2), data.Point(2, 0))
        expected = data.Circle(data.Point(1, 1), math.sqrt(2))
        self.assertEqual(hw1.circle_bound(rect), expected)

    def test_circle_bound_non_square_rectangle(self):
        rect = data.Rectangle(data.Point(-4, 3), data.Point(4, -3))
        expected = data.Circle(data.Point(0, 0), 5)
        self.assertEqual(hw1.circle_bound(rect), expected)

    def test_circle_bound_offset_rectangle(self):
        rect = data.Rectangle(data.Point(1, 10), data.Point(7, 2))
        expected = data.Circle(data.Point(4, 6), 5)
        self.assertEqual(hw1.circle_bound(rect), expected)

    # Part 8: below_pay_average
    def test_below_pay_average_different_pay_rates(self):
        employees = [data.Employee("Ana", 10),
                     data.Employee("Ben", 20),
                     data.Employee("Cam", 30)]
        self.assertEqual(hw1.below_pay_average(employees), ["Ana"])

    def test_below_pay_average_empty_list(self):
        self.assertEqual(hw1.below_pay_average([]), [])

    def test_below_pay_average_all_equal(self):
        employees = [data.Employee("Ana", 15), data.Employee("Ben", 15)]
        self.assertEqual(hw1.below_pay_average(employees), [])

    def test_below_pay_average_several_below(self):
        employees = [data.Employee("Ana", 12),
                     data.Employee("Ben", 18),
                     data.Employee("Cam", 40),
                     data.Employee("Dee", 10)]
        self.assertEqual(hw1.below_pay_average(employees), ["Ana", "Ben", "Dee"])


if __name__ == '__main__':
    unittest.main()