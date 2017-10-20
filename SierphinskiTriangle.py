
import turtle #draw graphics

def draw_triangle(points, color, turtle_instance):
    '''
    draw triangle
    '''
    #print("Color", color)
    turtle_instance.fillcolor(color)
    turtle_instance.up()
    turtle_instance.goto(points[0][0], points[0][1])
    turtle_instance.down()
    turtle_instance.begin_fill()
    turtle_instance.goto(points[1][0], points[1][1])
    turtle_instance.goto(points[2][0], points[2][1])
    turtle_instance.goto(points[0][0], points[0][1])
    turtle_instance.end_fill()

def draw_sierphinski_triangle(points, colors, level, turtle_instance):
    draw_triangle(points, colors[level], turtle_instance)
    if level >=0:
        mid_points = [((points[0][0] + points[1][0])/2, (points[0][1] + points[1][1])/2 ), ( (points[1][0] + points[2][0])/2, (points[1][1] + points[2][1])/2 ), ( (points[0][0] + points[2][0])/2, (points[0][1] + points[2][1])/2 )  ]
        draw_sierphinski_triangle([points[0], mid_points[0], mid_points[2]],    colors, level-1, turtle_instance)
        draw_sierphinski_triangle([ mid_points[0], points[1],  mid_points[1]],  colors, level-1, turtle_instance)
        draw_sierphinski_triangle([ mid_points[2], mid_points[1], points[2]],   colors, level-1, turtle_instance)
def main():
    '''
    main function
    '''
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    points = [(-100, 50), (0, 200), (100, -50)]
    #draw_triangle(points, "green", my_turtle)
    colors = ["green", "black", "blue", "orange"]
    draw_sierphinski_triangle(points, colors, 3, my_turtle)
    my_win.exitonclick()

main()

