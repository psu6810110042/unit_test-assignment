import unittest
from _6810110042.cat_and_mouse import cat_and_mouse


class CatAndMouseTest(unittest.TestCase):
    def test_cat_b_catches_mouse_first(self):
        # arrange
        x, y, z = 2, 5, 4
        expected_output = "Cat B"

        # act
        result = cat_and_mouse(x, y, z)

        # assert
        self.assertEqual(
            result,
            expected_output,
            "Cat B is closer (distance 1) than Cat A (distance 2).",
        )

    def test_cat_a_catches_mouse_first(self):
        # arrange
        x, y, z = 4, 9, 5
        expected_output = "Cat A"

        # act
        result = cat_and_mouse(x, y, z)

        # assert
        self.assertEqual(
            result,
            expected_output,
            "Cat A is closer (distance 1) than Cat B (distance 4).",
        )

    def test_mouse_escapes_when_equidistant(self):
        # arrange
        x, y, z = 1, 3, 2
        expected_output = "Mouse C"

        # act
        result = cat_and_mouse(x, y, z)

        # assert
        self.assertEqual(
            result,
            expected_output,
            "Both cats are exactly 1 unit away, so the mouse escapes.",
        )

    def test_cats_at_same_starting_position(self):
        # arrange
        x, y, z = 10, 10, 50
        expected_output = "Mouse C"

        # act
        result = cat_and_mouse(x, y, z)

        # assert
        self.assertEqual(
            result,
            expected_output,
            "Cats start together and arrive together, so the mouse escapes.",
        )

    def test_cat_a_starts_on_mouse(self):
        # arrange
        x, y, z = 5, 8, 5
        expected_output = "Cat A"

        # act
        result = cat_and_mouse(x, y, z)

        # assert
        self.assertEqual(
            result,
            expected_output,
            "Cat A is 0 units away and catches the mouse instantly.",
        )
