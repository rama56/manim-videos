from manim import *


def create_dot_2d(p):
    dot = Dot(point=np.array((p[0], p[1], 0)))
    return dot


class Point:
    counter = 1

    def __init__(self, position, dot=None, label_text=None):
        self.position = position
        if dot is None:
            self.set_dot()
        else:
            self.dot = dot

        if label_text is None:
            self.label = TextMobject(str(Point.counter)).next_to(self.dot)
            Point.counter = Point.counter + 1
        else:
            self.label = TextMobject(str(label_text)).next_to(self.dot)

    def set_dot(self):
        self.dot = create_dot_2d(self.position)

    def set_label(self, label_text):
        self.label = TextMobject(str(label_text)).next_to(self.dot)

    def square_highlight(self):
        square = Square(side_length=1).move_to(self.dot.get_center())
        animation = ShowCreationThenDestruction(square)
        return animation

    @staticmethod
    def reset_counter():
        Point.counter = 1
