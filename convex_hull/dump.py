def animate_hull(self):
    hull_indices = [1, 3, 5, 8, 10, 12, 13, 1]
    h = len(hull_indices) - 1
    sample_hull_dots = []

    # HIGHLIGHT HULL POINTS
    for i in range(h):
        self.play(FadeToColor(self.dots[hull_indices[i]], RED))
        sample_hull_dots.append(self.dots[hull_indices[i]])

    start = hull_indices[0]
    sample_hull_lines = []

    # GROW HULL EDGES
    for i in range(1, h + 1):
        end = hull_indices[i]
        line = Line(self.points[start], self.points[end]).set_color(YELLOW)
        sample_hull_lines.append(line)
        self.play(ShowCreation(line))
        # self.wait(0.2)
        start = end

    self.wait(2)

    # REMOVE HULL EDGES, UN-HIGHLIGHT HULL POINTS.
    self.play(*[FadeOut(line) for line in sample_hull_lines])
    self.play(*[FadeToColor(dot, WHITE) for dot in sample_hull_dots])


def run_jarvis_march(self):
    # ADD LEFT MOST POINT TO THE HULL.
    leftmost_point_index = self.get_leftmost_point()
    hull_indices = [leftmost_point_index]

    # HIGHLIGHT LEFT MOST POINT.
    self.play(FadeToColor(
        self.dots[leftmost_point_index], color=RED))

    # ITERATIVELY ADD POINTS TO THE HULL.
    new_hull_point = None
    iterations = 0
    while new_hull_point != leftmost_point_index and iterations < 10:
        iterations = iterations + 1
        recent_hull_point = hull_indices[-1]

        new_hull_point = None
        new_hull_line = None

        # ITERATE OVER ALL POINTS TO FIND NEXT POINT.
        for i in range(len(self.points)):
            self.play(Flash(self.dots[i]))

            if recent_hull_point == new_hull_point or recent_hull_point == i or new_hull_point == i:
                continue

            # CHECK IF POINT i IS A BETTER NEXT HULL POINT CANDIDATE.
            if self.is_left(recent_hull_point, new_hull_point, i):
                new_hull_point = i

                better_line = Line(start=self.points[recent_hull_point],
                                   end=self.points[new_hull_point])

                # DISPLAY THE BETTER NEXT EDGE CANDIDATE.
                if new_hull_line is None:
                    new_hull_line = better_line
                    self.play(ShowCreation(new_hull_line))
                else:
                    self.play(Transform(new_hull_line, better_line))

        # ADD THE BEST NEXT CANDIDATE TO THE HULL.
        hull_indices.append(new_hull_point)

        # DISPLAY THE HULL GROWING TO NEXT EDGE.
        hull_line = Line(start=self.points[recent_hull_point],
                         end=self.points[new_hull_point],
                         color=YELLOW)
        self.wait(0.5)
        self.play(Transform(new_hull_line, hull_line))
        self.wait(0.5)

    return hull_indices
    # We would have a cyclic list. First and last values same.

# end run_jarvis_march

    def is_left(self, line_start_index, line_end_index, point_index):
        if line_end_index is None:
            return True

        line_start = self.points[line_start_index]
        line_end = self.points[line_end_index]
        point = self.points[point_index]

        return is_left(line_start, line_end, point)

    def get_leftmost_point(self):
        leftmost_point_index = None
        leftmost_point_position = 100
        for i in range(self.size):
            if self.points[i][0] < leftmost_point_position:
                leftmost_point_index = i
                leftmost_point_position = self.points[i][0]

        return leftmost_point_index

    def get_bottommost_point(self):
        # Find bottom-most point.
        bottom_most_point_index = None
        bottom_most_point_position = 100
        for i in range(self.size):
            if self.points[i][0] < bottom_most_point_position:
                bottom_most_point_index = i
                bottom_most_point_position = self.points[i][0]

        return bottom_most_point_index


def graham_scan()
    hull_points = []

    # FIND BOTTOM MOST POINT
    bottom_most_point_index = self.get_bottommost_point()
    self.play(FadeToColor(self.dots[bottom_most_point_index], RED))

    # SORT POINTS IN ANTI-CLOCKWISE ORDER BASED ON BOTTOM MOST POINT.
    required_permutation = rank_by_angle(self.points, bottom_most_point_index)
    self.points = reorder(self.points, required_permutation)

    # DISPLAY THE SORTED LABELS.
    new_dots = [create_dot_2d(p) for p in self.points]
    new_labels = [TextMobject(str(i)).next_to(new_dots[i])
                  for i in range(self.size)]

    self.play(*tuple([ReplacementTransform(
        self.dots[i], new_dots[required_permutation[i]])
        for i in range(self.size)]))

    self.play(*tuple([ReplacementTransform(
        self.labels[i], new_labels[i])
        for i in range(self.size)]))

    self.wait(2)

    # ADD THE BOTTOM MOST POINT AND IT'S MOST ANTI-CLOCKWISE POINT TO THE HULL.
    hull_indices = [0, 1]

    line = Line(start=self.points[0], end=self.points[1])
    self.play(ShowCreation(line))
    hull_edges = [line]

    for i in range(2, self.size):

        new_hull_line = Line(start=self.points[hull_indices[-1]],
                             end=self.points[i])
        self.play(ShowCreation(new_hull_line))
        hull_edges.append(new_hull_line)

        all_joints_turn_left = False

        while not all_joints_turn_left:

            # TAKE LAST TWO EDGES.
            recent_hull_point = i
            second_recent_hull_point = hull_indices[-1]
            third_recent_hull_point = hull_indices[-2]

            recent_edge = hull_edges[-1]
            second_recent_edge = hull_edges[-2]

            last_two_edges = VGroup(recent_edge, second_recent_edge)
            # self.play(Flash(recent_edge), Flash(second_recent_edge))
            self.play(FadeToColor(last_two_edges, BLUE))

            if not self.is_left(third_recent_hull_point,
                                second_recent_hull_point,
                                recent_hull_point):

                hull_edges.pop()
                hull_edges.pop()
                hull_indices.pop()

                better_edge = Line(start=self.points[recent_hull_point],
                                   end=self.points[third_recent_hull_point])
                hull_edges.append(better_edge)

                # self.play(Uncreate(second_recent_edge), Uncreate(recent_edge))
                # self.play(ShowCreation(better_edge))
                self.play(ReplacementTransform(last_two_edges, better_edge))

            else:
                self.play(FadeToColor(last_two_edges, WHITE))
                all_joints_turn_left = True
                hull_indices.append(i)
    # end for

    # ADD THE FIRST (BOTTOM MOST) POINT TO COMPLETE CYCLE.
    recent_hull_point = hull_indices[-1]

    new_hull_line = Line(start=self.points[recent_hull_point],
                         end=self.points[0])
    self.play(ShowCreation(new_hull_line))
    hull_edges.append(new_hull_line)

    return hull_indices

# end graham scan

def rank_by_angle(points, bottom_most_point_index):
    # Move all points to base.
    points = [x for x in points]  # deep copy of list
    base_x, base_y, base_dummy_z = points[bottom_most_point_index]

    rebased_points = [[x-base_x, y-base_y, 0] for [x, y, dummy_z] in points]

    # negative cos theta is monotonically increasing and finite in [0,pi],
    # and can be used to sort points in a anti-clockwise sweep.

    neg_cos_angle = [- safe_cos(x,y) for x, y, dummy_z in rebased_points]

    # Find rank.
    indices = list(range(len(neg_cos_angle)))
    indices.sort(key=lambda x: neg_cos_angle[x])
    rank = [0] * len(indices)
    for i, x in enumerate(indices):
        rank[x] = i

    return rank


def reorder(points, required_permutation):
    size = len(required_permutation)
    output = [0] * size

    for i in range(size):
        output[required_permutation[i]] = points[i]

    return output

def split_points_into_groups_ave(points, dots, m):
    size = len(points)
    ave = math.floor(size/m)
    rem = size % m

    groups_of_points = [[] for i in range(m)]
    groups_of_dots = [[] for i in range(m)]

    for i in range(rem):
        groups_of_points[i] = points[(ave+1) * i: (ave+1) * (i+1)]
        groups_of_dots[i] = dots[(ave+1) * i: (ave+1) * (i+1)]

    classified = (ave+1) * rem

    for i in range(rem, m):
        j = i - rem
        groups_of_points[i] = points[classified + ave * j: classified + ave * (j+1)]
        groups_of_dots[i] = dots[classified + ave * j: classified + ave * (j+1)]

    return groups_of_points, groups_of_dots
