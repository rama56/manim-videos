from convex_hull.graph import WaitCommand, Graph as Grph

from convex_hull.jarvis_march import JarvisMarch
from convex_hull.graham_scan import GrahamScan
from manim import *

# TODO: Think about basing this class on a new Algorithm class which can contain animations, abstract run.
class Chan:
    def __init__(self, scene_camera, disable_animations=False):
        self.camera = scene_camera
        self.animations = []
        self.disable_animations = disable_animations

    def extend_animation(self, animations):
        if not self.disable_animations:
            self.animations.extend(animations)

    def add_animation(self, animation):
        if not self.disable_animations:
            self.animations.append(animation)

    '''
            Runs Chan's Algorithm on the given points, 
            returns the convex hull points, fills the animations.
    '''
    def run(self, graph):
        # SPLIT POINTS INTO GROUPS.
        m = 3  # number of groups.
        grouped_points = graph.split_points_into_groups_ave(m)

        colours = [YELLOW_E, GREEN_E, RED_E, BLUE_E, TEAL_E]
        small_graphs = []

        for i in range(m):
            points = grouped_points[i]

            small_graphs.append(Grph(points))

            self.add_animation(
                [FadeToColor(points[j].dot, colours[i]) for j in range(len(points))]
            )

            self.add_animation(WaitCommand(0.5))

        small_hull_points = []
        small_hull_edges = []
        for i in range(m):
            other_points = VGroup(*tuple([point.dot for point in graph.points if point not in small_graphs[i].points]))
            all_hull_edges = VGroup(*tuple([edge for hull in small_hull_edges for edge in hull]))

            self.add_animation(FadeToColor(other_points, GRAY))
            self.add_animation(FadeToColor(all_hull_edges, GRAY))
            algorithm = JarvisMarch()
            convex_hull_points, convex_hull_edges = algorithm.run(small_graphs[i])

            small_hull_points.append(convex_hull_points)
            small_hull_edges.append(convex_hull_edges)

            self.extend_animation(algorithm.animations)
            self.add_animation(WaitCommand(1))

        # RECOLOUR ALL HULLS.
        for i in range(m):
            self.add_animation([FadeToColor(point.dot, colours[i]) for point in small_hull_points[i]])
            self.add_animation([FadeToColor(edge, colours[i]) for edge in small_hull_edges[i]])

        # RUN JARVIS MARCH ON THE BUNCH OF SMALL HULLS.
        # TODO: How about just showing on 1 small hull?
        small_hull_origin = small_hull_points[0][0]
        self.add_animation(ShowCreationThenDestruction(small_hull_origin.dot))
        self.add_animation(self.camera.frame.animate.scale(0.5).move_to(small_hull_origin.dot.get_center()))

    # end chan algo
