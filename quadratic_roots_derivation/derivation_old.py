import os
from manim import *


class Derivation_1(Scene):
    def construct(self):
        # formula_1 = TexMobject("ax^2 + bx + c = 0", "\\quad \\implies \\quad ", "x = \\dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}")
        # self.play(Write(formula_1))
        # how = Text('How?', slant=ITALIC).scale(1)
        # how.next_to(formula_1[1], UP)
        # self.play(ShowCreation(how))

        f1 = MathTex("ax^2 + bx + c = 0")
        f2 = MathTex("x^2 + \\dfrac{bx}{a} + \\dfrac{c}{a} = 0")
        f3 = MathTex("x^2 + 2 \\dfrac{bx}{2a} + \\dfrac{c}{a} = 0")
        f4 = MathTex("x^2 + 2 \\dfrac{bx}{2a} + \\dfrac{b^2}{4a^2} + \\dfrac{c}{a} = \\dfrac{b^2}{4a^2}")
        f5 = MathTex("\\left(x + \\dfrac{b}{2a} \\right)^2 + \\dfrac{c}{a} = \\dfrac{b^2}{4a^2}")
        f6 = MathTex("\\left(x + \\dfrac{b}{2a} \\right)^2 = \\dfrac{b^2}{4a^2} - \\dfrac{c}{a}")
        f7 = MathTex("\\left(x + \\dfrac{b}{2a} \\right)^2 = \\dfrac{b^2 - 4ac}{4a^2}")
        f8 = MathTex("x + \\dfrac{b}{2a} = \\pm \\dfrac{\\sqrt{b^2 - 4ac}}{2a}")
        f9 = MathTex("x = -\\dfrac{b}{2a} \\pm \\dfrac{\\sqrt{b^2 - 4ac}}{2a}")
        f10 = MathTex("x = \\dfrac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}")

        self.play(Write(f1))
        self.play(Transform(f1, f2))
        self.play(Transform(f1, f3))
        self.play(Transform(f1, f4))
        self.play(Transform(f1, f5))
        self.play(Transform(f1, f6))
        self.play(Transform(f1, f7))
        self.play(Transform(f1, f8))
        self.play(Transform(f1, f9))
        self.play(Transform(f1, f10))
        self.play(FadeOut(f1))


class Derivation_2(Scene):
    def construct(self):
        # formula_1 = TexMobject("ax^2 + bx + c = 0", "\\quad \\implies \\quad ", "x = \\dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}")
        # self.play(Write(formula_1))
        # how = Text('How?', slant=ITALIC).scale(1)
        # how.next_to(formula_1[1], UP)
        # self.play(ShowCreation(how))

        formula = TexMobject("ax^2", " + bx", " + c", "=", " 0")
        self.play(Write(formula))

        ta = formula[0]
        tb = formula[1]
        tc = formula[2]
        td = formula[3]

        ta_1 = MathTex("x^2").move_to(ta.get_center())
        tb_1 = MathTex("\\dfrac{bx}{a}").move_to(tb.get_center())
        tc_1 = MathTex("\\dfrac{c}{a}").move_to(tc.get_center())

        self.play(Transform(ta, ta_1))
        self.play(Transform(tb, tb_1))
        self.play(Transform(tc, tc_1))

    # f2 = MathTex("x^2 + \\dfrac{bx}{a} + \\dfrac{c}{a} = 0")
    # f3 = MathTex("x^2 + 2 \\dfrac{bx}{2a} + \\dfrac{c}{a} = 0")
    # f4 = MathTex("x^2 + 2 \\dfrac{bx}{2a} + \\dfrac{b^2}{4a^2} + \\dfrac{c}{a} = \\dfrac{b^2}{4a^2}")
    # f5 = MathTex("\\left(x + \\dfrac{b}{2a} \\right)^2 + \\dfrac{c}{a} = \\dfrac{b^2}{4a^2}")
    # f6 = MathTex("\\left(x + \\dfrac{b}{2a} \\right)^2 = \\dfrac{b^2}{4a^2} - \\dfrac{c}{a}")
    # f7 = MathTex("\\left(x + \\dfrac{b}{2a} \\right)^2 = \\dfrac{b^2 - 4ac}{4a^2}")
    # f8 = MathTex("x + \\dfrac{b}{2a} = \\pm \\dfrac{\\sqrt{b^2 - 4ac}}{2a}")
    # f9 = MathTex("x = -\\dfrac{b}{2a} \\pm \\dfrac{\\sqrt{b^2 - 4ac}}{2a}")
    # f10 = MathTex("x = \\dfrac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}")

    # self.play(Write(f1))
    # self.play(Transform(f1, f2))
    # self.play(Transform(f1, f3))
    # self.play(Transform(f1, f4))
    # self.play(Transform(f1, f5))
    # self.play(Transform(f1, f6))
    # self.play(Transform(f1, f7))
    # self.play(Transform(f1, f8))
    # self.play(Transform(f1, f9))
    # self.play(Transform(f1, f10))
    # self.play(FadeOut(f1))


class SolveGeneralQuadraticEquation(Scene):
    def construct(self):
        # dirpath = "media/"
        # shutil.rmtree(dirpath)

        self.import_formulas()
        self.write_formulas()
        self.set_changes()

        self.step_formula(n_step=1,
                          changes=self.set_of_changes[0],
                          # fade=[10],
                          write=[7, 13],
                          pre_copy=[0],
                          pos_copy=[14],
                          path_arc=-PI / 2
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
        self.wait(2)

    def import_formulas(self):
        from quadratic_roots_derivation.formulas.formula_reader import formulas
        self.formulas = formulas

    def write_formulas(self):
        self.play(
            LaggedStart(*[
                Write(self.formulas[0][i])
                for i in [0, 1, 3, 4, 5, 6, 7, 8, 9, 10]
                # If you use Write(self.formulas[0])
                # the animation is not displayed correctly because
                # self.formulas[2] is empty
            ])
        )

        # self.play(
        #     LaggedStart(*[
        #         Write(self.formulas[1][i])
        #         for i in [0, 2, 3, 5, 6, 7, 8, 10, 12, 13, 14, 16, 17]
        #         # If you use Write(self.formulas[0])
        #         # the animation is not displayed correctly because
        #         # self.formulas[2] is empty
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
                (0, 1, 2, 4, 5,  6,  7,  9, 11, 13, 15, 16, 17, 18, 19, 21, 22, 23),
                (0, 1, 3, 4, 15, 16, 17, 5,  6,  7,  9, 10, 11, 12, 13, 15, 16, 17)
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
        # Use PIL when you want to import an image from the web
        # import requests
        # from PIL import Image
        # img = Image.open(requests.get("https://raw.githubusercontent.com/ManimCommunity/manim/master/logo/cropped.png",
        #                               stream=True).raw)
        # img_mobject = ImageMobject(img)
        # this line, when you want to import your Image on your machine

        teacher = ImageMobject("assets/pngs/Tau_person_cane.png")
        teacher.scale(1.2)
        teacher.to_corner(DR)

        # for i, layer in enumerate(teacher):
        #     layer.set_color(colors[i])
        #

        self.play(FadeIn(teacher))

        stu_g = ImageMobject("assets/pngs/delta_person_green.png").scale(1).to_corner(DL)
        stu_p = ImageMobject("assets/pngs/delta_person_peach.png").scale(1).next_to(stu_g, direction=RIGHT/2)
        stu_l = ImageMobject("assets/pngs/delta_person_lavendar.png").scale(1).next_to(stu_p)

        self.play(FadeIn(stu_g), FadeIn(stu_p), FadeIn(stu_l))
        self.wait(1)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    # command_A = "manim -p  -s -c  --video_dir ~/Downloads/  "
    # command_B = module_name +" " +"Example_Scene"

    command = "manim derivation.py SolveGeneralQuadraticEquation -pl"
    os.system(command)
