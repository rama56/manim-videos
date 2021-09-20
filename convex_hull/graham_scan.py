import copy
from manim import *
from convex_hull.graph import *


# TODO: Think about basing this class on a new Algorithm class which can contain animations, abstract run.
class GrahamScan:

    def __init__(self, disable_animations=False):
        self.animations = []
        self.disable_animations = disable_animations

    def add_animation(self, animation):
        if not self.disable_animations:
            self.animations.append(animation)

    '''
            Runs Graham Scan Algorithm on the given points, 
            returns the convex hull points, fills the animations.
    '''
    def run(self, graph):

        hull_points = []

        # ADD bottommost_point TO hull_points AND HIGHLIGHT IT.
        bottommost_point = graph.get_bottommost_point()
        hull_points.append(bottommost_point)

        highlight = bottommost_point.square_highlight()

        self.add_animation(FadeToColor(bottommost_point.dot, color=RED))
        self.add_animation(highlight)

        mobjects_created = self.show_sweep_animation(graph, bottommost_point)
        mobjects_created = VGroup(*tuple(mobjects_created))

        # SORT POINTS IN ANTI-CLOCKWISE SWEEP BASED ON bottommost_point.
        required_permutation = graph.rank_by_angle(bottommost_point)
        dot_animations, label_animations = graph.reorder(required_permutation)

        self.add_animation(dot_animations)
        self.add_animation(label_animations)
        self.add_animation(WaitCommand(1))

        self.add_animation(FadeOut(mobjects_created))

        # ADD THE BOTTOM MOST POINT AND IT'S MOST ANTI-CLOCKWISE POINT TO THE HULL.
        hull_points = [graph.points[0], graph.points[1]]

        hull_edge = Line(start=hull_points[0].dot.get_center(), end=hull_points[1].dot.get_center())
        self.add_animation(ShowCreation(hull_edge))

        hull_edges = [hull_edge]

        for point in graph.points[2:]:

            new_hull_edge = Line(start=hull_points[-1].dot.get_center(),
                                 end=point.dot.get_center())

            self.add_animation(ShowCreation(new_hull_edge))
            hull_edges.append(new_hull_edge)

            all_joints_turn_left = False

            while not all_joints_turn_left:

                # TAKE LAST TWO EDGES.
                recent_hull_point = point
                second_recent_hull_point = hull_points[-1]
                third_recent_hull_point = hull_points[-2]

                recent_edge = hull_edges[-1]
                second_recent_edge = hull_edges[-2]

                last_two_edges = VGroup(recent_edge, second_recent_edge)
                # self.play(Flash(recent_edge), Flash(second_recent_edge))
                self.add_animation(FadeToColor(last_two_edges, BLUE))

                if not is_left(third_recent_hull_point.position,
                               second_recent_hull_point.position,
                               recent_hull_point.position):

                    hull_edges.pop()
                    hull_edges.pop()
                    hull_points.pop()

                    better_hull_edge = Line(start=recent_hull_point.dot.get_center(),
                                       end=third_recent_hull_point.dot.get_center())

                    hull_edges.append(better_hull_edge)
                    self.add_animation(ReplacementTransform(last_two_edges, better_hull_edge))

                else:
                    self.add_animation(FadeToColor(last_two_edges, WHITE))
                    all_joints_turn_left = True
                    hull_points.append(point)
        # end for

        # ADD THE FIRST (BOTTOM MOST) POINT TO COMPLETE CYCLE.
        recent_hull_point = hull_points[-1]

        final_hull_edge = Line(start=recent_hull_point.dot.get_center(),
                               end=bottommost_point.dot.get_center())

        self.add_animation(ShowCreation(final_hull_edge))
        hull_edges.append(final_hull_edge)

        return hull_points

    # end graham scan

    def show_sweep_animation(self, graph, reference_point):

        mobjects_created = []

        og = reference_point.dot.get_center()

        lines_to_points = [DashedLine(og, point.dot.get_center()) for point in graph.points if point != reference_point]
        mobjects_created.extend(lines_to_points)

        self.add_animation([ShowCreation(line) for line in lines_to_points])

        base_line = Line(og + 12*LEFT, og + 12*RIGHT)
        # sweep_line = Line(og + DR, og + 10*RIGHT + 2*UP)
        sweep_line = DashedLine(og, og + 12*RIGHT).set_color(YELLOW)
        dupe_sweep = sweep_line.copy()
        mobjects_created.append(sweep_line)
        mobjects_created.append(dupe_sweep)

        theta_tracker = ValueTracker(0)

        # a = Angle(base_line, sweep_line, radius=0.5, other_angle=False).rotate(0.1, about_point=og)
        theta = MathTex(str(theta_tracker.get_value())).move_to(ORIGIN)
        mobjects_created.append(theta)

        # TODO: Why not VGroup here?
        show_items = [ShowCreation(base_line),
                      ShowCreation(sweep_line),
                      ShowCreation(theta)]
        # ShowCreation(a)

        self.add_animation(show_items)

        sweep_line.add_updater(
            lambda x: x.become(dupe_sweep.copy()).rotate(
                theta_tracker.get_value() * DEGREES, about_point=og
            )
        )

        # a.add_updater(
        #     lambda x: x.become(Angle(base_line, sweep_line, radius=0.5, other_angle=False))
        # )

        theta.add_updater(
            lambda x: x.become(MathTex(str(theta_tracker.get_value()))).move_to(og+DOWN)
        )

        self.add_animation(theta_tracker.animate.set_value(180))

        return mobjects_created
