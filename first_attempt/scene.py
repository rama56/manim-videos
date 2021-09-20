import os

from manim import *


class SquareToCircle(Scene):
	def construct(self):
		circle = Circle()
		# circle.set_fill(PINK, opacity=0.5)

		square = Square()
		square.flip(RIGHT)
		square.rotate(-3 * TAU / 8)

		self.play(ShowCreation(square))
		self.play(Transform(square, circle))

		self.play(FadeOut(square))


if __name__ == "__main__":
	module_name = os.path.basename(__file__)
	# command_A = "manim -p  -s -c  --video_dir ~/Downloads/  "
	# command_B = module_name +" " +"Example_Scene"

	command = "manim scene.py Scene -pl"
	os.system(command)
