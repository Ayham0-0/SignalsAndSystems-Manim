from cgitb import text
from tkinter import font
from turtle import right, width
from venv import create
from manim import *
from pyparsing import line

class Shift(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-1.5, 4, 1/2],
            y_range=[-0.5, 2, 1],
            x_length=8,
            y_length=4,
            axis_config={"numbers_to_exclude": [0]},
            tips=True,
        ).add_coordinates()
        labels = ax.get_axis_labels(
            x_label= "t", y_label= "y(t)"
        )

        p1 = [4,0,0]
        p2 = [4,2.5,0]
        brace = BraceBetweenPoints(p2,p1)

        formula =MathTex("x(t)=")

        text=MathTex("1 __ -1<t<0")
        text1=MathTex("1-0.5t __  0<t<2")
        text2=MathTex("0   __  otherwise")

        rule=VGroup(text,text1,text2)

        # line = Line([-1,0,0],[-1,1,0])  

        graph = ax.plot(
            lambda x: 1,
            x_range = [-1,0],
            color = YELLOW,)
        graph1 = ax.plot(
            lambda x: 1-0.5*x,
            x_range = [0,2],
            color = YELLOW,)
        graph2 = ax.get_vertical_lines_to_graph(graph, x_range=[-0.99,-1],num_lines=1, color=YELLOW, line_config={"dashed_ratio": 10})    
           
        
        graphing_stuff = VGroup(ax, graph, graph1, graph2, labels)
        axes_labels = VGroup(ax,labels, brace, rule, formula)
        # graphs = VGroup(graph,graph1,graph2)

        self.play(DrawBorderThenFill(ax), Write(labels))

        self.play(Create(graph), run_time=1.2)
        self.play(Create(graph1), run_time=1.2)
        self.play(Create(graph2), run_time=1)

        self.play(graphing_stuff.animate.shift(RIGHT*1.5), run_time=2)

        self.play(DrawBorderThenFill(brace), run_time=0.7)
        
        text1.next_to(text,DOWN)
        text2.next_to(text1,DOWN)
        rule.next_to(brace,RIGHT,buff=0.1)
        formula.next_to(brace,LEFT,buff=0.2)

        self.play(Create(rule),run_time=4)
        self.play(Create(formula))
    
        self.wait(0.5)
        self.play(axes_labels.animate.shift(LEFT*2), run_time = 3)