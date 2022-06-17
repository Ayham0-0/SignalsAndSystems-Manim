from turtle import right
from venv import create
from manim import *

class Shift(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-1.5, 4, 1/2],
            y_range=[-0.5, 2, 1],
            x_length=8,
            y_length=4,
            axis_config={"numbers_to_exclude": [0],"font_size": 35},
            tips=True,
            
        ).add_coordinates()
        labels = ax.get_axis_labels(
            x_label= "t", y_label= "y(t)"
        )

        # brace 
        p1 = [4,0,0]
        p2 = [4,2.5,0]
        brace = BraceBetweenPoints(p2,p1)
        
        # function 
        formula =MathTex("x(t)=")

        # text=MathTex("1 | -1<t<0")
        # text1=MathTex("1-0.5t |  0<t<2")
        # text2=MathTex("0   |  otherwise")

        # Or we can use this insted 
        # math notaion (variables and domains)
        text1=MathTex("1",color=YELLOW) 
        rule1=MathTex("-1<t<0",color=YELLOW)

        text2=MathTex("1-0.5t",color=ORANGE) 
        rule2=MathTex("0<t<2",color=ORANGE)

        text3=MathTex("0",color=GREEN) 
        rule3=MathTex("Otherwise",color=GREEN)
        
        # Grouping math expressions 
        texts = VGroup(text1,text2,text3)
        rules=VGroup(rule1,rule2,rule3)

        # line = Line([-1,0,0],[-1,1,0])  

        # Graphs configuration
        graph1 = ax.plot(
            lambda x: 1,
            x_range = [-1,0],
            color = YELLOW)
        graph2 = ax.plot(
            lambda x: 1-0.5*x,
            x_range = [0,2],
            color = ORANGE)
        graph3 = ax.get_vertical_lines_to_graph(
            graph1, 
            x_range=[-0.99,-1],
            num_lines=1, 
            color=BLUE, 
            line_config={"dashed_ratio": 10})    
           
        # Grouping graphs  
        graphing_stuff = VGroup(ax, graph1, graph2, graph3, labels)
        axes_labels = VGroup(ax,labels, brace, rules, formula, texts)
        # graphs = VGroup(graph,graph1,graph2)

        # positioning axies and labels *not working*
        # ax.move_to(LEFT)
        # labels.next_to(ax,RIGHT,buff=0.5)
        # animating axies
        self.play(DrawBorderThenFill(ax),Write(labels)) #,ax.animate.shift(LEFT*1.5, 
        
        ## ploting function notation ##
        # animating brace 
        self.play(DrawBorderThenFill(brace), run_time=0.7)
        
        # Hybrid Function visualization and placement(position) 
        rule2.next_to(rule1,DOWN)
        rule3.next_to(rule2,DOWN)
        text2.next_to(text1,DOWN)
        text3.next_to(text2,DOWN)
        texts.next_to(brace,RIGHT,buff=0.1)
        rules.next_to(texts,RIGHT,buff=0.1)
        formula.next_to(brace,LEFT,buff=0.2)

        self.play(Create(formula))
        self.play(Create(texts),run_time=2)
        self.play(Create(rules),run_time=2)
        ## ploting function notation ##

        # animating(Ploting) graphs 
        self.play(Create(graph1), run_time=1.2)
        self.play(Create(graph2), run_time=1.2)
        self.play(Create(graph3), run_time=1)

        # animating movement 
        self.play(graphing_stuff.animate.shift(RIGHT*1.5), run_time=2)
    
        self.wait(0.5)
        self.play(axes_labels.animate.shift(LEFT*2), run_time = 3)