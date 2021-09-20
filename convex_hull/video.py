import os
from manim import *

from convex_hull.graph import Graph as Grph
from convex_hull.jarvis_march import *
from convex_hull.graham_scan import *
from convex_hull.chan_algo import *

import random
import time

random.seed(time.time() % 1000)

def get_input_point_coordinates():
    # Grid appears to be [-7,7]x[-4,4]
    # TODO: Read from a csv file.
    points = [[1, 0.5, 0],
              [2, 2, 0],
              [2, 0, 0],
              [4, 1, 0],
              [3, -1, 0],
              [4.5, -1, 0],
              [0.5, -1.5, 0],
              [2, -2.8, 0],
              [4, -3, 0],
              [-1.2, -3, 0],
              [-4, -3.5, 0],
              [-3, -2, 0],
              [-3, -1, 0],
              [-2, 1, 0]]
    return points


def get_random_input_points_rectangle(size):
    # Create a set of 'size' input points,
    # chosen independently and uniformly at random from [-7,7] x [-4,4]
    points = []
    for i in range(size):
        x = random.uniform(-6.5, 6.5)
        y = random.uniform(-3.5, 3.5)
        points.append([x, y, 0])

    return points


def get_random_input_points_circle(size):
    # Create a set of 'size' input points,
    # chosen independently and uniformly at random
    # from a circle of radius 5 centered at origin.

    points = []
    for i in range(size):
        radius = random.uniform(0, 5)
        angle = random.uniform(0, 2 * math.pi)
        points.append([radius * math.cos(angle), math.sin(angle), 0])

    return points
    # NOTE : This generation isn't uniformly at random !!!

'''
    It is a conscious decision to not base Video on GraphScene. We don't need the axes. 
    We don't need curve-plots (like y=x^2, referred to as graph in the manim community) 
'''
class Video(MovingCameraScene):

    def play_animations(self, animations):
        for animation in animations:
            if isinstance(animation, WaitCommand):
                self.wait(animation.time_in_seconds)
            elif isinstance(animation, list):
                self.play(*tuple(animation))
            else:
                self.play(animation)

    def construct(self):
        # Grid appears to be [-7,7]x[-4,4]
        coordinates = get_input_point_coordinates()

        graph = Grph(coordinates)

        #graph.show_points() or show_points(graph) within this file?
        self.show_points(graph)
        # self.animate_hull(graph)

        # algorithm = JarvisMarch()
        # convex_hull_points = algorithm.run(graph)
        # self.play_animations(algorithm.animations)

        # algorithm = GrahamScan()
        # convex_hull_points = algorithm.run(graph)
        # self.play_animations(algorithm.animations)

        algorithm = Chan(self.camera)
        convex_hull_points = algorithm.run(graph)
        self.play_animations(algorithm.animations)

    def show_points(self, graph):
        # DISPLAY INPUT POINTS
        self.play(*tuple([ShowCreation(point.dot) for point in graph.points]))
        self.play(*tuple([ShowCreation(point.label) for point in graph.points]))

        self.wait(2)

    def animate_hull(self, graph):
        # hull_indices = graph.get_hull_indices() # Can we implement such a helper?
        hull_indices = [1, 3, 5, 8, 10, 12, 13, 1]
        hull_points = [graph.points[i] for i in hull_indices]

        # HIGHLIGHT HULL POINTS
        for point in hull_points:
            self.play(FadeToColor(point.dot, RED))

        # GROW HULL EDGES
        hull_edges = []
        start = hull_points[0]

        for point in hull_points[1:]:
            end = point

            hull_edge = Line(start.dot.get_center(), end.dot.get_center()).set_color(YELLOW)
            hull_edges.append(hull_edge)
            self.play(ShowCreation(hull_edge))

            start = end

        self.wait(2)

        # REMOVE HULL EDGES, UN-HIGHLIGHT HULL POINTS.
        self.play(*[FadeOut(edge) for edge in hull_edges])
        self.play(*[FadeToColor(point.dot, WHITE) for point in hull_points])


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    # command_A = "manim -p  -s -c  --video_dir ~/Downloads/  "
    # command_B = module_name +" " +"Example_Scene"

    command = "manim video.py Video -pl"
    os.system(command)
