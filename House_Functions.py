from turtle import *
import random

#make lists of colors
house_wall_colors = ["AntiqueWhite1", "AntiqueWhite2", "AntiqueWhite3", "beige",
                    "bisque1", "bisque2", "bisque3", "burlywood1", "burlywood2",
                    "burlywood3", "tan", "navajowhite1", "navajowhite2", "navajowhite3"]


skyscraper_wall_colors = ["azure2", "azure3", "azure4", "gray90", "gray80", "gray70",
                          "gray60", "ivory2", "ivory3", "ivory4", "honeydew2",
                          "honeydew3", "honeydew4", "gainsboro", "lightsteelblue2",
                          "lightsteelblue3"]


window_colors = ["aliceblue", "azure1", "cadetblue1", "lightcyan1", "DarkSlateGray1",
                 "floralwhite", "ghostwhite", "gray98", "gray96", "gray94",
                 "honeydew", "lavenderblush", "lightskyblue1", "mintcream",
                 "paleturquoise1", "powderblue", "snow1", "whitesmoke"]


door_colors = ["azure4", "burlywood4", "chocolate3", "chocolate4",
               "coral4", "darkorange4", "gray30", "lightblue4", "lightcyan4",
               "khaki4", "lemonchiffon4", "lightgoldenrod4",
               "navajowhite4", "paleturquoise4"]


roof_colors = ["burlywood3", "burlywood4", "chocolate3", "chocolate4",
               "saddlebrown", "sienna", "sienna3", "sienna4", "tan3",
               "tan4", "goldenrod4", "LightGoldenrod4", "DarkGoldenrod3",
               "DarkGoldenrod4", "DarkOrange4", "brown4", "firebrick"]

#define houses
def randomSquareHouse(x, y, scale):
    squareHouse(x, y, scale, random.choice(house_wall_colors), random.choice(window_colors), random.choice(door_colors), random.choice(roof_colors))

def squareHouse(x, y, scale, wall_color, window_color, door_color, roof_color):
    pencolor("black")
    pensize(1)
    penup()
    goto(x, y)
    setheading(0)
    fillcolor(wall_color)
    begin_fill()
    pendown()
    for _ in range(4):
        forward(35 * scale)
        left(90)
    
    penup()
    end_fill()
    
    #windows
    goto(x + 5 * scale, y + 20 * scale)
    fillcolor(window_color)
    for _ in range(2):
        begin_fill()
        pendown()
        for _ in range(4):
            forward(10 * scale)
            left(90)
        
        penup()
        end_fill()
        forward(15 * scale)
    
    #door
    goto(x + 12.5 * scale, y)
    fillcolor(door_color)
    begin_fill()
    pendown()
    for _ in range(2):
        forward(10 * scale)
        left(90)
        forward(15 * scale)
        left(90)
    
    penup()
    end_fill()
    
    #roof
    goto(x - 7.5 * scale, y + 35 * scale)
    setheading(45)
    fillcolor(roof_color)
    begin_fill()
    pendown()
    forward(35.5 * scale)
    right(90)
    forward(35.5 * scale)
    goto(x - 7.5 * scale, y + 35 * scale)
    penup()
    end_fill()
    
    goto(x, y)


def randomSkyscraper(x, y, scale, h_to_w_ratio):
    skyscraper(x, y, scale, h_to_w_ratio, random.choice(skyscraper_wall_colors), random.choice(window_colors))

def skyscraper(x, y, scale, h_to_w_ratio, wall_color, window_color):
    penup()
    goto(x, y)
    setheading(0)
    fillcolor(wall_color)
    pencolor("black")
    pensize(1)
    begin_fill()
    pendown()
    for _ in range(2):
        forward(30 * scale)
        left(90)
        forward(30 * h_to_w_ratio * scale)
        left(90)
    penup()
    end_fill()
    
    #windows
    fillcolor(window_color)
    for i in range(h_to_w_ratio * 3 - 1):
        goto(x + 5 * scale, y + 10 * i * scale)
        for _ in range(2):
            begin_fill()
            pendown()
            for _ in range(4):
                forward(10 * scale)
                left(90)
            
            penup()
            end_fill()
            forward(10 * scale)
    
    goto(x, y)
