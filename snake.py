import turtle
import random



# our generic polygon function
def polygon(sides, length):

    for x in range(sides):
        turtle.forward(length)
        turtle.right(360/sides)

# create a drawing variable
is_drawing = True

# bound to the "q" key - will draw a random polygon
def draw_poly():
    polygon(random.randint(4,10), 50)

# bound to the "up" key - turtle up
def go_up():
    if turtle.ycor() > 250:
        return;
    print turtle.position()

    turtle.shape("homie_back.gif")

    turtle.setheading(90)
    turtle.forward(10)

# bound to the "right" key - turtle right
def go_right():
    if turtle.xcor() > 240:
        return;
    print turtle.position()
    turtle.shape("homie_right.gif")
    turtle.setheading(0)
    turtle.forward(10)

# bound to the "left" key - turtle left
def go_left():
    if turtle.xcor() < -250:
        return;
    print turtle.position()

    turtle.shape("homie_left.gif")

    turtle.setheading(180)
    turtle.forward(10)

# bound to the "down" key - turtle down
def go_down():
    if turtle.ycor() < -250: #IM ON TO SOMETHIN RIGHT HEA
        return;
    print turtle.position()

    turtle.shape("homie_front.gif")

    turtle.setheading(270)
    print turtle.heading()

    turtle.forward(10)

# bound to the "p" key - toggles pen up/down
def toggle_pen():
    global is_drawing

    # if we are currently drawing then pull
    # up the pen
    if is_drawing == True:
        turtle.penup()
        is_drawing = False
    else:
        turtle.pendown()
        is_drawing = True
def shoot():
    bullet.penup()
    bullet.speed(0)
    bullet.setheading(turtle.heading())
    bullet.goto(turtle.xcor(),turtle.ycor())
    for i in range(252):
        bullet.forward(10)
        if bullet.distance(enemy) == 0:

            print "you killed him!"

        

    

# main program
turtle.register_shape("homie_front.gif")
turtle.register_shape("homie_back.gif")
turtle.register_shape("homie_left.gif")
turtle.register_shape("homie_right.gif")
turtle.title("My Turtle")
turtle.setup(500,500, 0,0)
bullet = turtle.Turtle()
enemy = turtle.Turtle()
enemy.penup()
enemy.goto(100,100)





# bind keys to our functions
turtle.onkey(go_up, "Up")
turtle.onkey(go_down, "Down")
turtle.onkey(go_left, "Left")
turtle.onkey(go_right, "Right")
turtle.onkey(toggle_pen, "p")
turtle.onkey(draw_poly, "q")
turtle.onkey(shoot,"b")

# listen for key presses
turtle.listen()


turtle.exitonclick()