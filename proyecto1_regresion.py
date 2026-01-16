from manim import *
import numpy as np
from manim.utils.rate_functions import ease_out_cubic


class ProyectoRegresionFinalCompleto(Scene):
    def construct(self):

        texto_color = WHITE

        titulo = Text("Regresion Lineal y No lineal", font_size=40, weight=BOLD).to_edge(UP)
        subtitulo = Text("Del modelo general a la regularizacion", font_size=24, color=BLUE).next_to(titulo, DOWN)
        grupo = Text("Grupo 3: Carlos Angel, Jean Terrazo, Carlos Villanueva", font_size=20, color=GRAY).next_to(
            subtitulo, DOWN)

        self.play(Write(titulo), FadeIn(subtitulo))
        self.play(FadeIn(grupo))
        self.wait(2)

        header_gen = Text("Modelo General Lineal", font_size=32, color=YELLOW).next_to(grupo, DOWN, buff=1)
        formula_gen = MathTex(
            r"y_i = b + w_1 x_{i1} + w_2 x_{i2} + \dots + w_k x_{ik} + \epsilon_i",
            font_size=36
        ).center()

        self.play(Write(header_gen))
        self.play(Write(formula_gen))
        self.wait(3)

        # Limpieza
        self.play(
            FadeOut(subtitulo), FadeOut(grupo),
            FadeOut(header_gen), FadeOut(formula_gen)
        )

        titulo_uni = Text("Regresion Lineal 1 Variable", font_size=32, color=BLUE).next_to(titulo, DOWN)
        self.play(Write(titulo_uni))

        # Plano
        axes = Axes(
            x_range=[0, 10, 2], y_range=[0, 14, 2],
            x_length=6, y_length=5,
            axis_config={"color": BLUE, "include_numbers": False},
        ).to_edge(LEFT).shift(DOWN * 0.3)

        labels = axes.get_axis_labels(x_label="x", y_label="y")
        self.play(Create(axes), Write(labels))

        np.random.seed(42)
        x_val = np.linspace(1, 9, 10)
        y_val = 1.2 * x_val + 1 + np.random.normal(0, 0.9, 10)
        puntos = VGroup(*[Dot(axes.c2p(x, y), color=RED) for x, y in zip(x_val, y_val)])
        self.play(FadeIn(puntos))

        f1 = MathTex(r"h(x_i) = b + w x_i", font_size=28).to_edge(RIGHT).shift(UP * 2.5)
        f2 = MathTex(r"\mathcal{L} = \frac{1}{2n}\sum (y_i - h(x_i))^2", font_size=28).next_to(f1, DOWN, buff=0.3)
        f3_w = MathTex(r"\frac{\partial \mathcal{L}}{\partial w} = \frac{\sum (y_i - h(x_i))(-x_i)}{n}",
                       font_size=24).next_to(f2, DOWN, buff=0.3)
        f3_b = MathTex(r"\frac{\partial \mathcal{L}}{\partial b} = \frac{\sum (y_i - h(x_i))(-1)}{n}",
                       font_size=24).next_to(f3_w, DOWN, buff=0.2)
        f4 = MathTex(
            r"w = w - \alpha \frac{\partial \mathcal{L}}{\partial w},\quad b = b - \alpha \frac{\partial \mathcal{L}}{\partial b}",
            font_size=24).next_to(f3_b, DOWN, buff=0.3)

        for eq in [f1, f2, f3_w, f3_b, f4]:
            self.play(Write(eq))
            self.wait(0.3)

        w_trk = ValueTracker(0.1)
        b_trk = ValueTracker(0)

        linea = always_redraw(lambda: axes.plot(
            lambda x: w_trk.get_value() * x + b_trk.get_value(),
            color=YELLOW, x_range=[0, 10]
        ))

        self.play(Create(linea))
        self.play(
            w_trk.animate.set_value(1.25),
            b_trk.animate.set_value(0.9),
            run_time=4,
            rate_func=ease_out_cubic
        )
        self.wait(1)

        # Limpieza
        self.play(FadeOut(
            Group(axes, puntos, linea, labels, f1, f2, f3_w, f3_b, f4, titulo_uni)))

        titulo_multi = Text("Regresion Lineal Multivariable", font_size=32, color=GREEN).next_to(titulo, DOWN)
        self.play(Write(titulo_multi))

        # Matrices X, W, Y
        matrix_group = VGroup(
            MathTex(
                r"X \in \mathbb{R}^{n \times (d+1)} = \begin{bmatrix} 1 & x_{01} & \cdots & x_{0d} \\ \vdots & \vdots & \ddots & \vdots \\ 1 & x_{n1} & \cdots & x_{nd} \end{bmatrix}",
                font_size=22),
            MathTex(r"W \in \mathbb{R}^{(d+1) \times 1} = \begin{bmatrix} w_0 \\ w_1 \\ \vdots \\ w_d \end{bmatrix}",
                    font_size=24),
            MathTex(r"Y \in \mathbb{R}^{n \times 1} = \begin{bmatrix} y_0 \\ y_1 \\ \vdots \\ y_n \end{bmatrix}",
                    font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(LEFT).shift(UP * 0.5)

        self.play(Write(matrix_group))
        self.wait(2)

        formulas_matrix = VGroup(
            MathTex(r"1.\ h(X) = X W", font_size=32),
            MathTex(r"2.\ \mathcal{L} = \frac{1}{2n} \lVert Y - XW \rVert_2^2", font_size=28),
            MathTex(r"3.\ \nabla_W\mathcal{L} = -\frac{1}{n} X^T (Y - XW)", font_size=26),
            MathTex(r"4.\ W := W - \alpha \nabla_W\mathcal{L}", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).to_edge(RIGHT).shift(UP * 0.5)

        for i, eq in enumerate(formulas_matrix):
            self.play(Write(eq))
            self.wait(0.5 if i < 3 else 1)

        self.wait(2)
        self.play(FadeOut(matrix_group), FadeOut(formulas_matrix))

        titulo_poly = Text("Regresion No Lineal (Polinomial)", font_size=32, color=ORANGE).next_to(titulo, DOWN)
        self.play(Transform(titulo_multi, titulo_poly))

        explanation = VGroup(
            Text("Feature Transformation:", font_size=24, color=YELLOW),
            MathTex(r"x \rightarrow \phi(x) = [1, x, x^2, x^3, \dots]", font_size=26),
            MathTex(r"h(x) = w_0 + w_1 x + w_2 x^2 + w_3 x^3 + \dots", font_size=26, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(LEFT).shift(UP * 0.5)

        self.play(Write(explanation))
        self.wait(2)

        # Ejes y datos curvos
        axes_p = Axes(x_range=[0, 10], y_range=[-5, 25], x_length=6, y_length=5).to_edge(RIGHT).shift(
            DOWN * 0.5)
        x_p = np.linspace(1, 9, 15)
        y_p = 0.5 * (x_p - 5) ** 2 + 2 + np.random.normal(0, 0.8, 15)
        puntos_p = VGroup(*[Dot(axes_p.c2p(x, y), color=RED) for x, y in zip(x_p, y_p)])

        self.play(Create(axes_p), FadeIn(puntos_p))

        a, b, c = ValueTracker(0), ValueTracker(0), ValueTracker(5)
        curva = always_redraw(lambda: axes_p.plot(
            lambda x: a.get_value() * (x - 5) ** 2 + b.get_value() * (x - 5) + c.get_value(),
            color=GREEN, x_range=[0, 10]
        ))

        self.play(Create(curva))
        self.play(
            a.animate.set_value(0.5),
            c.animate.set_value(2),
            run_time=4
        )
        self.wait(2)

        self.play(FadeOut(explanation), FadeOut(axes_p), FadeOut(puntos_p), FadeOut(curva))

        titulo_reg = Text("Regularizacion", font_size=36, color=PURPLE).next_to(titulo, DOWN)
        self.play(Transform(titulo_multi, titulo_reg))

        gen_form = MathTex(
            r"\mathcal{L}_{\text{total}} = \frac{1}{2n}\lVert Y - XW \rVert_2^2 + \lambda \mathcal{R}(W)",
            font_size=32
        ).to_edge(RIGHT).shift(UP*1.5, LEFT*1)

        self.play(Write(gen_form))
        self.wait(2)

        reg_types = VGroup(
            MathTex(r"\text{Ridge (L2): } \mathcal{R}(W) = \lVert W \rVert_2^2 = \sum w_i^2",
                    font_size=24, color=BLUE),
            MathTex(r"\text{Lasso (L1): } \mathcal{R}(W) = \lVert W \rVert_1 = \sum |w_i|",
                    font_size=24, color=RED),
            MathTex(r"\text{ElasticNet: } \mathcal{R}(W) = \alpha\lVert W \rVert_1 + (1-\alpha)\lVert W \rVert_2^2",
                    font_size=24, color=PURPLE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(gen_form, DOWN, buff=0.5).align_to(gen_form, LEFT)

        self.play(Write(reg_types))
        self.wait(3)

        ax_small = Axes(
            x_range=[0, 6],
            y_range=[0, 8],
            x_length=5,
            y_length=3.5
        ).to_edge(LEFT).shift(DOWN * 0.5, RIGHT * 0.5)

        x_pts = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]
        y_pts = [1, 5, 2, 6, 2.5, 5, 3, 6]
        puntos_locos = VGroup(*[Dot(ax_small.c2p(x, y), color=GRAY) for x, y in zip(x_pts, y_pts)])

        curva_mala = ax_small.plot_line_graph(x_pts, y_pts, line_color=RED, add_vertex_dots=False)
        lbl_mala = Text("Overfitting (No Reg)", color=RED, font_size=18).next_to(ax_small, UP)

        curva_buena = ax_small.plot(lambda x: 0.6 * x + 2, color=BLUE, x_range=[0.5, 5])
        lbl_buena = Text("Regularizado", color=BLUE, font_size=18).next_to(ax_small, UP)

        self.play(Create(ax_small), FadeIn(puntos_locos))
        self.play(Create(curva_mala), Write(lbl_mala))
        self.wait(1)

        self.play(
            Transform(curva_mala, curva_buena),
            Transform(lbl_mala, lbl_buena),
            run_time=3
        )
        self.wait(2)

        self.play(
            FadeOut(Group(ax_small, puntos_locos, curva_mala, lbl_mala, gen_form, reg_types, titulo_multi, titulo)))

        final = VGroup(
            Text("Gracias por ver!", font_size=48),
            Text("Grupo 3", font_size=24, color=GRAY).next_to( DOWN, buff=0.5)
        )

        self.play(Write(final))
        self.wait(3)