from convex_hull.graph import is_left, WaitCommand
from manim import *


# TODO: Think about basing this class on a new Algorithm class which can contain animations, abstract run.
class JarvisMarch:

    def __init__(self, disable_animations = False):
        self.animations = []
        self.disable_animations = disable_animations

    def add_animation(self, animation):
        if not self.disable_animations:
            self.animations.append(animation)

    '''
        Runs Jarvis March Algorithm on the given points, 
        returns the convex hull points, fills the animations.
    '''
    def run(self, graph):

        hull_points = []
        hull_edges = []

        # ADD leftmost_point TO hull_points AND HIGHLIGHT IT.
        leftmost_point = graph.get_leftmost_point()
        hull_points.append(leftmost_point)
        self.add_animation(FadeToColor(leftmost_point.dot, color=RED))

        # ITERATIVELY ADD POINTS TO hull_points.
        best_next_hull_point_so_far = None
        iterations = 0
        while best_next_hull_point_so_far != leftmost_point and iterations < 10:
            iterations = iterations + 1
            recent_hull_point = hull_points[-1]

            best_next_hull_point_so_far = None
            best_next_hull_edge_so_far = None

            # ITERATE OVER ALL POINTS TO FIND NEXT POINT.
            for candidate_point in graph.points:
                self.add_animation(Flash(candidate_point.dot))
                candidate_edge = DashedLine(start=recent_hull_point.dot.get_center(),
                                      end=candidate_point.dot.get_center())
                self.add_animation(ShowCreation(candidate_edge))

                if recent_hull_point == best_next_hull_point_so_far or\
                        recent_hull_point == candidate_point or\
                        best_next_hull_point_so_far == candidate_point:
                    continue

                # CHECK IF candidate_point IS A BETTER THAN best_next_hull_point_so_far.
                if (best_next_hull_point_so_far is None) or \
                        is_left(recent_hull_point.position,
                                best_next_hull_point_so_far.position,
                                candidate_point.position):

                    best_next_hull_point_so_far = candidate_point
                    better_hull_edge = Line(start=recent_hull_point.dot.get_center(),
                                            end=best_next_hull_point_so_far.dot.get_center())

                    fade_candidate_edge = Uncreate(candidate_edge)

                    # SHOW best_next_hull_edge_so_far.
                    if best_next_hull_edge_so_far is None:
                        best_next_hull_edge_so_far = better_hull_edge
                        self.add_animation([ShowCreation(best_next_hull_edge_so_far),
                                           fade_candidate_edge])
                    else:
                        self.add_animation([Transform(best_next_hull_edge_so_far, better_hull_edge),
                                            fade_candidate_edge])
                        # No need to update best_ to better_. The transform does it.

                else:
                    self.add_animation(Uncreate(candidate_edge))

            # ADD best_next_hull_point_so_far TO THE HULL.
            hull_points.append(best_next_hull_point_so_far)

            # DISPLAY THE HULL GROWING TO NEXT EDGE.
            next_hull_edge = Line(start=recent_hull_point.dot.get_center(),
                             end=best_next_hull_point_so_far.dot.get_center(),
                             color=YELLOW)

            hull_edges.append(next_hull_edge)

            # self.wait(0.5)
            self.add_animation(WaitCommand(0.5))
            self.add_animation(Transform(best_next_hull_edge_so_far, next_hull_edge))
            self.add_animation(WaitCommand(0.5))
            # self.wait(0.5)

        return hull_points, hull_edges
        # We would have a cyclic list. First and last values same.

    # end run_jarvis_march