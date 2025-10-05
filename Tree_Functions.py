
from turtle import *
import random

#make lists of colors
stem_colors = ["burlywood3", "burlywood4", "chocolate3", "chocolate4",
               "saddlebrown", "sienna", "sienna3", "sienna4", "tan3",
               "tan4", "goldenrod4", "LightGoldenrod4", "DarkGoldenrod3",
               "DarkGoldenrod4", "DarkOrange4", "brown4"]


leaf_colors = ["chartreuse1", "chartreuse2", "chartreuse3", "chartreuse4",
               "palegreen4", "darkgreen", "forestgreen", "green1", "green2",
               "green3", "green4", "DarkOliveGreen3", "DarkOliveGreen4",
               "SpringGreen3", "SpringGreen4", "limegreen"]


#define trees
def randomPinetree(x, y, scale):
    pinetree(x, y, scale, random.choice(stem_colors), random.choice(leaf_colors))

def pinetree(x, y, scale, stem_color, leaf_color):
    goto(x, y)
    setheading(0)
    fillcolor(stem_color)
    begin_fill()
    for _ in range(2):
        forward(scale * 10)
        left(90)
        forward(scale * 40)
        left(90)
        
    end_fill()
    
    for i in range(3):
        setheading(45)
        goto(x - scale * (17 + i * 7), y + scale * (70 - i * 17))
        fillcolor(leaf_color)
        begin_fill()
        forward(scale * (30 + i * 10))
        right(90)
        forward(scale * (30 + i * 10))
        end_fill()


def randomNormaltree(x, y, scale):
    normaltree(x, y, scale, random.choice(stem_colors), random.choice(leaf_colors))

def normaltree(x, y, scale, stem_color, leaf_color):
    goto(x, y)
    setheading(0)
    fillcolor(stem_color)
    begin_fill()
    for _ in range(2):
        forward(scale * 10)
        left(90)
        forward(scale * 40)
        left(90)
    
    end_fill()
    
    for _ in range(100):
        goto(random.uniform(x - scale * 30, x + scale * 40), random.uniform(y + scale * 35, y + scale * 90))
        pencolor(leaf_color)
        dot(round(random.uniform(scale * 5, scale * 15)))

def treeRow(x, y, scale1, scale2, amount, spacing):
    for i in range(amount):
        scale = random.uniform(scale1, scale2)
        if random.randint(0, 1) == 0:
            randomPinetree(x + i * spacing, y + random.uniform(scale * -20, scale * 20) , scale)
        else:
            randomNormaltree(x + i * spacing, y + random.uniform(scale * -20, scale * 20), scale)
