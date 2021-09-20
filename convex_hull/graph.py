import math

from manim import *

from convex_hull.point import Point as Pnt

import random
import time
random.seed(time.time()%1000)


class WaitCommand:
    def __init__(self, time_in_seconds):
        self.time_in_seconds = time_in_seconds


def safe_cos(adj, opp):
    hyp = math.sqrt(adj**2 + opp**2)

    # If it's the base point at the origin,
    # Return a maximum value so it's negative value will be ranked first.
    if hyp == 0:
        return 2

    return adj/hyp


def is_left(line_start, line_end, point):
    cross_product = (line_end[0] - line_start[0]) * (point[1] - line_start[1]) \
                    - (line_end[1] - line_start[1]) * (point[0] - line_start[0])

    return True if cross_product > 0 else False


def split_points_into_groups(points, dots, m):
    size = len(points)

    groups_of_points = [[] for i in range(m)]
    groups_of_dots = [[] for i in range(m)]
    for i in range(size):
        groups_of_points[i%m].append(points[i])
        groups_of_dots[i%m].append(dots[i])

    return groups_of_points, groups_of_dots

'''
    Here, a Graph refers to a bunch of points and some edges between the points.
'''
class Graph:

    points = []
    size = 0

    def __init__(self, coordinates):

        if isinstance(coordinates[0], Pnt):
            self.create_graph_from_points(coordinates)
            return

        for coordinate in coordinates:
            point = Pnt(coordinate)
            # point.set_dot()
            self.points.append(point)

        self.size = len(self.points)

    def create_graph_from_points(self, points):
        # TODO: Check if every value in points is a Point.
        self.points = points
        self.size = len(self.points)

    def get_leftmost_point(self):
        leftmost_point = self.points[0]

        for point in self.points:
            if point.position[0] < leftmost_point.position[0]:
                leftmost_point = point

        return leftmost_point

    def get_bottommost_point(self):
        bottommost_point = self.points[0]

        for point in self.points:
            if point.position[1] < bottommost_point.position[1]:
                bottommost_point = point

        return bottommost_point

    ''' Returns the rank in increasing order of angle
        made by points in the graph
        to the horizontal line (positive X direction) 
        passing through reference_point.
    '''
    def rank_by_angle(self, reference_point):

        base_x, base_y, dummy_base_z = reference_point.position

        rebased_point_positions = [[point.position[0] - base_x,
                           point.position[1] - base_y,
                           0] for point in self.points]

        # negative cos theta is monotonically increasing and finite in [0,pi],
        # and can be used to sort points in an anti-clockwise sweep from
        # angle 0, which is the horizontal line in positive X direction.

        neg_cos_angle = [- safe_cos(x, y)
                         for x, y, dummy_z in rebased_point_positions]

        # Find rank.
        indices = list(range(len(neg_cos_angle)))
        indices.sort(key=lambda x: neg_cos_angle[x])
        rank = [0] * len(indices)
        for i, x in enumerate(indices):
            rank[x] = i

        return rank

    ''' Reorders points in the graph based on the 
        required_permutation given.
    '''
    def reorder(self, required_permutation):
        # TODO: Check if required_permutation is valid.
        size = len(required_permutation) # Why not use self.size?
        reordered_points = [None] * size

        # PERFORM REORDER
        for i in range(size):
            reordered_points[required_permutation[i]] = copy.deepcopy(self.points[i])
            reordered_points[required_permutation[i]].set_label(required_permutation[i])

        # CREATE ANIMATIONS
        dot_animations = []
        label_animations = []

        for i in range(size):
            dot_animations.append(ReplacementTransform(
                self.points[i].dot, reordered_points[required_permutation[i]].dot))

            label_animations.append(ReplacementTransform(
                self.points[i].label, reordered_points[i].label))

        self.points = reordered_points
        # deep copy in 141 ensures animations don't get overridden?

        return dot_animations, label_animations

    def split_points_into_groups_ave(self, m):
        ave = math.floor(self.size / m)
        rem = self.size % m

        groups_of_points = [[] for i in range(m)]

        for i in range(rem):
            groups_of_points[i] = self.points[(ave + 1) * i: (ave + 1) * (i + 1)]

        classified = (ave + 1) * rem

        for i in range(rem, m):
            j = i - rem
            groups_of_points[i] = self.points[classified + ave * j: classified + ave * (j + 1)]

        return groups_of_points
