import turtle as t
import random

# import colorgram
#
# colors = colorgram.extract('image.png', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color_tuple = (r, g, b)
#     rgb_colors.append(rgb_color_tuple)
#
# print(rgb_colors)

color_list = [(245, 245, 243), (241, 245, 243), (239, 242, 247), (247, 241, 244), (241, 228, 89), (24, 24, 61),
              (183, 73, 38), (144, 17, 31), (39, 29, 21), (214, 145, 85), (124, 159, 216), (204, 73, 115), (68, 26, 35),
              (55, 92, 138), (37, 45, 126), (23, 33, 23), (161, 21, 14), (142, 57, 80), (71, 78, 32), (67, 113, 74),
              (100, 98, 192), (141, 178, 161), (207, 77, 62), (144, 213, 191), (98, 168, 76), (192, 141, 156),
              (49, 85, 26), (156, 210, 221), (225, 172, 184), (175, 185, 221)]

t.colormode(255)
screen = t.Screen()
spot = t.Turtle()
spot.speed("fastest")
# No need for pen to come down for drawing of dots
spot.penup()
spot.hideturtle()
spot.setheading(225)
spot.forward(250)
spot.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    spot.dot(20, random.choice(color_list))
    spot.forward(50)

    if dot_count % 10 == 0:
        spot.setheading(90)
        spot.forward(50)
        spot.setheading(180)
        spot.forward(500)
        spot.setheading(0)

screen.exitonclick()
