from turtle import *
import random
import tree_functions as trees
import house_functions as houses

setworldcoordinates(-400, -400, 400, 400)
tracer(0)

hideturtle()
penup()

#sky
goto(400, 400)
fillcolor("cyan")
begin_fill()

for _ in range(4):
    right(90)
    forward(800)

end_fill()


#mountain 1
goto(-50, 90)
setheading(30)
fillcolor("palegreen3")
begin_fill()

forward(150)
circle(-70, 60)
forward(150)
goto(0, -400)

end_fill()


#mountain 2
goto(400, 100)
setheading(140)
fillcolor("darkolivegreen3")
begin_fill()

forward(50)
circle(70, 80)
forward(200)
goto(400, -400)

end_fill()


#mountain 3
goto(-400, 150)
setheading(45)
fillcolor("palegreen3")
begin_fill()

forward(50)
circle(-70, 90)
forward(200)
goto(-400, -400)

end_fill()


#mountain 4
goto(-400, 0)
setheading(0)
fillcolor("yellowgreen")
begin_fill()

circle(200, 45)
forward(100)
circle(-100, 90)
forward(100)
circle(200, 45)
goto(-400, -400)

end_fill()


#mountain 5
goto(400, 0)
setheading(180)
fillcolor("darkolivegreen2")
begin_fill()

circle(-200, 30)
forward(100)
circle(100, 60)
forward(100)
circle(-500, 30)
goto(-400, ycor())
goto(-400, -400)
goto(400, -400)

end_fill()


#road
goto(400, -100)
fillcolor("grey")
setheading(190)
begin_fill()

circle(300, 30)
circle(-400, 40)
circle(400, 30)
circle(-400, 30)
goto(-400, ycor())
goto(-400, -400)
goto(-200, -400)
setheading(30)
circle(-500, 25)
circle(400, 40)
circle(-400, 25)

end_fill()


#trees
for i in range(18):
    x = -410 + random.randint(0, 20)
    y = -40 - 10 * i
    minimum_scale = 0.3 + i * 0.03
    maximum_scale = 0.5 + i * 0.03
    amount = 20 - i
    spacing = 20
    trees.treeRow(x, y, minimum_scale, maximum_scale, amount, spacing)


#skyscrapers
for i in range(3):
    for j in range(5):
        x = 120 + j * 40 + i * 15
        y = -190 + j * 23 - i * 4
        scale = 0.8 + i * 0.07 - j * 0.01
        width_to_height_ratio = random.randint(7 - i, 10 - i)
        houses.randomSkyscraper(x, y, scale, width_to_height_ratio)
    for j in range(2):
        x = 320 + i * 15 + j * 40
        y = -88 - i * 4 + j * 10
        scale = 0.75 + i * 0.07 - j * 0.01
        width_to_height_ratio = random.randint(7 - i, 10 - i)
        houses.randomSkyscraper(x, y, scale, width_to_height_ratio)


#houses
for i in range(3):
    goto(-25 + i * 25, -355 - i * 20)
    direction = 10
    for j in range(6):
        scale = 0.9 + i * 0.1 - j * 0.02
        houses.randomSquareHouse(xcor(), ycor(), scale)
        setheading(direction)
        circle(650, 5)
        direction = int(heading())

for i in range(2):
    goto(-45 + i * 25, -210 - i * 20)
    direction = 180
    for _ in range(5):
        houses.randomSquareHouse(xcor(), ycor(), 0.8 + i * 0.1)
        setheading(direction)
        circle(400, 8)
        direction = int(heading())


#clean left edge
goto(-430, 400)
pencolor("white")
pensize(50)
pendown()
goto(-430, -400)
penup()

#clean right edge
goto(430, 400)
pencolor("white")
pensize(50)
pendown()
goto(430, -400)

update()
done()
