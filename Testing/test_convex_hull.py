from unittest import TestCase
import sys
print(sys.path)
from first_attempt.scene import *
from convex_hull.video import *

#from .. import convex_hull.plot_points


class TestConvexHull(TestCase):

    def test_graham_sort(self):
        points = get_input_points()
        bottom_most_point_index = 10

        # SORT POINTS IN ANTI-CLOCKWISE ORDER.
        required_permutation = rank_by_angle(points, bottom_most_point_index)
        points = reorder(points, required_permutation)

        x = 5

    def test_is_left(self):
        start = [2, 2]
        end = [5, 5]
        point = [6, 7]

        answer = is_left(start, end, point)

        assert answer is True

    def test_group_split(self):
        points = get_input_points()
        dots = [create_dot_2d(p) for p in points]

        # Round robin
        # grouped_points, grouped_dots = split_points_into_groups(points, dots, 5)
        # assert len(grouped_points[0]) == 3

        # Fill and move
        grouped_points, grouped_dots = split_points_into_groups_ave(points, dots, 5)
        assert len(grouped_points[0]) == 3

    def test_random_point_generator(self):
        points = get_random_input_points_rectangle(20)

        more_points = get_random_input_points_rectangle(20)

        assert points != more_points