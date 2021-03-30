import time
from turtle import *
from PIL import Image
import turtle

pen = turtle.Turtle()

color("red")
begin_fill()
left(40)
forward(150)

circle(90,180)
left(280)
circle(90,180)
forward(150)
end_fill()
pen.up()

# Move turtle to a given position
pen.setpos(-120,120)
pen.write("Wish you Happy Birthday  \n", font=("Helvetica", 14, "bold"))
pen.write("                  Preeti ", font=("Helvetica", 14, "bold"))
time.sleep(6)
img = Image.open("pic3.jpeg")
print("img.size")
img.show()

