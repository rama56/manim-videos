import os
# from manim import *
from manimlib.imports import *


class SolveGeneralQuadraticEquation(Scene):
    def construct(self):
        self.import_formulas()

        teacher = ImageMobject("assets/pngs/Tau_person_cane.png")
        teacher.scale(1.2)
        teacher.to_corner(DR)

        self.play(FadeIn(teacher))

        stu_g = ImageMobject("assets/pngs/delta_person_green.png").scale(1).to_corner(DL)
        stu_p = ImageMobject("assets/pngs/delta_person_peach.png").scale(1).next_to(stu_g).shift(0.3 * LEFT)
        stu_l = ImageMobject("assets/pngs/delta_person_lavendar.png").scale(1).next_to(stu_p).shift(0.3 * LEFT)

        self.play(FadeIn(stu_g), FadeIn(stu_p), FadeIn(stu_l))
        self.wait(1)

        teacher_bubble = ImageMobject("assets/speech_bubble.png").scale(2.5). \
            next_to(teacher, direction=UL).shift(1.2 * RIGHT + 0.5 * DOWN)

        tl1 = TextMobject("The quadratic equation").move_to(teacher_bubble.get_center()).shift(1.6 * UP)
        tl2 = TexMobject(r"ax^2 + bx + c = 0").next_to(tl1, direction=DOWN).shift(0.9 * LEFT)
        tl3 = TextMobject("has roots").next_to(tl2)
        tl4 = TexMobject(r"x={-b \pm \sqrt{b^2 - 4ac} \over 2a}").next_to(tl2, direction=DOWN).shift(1.1 * RIGHT)

        self.play(FadeIn(teacher_bubble), Write(tl1))
        self.play(Write(tl2))
        self.play(Write(tl3))
        self.play(Write(tl4))

        self.wait(1)

        stu_bubble = ImageMobject("assets/speech_bubble.png").scale(1).next_to(stu_g, direction=UP).shift(RIGHT)
        sl1 = TextMobject("But how?").move_to(stu_bubble.get_center()).shift(0.25 * UP)

        self.play(FadeIn(stu_bubble), Write(sl1))
        self.wait(1)

        tl2.target = self.formulas[0].get_center()
        self.play(FadeOut(teacher_bubble), FadeOut(tl1), FadeOut(tl3), FadeOut(tl4),
                  FadeOut(stu_bubble), FadeOut(sl1))

        # MoveToTarget(tl2),
        # ACTUAL EQUATIONS

        self.write_initial_formula(tl2)
        self.set_changes()

        self.step_formula(n_step=1,
                          changes=self.set_of_changes[0],
                          # fade=[10],
                          write=[7, 13],
                          pre_copy=[0],
                          pos_copy=[14],
                          path_arc=PI / 2
                          )

        # Multiply 2/2
        self.step_formula(n_step=2,
                          changes=self.set_of_changes[1],
                          pos_write=[4, 9]
                          # path_arc=PI / 2
                          # pre_copy=[0],
                          # pos_copy=[15]
                          )

        # Add b^2/4ac on both sides
        self.step_formula(n_step=3,
                          changes=self.set_of_changes[2],
                          fade=[19],
                          pos_write=[12, 14, 16, 17, 18, 19, 21, 31, 33, 34, 35, 36, 38]
                          )

        bracket_start_pos = self.formulas[3][0].get_center() + 0.9 * DOWN + 0.2 * LEFT
        line = Line(bracket_start_pos, bracket_start_pos + 6 * RIGHT)
        b1 = Brace(line)
        b1text = b1.get_tex("p^2+2pq+q^2 \\text{ format}")
        self.play(FadeIn(b1), FadeIn(b1text))
        self.wait(1)
        self.play(FadeOut(b1), FadeOut(b1text))

        # Group into (a+b)^2 form.
        self.step_formula(n_step=4,
                          changes=self.set_of_changes[3],
                          fade=[4],
                          write=[0, 9]
                          )

        # Move + c/a to other side.
        self.step_formula(n_step=5,
                          changes=self.set_of_changes[4]
                          )

        # c/a to 4ac/aa
        self.step_formula(n_step=6,
                          changes=self.set_of_changes[5],
                          pos_write=[25, 26, 29, 30]
                          )

        # 4ac/aa to 4ac / a^2
        self.step_formula(n_step=7,
                          changes=self.set_of_changes[6],
                          write=[32],
                          )

        # Merge fractions
        self.step_formula(n_step=8,
                          changes=self.set_of_changes[7]
                          )

        # Square root on both sides
        self.step_formula(n_step=9,
                          changes=self.set_of_changes[8],
                          pos_write=[0, 16]
                          )

        # Apply square root
        self.step_formula(n_step=10,
                          changes=self.set_of_changes[9],
                          write=[10],
                          fade=[0, 2, 11, 13, 30],
                          )
        # Move b/2a to other side
        self.step_formula(n_step=11,
                          changes=self.set_of_changes[10],
                          )

        # Merge fractions
        self.step_formula(n_step=12,
                          changes=self.set_of_changes[11],
                          )

        c1 = SurroundingRectangle(self.formulas[12], buff=0.2)
        c2 = SurroundingRectangle(self.formulas[12], buff=0.2)
        c2.rotate(PI)
        self.play(ShowCreationThenDestruction(c1), ShowCreationThenDestruction(c2))

        self.play(FadeOut(self.formulas[12]))

        stu_bubble = ImageMobject("assets/bubble_rightwards.png").scale(1).next_to(stu_g, direction=UR)
        sl2 = TextMobject("Got it!").scale(1.2).move_to(stu_bubble.get_center()).shift(0.2 * UP)
        self.play(FadeIn(stu_bubble), FadeIn(sl2))
        self.wait(2)

    def import_formulas(self):
        from quadratic_roots_derivation.formulas.formula_reader import formulas
        # from formulas.formula_reader import formulas
        self.formulas = formulas

    def write_initial_formula(self, prev_obj):
        # FORMULA 1
        self.play(
            LaggedStart(*[
                Write(self.formulas[0][i])
                for i in [0, 1, 3, 4, 5, 6, 7, 8, 9, 10]
                # If you use Write(self.formulas[0])
                # the animation is not displayed correctly because
                # self.formulas[2] is empty
            ]),
            FadeOut(prev_obj)
        )

        # # FORMULA 2
        # self.play(
        #     LaggedStart(*[
        #         Write(self.formulas[1][i])
        #         for i in [0, 2, 3, 5, 6, 7, 8, 10, 12, 13, 14, 16, 17]
        #     ])
        # )

        # FORMULA 3
        # self.play(
        #     LaggedStart(*[
        #         Write(self.formulas[2][i])
        #         for i in [0, 2, 3, 4, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 19]
        #     ])
        # )

        # # FORMULA 5
        # self.play(
        #     LaggedStart(*[
        #         Write(self.formulas[4][i])
        #         for i in [0, 1, 2, 4, 5, 6, 7, 9, 11, 12, 14, 15, 16, 18, 20, 22, 23, 24, 25, 27]
        #     ])
        # )


    def set_changes(self):
        self.set_of_changes = [
            # 1
            [[
                (0, 1, 3, 4, 5, 6, 7, 8, 9, 10),
                (8, 0, 2, 3, 5, 6, 10, 12, 16, 17)
            ]],
            # 2
            [[
                (0, 2, 3, 5, 6, 7, 8, 10, 12, 13, 14, 16, 17),
                (0, 2, 3, 6, 7, 8, 10, 12, 14, 15, 16, 18, 19)
            ]],
            # 3
            [[
                (0, 2, 3, 4, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18),
                (0, 2, 3, 4, 6, 7, 8, 9, 10, 23, 25, 26, 27, 29)
            ]],
            # 4
            [[
                (0,  2, 3, 6, 7, 8, 9, 10, 12, 14, 16, 17, 18, 19, 21, 23, 25, 26, 27, 29, 31, 33, 34, 35, 36, 38),
                (1, 11, 2, 4, 1, 5, 6,  7,  2,  4, 11,  5,  6,  7, 11, 12, 14, 15, 16, 18, 20, 22, 23, 24, 25, 27)
            ]],
            # 5
            [[
                (0, 1, 2, 4, 5, 6, 7, 9, 11, 12, 14, 15, 16, 18, 20, 22, 23, 24, 25, 27),
                (0, 1, 2, 4, 5, 6, 7, 9, 11, 23, 25, 26, 27, 12, 14, 16, 17, 18, 19, 21)
            ]],
            # 6
            [[
                (0, 1, 2, 4, 5, 6, 7, 9, 11, 12, 14, 16, 17, 18, 19, 21, 23, 25, 26, 27),
                (0, 1, 2, 4, 5, 6, 7, 9, 11, 12, 14, 16, 17, 18, 19, 21, 23, 27, 28, 31)
            ]],
            # 7
            [[
                (0, 1, 2, 4, 5, 6, 7, 9, 11, 12, 14, 16, 17, 18, 19, 21, 23, 25, 26, 27, 28, 29, 30, 31),
                (0, 1, 2, 4, 5, 6, 7, 9, 11, 12, 14, 16, 17, 18, 19, 21, 23, 25, 26, 27, 28, 29, 30, 30)
            ]],
            # 8
            [[
                (0, 1, 2, 4, 5, 6, 7, 9, 11, 12, 14, 16, 17, 18, 19, 21, 23, 25, 26, 27, 28, 29, 30, 32),
                (0, 1, 2, 4, 5, 6, 7, 9, 11, 12, 14, 16, 21, 22, 23, 25, 17, 18, 19, 20, 21, 22, 23, 25)
            ]],
            # 9
            [[
                (0, 1, 2, 4, 5, 6, 7,  9, 11, 12, 14, 16, 17, 18, 19, 20, 21, 22, 23, 25),
                (2, 3, 4, 6, 7, 8, 9, 11, 13, 15, 19, 21, 22, 23, 24, 25, 26, 27, 28, 30)
            ]],
            # 10
            [[
                (3, 4, 6, 7, 8, 9, 15, 16,   19, 21, 22, 23, 24, 25, 26, 27, 28),
                (0, 1, 3, 4, 5, 6,  8, 11,   13, 15, 16, 17, 18, 19, 21, 22, 23)
            ]],
            # 11
            [[
                (0, 1, 3, 4, 5, 6, 8, 10, 11, 13, 15, 16, 17, 18, 19, 21, 22, 23),
                (0, 2, 4, 5, 6, 7, 1,  9, 11, 13, 15, 16, 17, 18, 19, 21, 22, 23)
            ]],
            # 12
            [[
                (0, 1, 2, 4,  5,  6,  7, 9, 11, 13, 15, 16, 17, 18, 19, 21, 22, 23),
                (0, 1, 3, 4, 16, 17, 18, 5,  6,  8, 10, 11, 12, 13, 14, 16, 17, 18)
            ]]
            #,
            # # 13
            # [[
            #     (0, 1, 2, 4, 5, 6, 7, 9, 10, 12, 14, 15, 16, 17, 18, 19, 20, 21, 24,),
            #     (0, 1, 2, 4, 5, 6, 7, 9, 11, 12, 14, 15, 16, 17, 18, 20, 21, 22, 23,)
            # ]],
            # # 14
            # [[
            #     (0, 1, 2, 4, 5, 6, 7, 9, 11, 12, 14, 15, 16, 17, 18, 20, 21, 22, 23,),
            #     (0, 1, 3, 4, 16, 17, 18, 5, 6, 7, 9, 10, 11, 12, 13, 15, 16, 17, 18,)
            # ]]
        ]

    def step_formula(self,
                            pre_write=[],
                            pos_write=[],
                            pre_fade=[],
                            pos_fade=[],
                            fade=[],
                            write=[],
                            changes=[[]],
                            path_arc=0,
                            n_step=0,
                            pre_copy=[],
                            pos_copy=[],
                            time_pre_changes=0.3,
                            time_pos_changes=0.3,
                            run_time=2,
                            time_end=0.3,
                            pre_order=["w","f"],
                            pos_order=["w","f"]
                            ):
        formula_copy=[]
        for c in pre_copy:
            formula_copy.append(self.formulas[n_step-1][c].copy())

        for ani_ in pre_order:
            if len(pre_write)>0 and ani_=="w":
                self.play(*[Write(self.formulas[n_step-1][w])for w in pre_write])
            if len(pre_fade)>0 and ani_=="f":
                self.play(*[FadeOut(self.formulas[n_step-1][w])for w in pre_fade])

        self.wait(time_pre_changes)

        for pre_ind,post_ind in changes:
            self.play(*[
                ReplacementTransform(
                    self.formulas[n_step-1][i],self.formulas[n_step][j],
                    path_arc=path_arc
                    )
                for i,j in zip(pre_ind,post_ind)
                ],
                *[FadeOut(self.formulas[n_step-1][f])for f in fade if len(fade)>0],
                *[Write(self.formulas[n_step][w])for w in write if len(write)>0],
                *[ReplacementTransform(formula_copy[j],self.formulas[n_step][f])
                for j,f in zip(range(len(pos_copy)),pos_copy) if len(pre_copy)>0
                ],
                run_time=run_time
            )

        self.wait(time_pos_changes)

        for ani_ in pos_order:
            if len(pos_write)>0 and ani_=="w":
                self.play(*[Write(self.formulas[n_step][w])for w in pos_write])
            if len(pos_fade)>0 and ani_=="f":
                self.play(*[FadeOut(self.formulas[n_step][w])for w in pos_fade])

        self.wait(time_end)


class TestImage(Scene):
    def construct(self):

        teacher = ImageMobject("assets/pngs/Tau_person_cane.png")
        teacher.scale(1.2)
        teacher.to_corner(DR)

        self.play(FadeIn(teacher))

        stu_g = ImageMobject("assets/pngs/delta_person_green.png").scale(1).to_corner(DL)
        stu_p = ImageMobject("assets/pngs/delta_person_peach.png").scale(1).next_to(stu_g).shift(0.3 * LEFT)
        stu_l = ImageMobject("assets/pngs/delta_person_lavendar.png").scale(1).next_to(stu_p).shift(0.3 * LEFT)

        self.play(FadeIn(stu_g), FadeIn(stu_p), FadeIn(stu_l))
        self.wait(1)

        teacher_bubble = ImageMobject("assets/speech_bubble.png").scale(2.5).\
            next_to(teacher, direction=UL).shift(1.2 * RIGHT + 0.5 * DOWN)

        tl1 = TextMobject("The quadratic equation").move_to(teacher_bubble.get_center()).shift(1.6 * UP)
        tl2 = TexMobject(r"ax^2 + bx + c = 0").next_to(tl1, direction=DOWN).shift(0.9 * LEFT)
        tl3 = TextMobject("has roots").next_to(tl2)
        tl4 = TexMobject(r"x={-b \pm \sqrt{b^2 - 4ac} \over 2a}").next_to(tl2, direction=DOWN).shift(0.3 * RIGHT)

        self.play(FadeIn(teacher_bubble), Write(tl1))
        self.play(Write(tl2))
        self.play(Write(tl3))
        self.play(Write(tl4))

        self.wait(1)

        stu_bubble = ImageMobject("assets/bubble_rightwards.png").scale(1).next_to(stu_g, direction=UR)
        sl1 = TextMobject("But how?").move_to(stu_bubble.get_center()).shift(0.25 * UP)

        self.play(FadeIn(stu_bubble), Write(sl1))
        self.wait(1)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    # command_A = "manim -p  -s -c  --video_dir ~/Downloads/  "
    # command_B = module_name +" " +"Example_Scene"

    command = "manim derivation.py SolveGeneralQuadraticEquation -pl"
    os.system(command)
